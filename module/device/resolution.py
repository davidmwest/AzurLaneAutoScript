"""
Alas works on a fixed 1280x720 canvas: every asset, button area and map homography
is expressed in those pixels.

Devices running at a larger resolution of the same aspect ratio (1920x1080, 2560x1440,
3840x2160) are supported by converting at the device boundary. Whatever comes out of the
device (screenshots, UI hierarchy bounds) is brought down to the canvas, and whatever goes
in as raw device pixels (ADB and uiautomator2 touches) is scaled back up.
Everything above the device layer keeps working in canvas pixels.
"""
import re

import cv2

from module.base.utils import image_size

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

_WM_SIZE_RE = re.compile(r'(Physical|Override) size: (\d+)x(\d+)')
_BOUNDS_RE = re.compile(r'\d+')


def canvas_scale(width, height):
    """
    Args:
        width (int): Device width in pixels.
        height (int): Device height in pixels.

    Returns:
        float: Device pixels per canvas pixel, 1.0 for 1280x720 and 2.0 for 2560x1440,
            portrait sizes included.
            None if the size is smaller than the canvas or has another aspect ratio.
    """
    for canvas_w, canvas_h in ((CANVAS_WIDTH, CANVAS_HEIGHT), (CANVAS_HEIGHT, CANVAS_WIDTH)):
        if width >= canvas_w and width * canvas_h == height * canvas_w:
            return width / canvas_w
    return None


def parse_wm_size(output):
    """
    Args:
        output (str): Output of `wm size`, such as:
            Physical size: 2560x1440
            Override size: 1280x720

    Returns:
        tuple[int, int]: (width, height) the device is rendering at, (0, 0) if unknown.
    """
    sizes = {kind: (int(w), int(h)) for kind, w, h in _WM_SIZE_RE.findall(output)}
    # An override is what apps actually render at
    return sizes.get('Override', sizes.get('Physical', (0, 0)))


def image_to_canvas(image):
    """
    Args:
        image (np.ndarray): Screenshot at device resolution.

    Returns:
        np.ndarray: Screenshot at canvas resolution.
            Returned untouched if it is already there or cannot be scaled without distortion.
    """
    width, height = image_size(image)
    scale = canvas_scale(width, height)
    if scale is None or scale == 1:
        return image
    size = (int(round(width / scale)), int(round(height / scale)))
    # INTER_AREA averages the device pixels each canvas pixel covers,
    # the closest match to what the game renders at 1280x720
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)


def point_to_device(x, y, scale):
    """
    Args:
        x (int, float): Canvas x.
        y (int, float): Canvas y.
        scale (float): Device pixels per canvas pixel.

    Returns:
        tuple[int, int]: The device pixel at the middle of that canvas pixel.
    """
    if scale == 1:
        return x, y
    return int((x + 0.5) * scale), int((y + 0.5) * scale)


def hierarchy_to_canvas(hierarchy, scale):
    """
    Rewrite `bounds` of every node in a UI hierarchy from device pixels to canvas pixels.

    Args:
        hierarchy (etree._Element):
        scale (float): Device pixels per canvas pixel.

    Returns:
        etree._Element: The same hierarchy, modified in place.
    """
    if scale == 1:
        return hierarchy
    for node in hierarchy.iter():
        bounds = node.attrib.get('bounds')
        if not bounds:
            continue
        numbers = [int(int(n) / scale) for n in _BOUNDS_RE.findall(bounds)]
        if len(numbers) == 4:
            node.attrib['bounds'] = '[{},{}][{},{}]'.format(*numbers)
    return hierarchy
