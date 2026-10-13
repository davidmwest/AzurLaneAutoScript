import numpy as np
import pytest
from lxml import etree

from module.device.resolution import (canvas_scale, hierarchy_to_canvas, image_to_canvas, parse_wm_size,
                                      point_to_device)


@pytest.mark.parametrize('size, scale', [
    ((1280, 720), 1.0),
    ((1920, 1080), 1.5),
    ((2560, 1440), 2.0),
    ((3840, 2160), 3.0),
    # Portrait devices report the short side first
    ((720, 1280), 1.0),
    ((1440, 2560), 2.0),
])
def test_canvas_scale_of_supported_sizes(size, scale):
    assert canvas_scale(*size) == scale


@pytest.mark.parametrize('size', [
    (640, 360),  # Smaller than the canvas
    (1920, 1200),  # 16:10
    (3072, 1440),  # BlueStacks with its ad panel during boot
    (0, 0),
])
def test_canvas_scale_of_unsupported_sizes(size):
    assert canvas_scale(*size) is None


def test_parse_wm_size_physical():
    assert parse_wm_size('Physical size: 2560x1440') == (2560, 1440)


def test_parse_wm_size_prefers_override():
    output = 'Physical size: 2560x1440\nOverride size: 1280x720\n'
    assert parse_wm_size(output) == (1280, 720)


def test_parse_wm_size_unknown():
    assert parse_wm_size('error: closed') == (0, 0)


def test_image_to_canvas_averages_device_pixels():
    image = np.zeros((1440, 2560, 3), dtype=np.uint8)
    # One canvas pixel worth of device pixels: 2x2 block at canvas (10, 20)
    image[40:42, 20:22] = [[[0, 0, 0], [100, 100, 100]], [[100, 100, 100], [200, 200, 200]]]

    canvas = image_to_canvas(image)

    assert canvas.shape == (720, 1280, 3)
    assert canvas[20, 10].tolist() == [100, 100, 100]
    assert canvas[20, 11].tolist() == [0, 0, 0]


def test_image_to_canvas_keeps_canvas_sized_image():
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    assert image_to_canvas(image) is image


def test_image_to_canvas_keeps_unsupported_image():
    # Left for check_screen_size() to report
    image = np.zeros((1200, 1920, 3), dtype=np.uint8)
    assert image_to_canvas(image) is image


def test_image_to_canvas_portrait():
    image = np.zeros((2560, 1440, 3), dtype=np.uint8)
    assert image_to_canvas(image).shape == (1280, 720, 3)


def test_point_to_device_is_identity_on_canvas_sized_device():
    assert point_to_device(123, 456, scale=1.0) == (123, 456)


@pytest.mark.parametrize('scale, device_size', [(1.5, (1920, 1080)), (2.0, (2560, 1440)), (3.0, (3840, 2160))])
def test_point_to_device_stays_inside_the_canvas_pixel(scale, device_size):
    for x, y in [(0, 0), (640, 360), (1279, 719)]:
        device_x, device_y = point_to_device(x, y, scale=scale)
        assert 0 <= device_x < device_size[0] and 0 <= device_y < device_size[1]
        # The device pixel must map back to the canvas pixel that was asked for
        assert (int(device_x / scale), int(device_y / scale)) == (x, y)


def test_hierarchy_to_canvas_rewrites_bounds():
    hierarchy = etree.fromstring(
        '<hierarchy><node text="Login" bounds="[200,100][600,300]"><node bounds="[1280,720][2560,1440]"/></node>'
        '</hierarchy>')

    hierarchy_to_canvas(hierarchy, scale=2.0)

    assert hierarchy.xpath('//*[@text="Login"]')[0].attrib['bounds'] == '[100,50][300,150]'
    assert hierarchy.xpath('//node/node')[0].attrib['bounds'] == '[640,360][1280,720]'


def test_hierarchy_to_canvas_is_identity_on_canvas_sized_device():
    hierarchy = etree.fromstring('<hierarchy><node bounds="[200,100][600,300]"/></hierarchy>')

    hierarchy_to_canvas(hierarchy, scale=1.0)

    assert hierarchy[0].attrib['bounds'] == '[200,100][600,300]'
