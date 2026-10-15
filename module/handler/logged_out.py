"""
The account logged out during a task, most likely because it logged in on another device.
Logging in again at once would log the other device out, the scheduler waits Error.LoggedOutWait minutes first.
"""
from module.base.button import Button
from module.handler.assets import LOGIN_CHECK
from module.ocr.ocr import Ocr

# What a popup says when the account logs in elsewhere, in lower case
LOGGED_OUT_KEYWORDS = ('another device', 'other device', 'logged in elsewhere', 'logged in on',
                       'log in again', 'login again', 're-login', 'relogin')
# Lines of text in the middle of the screen, where popups write
POPUP_LINES = [Button(area=(240, y, 1040, y + 36), color=(), button=(240, y, 1040, y + 36), name=f'POPUP_LINE_{i}')
               for i, y in enumerate(range(180, 540, 36))]
# White text on dark popups, dark text on light ones
POPUP_LETTERS = [(255, 255, 255), (60, 60, 60)]


def logged_out_text(text):
    """
    Returns:
        bool: If the text of a popup asks to log in again.
    """
    text = ' '.join(str(text).lower().split())
    return any(keyword in text for keyword in LOGGED_OUT_KEYWORDS)


def logged_out(image):
    """
    Args:
        image (np.ndarray): Screenshot.

    Returns:
        bool: If the game shows its login page, or a popup that asks to log in again.
    """
    if LOGIN_CHECK.match(image, offset=(30, 30)):
        return True
    for letter in POPUP_LETTERS:
        lines = Ocr(POPUP_LINES, lang='cnocr', letter=letter, threshold=128, name='POPUP_TEXT').ocr(image)
        if logged_out_text(' '.join(lines)):
            return True
    return False
