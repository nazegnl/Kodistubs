# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
**GUI functions on Kodi.**

Offers classes and functions that manipulate the Graphical User Interface
through windows, dialogs, and various control widgets.
"""
import sys
from typing import Union, List, Dict, Tuple, Optional

__kodistubs__ = True

from xbmc import InfoTagVideo, InfoTagMusic

ICON_OVERLAY_NONE = 0
ICON_OVERLAY_RAR = 0
ICON_OVERLAY_ZIP = 0
ICON_OVERLAY_LOCKED = 0
ICON_OVERLAY_UNWATCHED = 0
ICON_OVERLAY_WATCHED = 0
ICON_OVERLAY_HD = 0
INPUT_TYPE_TEXT = 0
INPUT_TYPE_NUMBER = 0
INPUT_TYPE_DATE = 0
INPUT_TYPE_TIME = 0
INPUT_TYPE_IPADDRESS = 0
INPUT_TYPE_PASSWORD = 0
INPUT_TYPE_PASSWORD_MD5 = 0
INPUT_TYPE_SECONDS = 0
INPUT_TYPE_PASSWORD_NUMBER_VERIFY_NEW = 0
NOTIFICATION_INFO = 0
NOTIFICATION_WARNING = 0
NOTIFICATION_ERROR = 0
INPUT_ALPHANUM = 0
INPUT_NUMERIC = 0
INPUT_DATE = 0
INPUT_TIME = 0
INPUT_IPADDRESS = 0
INPUT_PASSWORD = 0
HORIZONTAL = 0
VERTICAL = 0
PASSWORD_VERIFY = 0
ALPHANUM_HIDE_INPUT = 0
CONTROL_TEXT_OFFSET_X = 0
CONTROL_TEXT_OFFSET_Y = 0
ACTION_NONE = 0
ACTION_MOVE_LEFT = 0
ACTION_MOVE_RIGHT = 0
ACTION_MOVE_UP = 0
ACTION_MOVE_DOWN = 0
ACTION_PAGE_UP = 0
ACTION_PAGE_DOWN = 0
ACTION_SELECT_ITEM = 0
ACTION_HIGHLIGHT_ITEM = 0
ACTION_PARENT_DIR = 0
ACTION_PREVIOUS_MENU = 0
ACTION_SHOW_INFO = 0
ACTION_PAUSE = 0
ACTION_STOP = 0
ACTION_NEXT_ITEM = 0
ACTION_PREV_ITEM = 0
ACTION_FORWARD = 0
ACTION_REWIND = 0
ACTION_SHOW_GUI = 0
ACTION_ASPECT_RATIO = 0
ACTION_STEP_FORWARD = 0
ACTION_STEP_BACK = 0
ACTION_BIG_STEP_FORWARD = 0
ACTION_BIG_STEP_BACK = 0
ACTION_SHOW_OSD = 0
ACTION_SHOW_SUBTITLES = 0
ACTION_NEXT_SUBTITLE = 0
ACTION_BROWSE_SUBTITLE = 0
ACTION_PLAYER_DEBUG = 0
ACTION_NEXT_PICTURE = 0
ACTION_PREV_PICTURE = 0
ACTION_ZOOM_OUT = 0
ACTION_ZOOM_IN = 0
ACTION_TOGGLE_SOURCE_DEST = 0
ACTION_SHOW_PLAYLIST = 0
ACTION_QUEUE_ITEM = 0
ACTION_REMOVE_ITEM = 0
ACTION_SHOW_FULLSCREEN = 0
ACTION_ZOOM_LEVEL_NORMAL = 0
ACTION_ZOOM_LEVEL_1 = 0
ACTION_ZOOM_LEVEL_2 = 0
ACTION_ZOOM_LEVEL_3 = 0
ACTION_ZOOM_LEVEL_4 = 0
ACTION_ZOOM_LEVEL_5 = 0
ACTION_ZOOM_LEVEL_6 = 0
ACTION_ZOOM_LEVEL_7 = 0
ACTION_ZOOM_LEVEL_8 = 0
ACTION_ZOOM_LEVEL_9 = 0
ACTION_CALIBRATE_SWAP_ARROWS = 0
ACTION_CALIBRATE_RESET = 0
ACTION_ANALOG_MOVE = 0
ACTION_ROTATE_PICTURE_CW = 0
ACTION_ROTATE_PICTURE_CCW = 0
ACTION_SUBTITLE_DELAY_MIN = 0
ACTION_SUBTITLE_DELAY_PLUS = 0
ACTION_AUDIO_DELAY_MIN = 0
ACTION_AUDIO_DELAY_PLUS = 0
ACTION_AUDIO_NEXT_LANGUAGE = 0
ACTION_CHANGE_RESOLUTION = 0
REMOTE_0 = 0
REMOTE_1 = 0
REMOTE_2 = 0
REMOTE_3 = 0
REMOTE_4 = 0
REMOTE_5 = 0
REMOTE_6 = 0
REMOTE_7 = 0
REMOTE_8 = 0
REMOTE_9 = 0
ACTION_PLAYER_PROCESS_INFO = 0
ACTION_PLAYER_PROGRAM_SELECT = 0
ACTION_PLAYER_RESOLUTION_SELECT = 0
ACTION_SMALL_STEP_BACK = 0
ACTION_PLAYER_FORWARD = 0
ACTION_PLAYER_REWIND = 0
ACTION_PLAYER_PLAY = 0
ACTION_DELETE_ITEM = 0
ACTION_COPY_ITEM = 0
ACTION_MOVE_ITEM = 0
ACTION_TAKE_SCREENSHOT = 0
ACTION_RENAME_ITEM = 0
ACTION_VOLUME_UP = 0
ACTION_VOLUME_DOWN = 0
ACTION_VOLAMP = 0
ACTION_MUTE = 0
ACTION_NAV_BACK = 0
ACTION_VOLAMP_UP = 0
ACTION_VOLAMP_DOWN = 0
ACTION_CREATE_EPISODE_BOOKMARK = 0
ACTION_CREATE_BOOKMARK = 0
ACTION_CHAPTER_OR_BIG_STEP_FORWARD = 0
ACTION_CHAPTER_OR_BIG_STEP_BACK = 0
ACTION_CYCLE_SUBTITLE = 0
ACTION_MOUSE_START = 0
ACTION_MOUSE_LEFT_CLICK = 0
ACTION_MOUSE_RIGHT_CLICK = 0
ACTION_MOUSE_MIDDLE_CLICK = 0
ACTION_MOUSE_DOUBLE_CLICK = 0
ACTION_MOUSE_WHEEL_UP = 0
ACTION_MOUSE_WHEEL_DOWN = 0
ACTION_MOUSE_DRAG = 0
ACTION_MOUSE_MOVE = 0
ACTION_MOUSE_LONG_CLICK = 0
ACTION_MOUSE_DRAG_END = 0
ACTION_MOUSE_END = 0
ACTION_BACKSPACE = 0
ACTION_SCROLL_UP = 0
ACTION_SCROLL_DOWN = 0
ACTION_ANALOG_FORWARD = 0
ACTION_ANALOG_REWIND = 0
ACTION_MOVE_ITEM_UP = 0
ACTION_MOVE_ITEM_DOWN = 0
ACTION_CONTEXT_MENU = 0
ACTION_SHIFT = 0
ACTION_SYMBOLS = 0
ACTION_CURSOR_LEFT = 0
ACTION_CURSOR_RIGHT = 0
ACTION_BUILT_IN_FUNCTION = 0
ACTION_SHOW_OSD_TIME = 0
ACTION_ANALOG_SEEK_FORWARD = 0
ACTION_ANALOG_SEEK_BACK = 0
ACTION_VIS_PRESET_SHOW = 0
ACTION_VIS_PRESET_NEXT = 0
ACTION_VIS_PRESET_PREV = 0
ACTION_VIS_PRESET_LOCK = 0
ACTION_VIS_PRESET_RANDOM = 0
ACTION_VIS_RATE_PRESET_PLUS = 0
ACTION_VIS_RATE_PRESET_MINUS = 0
ACTION_SHOW_VIDEOMENU = 0
ACTION_ENTER = 0
ACTION_INCREASE_RATING = 0
ACTION_DECREASE_RATING = 0
ACTION_NEXT_SCENE = 0
ACTION_PREV_SCENE = 0
ACTION_NEXT_LETTER = 0
ACTION_PREV_LETTER = 0
ACTION_JUMP_SMS2 = 0
ACTION_JUMP_SMS3 = 0
ACTION_JUMP_SMS4 = 0
ACTION_JUMP_SMS5 = 0
ACTION_JUMP_SMS6 = 0
ACTION_JUMP_SMS7 = 0
ACTION_JUMP_SMS8 = 0
ACTION_JUMP_SMS9 = 0
ACTION_FILTER_CLEAR = 0
ACTION_FILTER_SMS2 = 0
ACTION_FILTER_SMS3 = 0
ACTION_FILTER_SMS4 = 0
ACTION_FILTER_SMS5 = 0
ACTION_FILTER_SMS6 = 0
ACTION_FILTER_SMS7 = 0
ACTION_FILTER_SMS8 = 0
ACTION_FILTER_SMS9 = 0
ACTION_FIRST_PAGE = 0
ACTION_LAST_PAGE = 0
ACTION_AUDIO_DELAY = 0
ACTION_SUBTITLE_DELAY = 0
ACTION_MENU = 0
ACTION_SET_RATING = 0
ACTION_RECORD = 0
ACTION_PASTE = 0
ACTION_NEXT_CONTROL = 0
ACTION_PREV_CONTROL = 0
ACTION_CHANNEL_SWITCH = 0
ACTION_CHANNEL_UP = 0
ACTION_CHANNEL_DOWN = 0
ACTION_NEXT_CHANNELGROUP = 0
ACTION_PREVIOUS_CHANNELGROUP = 0
ACTION_PVR_PLAY = 0
ACTION_PVR_PLAY_TV = 0
ACTION_PVR_PLAY_RADIO = 0
ACTION_PVR_SHOW_TIMER_RULE = 0
ACTION_CHANNEL_NUMBER_SEP = 0
ACTION_PVR_ANNOUNCE_REMINDERS = 0
ACTION_TOGGLE_FULLSCREEN = 0
ACTION_TOGGLE_WATCHED = 0
ACTION_SCAN_ITEM = 0
ACTION_TOGGLE_DIGITAL_ANALOG = 0
ACTION_RELOAD_KEYMAPS = 0
ACTION_GUIPROFILE_BEGIN = 0
ACTION_TELETEXT_RED = 0
ACTION_TELETEXT_GREEN = 0
ACTION_TELETEXT_YELLOW = 0
ACTION_TELETEXT_BLUE = 0
ACTION_INCREASE_PAR = 0
ACTION_DECREASE_PAR = 0
ACTION_VSHIFT_UP = 0
ACTION_VSHIFT_DOWN = 0
ACTION_PLAYER_PLAYPAUSE = 0
ACTION_SUBTITLE_VSHIFT_UP = 0
ACTION_SUBTITLE_VSHIFT_DOWN = 0
ACTION_SUBTITLE_ALIGN = 0
ACTION_FILTER = 0
ACTION_SWITCH_PLAYER = 0
ACTION_STEREOMODE_NEXT = 0
ACTION_STEREOMODE_PREVIOUS = 0
ACTION_STEREOMODE_TOGGLE = 0
ACTION_STEREOMODE_SELECT = 0
ACTION_STEREOMODE_TOMONO = 0
ACTION_STEREOMODE_SET = 0
ACTION_SETTINGS_RESET = 0
ACTION_SETTINGS_LEVEL_CHANGE = 0
ACTION_TRIGGER_OSD = 0
ACTION_INPUT_TEXT = 0
ACTION_VOLUME_SET = 0
ACTION_TOGGLE_COMMSKIP = 0
ACTION_HDR_TOGGLE = 0
ACTION_PLAYER_RESET = 0
ACTION_TOGGLE_FONT = 0
ACTION_VIDEO_NEXT_STREAM = 0
ACTION_QUEUE_ITEM_NEXT = 0
ACTION_VOICE_RECOGNIZE = 0
ACTION_TOUCH_TAP = 0
ACTION_TOUCH_TAP_TEN = 0
ACTION_TOUCH_LONGPRESS = 0
ACTION_TOUCH_LONGPRESS_TEN = 0
ACTION_GESTURE_NOTIFY = 0
ACTION_GESTURE_BEGIN = 0
ACTION_GESTURE_ZOOM = 0
ACTION_GESTURE_ROTATE = 0
ACTION_GESTURE_PAN = 0
ACTION_GESTURE_ABORT = 0
ACTION_GESTURE_SWIPE_LEFT = 0
ACTION_GESTURE_SWIPE_LEFT_TEN = 0
ACTION_GESTURE_SWIPE_RIGHT = 0
ACTION_GESTURE_SWIPE_RIGHT_TEN = 0
ACTION_GESTURE_SWIPE_UP = 0
ACTION_GESTURE_SWIPE_UP_TEN = 0
ACTION_GESTURE_SWIPE_DOWN = 0
ACTION_GESTURE_SWIPE_DOWN_TEN = 0
ACTION_GESTURE_END = 0
ACTION_ANALOG_MOVE_X_LEFT = 0
ACTION_ANALOG_MOVE_X_RIGHT = 0
ACTION_ANALOG_MOVE_Y_UP = 0
ACTION_ANALOG_MOVE_Y_DOWN = 0
ACTION_ERROR = 0
ACTION_NOOP = 0
KEY_BUTTON_A = 0
KEY_BUTTON_B = 0
KEY_BUTTON_X = 0
KEY_BUTTON_Y = 0
KEY_BUTTON_BLACK = 0
KEY_BUTTON_WHITE = 0
KEY_BUTTON_LEFT_TRIGGER = 0
KEY_BUTTON_RIGHT_TRIGGER = 0
KEY_BUTTON_LEFT_THUMB_STICK = 0
KEY_BUTTON_RIGHT_THUMB_STICK = 0
KEY_BUTTON_RIGHT_THUMB_STICK_UP = 0
KEY_BUTTON_RIGHT_THUMB_STICK_DOWN = 0
KEY_BUTTON_RIGHT_THUMB_STICK_LEFT = 0
KEY_BUTTON_RIGHT_THUMB_STICK_RIGHT = 0
KEY_BUTTON_DPAD_UP = 0
KEY_BUTTON_DPAD_DOWN = 0
KEY_BUTTON_DPAD_LEFT = 0
KEY_BUTTON_DPAD_RIGHT = 0
KEY_BUTTON_START = 0
KEY_BUTTON_BACK = 0
KEY_BUTTON_LEFT_THUMB_BUTTON = 0
KEY_BUTTON_RIGHT_THUMB_BUTTON = 0
KEY_BUTTON_LEFT_ANALOG_TRIGGER = 0
KEY_BUTTON_RIGHT_ANALOG_TRIGGER = 0
KEY_BUTTON_LEFT_THUMB_STICK_UP = 0
KEY_BUTTON_LEFT_THUMB_STICK_DOWN = 0
KEY_BUTTON_LEFT_THUMB_STICK_LEFT = 0
KEY_BUTTON_LEFT_THUMB_STICK_RIGHT = 0
KEY_VKEY = 0
KEY_UNICODE = 0
KEY_VMOUSE = 0
KEY_MOUSE_START = 0
KEY_MOUSE_CLICK = 0
KEY_MOUSE_RIGHTCLICK = 0
KEY_MOUSE_MIDDLECLICK = 0
KEY_MOUSE_DOUBLE_CLICK = 0
KEY_MOUSE_LONG_CLICK = 0
KEY_MOUSE_WHEEL_UP = 0
KEY_MOUSE_WHEEL_DOWN = 0
KEY_MOUSE_MOVE = 0
KEY_MOUSE_DRAG = 0
KEY_MOUSE_DRAG_START = 0
KEY_MOUSE_DRAG_END = 0
KEY_MOUSE_RDRAG = 0
KEY_MOUSE_RDRAG_START = 0
KEY_MOUSE_RDRAG_END = 0
KEY_MOUSE_NOOP = 0
KEY_MOUSE_END = 0
KEY_APPCOMMAND = 0
KEY_INVALID = 0
ICON_TYPE_NONE = 0
ICON_TYPE_PROGRAMS = 0
ICON_TYPE_MUSIC = 0
ICON_TYPE_PICTURES = 0
ICON_TYPE_VIDEOS = 0
ICON_TYPE_FILES = 0
ICON_TYPE_WEATHER = 0
ICON_TYPE_SETTINGS = 0


class Control:
    """
    **Code based skin access.**

    Offers classes and functions that manipulate the add-on gui controls.

    \python_class{ Control() }

    **Code based skin access.**

    Kodi is noted as having a very flexible and robust framework for its GUI, making
    theme-skinning and personal customization very accessible. Users can create
    their own skin (or modify an existing skin) and share it with others.

    Kodi includes a new GUI library written from scratch. This library allows you to
    skin/change everything you see in Kodi, from the images, the sizes and positions
    of all controls, colours, fonts, and text, through to altering navigation and
    even adding new functionality. The skin system is quite complex, and this
    portion of the manual is dedicated to providing in depth information on how it
    all works, along with tips to make the experience a little more pleasant.
    """
    
    def __init__(self) -> None:
        pass
    
    def getId(self) -> int:
        """
        \python_func{`getId()` } Returns the control's current id as an integer.

        :return: int - Current id

        Example::

            ...
            id = self.button.getId()
            ...
        """
        return 0
    
    def getX(self) -> int:
        """
        \python_func{`getX()` } Returns the control's current X position.

        :return: int - Current X position

        Example::

            ...
            posX = self.button.getX()
            ...
        """
        return 0
    
    def getY(self) -> int:
        """
        \python_func{`getY()` } Returns the control's current Y position.

        :return: int - Current Y position

        Example::

            ...
            posY = self.button.getY()
            ...
        """
        return 0
    
    def getHeight(self) -> int:
        """
        \python_func{`getHeight()` } Returns the control's current height as an integer.

        :return: int - Current height

        Example::

            ...
            height = self.button.getHeight()
            ...
        """
        return 0
    
    def getWidth(self) -> int:
        """
        \python_func{`getWidth()` } Returns the control's current width as an integer.

        :return: int - Current width

        Example::

            ...
            width = self.button.getWidth()
            ...
        """
        return 0
    
    def setEnabled(self, enabled: bool) -> None:
        """
        \python_func{ setEnabled(enabled) } Set's the control's enabled/disabled state.

        :param enabled: bool - True=enabled / False=disabled.

        Example::

            ...
            self.button.setEnabled(False)
            ...
        """
        pass
    
    def setVisible(self, visible: bool) -> None:
        """
        \python_func{ setVisible(visible) } Set's the control's visible/hidden state.

        :param visible: bool - True=visible / False=hidden.

        Example::

            ...
            self.button.setVisible(False)
            ...
        """
        pass
    
    def isVisible(self) -> bool:
        """
        \python_func{`isVisible()` } Get the control's visible/hidden state.

         @python_v18 New function added.

        Example::

            ...
            if self.button.isVisible():
                ...
        """
        return True
    
    def setVisibleCondition(self, visible: str,
                            allowHiddenFocus: bool = False) -> None:
        """
        \python_func{ setVisibleCondition(visible[,allowHiddenFocus]) } Set's the
        control's visible condition.

        Allows Kodi to control the visible status of the control.

        List of Conditions

        :param visible: string - Visible condition
        :param allowHiddenFocus: [opt] bool - True=gains focus even if hidden

        Example::

            ...
            # setVisibleCondition(visible[,allowHiddenFocus])
            self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
            ...
        """
        pass
    
    def setEnableCondition(self, enable: str) -> None:
        """
        \python_func{ setEnableCondition(enable) } Set's the control's enabled
        condition.

        Allows Kodi to control the enabled status of the control.

        List of Conditions

        :param enable: string - Enable condition.

        Example::

            ...
            # setEnableCondition(enable)
            self.button.setEnableCondition('System.InternetState')
            ...
        """
        pass
    
    def setAnimations(self, eventAttr: List[Tuple[str, str]]) -> None:
        """
        \python_func{ setAnimations([(event, attr,)*]) } Set's the control's animations.

        **[(event,attr,)*]**: list - A list of tuples consisting of event and attributes
        pairs.

        Animating your skin

        :param event: string - The event to animate.
        :param attr: string - The whole attribute string separated by spaces.

        Example::

            ...
            # setAnimations([(event, attr,)*])
            self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
            ...
        """
        pass
    
    def setPosition(self, x: int, y: int) -> None:
        """
        \python_func{ setPosition(x, y) } Set's the controls position.

        :param x: integer - x coordinate of control.
        :param y: integer - y coordinate of control.

        .. note::
            You may use negative integers. (e.g sliding a control into view)

        Example::

            ...
            self.button.setPosition(100, 250)
            ...
        """
        pass
    
    def setWidth(self, width: int) -> None:
        """
        \python_func{ setWidth(width) } Set's the controls width.

        :param width: integer - width of control.

        Example::

            ...
            self.image.setWidth(100)
            ...
        """
        pass
    
    def setHeight(self, height: int) -> None:
        """
        \python_func{ setHeight(height) } Set's the controls height.

        :param height: integer - height of control.

        Example::

            ...
            self.image.setHeight(100)
            ...
        """
        pass
    
    def setNavigation(self, up: 'Control',
                      down: 'Control',
                      left: 'Control',
                      right: 'Control') -> None:
        """
        \python_func{ setNavigation(up, down, left, right) } Set's the controls
        navigation.

        :param up: control object - control to navigate to on up.
        :param down: control object - control to navigate to on down.
        :param left: control object - control to navigate to on left.
        :param right: control object - control to navigate to on right.
        :raises TypeError: if one of the supplied arguments is not a control type.
        :raises ReferenceError: if one of the controls is not added to a window.

        .. note::
            Same
            as `controlUp()`,`controlDown()`,`controlLeft()`,`controlRight()`.
            Set to self to disable navigation for that direction.

        Example::

            ...
            self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
            ...
        """
        pass
    
    def controlUp(self, up: 'Control') -> None:
        """
        \python_func{ controlUp(control) } Set's the controls up navigation.

        :param control: control object - control to navigate to on up.
        :raises TypeError: if one of the supplied arguments is not a control type.
        :raises ReferenceError: if one of the controls is not added to a window.

        .. note::
            You can also use `setNavigation()`. Set to self to disable
            navigation.

        Example::

            ...
            self.button.controlUp(self.button1)
            ...
        """
        pass
    
    def controlDown(self, control: 'Control') -> None:
        """
        \python_func{ controlDown(control) } Set's the controls down navigation.

        :param control: control object - control to navigate to on down.
        :raises TypeError: if one of the supplied arguments is not a control type.
        :raises ReferenceError: if one of the controls is not added to a window.

        .. note::
            You can also use `setNavigation()`. Set to self to disable
            navigation.

        Example::

            ...
            self.button.controlDown(self.button1)
            ...
        """
        pass
    
    def controlLeft(self, control: 'Control') -> None:
        """
        \python_func{ controlLeft(control) } Set's the controls left navigation.

        :param control: control object - control to navigate to on left.
        :raises TypeError: if one of the supplied arguments is not a control type.
        :raises ReferenceError: if one of the controls is not added to a window.

        .. note::
            You can also use `setNavigation()`. Set to self to disable
            navigation.

        Example::

            ...
            self.button.controlLeft(self.button1)
            ...
        """
        pass
    
    def controlRight(self, control: 'Control') -> None:
        """
        \python_func{ controlRight(control) } Set's the controls right navigation.

        :param control: control object - control to navigate to on right.
        :raises TypeError: if one of the supplied arguments is not a control type.
        :raises ReferenceError: if one of the controls is not added to a window.

        .. note::
            You can also use `setNavigation()`. Set to self to disable
            navigation.

        Example::

            ...
            self.button.controlRight(self.button1)
            ...
        """
        pass
    

class ControlSpin(Control):
    """
    **Used for cycling up/down controls.**

    Offers classes and functions that manipulate the add-on gui controls.

    \python_class{ ControlSpin() }

    **Code based skin access.**

    The spin control is used for when a list of options can be chosen (such as a
    page up/down control). You can choose the position, size, and look of the spin
    control.

    .. note::
        This class include also all calls from `Control`

    **Not working yet**. You can't create this object, it is returned by objects
    like `ControlTextBox` and `ControlList`.
    """
    
    def __init__(self) -> None:
        pass
    
    def setTextures(self, up: str,
                    down: str,
                    upFocus: str,
                    downFocus: str,
                    upDisabled: str,
                    downDisabled: str) -> None:
        """
        \python_func{ setTextures(up, down, upFocus, downFocus) } Set's textures for
        this control.

        Texture are image files that are used for example in the skin

        **Not working yet**.

        :param up: label - for the up arrow when it doesn't have focus.
        :param down: label - for the down button when it is not focused.
        :param upFocus: label - for the up button when it has focus.
        :param downFocus: label - for the down button when it has focus.
        :param upDisabled: label - for the up arrow when the button is disabled.
        :param downDisabled: label - for the up arrow when the button is disabled.

        Example::

            ...
            # setTextures(up, down, upFocus, downFocus, upDisabled, downDisabled)
            
            ...
        """
        pass
    

class ControlLabel(Control):
    """
    **Used to show some lines of text.**

    \python_class{`ControlLabel`(x, y, width, height, label[, font, textColor,
    disabledColor, alignment, hasPath, angle]) }

    The label control is used for displaying text in Kodi. You can choose the font,
    size, colour, location and contents of the text to be displayed.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param label: string or unicode - text string.
    :param font: [opt] string - font used for label text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of label  Flags for alignment used as bits
        to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    :param hasPath: [opt] bool - True=stores a path / False=no path
    :param angle: [opt] integer - angle of control. (**+** rotates CCW, **-** rotates C)

    Example::

        ...
        # ControlLabel(x, y, width, height, label[, font, textColor,
        #              disabledColor, alignment, hasPath, angle])
        self.label = xbmcgui.ControlLabel(100, 250, 125, 75, 'Status', angle=45)
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 label: str,
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 alignment: int = 0,
                 hasPath: bool = False,
                 angle: int = 0) -> None:
        pass
    
    def getLabel(self) -> str:
        """
        \python_func{`getLabel()` } Returns the text value for this label.

        :return: This label

        Example::

            ...
            label = self.label.getLabel()
            ...
        """
        return ""
    
    def setLabel(self, label: str = "",
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None,
                 label2: str = "") -> None:
        """
        \python_func{ setLabel(label[, font, textColor, disabledColor, shadowColor,
        focusedColor, label2]) } Set's text for this label.

        :param label: string or unicode - text string.
        :param font: [opt] string - font used for label text. (e.g. 'font13')
        :param textColor: [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow. (e.g.
            '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label. (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.label.setLabel('Status')
            ...
        """
        pass
    

class ControlEdit(Control):
    """
    **Used as an input control for the osd keyboard and other input fields.**

    \python_class{`ControlEdit`(x, y, width, height, label[, font, textColor,
    disabledColor, alignment, focusTexture, noFocusTexture]) }

    The edit control allows a user to input text in Kodi. You can choose the font,
    size, colour, location and header of the text to be displayed.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param label: string or unicode - text string.
    :param font: [opt] string - font used for label text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of label  Flags for alignment used as bits
        to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    :param focusTexture: [opt] string - filename for focus texture.
    :param noFocusTexture: [opt] string - filename for no focus texture.

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

     @python_v18 Deprecated **isPassword** @python_v19
    Removed **isPassword**Example::

        ...
        self.edit = xbmcgui.ControlEdit(100, 250, 125, 75, 'Status')
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 label: str,
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 _alignment: int = 0,
                 focusTexture: Optional[str] = None,
                 noFocusTexture: Optional[str] = None) -> None:
        pass
    
    def setLabel(self, label: str = "",
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None,
                 label2: str = "") -> None:
        """
        \python_func{ setLabel(label[, font, textColor, disabledColor, shadowColor,
        focusedColor, label2]) } Set's text heading for this edit control.

        :param label: string or unicode - text string.
        :param font: [opt] string - font used for label text. (e.g. 'font13')
        :param textColor: [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow. (e.g.
            '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label. (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.edit.setLabel('Status')
            ...
        """
        pass
    
    def getLabel(self) -> str:
        """
        \python_func{`getLabel()` } Returns the text heading for this edit control.

        :return: Heading text

        Example::

            ...
            label = self.edit.getLabel()
            ...
        """
        return ""
    
    def setText(self, text: str) -> None:
        """
        \python_func{ setText(value) } Set's text value for this edit control.

        :param value: string or unicode - text string.

        Example::

            ...
            self.edit.setText('online')
            ...
        """
        pass
    
    def getText(self) -> str:
        """
        \python_func{`getText()` } Returns the text value for this edit control.

        :return: Text value of control

         @python_v14 New function added.Example::

            ...
            value = self.edit.getText()
            ...
        """
        return ""
    
    def setType(self, type: int, heading: str) -> None:
        """
        \python_func{ setType(type, heading) } Sets the type of this edit control.

        :param type: integer - type of the edit control.

        ============================================= =========================================== 
        Param                                         Definition                                  
        ============================================= =========================================== 
        xbmcgui.INPUT_TYPE_TEXT                       (standard keyboard)                         
        xbmcgui.INPUT_TYPE_NUMBER                     (format: #)                                 
        xbmcgui.INPUT_TYPE_DATE                       (format: DD/MM/YYYY)                        
        xbmcgui.INPUT_TYPE_TIME                       (format: HH:MM)                             
        xbmcgui.INPUT_TYPE_IPADDRESS                  (format: #.#.#.#)                           
        xbmcgui.INPUT_TYPE_PASSWORD                   (input is masked)                           
        xbmcgui.INPUT_TYPE_PASSWORD_MD5               (input is masked, return md5 hash of input) 
        xbmcgui.INPUT_TYPE_SECONDS                    (format: SS or MM:SS or HH:MM:SS or MM min) 
        xbmcgui.INPUT_TYPE_PASSWORD_NUMBER_VERIFY_NEW (numeric input is masked)                   
        ============================================= =========================================== 

        :param heading: string or unicode - heading that will be used for to numeric or
            keyboard dialog when the edit control is clicked.
         @python_v18 New function added. @python_v19 New option added to mask
        numeric input.Example::

            ...
            self.edit.setType(xbmcgui.INPUT_TYPE_TIME, 'Please enter the time')
            ...
        """
        pass
    

class ControlList(Control):
    """
    **Used for a scrolling lists of items. Replaces the list control.**

    \python_class{`ControlList`(x, y, width, height[, font, textColor,
    buttonTexture, buttonFocusTexture, selectedColor, imageWidth, imageHeight,
    itemTextXOffset, itemTextYOffset, itemHeight, space, alignmentY, shadowColor]) }

    The list container is one of several containers used to display items from file
    lists in various ways. The list container is very flexible - it's only
    restriction is that it is a list - i.e. a single column or row of items. The
    layout of the items is very flexible and is up to the skinner.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param font: [opt] string - font used for items label. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of items label. (e.g. '0xFFFFFFFF')
    :param buttonTexture: [opt] string - filename for focus texture.
    :param buttonFocusTexture: [opt] string - filename for no focus texture.
    :param selectedColor: [opt] integer - x offset of label.
    :param imageWidth: [opt] integer - width of items icon or thumbnail.
    :param imageHeight: [opt] integer - height of items icon or thumbnail.
    :param itemTextXOffset: [opt] integer - x offset of items label.
    :param itemTextYOffset: [opt] integer - y offset of items label.
    :param itemHeight: [opt] integer - height of items.
    :param space: [opt] integer - space between items.
    :param alignmentY: [opt] integer - Y-axis alignment of items label  Flags for alignment
        used as bits to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    :param shadowColor: [opt] hexstring - color of items label's shadow. (e.g. '0xFF000000')

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        self.cList = xbmcgui.ControlList(100, 250, 200, 250, 'font14', space=5)
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 buttonTexture: Optional[str] = None,
                 buttonFocusTexture: Optional[str] = None,
                 selectedColor: Optional[str] = None,
                 _imageWidth: int = 10,
                 _imageHeight: int = 10,
                 _itemTextXOffset: int = 10,
                 _itemTextYOffset: int = 2,
                 _itemHeight: int = 27,
                 _space: int = 2,
                 _alignmentY: int = 4) -> None:
        pass
    
    def addItem(self, item: Union[str, 'ListItem'],
                sendMessage: bool = True) -> None:
        """
        \python_func{ addItem(item) } Add a new item to this list control.

        :param item: string, unicode or `ListItem` - item to add.

        Example::

            ...
            cList.addItem('Reboot Kodi')
            ...
        """
        pass
    
    def addItems(self, items: List[Union[str, 'ListItem']]) -> None:
        """
        \python_func{ addItems(items) } Adds a list of listitems or strings to this list
        control.

        :param items: `List` - list of strings, unicode objects or ListItems to add.

        .. note::
            You can use the above as keywords for arguments.

        Large lists benefit considerably, than using the standard `addItem()`Example::

            ...
            cList.addItems(items=listitems)
            ...
        """
        pass
    
    def selectItem(self, item: int) -> None:
        """
        \python_func{ selectItem(item) } Select an item by index number.

        :param item: integer - index number of the item to select.

        Example::

            ...
            cList.selectItem(12)
            ...
        """
        pass
    
    def removeItem(self, index: int) -> None:
        """
        \python_func{ removeItem(index) } Remove an item by index number.

        :param index: integer - index number of the item to remove.
         @python_v13 New function added.Example::

            ...
            cList.removeItem(12)
            ...
        """
        pass
    
    def reset(self) -> None:
        """
        \python_func{`reset()` } Clear all ListItems in this control list.

        Calling```reset()``` will destroy any```ListItem``` objects in
        the```ControlList``` if not hold by any other class. Make sure you you don't
        call```addItems()``` with the previous```ListItem``` references after
        calling```reset()```. If you need to preserve the```ListItem``` objects
        after```reset()``` make sure you store them as members of your```WindowXML```
        class (see examples).

        **Examples:**

            ...
            cList.reset()
            ...
        The below example shows you how you can reset the```ControlList``` but this time
        avoiding```ListItem``` object destruction. The example assumes ``self`` as
        a```WindowXMLDialog``` instance containing a```ControlList``` with id = 800. The
        class preserves the```ListItem``` objects in a class member variable.

            ...
            # Get all the ListItem objects in the control
            self.list_control = self.getControl(800) # ControlList object
            self.listitems = [self.list_control.getListItem(item) for item in range(0, self.list_control.size())]
            # Reset the ControlList control
            self.list_control.reset()
            #
            # do something with your ListItem objects here (e.g. sorting.)
            # ...
            #
            # Add them again to the ControlList
            self.list_control.addItems(self.listitems)
            ...
        """
        pass
    
    def getSpinControl(self) -> Control:
        """
        \python_func{`getSpinControl()` } Returns the associated `ControlSpin` object.

        Not working completely yet  After adding this control list to a window it is not
        possible to change the settings of this spin control.

        Example::

            ...
            ctl = cList.getSpinControl()
            ...
        """
        return Control()
    
    def getSelectedPosition(self) -> int:
        """
        \python_func{`getSelectedPosition()` } Returns the position of the selected item
        as an integer.

        .. note::
            Returns -1 for empty lists.

        Example::

            ...
            pos = cList.getSelectedPosition()
            ...
        """
        return 0
    
    def getSelectedItem(self) -> 'ListItem':
        """
        \python_func{`getSelectedItem()` } Returns the selected item as a `ListItem`
        object.

        :return: The selected item

        .. note::
            Same as `getSelectedPosition()`, but instead of an integer
            a `ListItem` object is returned. Returns None for empty lists.  See
            windowexample.py on how to use this.

        Example::

            ...
            item = cList.getSelectedItem()
            ...
        """
        return ListItem()
    
    def setImageDimensions(self, imageWidth: int, imageHeight: int) -> None:
        """
        \python_func{ setImageDimensions(imageWidth, imageHeight) } Sets the
        width/height of items icon or thumbnail.

        :param imageWidth: [opt] integer - width of items icon or thumbnail.
        :param imageHeight: [opt] integer - height of items icon or thumbnail.

        Example::

            ...
            cList.setImageDimensions(18, 18)
            ...
        """
        pass
    
    def setSpace(self, space: int) -> None:
        """
        \python_func{ setSpace(space) } Set's the space between items.

        :param space: [opt] integer - space between items.

        Example::

            ...
            cList.setSpace(5)
            ...
        """
        pass
    
    def setPageControlVisible(self, visible: bool) -> None:
        """
        \python_func{ setPageControlVisible(visible) } Sets the spin control's
        visible/hidden state.

        :param visible: boolean - True=visible / False=hidden.

        Example::

            ...
            cList.setPageControlVisible(True)
            ...
        """
        pass
    
    def size(self) -> int:
        """
        \python_func{`size()` } Returns the total number of items in this list control
        as an integer.

        :return: Total number of items

        Example::

            ...
            cnt = cList.size()
            ...
        """
        return 0
    
    def getItemHeight(self) -> int:
        """
        \python_func{`getItemHeight()` } Returns the control's current item height as an
        integer.

        :return: Current item heigh

        Example::

            ..
            item_height = self.cList.getItemHeight()
            ...
        """
        return 0
    
    def getSpace(self) -> int:
        """
        \python_func{`getSpace()` } Returns the control's space between items as an
        integer.

        :return: Space between items

        Example::

            ...
            gap = self.cList.getSpace()
            ...
        """
        return 0
    
    def getListItem(self, index: int) -> 'ListItem':
        """
        \python_func{ getListItem(index) } Returns a given `ListItem` in this `List`.

        :param index: integer - index number of item to return.
        :return: `List` item

        :raises ValueError: if index is out of range.

        Example::

            ...
            listitem = cList.getListItem(6)
            ...
        """
        return ListItem()
    
    def setStaticContent(self, items: List['ListItem']) -> None:
        """
        \python_func{ setStaticContent(items) } Fills a static list with a list of
        listitems.

        :param items: `List` - list of listitems to add.

        .. note::
            You can use the above as keywords for arguments.

        Example::

            ...
            cList.setStaticContent(items=listitems)
            ...
        """
        pass
    

class ControlFadeLabel(Control):
    """
    **Used to show multiple pieces of text in the same position, by fading from one
    to the other.**

    \python_class{ ControlFadeLabel(x, y, width, height[, font, textColor,
    alignment]) }

    The fade label control is used for displaying multiple pieces of text in the
    same space in Kodi. You can choose the font, size, colour, location and contents
    of the text to be displayed. The first piece of information to display fades in
    over 50 frames, then scrolls off to the left. Once it is finished scrolling off
    screen, the second piece of information fades in and the process repeats. A fade
    label control is not supported in a list container.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param font: [opt] string - font used for label text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of fadelabel's labels. (e.g. '0xFFFFFFFF')
    :param alignment: [opt] integer - alignment of label  Flags for alignment used as bits
        to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        self.fadelabel = xbmcgui.ControlFadeLabel(100, 250, 200, 50, textColor='0xFFFFFFFF')
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 _alignment: int = 0) -> None:
        pass
    
    def addLabel(self, label: str) -> None:
        """
        \python_func{ addLabel(label) } Add a label to this control for scrolling.

        :param label: string or unicode - text string to add.

        .. note::
            To remove added text use```reset()``` for them.

        Example::

            ...
            self.fadelabel.addLabel('This is a line of text that can scroll.')
            ...
        """
        pass
    
    def setScrolling(self, scroll: bool) -> None:
        """
        \python_func{ setScrolling(scroll) } Set scrolling. If set to false, the labels
        won't scroll. Defaults to true.

        :param scroll: boolean - True = enabled / False = disabled

        Example::

            ...
            self.fadelabel.setScrolling(False)
            ...
        """
        pass
    

class ControlTextBox(Control):
    """
    **Used to show a multi-page piece of text.**

    \python_class{ ControlTextBox(x, y, width, height[, font, textColor]) }

    The text box is used for showing a large multipage piece of text in Kodi. You
    can choose the position, size, and look of the text.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param font: [opt] string - font used for text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of textbox's text. (e.g. '0xFFFFFFFF')

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        # ControlTextBox(x, y, width, height[, font, textColor])
        self.textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor='0xFFFFFFFF')
        ...
    As stated above, the GUI control is only created once added to a window. The
    example below shows how a `ControlTextBox` can be created, added to the current
    window and have some of its properties changed.

    ///**Extended example:**

        ...
        textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor='0xFFFFFFFF')
        window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
        window.addControl(textbox)
        textbox.setText("My Text Box")
        textbox.scroll()
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 font: Optional[str] = None,
                 textColor: Optional[str] = None) -> None:
        pass
    
    def setText(self, text: str) -> None:
        """
        \python_func{ setText(text) } Set's the text for this textbox.

        :param text: string - text string.

        .. note::
            setText only has effect after the control is added to a window

        Example::

            ...
            # setText(text)
            self.textbox.setText('This is a line of text that can wrap.')
            ...
        """
        pass
    
    def getText(self) -> str:
        """
        \python_func{`getText()` } Returns the text value for this textbox.

        :return: To get text from box

        .. note::
            getText only works after you add the control to a window and set
            the control text (using `setText`).

        Example::

            ...
            # getText()
            text = self.text.getText()
            ...
        """
        return ""
    
    def reset(self) -> None:
        """
        \python_func{`reset()` } Clear's this textbox.

        .. note::
            reset only works after you add the control to a window.

        Example::

            ...
            # reset()
            self.textbox.reset()
            ...
        """
        pass
    
    def scroll(self, id: int) -> None:
        """
        \python_func{ scroll(id) } Scrolls to the given position.

        :param id: integer - position to scroll to.

        .. note::
            `scroll()` only works after the control is added to a window.

        Example::

            ...
            # scroll(position)
            self.textbox.scroll(10)
            ...
        """
        pass
    
    def autoScroll(self, delay: int, time: int, repeat: int) -> None:
        """
        \python_func{ autoScroll(delay, time, repeat) } Set autoscrolling times.

        :param delay: integer - Scroll delay (in ms)
        :param time: integer - Scroll time (in ms)
        :param repeat: integer - Repeat time

        .. note::
            autoScroll only works after you add the control to a window.

         @python_v15 New function added.Example::

            ...
            self.textbox.autoScroll(1, 2, 1)
            ...
        """
        pass
    

class ControlImage(Control):
    """
    **Used to show an image.**

    \python_class{ ControlImage(x, y, width, height, filename[, aspectRatio,
    colorDiffuse]) }

    The image control is used for displaying images in Kodi. You can choose the
    position, size, transparency and contents of the image to be displayed.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param filename: string - image filename.
    :param aspectRatio: [opt] integer - (values 0 = stretch (default), 1 = scale up (crops), 2
        = scale down (black bar)
    :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        # ControlImage(x, y, width, height, filename[, aspectRatio, colorDiffuse])
        self.image = xbmcgui.ControlImage(100, 250, 125, 75, aspectRatio=2)
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 filename: str,
                 aspectRatio: int = 0,
                 colorDiffuse: Optional[str] = None) -> None:
        pass
    
    def setImage(self, imageFilename: str, useCache: bool = True) -> None:
        """
        \python_func{ setImage(filename[, useCache]) } Changes the image.

        :param filename: string - image filename.
        :param useCache: [opt] bool - True=use cache (default) / False=don't use cache.
         @python_v13 Added new option **useCache**.Example::

            ...
            # setImage(filename[, useCache])
            self.image.setImage('special://home/scripts/test.png')
            self.image.setImage('special://home/scripts/test.png', False)
            ...
        """
        pass
    
    def setColorDiffuse(self, hexString: str) -> None:
        """
        \python_func{ setColorDiffuse(colorDiffuse) } Changes the images color.

        :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

        Example::

            ...
            # setColorDiffuse(colorDiffuse)
            self.image.setColorDiffuse('0xC0FF0000')
            ...
        """
        pass
    

class ControlProgress(Control):
    """
    **Used to show the progress of a particular operation.**

    \python_class{ ControlProgress(x, y, width, height, filename[, texturebg,
    textureleft, texturemid, textureright, textureoverlay]) }

    The progress control is used to show the progress of an item that may take a
    long time, or to show how far through a movie you are. You can choose the
    position, size, and look of the progress control.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param filename: string - image filename.
    :param texturebg: [opt] string - specifies the image file whichshould be displayed in
        the background of the progress control.
    :param textureleft: [opt] string - specifies the image file whichshould be displayed for
        the left side of the progress bar. This is rendered on the left
        side of the bar.
    :param texturemid: [opt] string - specifies the image file which should be displayed for
        the middl portion of the progress bar. This is the ``fill`` texture
        used to fill up the bar. It's positioned on the right of
        the``<lefttexture>`` texture, and fills the gap between
        the``<lefttexture>`` and``<righttexture>`` textures, depending on
        how far progressed the item is.
    :param textureright: [opt] string - specifies the image file which should be displayed for
        the right side of the progress bar. This is rendered on the right
        side of the bar.
    :param textureoverlay: [opt] string - specifies the image file which should be displayed over
        the top of all other images in the progress bar. It is centered
        vertically and horizontally within the space taken up by the
        background image.

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        # ControlProgress(x, y, width, height, filename[, texturebg, textureleft, texturemid, textureright, textureoverlay])
        self.image = xbmcgui.ControlProgress(100, 250, 250, 30, 'special://home/scripts/test.png')
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 texturebg: Optional[str] = None,
                 textureleft: Optional[str] = None,
                 texturemid: Optional[str] = None,
                 textureright: Optional[str] = None,
                 textureoverlay: Optional[str] = None) -> None:
        pass
    
    def setPercent(self, pct: float) -> None:
        """
        \python_func{ setPercent(percent) } Sets the percentage of the progressbar to
        show.

        :param percent: float - percentage of the bar to show.

        .. note::
            valid range for percent is 0-100

        Example::

            ...
            # setPercent(percent)
            self.progress.setPercent(60)
            ...
        """
        pass
    
    def getPercent(self) -> float:
        """
        \python_func{`getPercent()` } Returns a float of the percent of the progress.

        :return: Percent position

        Example::

            ...
            # getPercent()
            print(self.progress.getPercent())
            ...
        """
        return 0.0
    

class ControlButton(Control):
    """
    **A standard push button control.**

    \python_class{`ControlButton`(x, y, width, height, label[, focusTexture,
    noFocusTexture, textOffsetX, textOffsetY, alignment, font, textColor,
    disabledColor, angle, shadowColor, focusedColor]) }

    The button control is used for creating push buttons in Kodi. You can choose the
    position, size, and look of the button, as well as choosing what action(s)
    should be performed when pushed.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param label: string or unicode - text string.
    :param focusTexture: [opt] string - filename for focus texture.
    :param noFocusTexture: [opt] string - filename for no focus texture.
    :param textOffsetX: [opt] integer - x offset of label.
    :param textOffsetY: [opt] integer - y offset of label.
    :param alignment: [opt] integer - alignment of label  Flags for alignment used as bits
        to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    :param font: [opt] string - font used for label text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of enabled button's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled button's label. (e.g.
        '0xFFFF3300')
    :param angle: [opt] integer - angle of control. (+ rotates CCW, - rotates CW)
    :param shadowColor: [opt] hexstring - color of button's label's shadow. (e.g.
        '0xFF000000')
    :param focusedColor: [opt] hexstring - color of focused button's label. (e.g. '0xFF00FFFF')

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

    Example::

        ...
        # ControlButton(x, y, width, height, label[, focusTexture, noFocusTexture, textOffsetX, textOffsetY,
        #               alignment, font, textColor, disabledColor, angle, shadowColor, focusedColor])
        self.button = xbmcgui.ControlButton(100, 250, 200, 50, 'Status', font='font14')
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 label: str,
                 focusTexture: Optional[str] = None,
                 noFocusTexture: Optional[str] = None,
                 textOffsetX: int = 10,
                 textOffsetY: int = 2,
                 alignment: int = (0|4),
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 angle: int = 0,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None) -> None:
        pass
    
    def setLabel(self, label: str = "",
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None,
                 label2: str = "") -> None:
        """
        \python_func{ setLabel([label, font, textColor, disabledColor, shadowColor,
        focusedColor, label2]) } Set's this buttons text attributes.

        :param label: [opt] string or unicode - text string.
        :param font: [opt] string - font used for label text. (e.g. 'font13')
        :param textColor: [opt] hexstring - color of enabled button's label. (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled button's label. (e.g.
            '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow. (e.g.
            '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label. (e.g. '0xFFFFFF00')
        :param label2: [opt] string or unicode - text string.

        .. note::
            You can use the above as keywords for arguments and skip certain
            optional arguments.  Once you use a keyword, all following
            arguments require the keyword.

        Example::

            ...
            # setLabel([label, font, textColor, disabledColor, shadowColor, focusedColor])
            self.button.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setDisabledColor(self, color: str) -> None:
        """
        \python_func{ setDisabledColor(disabledColor) } Set's this buttons disabled
        color.

        :param disabledColor: hexstring - color of disabled button's label. (e.g. '0xFFFF3300')

        Example::

            ...
            # setDisabledColor(disabledColor)
            self.button.setDisabledColor('0xFFFF3300')
            ...
        """
        pass
    
    def getLabel(self) -> str:
        """
        \python_func{`getLabel()` } Returns the buttons label as a unicode string.

        :return: Unicode string

        Example::

            ...
            # getLabel()
            label = self.button.getLabel()
            ...
        """
        return ""
    
    def getLabel2(self) -> str:
        """
        \python_func{`getLabel2()` } Returns the buttons label2 as a string.

        :return: string of label 2

        Example::

            ...
            # getLabel2()
            label = self.button.getLabel2()
            ...
        """
        return ""
    

class ControlGroup(Control):
    """
    **Used to group controls together..**

    \python_class{ ControlGroup(x, y, width, height) }

    The group control is one of the most important controls. It allows you to group
    controls together, applying attributes to all of them at once. It also remembers
    the last navigated button in the group, so you can set the ``<onup>`` of a
    control to a group of controls to have it always go back to the one you were at
    before. It also allows you to position controls more accurately relative to each
    other, as any controls within a group take their coordinates from the group's
    top left corner (or from elsewhere if you use the ``r`` attribute). You can
    have as many groups as you like within the skin, and groups within groups are
    handled with no issues.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.

    Example::

        ...
        self.group = xbmcgui.ControlGroup(100, 250, 125, 75)
        ...
    """
    
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        pass
    

class ControlRadioButton(Control):
    """
    **For control a radio button (as used for on/off settings).**

    \python_class{`ControlRadioButton`(x, y, width, height, label[, focusOnTexture,
    noFocusOnTexture, focusOffTexture, noFocusOffTexture, textOffsetX, textOffsetY,
    alignment, font, textColor, disabledColor]) }

    The radio button control is used for creating push button on/off settings in
    Kodi. You can choose the position, size, and look of the button. When the user
    clicks on the radio button, the state will change, toggling the extra textures
    (textureradioon and textureradiooff). Used for settings controls.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control.
    :param y: integer - y coordinate of control.
    :param width: integer - width of control.
    :param height: integer - height of control.
    :param label: string or unicode - text string.
    :param focusOnTexture: [opt] string - filename for radio ON focused texture.
    :param noFocusOnTexture: [opt] string - filename for radio ON not focused texture.
    :param focusOfTexture: [opt] string - filename for radio OFF focused texture.
    :param noFocusOffTexture: [opt] string - filename for radio OFF not focused texture.
    :param textOffsetX: [opt] integer - horizontal text offset
    :param textOffsetY: [opt] integer - vertical text offset
    :param alignment: [opt] integer - alignment of label  Flags for alignment used as bits
        to have several together:

    ================ ========== ============== 
    Defination name  Bitflag    Description    
    ================ ========== ============== 
    XBFONT_LEFT      0x00000000 Align X left   
    XBFONT_RIGHT     0x00000001 Align X right  
    XBFONT_CENTER_X  0x00000002 Align X center 
    XBFONT_CENTER_Y  0x00000004 Align Y center 
    XBFONT_TRUNCATED 0x00000008 Truncated text 
    XBFONT_JUSTIFIED 0x00000010 Justify text   
    ================ ========== ============== 

    :param font: [opt] string - font used for label text. (e.g. 'font13')
    :param textColor: [opt] hexstring - color of label when control is enabled.
        radiobutton's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of label when control is disabled. (e.g.
        '0xFFFF3300')

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

     @python_v13 New function added. @python_v18
    Deprecated **focusTexture** and **noFocusTexture**.
    Use **focusOnTexture** and **noFocusOnTexture**. @python_v19
    Removed **focusTexture** and **noFocusTexture**.Example::

        ...
        self.radiobutton = xbmcgui.ControlRadioButton(100, 250, 200, 50, 'Enable', font='font14')
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 label: str,
                 focusOnTexture: Optional[str] = None,
                 noFocusOnTexture: Optional[str] = None,
                 focusOffTexture: Optional[str] = None,
                 noFocusOffTexture: Optional[str] = None,
                 textOffsetX: int = 10,
                 textOffsetY: int = 2,
                 _alignment: int = (0|4),
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 angle: int = 0,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None,
                 disabledOnTexture: Optional[str] = None,
                 disabledOffTexture: Optional[str] = None) -> None:
        pass
    
    def setSelected(self, selected: bool) -> None:
        """
        \python_func{ setSelected(selected) }**Sets the radio buttons's selected
        status.**

        :param selected: bool - True=selected (on) / False=not selected (off)

        .. note::
            You can use the above as keywords for arguments and skip certain
            optional arguments.  Once you use a keyword, all following
            arguments require the keyword.

        Example::

            ...
            self.radiobutton.setSelected(True)
            ...
        """
        pass
    
    def isSelected(self) -> bool:
        """
        \python_func{`isSelected()` } Returns the radio buttons's selected status.

        :return: True if selected on

        Example::

            ...
            is = self.radiobutton.isSelected()
            ...
        """
        return True
    
    def setLabel(self, label: str = "",
                 font: Optional[str] = None,
                 textColor: Optional[str] = None,
                 disabledColor: Optional[str] = None,
                 shadowColor: Optional[str] = None,
                 focusedColor: Optional[str] = None,
                 label2: str = "") -> None:
        """
        \python_func{ setLabel(label[, font, textColor, disabledColor, shadowColor,
        focusedColor]) } Set's the radio buttons text attributes.

        :param label: string or unicode - text string.
        :param font: [opt] string - font used for label text. (e.g. 'font13')
        :param textColor: [opt] hexstring - color of enabled radio button's label. (e.g.
            '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled radio button's label. (e.g.
            '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of radio button's label's shadow. (e.g.
            '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused radio button's label. (e.g.
            '0xFFFFFF00')

        .. note::
            You can use the above as keywords for arguments and skip certain
            optional arguments.  Once you use a keyword, all following
            arguments require the keyword.

        Example::

            ...
            # setLabel(label[, font, textColor, disabledColor, shadowColor, focusedColor])
            self.radiobutton.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setRadioDimension(self, x: int,
                          y: int,
                          width: int,
                          height: int) -> None:
        """
        \python_func{ setRadioDimension(x, y, width, height) } Sets the radio buttons's
        radio texture's position and size.

        :param x: integer - x coordinate of radio texture.
        :param y: integer - y coordinate of radio texture.
        :param width: integer - width of radio texture.
        :param height: integer - height of radio texture.

        .. note::
            You can use the above as keywords for arguments and skip certain
            optional arguments.  Once you use a keyword, all following
            arguments require the keyword.

        Example::

            ...
            self.radiobutton.setRadioDimension(x=100, y=5, width=20, height=20)
            ...
        """
        pass
    

class ControlSlider(Control):
    """
    **Used for a volume slider.**

    \python_class{ ControlSlider(x, y, width, height[, textureback, texture,
    texturefocus, orientation]) }

    The slider control is used for things where a sliding bar best represents the
    operation at hand (such as a volume control or seek control). You can choose the
    position, size, and look of the slider control.

    .. note::
        This class include also all calls from `Control`

    :param x: integer - x coordinate of control
    :param y: integer - y coordinate of control
    :param width: integer - width of control
    :param height: integer - height of control
    :param textureback: [opt] string - image filename
    :param texture: [opt] string - image filename
    :param texturefocus: [opt] string - image filename
    :param orientation: [opt] integer - orientation of slider (xbmcgui.HORIZONTAL /
        xbmcgui.VERTICAL (default))

    .. note::
        You can use the above as keywords for arguments and skip certain
        optional arguments.  Once you use a keyword, all following
        arguments require the keyword.  After you create the control, you
        need to add it to the window with addControl().

     @python_v17 **orientation** option added.Example::

        ...
        self.slider = xbmcgui.ControlSlider(100, 250, 350, 40)
        ...
    """
    
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 textureback: Optional[str] = None,
                 texture: Optional[str] = None,
                 texturefocus: Optional[str] = None,
                 orientation: int = 1) -> None:
        pass
    
    def getPercent(self) -> float:
        """
        \python_func{`getPercent()` } Returns a float of the percent of the slider.

        :return: float - Percent of slider

        Example::

            ...
            print(self.slider.getPercent())
            ...
        """
        return 0.0
    
    def setPercent(self, pct: float) -> None:
        """
        \python_func{ setPercent(pct) } Sets the percent of the slider.

        :param pct: float - Percent value of slider

        Example::

            ...
            self.slider.setPercent(50)
            ...
        """
        pass
    
    def getInt(self) -> int:
        """
        \python_func{`getInt()` } Returns the value of the slider.

        :return: int - value of slider

         @python_v18 New function added.Example::

            ...
            print(self.slider.getInt())
            ...
        """
        return 0
    
    def setInt(self, value: int, min: int, delta: int, max: int) -> None:
        """
        \python_func{ setInt(value, min, delta, max) } Sets the range, value and step
        size of the slider.

        :param value: int - value of slider
        :param min: int - min of slider
        :param delta: int - step size of slider
        :param max: int - max of slider
         @python_v18 New function added.Example::

            ...
            self.slider.setInt(450, 200, 10, 900)
            ...
        """
        pass
    
    def getFloat(self) -> float:
        """
        \python_func{`getFloat()` } Returns the value of the slider.

        :return: float - value of slider

         @python_v18 New function added.Example::

            ...
            print(self.slider.getFloat())
            ...
        """
        return 0.0
    
    def setFloat(self, value: float,
                 min: float,
                 delta: float,
                 max: float) -> None:
        """
        \python_func{ setFloat(value, min, delta, max) } Sets the range, value and step
        size of the slider.

        :param value: float - value of slider
        :param min: float - min of slider
        :param delta: float - step size of slider
        :param max: float - max of slider
         @python_v18 New function added.Example::

            ...
            self.slider.setFloat(15.0, 10.0, 1.0, 20.0)
            ...
        """
        pass
    

class Dialog:
    """
    **Kodi's dialog class**

    The graphical control element dialog box (also called dialogue box or just
    dialog) is a small window that communicates information to the user and prompts
    them for a response.
    """
    
    def __init__(self) -> None:
        pass
    
    def yesno(self, heading: str,
              message: str,
              nolabel: str = "",
              yeslabel: str = "",
              customlabel: str = "",
              autoclose: int = 0) -> bool:
        """
        \python_func{ xbmcgui.Dialog().yesno(heading, message, nolabel, yeslabel,
        customlabel, autoclose]) }**Yes / no dialog **

        The Yes / No dialog can be used to inform the user about questions and get the
        answer.

        :param heading: string or unicode - dialog heading.
        :param message: string or unicode - message text.
        :param nolabel: [opt] label to put on the no button.
        :param yeslabel: [opt] label to put on the yes button.
        :param customlabel: [opt] label to put on the custom button.
        :param autoclose: [opt] integer - milliseconds to autoclose dialog. (default=do not
            autoclose)
        :return: Returns True if 'Yes' was pressed, else False.

         @python_v13 Added new option**autoclose **. @python_v19 Renamed
        option**line1 ** to**message **. @python_v19 Removed option**line2 **.
        @python_v19 Removed option**line3 **. @python_v19 Added new
        option**customlabel**.Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Kodi', 'Do you want to exit this script?')
            ..
        """
        return True
    
    def info(self, item: 'ListItem') -> bool:
        """
        \python_func{ xbmcgui.Dialog().info(listitem) }**Info dialog**

        Show the corresponding info dialog for a given listitem

        :param listitem: `xbmcgui.ListItem` -`ListItem` to show info for.
        :return: Returns whether the dialog opened successfully.

         @python_v17 New function added.Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.info(listitem)
            ..
        """
        return True
    
    def select(self, heading: str,
               list: List[Union[str, 'ListItem']],
               autoclose: int = 0,
               preselect: int = -1,
               useDetails: bool = False) -> int:
        """
        \python_func{ xbmcgui.Dialog().select(heading, list[, autoclose, preselect,
        useDetails]) }**Select dialog **

        Show of a dialog to select of an entry as a key

        :param heading: string or unicode - dialog heading.
        :param list: list of strings / xbmcgui.ListItems - list of items shown in dialog.
        :param autoclose: [opt] integer - milliseconds to autoclose dialog. (default=do not
            autoclose)
        :param preselect: [opt] integer - index of preselected item. (default=no preselected
            item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the position of the highlighted item as an integer.

         @python_v17**preselect ** option added. @python_v17 Added new
        option**useDetails **. @python_v17 Allow listitems for
        parameter**list**Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.select('Choose a playlist', ['Playlist #1', 'Playlist #2, 'Playlist #3'])
            ..
        """
        return 0
    
    def contextmenu(self, list: List[str]) -> int:
        """
        \python_func{ xbmcgui.Dialog().contextmenu(list) } Show a context menu.

        :param list: string list - list of items.
        :return: the position of the highlighted item as an integer (-1 if cancelled).

         @python_v17 New function addedExample::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.contextmenu(['Option #1', 'Option #2', 'Option #3'])
            ..
        """
        return 0
    
    def multiselect(self, heading: str,
                    options: List[Union[str, 'ListItem']],
                    autoclose: int = 0,
                    preselect: Optional[List[int]] = None,
                    useDetails: bool = False) -> List[int]:
        """
        \python_func{ xbmcgui.Dialog().multiselect(heading, options[, autoclose,
        preselect, useDetails]) } Show a multi-select dialog.

        :param heading: string or unicode - dialog heading.
        :param options: list of strings / xbmcgui.ListItems - options to choose from.
        :param autoclose: [opt] integer - milliseconds to autoclose dialog. (default=do not
            autoclose)
        :param preselect: [opt] list of int - indexes of items to preselect in list (default: do
            not preselect any item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the selected items as a list of indices, or None if cancelled.

         @python_v16 New function added. @python_v17 Added new
        option **preselect**. @python_v17 Added new option **useDetails**.
        @python_v17 Allow listitems for parameter **options**Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.multiselect("Choose something", ["Foo", "Bar", "Baz"], preselect=[1,2])
            ..
        """
        return [0]
    
    def ok(self, heading: str, message: str) -> bool:
        """
        \python_func{ xbmcgui.Dialog().ok(heading, message) }**OK dialog **

        The functions permit the call of a dialog of information, a confirmation of the
        user by press from OK required.

        :param heading: string or unicode - dialog heading.
        :param message: string or unicode - message text.
        :return: Returns True if 'Ok' was pressed, else False.

         @python_v19 Renamed option**line1 ** to**message **. @python_v19
        Removed option**line2 **. @python_v19 Removed option**line3**.Example::

            ..
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Kodi', 'There was an error.')
            ..
        """
        return True
    
    def textviewer(self, heading: str,
                   text: str,
                   usemono: bool = False) -> None:
        """
        \python_func{ xbmcgui.Dialog().textviewer(heading, text, usemono) }**TextViewer
        dialog **

        The text viewer dialog can be used to display descriptions, help texts or other
        larger texts.

        :param heading: string or unicode - dialog heading.
        :param text: string or unicode - text.
        :param usemono: [opt] bool - use monospace font
         @python_v16 New function added. @python_v18 New optional param
        added**usemono**.Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.textviewer('Plot', 'Some movie plot.')
            ..
        """
        pass
    
    def browse(self, type: int,
               heading: str,
               shares: str,
               mask: str = "",
               useThumbs: bool = False,
               treatAsFolder: bool = False,
               defaultt: str = "",
               enableMultiple: bool = False) -> Union[str, List[str]]:
        """
        \python_func{ xbmcgui.Dialog().browse(type, heading, shares[, mask, useThumbs,
        treatAsFolder, defaultt, enableMultiple]) }**Browser dialog**

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers all
        support file types.

        :param type: integer - the type of browse dialog.

        ===== ============================ 
        Param Name                         
        ===== ============================ 
        0     ShowAndGetDirectory          
        1     ShowAndGetFile               
        2     ShowAndGetImage              
        3     ShowAndGetWriteableDirectory 
        ===== ============================ 

        :param heading: string or unicode - dialog heading.
        :param shares: string or unicode - fromsources.xml

        ========== ============================================= 
        Param      Name                                          
        ========== ============================================= 
        "programs" list program addons                           
        "video"    list video sources                            
        "music"    list music sources                            
        "pictures" list picture sources                          
        "files"    list file sources (added through filemanager) 
        "games"    list game sources                             
        "local"    list local drives                             
        ""         list local drives and network shares          
        ========== ============================================= 

        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if files exist.
        :param treatAsFolder: [opt] boolean - if True playlists and archives act as folders.
        :param defaultt: [opt] string - default path or file.
        :param enableMultiple: [opt] boolean - if True multiple file selection is enabled.
        :return: If enableMultiple is False (default): returns filename and/or path as a string to the location of the highlighted item, if user pressed 'Ok' or a masked item was selected. Returns the default value if dialog was canceled. If enableMultiple is True: returns tuple of marked filenames as a string if user pressed 'Ok' or a masked item was selected. Returns empty tuple if dialog was canceled.

         If type is 0 or 3 the enableMultiple parameter is ignore

         @python_v18 New option added to browse network and/or local drives.Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browse(3, 'Kodi', 'files', '', False, False, False, 'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseSingle(self, type: int,
                     heading: str,
                     shares: str,
                     mask: str = "",
                     useThumbs: bool = False,
                     treatAsFolder: bool = False,
                     defaultt: str = "") -> str:
        """
        \python_func{ xbmcgui.Dialog().browseSingle(type, heading, shares[, mask,
        useThumbs, treatAsFolder, defaultt]) }**Browse single dialog**

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers all
        support file types.

        :param type: integer - the type of browse dialog.

        ===== ============================ 
        Param Name                         
        ===== ============================ 
        0     ShowAndGetDirectory          
        1     ShowAndGetFile               
        2     ShowAndGetImage              
        3     ShowAndGetWriteableDirectory 
        ===== ============================ 

        :param heading: string or unicode - dialog heading.
        :param shares: string or unicode - fromsources.xml

        ========== ============================================= 
        Param      Name                                          
        ========== ============================================= 
        "programs" list program addons                           
        "video"    list video sources                            
        "music"    list music sources                            
        "pictures" list picture sources                          
        "files"    list file sources (added through filemanager) 
        "games"    list game sources                             
        "local"    list local drives                             
        ""         list local drives and network shares          
        ========== ============================================= 

        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if files exist
            (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives act as folders
            (default=false).
        :param defaultt: [opt] string - default path or file.
        :return: Returns filename and/or path as a string to the location of the highlighted item, if user pressed 'Ok' or a masked item was selected. Returns the default value if dialog was canceled.

         @python_v18 New option added to browse network and/or local drives.Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseSingle(3, 'Kodi', 'files', '', False, False, 'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseMultiple(self, type: int,
                       heading: str,
                       shares: str,
                       mask: str = "",
                       useThumbs: bool = False,
                       treatAsFolder: bool = False,
                       defaultt: str = "") -> List[str]:
        """
        \python_func{ xbmcgui.Dialog().browseMultiple(type, heading, shares[, mask,
        useThumbs, treatAsFolder, defaultt]) }**Browser dialog**

        The function offer the possibility to select multiple files by the user of the
        add-on.

        It allows all the options that are possible in Kodi itself and offers all
        support file types.

        :param type: integer - the type of browse dialog.

        ===== =============== 
        Param Name            
        ===== =============== 
        1     ShowAndGetFile  
        2     ShowAndGetImage 
        ===== =============== 

        :param heading: string or unicode - dialog heading.
        :param shares: string or unicode - fromsources.xml

        ========== ============================================= 
        Param      Name                                          
        ========== ============================================= 
        "programs" list program addons                           
        "video"    list video sources                            
        "music"    list music sources                            
        "pictures" list picture sources                          
        "files"    list file sources (added through filemanager) 
        "games"    list game sources                             
        "local"    list local drives                             
        ""         list local drives and network shares          
        ========== ============================================= 

        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if files exist
            (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives act as folders
            (default=false).
        :param defaultt: [opt] string - default path or file.
        :return: Returns tuple of marked filenames as a string," if user pressed 'Ok' or a masked item was selected. Returns empty tuple if dialog was canceled.

         @python_v18 New option added to browse network and/or local drives.Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseMultiple(2, 'Kodi', 'files', '', False, False, 'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return [""]
    
    def numeric(self, type: int,
                heading: str,
                defaultt: str = "",
                bHiddenInput: bool = False) -> str:
        """
        \python_func{ xbmcgui.Dialog().numeric(type, heading[, defaultt, bHiddenInput])
        }**Numeric dialog**

        The function have to be permitted by the user for the representation of a
        numeric keyboard around an input.

        :param type: integer - the type of numeric dialog.

        ===== ======================== ============================ 
        Param Name                     Format                       
        ===== ======================== ============================ 
        0     ShowAndGetNumber         (default format: #)          
        1     ShowAndGetDate           (default format: DD/MM/YYYY) 
        2     ShowAndGetTime           (default format: HH:MM)      
        3     ShowAndGetIPAddress      (default format: #.#.#.#)    
        4     ShowAndVerifyNewPassword (default format: *)          
        ===== ======================== ============================ 

        :param heading: string or unicode - dialog heading (will be ignored for type 4).
        :param defaultt: [opt] string - default value.
        :param bHiddenInput: [opt] bool - mask input (available for type 0).
        :return: Returns the entered data as a string. Returns the default value if dialog was canceled.

         @python_v19 New option added ShowAndVerifyNewPassword. @python_v19
        Added new option **bHiddenInput**.Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.numeric(1, 'Enter date of birth')
            ..
        """
        return ""
    
    def notification(self, heading: str,
                     message: str,
                     icon: str = "",
                     time: int = 0,
                     sound: bool = True) -> None:
        """
        \python_func{ xbmcgui.Dialog().notification(heading, message[, icon, time,
        sound]) } Show a Notification alert.

        :param heading: string - dialog heading.
        :param message: string - dialog message.
        :param icon: [opt] string - icon to use. (default xbmcgui.NOTIFICATION_INFO)
        :param time: [opt] integer - time in milliseconds (default 5000)
        :param sound: [opt] bool - play notification sound (default True)

        Builtin Icons:xbmcgui.NOTIFICATION_INFO

        xbmcgui.NOTIFICATION_WARNING

        xbmcgui.NOTIFICATION_ERROR

         @python_v13 New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_INFO, 5000)
            ..
        """
        pass
    
    def input(self, heading: str,
              defaultt: str = "",
              type: int = INPUT_ALPHANUM,
              option: int = 0,
              autoclose: int = 0) -> str:
        """
        \python_func{ xbmcgui.Dialog().input(heading[, defaultt, type, option,
        autoclose]) } Show an Input dialog.

        :param heading: string - dialog heading.
        :param defaultt: [opt] string - default value. (default=empty string)
        :param type: [opt] integer - the type of keyboard dialog.
            (default=`xbmcgui.INPUT_ALPHANUM`)

        ============================= =========================================== 
        Parameter                     Format                                      
        ============================= =========================================== 
        ```xbmcgui.INPUT_ALPHANUM```  (standard keyboard)                         
        ```xbmcgui.INPUT_NUMERIC```   (format: #)                                 
        ```xbmcgui.INPUT_DATE```      (format: DD/MM/YYYY)                        
        ```xbmcgui.INPUT_TIME```      (format: HH:MM)                             
        ```xbmcgui.INPUT_IPADDRESS``` (format: #.#.#.#)                           
        ```xbmcgui.INPUT_PASSWORD```  (return md5 hash of input, input is masked) 
        ============================= =========================================== 

        :param option: [opt] integer - option for the dialog. (see Options below)  Password
            dialog:  ```xbmcgui.PASSWORD_VERIFY``` (verifies an existing
            (default) md5 hashed password)Alphanum dialog:
            ```xbmcgui.ALPHANUM_HIDE_INPUT``` (masks input)
        :param autoclose: [opt] integer - milliseconds to autoclose dialog. (default=do not
            autoclose)
        :return: Returns the entered data as a string. Returns an empty string if dialog was canceled.

         @python_v13 New function added.Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
            ..
        """
        return ""
    

class DialogProgress:
    """
    **Kodi's progress dialog class (Duh!)**
    """
    
    def __init__(self) -> None:
        pass
    
    def create(self, heading: str, message: str = "") -> None:
        """
        \python_func{ xbmcgui.DialogProgress().create(heading[, message]) } Create and
        show a progress dialog.

        :param heading: string or unicode - dialog heading.
        :param message: [opt] string or unicode - message text.

        .. note::
            Use `update()` to update lines and progressbar.

         @python_v19 Renamed option **line1** to **message**. @python_v19
        Removed option **line2**. @python_v19 Removed option **line3**.Example::

            ..
            pDialog = xbmcgui.DialogProgress()
            pDialog.create('Kodi', 'Initializing script...')
            ..
        """
        pass
    
    def update(self, percent: int, message: str = "") -> None:
        """
        \python_func{ xbmcgui.DialogProgress().update(percent[, message]) } Updates the
        progress dialog.

        :param percent: integer - percent complete. (0:100)
        :param message: [opt] string or unicode - message text.
         @python_v19 Renamed option **line1** to **message**. @python_v19
        Removed option **line2**. @python_v19 Removed option **line3**.Example::

            ..
            pDialog.update(25, 'Importing modules...')
            ..
        """
        pass
    
    def close(self) -> None:
        """
        \python_func{ xbmcgui.DialogProgress().`close()` } Close the progress dialog.

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def iscanceled(self) -> bool:
        """
        \python_func{ xbmcgui.DialogProgress().`iscanceled()` } Checks progress is
        canceled.

        :return: True if the user pressed cancel.

        Example::

            ..
            if (pDialog.iscanceled()): return
            ..
        """
        return True
    

class DialogProgressBG:
    """
    **Kodi's background progress dialog class**
    """
    
    def __init__(self) -> None:
        pass
    
    def deallocating(self) -> None:
        """
        This method is meant to be called from the destructor of the lowest level class.

        It's virtual because it's a convenient place to receive messages that we're
        about to go be deleted but prior to any real tear-down.

        Any overloading classes need to remember to pass the call up the chain.
        """
        pass
    
    def deallocating(self) -> None:
        """
        This method is meant to be called from the destructor of the lowest level class.

        It's virtual because it's a convenient place to receive messages that we're
        about to go be deleted but prior to any real tear-down.

        Any overloading classes need to remember to pass the call up the chain.
        """
        pass
    
    def create(self, heading: str, message: str = "") -> None:
        """
        \python_func{ xbmcgui.DialogProgressBG().create(heading[, message]) } Create and
        show a background progress dialog.

        :param heading: string or unicode - dialog heading.
        :param message: [opt] string or unicode - message text.

        .. note::
            'heading' is used for the dialog's id. Use a unique heading.
            Use `update()` to update heading, message and progressbar.

        Example::

            ..
            pDialog = xbmcgui.DialogProgressBG()
            pDialog.create('Movie Trailers', 'Downloading Monsters Inc... .')
            ..
        """
        pass
    
    def update(self, percent: int = 0,
               heading: str = "",
               message: str = "") -> None:
        """
        \python_func{ xbmcgui.DialogProgressBG().update([percent, heading, message]) }
        Updates the background progress dialog.

        :param percent: [opt] integer - percent complete. (0:100)
        :param heading: [opt] string or unicode - dialog heading.
        :param message: [opt] string or unicode - message text.

        .. note::
            To clear heading or message, you must pass a blank character.

        Example::

            ..
            pDialog.update(25, message='Downloading Finding Nemo ...')
            ..
        """
        pass
    
    def close(self) -> None:
        """
        \python_func{ xbmcgui.DialogProgressBG().`close()` } Close the background
        progress dialog

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def isFinished(self) -> bool:
        """
        \python_func{ xbmcgui.DialogProgressBG().`isFinished()` } Checks progress is
        finished

        :return: True if the background dialog is active.

        Example::

            ..
            if (pDialog.isFinished()): return
            ..
        """
        return True
    

class ListItem:
    """
    **Selectable window list item.**

    The list item control is used for creating item lists in Kodi

    \python_class{ ListItem([label, label2, path]) }

    :param label: [opt] string
    :param label2: [opt] string
    :param path: [opt] string
     @python_v16 **iconImage** and **thumbnailImage** are deprecated.
    Use **setArt()**. @python_v19 Removed **iconImage**
    and **thumbnailImage**. Use **setArt()**.Example::

        ...
        listitem = xbmcgui.ListItem('Casino Royale')
        ...
    """
    
    def __init__(self, label: str = "",
                 label2: str = "",
                 path: str = "",
                 offscreen: bool = False) -> None:
        pass
    
    def getLabel(self) -> str:
        """
        \python_func{`getLabel()` } Returns the listitem label.

        :return: Label of item

        Example::

            ...
            # getLabel()
            label = listitem.getLabel()
            ...
        """
        return ""
    
    def getLabel2(self) -> str:
        """
        \python_func{`getLabel2()` } Returns the second listitem label.

        :return: Second label of item

        Example::

            ...
            # getLabel2()
            label = listitem.getLabel2()
            ...
        """
        return ""
    
    def setLabel(self, label: str) -> None:
        """
        \python_func{ setLabel(label) } Sets the listitem's label.

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel(label)
            listitem.setLabel('Casino Royale')
            ...
        """
        pass
    
    def setLabel2(self, label: str) -> None:
        """
        \python_func{ setLabel2(label) } Sets the listitem's label2.

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel2(label)
            listitem.setLabel2('Casino Royale')
            ...
        """
        pass
    
    def setArt(self, dictionary: Dict[str, str]) -> None:
        """
        \python_func{ setArt(values) } Sets the listitem's art

        :param values: dictionary - pairs of``{ label: value }``.  Some default art values
            (any string possible):

        ========= ======================= 
        Label     Type                    
        ========= ======================= 
        thumb     string - image filename 
        poster    string - image filename 
        banner    string - image filename 
        fanart    string - image filename 
        clearart  string - image filename 
        clearlogo string - image filename 
        landscape string - image filename 
        icon      string - image filename 
        ========= ======================= 

         @python_v13 New function added. @python_v16 Added new label **icon**.Example::

            ...
            # setArt(values)
            listitem.setArt({ 'poster': 'poster.png', 'banner' : 'banner.png' })
            ...
        """
        pass
    
    def setIsFolder(self, isFolder: bool) -> None:
        """
        \python_func{ setIsFolder(isFolder) } Sets if this listitem is a folder.

        :param isFolder: bool - True=folder / False=not a folder (default).
        @python_v18 New function added.

        Example::

            ...
            # setIsFolder(isFolder)
            listitem.setIsFolder(True)
            ...
        """
        pass
    
    def setUniqueIDs(self, dictionary: Dict[str, str],
                     defaultrating: str = "") -> None:
        """
        \python_func{ setUniqueIDs(values, defaultrating) } Sets the listitem's uniqueID

        :param values: dictionary - pairs of``{ label: value }``.
        :param defaultrating: [opt] string - the name of default rating.

        Some example values (any string possible):

        ===== ====================== 
        Label Type                   
        ===== ====================== 
        imdb  string - uniqueid name 
        tvdb  string - uniqueid name 
        tmdb  string - uniqueid name 
        anidb string - uniqueid name 
        ===== ====================== 

        Example::

            ...
            # setUniqueIDs(values, defaultrating)
            listitem.setUniqueIDs({ 'imdb': 'tt8938399', 'tmdb' : '9837493' }, "imdb")
            ...
        """
        pass
    
    def setRating(self, type: str,
                  rating: float,
                  votes: int = 0,
                  defaultt: bool = False) -> None:
        """
        \python_func{ setRating(type, rating, votes = 0, defaultt = False) } Sets a
        listitem's rating. It needs at least type and rating param

        :param type: string - the type of the rating. Any string.
        :param rating: float - the value of the rating.
        :param votes: int - the number of votes. Default 0.
        :param defaultt: bool - is the default rating?. Default False.  Some example type (any
            string possible):

        ===== ==================== 
        Label Type                 
        ===== ==================== 
        imdb  string - rating type 
        tvdb  string - rating type 
        tmdb  string - rating type 
        anidb string - rating type 
        ===== ==================== 

        Example::

            ...
            # setRating(type, rating, votes, defaultt))
            listitem.setRating("imdb", 4.6, 8940, True)
            ...
        """
        pass
    
    def addSeason(self, number: int, name: str = "") -> None:
        """
        \python_func{ addSeason(number, name = "") } Add a season with name to a
        listitem. It needs at least the season number

        :param number: int - the number of the season.
        :param name: string - the name of the season. Default "".
        @python_v18 New function added.

        Example::

            ...
            # addSeason(number, name))
            listitem.addSeason(1, "Murder House")
            ...
        """
        pass
    
    def getArt(self, key: str) -> str:
        """
        \python_func{`getArt(key)` } Returns a listitem art path as a string, similar to
        an infolabel.

        :param key: string - art name.  Some default art values (any string possible):

        ========= =================== 
        Label     Type                
        ========= =================== 
        thumb     string - image path 
        poster    string - image path 
        banner    string - image path 
        fanart    string - image path 
        clearart  string - image path 
        clearlogo string - image path 
        landscape string - image path 
        icon      string - image path 
        ========= =================== 

         @python_v17 New function added.Example::

            ...
            poster = listitem.getArt('poster')
            ...
        """
        return ""
    
    def getUniqueID(self, key: str) -> str:
        """
        \python_func{`getUniqueID(key)` } Returns a listitem uniqueID as a string,
        similar to an infolabel.

        :param key: string - uniqueID name.  Some default uniqueID values (any string
            possible):

        ===== ====================== 
        Label Type                   
        ===== ====================== 
        imdb  string - uniqueid name 
        tvdb  string - uniqueid name 
        tmdb  string - uniqueid name 
        anidb string - uniqueid name 
        ===== ====================== 

        Example::

            ...
            uniqueID = listitem.getUniqueID('imdb')
            ...
        """
        return ""
    
    def getRating(self, key: str) -> float:
        """
        \python_func{`getRating(key)` } Returns a listitem rating as a float.

        :param key: string - rating type.  Some default key values (any string possible):

        ===== ================== 
        Label Type               
        ===== ================== 
        imdb  string - type name 
        tvdb  string - type name 
        tmdb  string - type name 
        anidb string - type name 
        ===== ================== 

        Example::

            ...
            rating = listitem.getRating('imdb')
            ...
        """
        return 0.0
    
    def getVotes(self, key: str) -> int:
        """
        \python_func{`getVotes(key)` } Returns a listitem votes as a integer.

        :param key: string - rating type.  Some default key values (any string possible):

        ===== ================== 
        Label Type               
        ===== ================== 
        imdb  string - type name 
        tvdb  string - type name 
        tmdb  string - type name 
        anidb string - type name 
        ===== ================== 

        Example::

            ...
            votes = listitem.getVotes('imdb')
            ...
        """
        return 0
    
    def select(self, selected: bool) -> None:
        """
        \python_func{ select(selected) } Sets the listitem's selected status.

        :param selected: bool - True=selected/False=not selected

        Example::

            ...
            # select(selected)
            listitem.select(True)
            ...
        """
        pass
    
    def isSelected(self) -> bool:
        """
        \python_func{`isSelected()` } Returns the listitem's selected status.

        :return: bool - true if selected, otherwise false

        Example::

            ...
            # isSelected()
            selected = listitem.isSelected()
            ...
        """
        return True
    
    def setInfo(self, type: str, infoLabels: Dict[str, str]) -> None:
        """
        \python_func{ setInfo(type, infoLabels) } Sets the listitem's infoLabels.

        :param type: string - type of
        :param infoLabels: dictionary - pairs of``{ label: value }``
        **Available types **

        ============ ==================== 
        Command name Description          
        ============ ==================== 
        video        Video information    
        music        Music information    
        pictures     Pictures informanion 
        game         Game information     
        ============ ==================== 

        .. note::
            To set pictures exif info, prepend ``exif:`` to the label. Exif
            values must be passed as strings, separate value pairs with a
            comma.**(eg.``{'exif:resolution': '720,480'}`` See
            kodi_pictures_infotag for valid strings.   You can use the above
            as keywords for arguments and skip certain optional arguments.
            Once you use a keyword, all following arguments require the
            keyword.

        **General Values ** (that apply to all types):

        ========== ============================================================================ 
        Info label Description                                                                  
        ========== ============================================================================ 
        count      integer (12) - can be used to store an id for later, or for sorting purposes 
        size       long (1024) - size in bytes                                                  
        date       string (d.m.Y / 01.01.2009) - file date                                      
        ========== ============================================================================ 

        **Video Values **:

        ============= ===================================================================================================================== 
        Info label    Description                                                                                                           
        ============= ===================================================================================================================== 
        genre         string (Comedy) or list of strings (["Comedy", "Animation", "Drama"])                                                 
        country       string (Germany) or list of strings (["Germany", "Italy", "France"])                                                  
        year          integer (2009)                                                                                                        
        episode       integer (4)                                                                                                           
        season        integer (1)                                                                                                           
        sortepisode   integer (4)                                                                                                           
        sortseason    integer (1)                                                                                                           
        episodeguide  string (Episode guide)                                                                                                
        showlink      string (Battlestar Galactica) or list of strings (["Battlestar Galactica", "Caprica"])                                
        top250        integer (192)                                                                                                         
        setid         integer (14)                                                                                                          
        tracknumber   integer (3)                                                                                                           
        rating        float (6.4) - range is 0..10                                                                                          
        userrating    integer (9) - range is 1..10 (0 to reset)                                                                             
        watched       depreciated - use playcount instead                                                                                   
        playcount     integer (2) - number of times this item has been played                                                               
        overlay       integer (2) - range is ``0..7``. See Overlay icon types for values                                                     
        cast          list (["Michal C. Hall","Jennifer Carpenter"]) - if provided a list of tuples cast will be interpreted as castandrole 
        castandrole   list of tuples ([("Michael C. Hall","Dexter"),("Jennifer Carpenter","Debra")])                                        
        director      string (Dagur Kari) or list of strings (["Dagur Kari", "Quentin Tarantino", "Chrstopher Nolan"])                      
        mpaa          string (PG-13)                                                                                                        
        plot          string (Long Description)                                                                                             
        plotoutline   string (Short Description)                                                                                            
        title         string (Big Fan)                                                                                                      
        originaltitle string (Big Fan)                                                                                                      
        sorttitle     string (Big Fan)                                                                                                      
        duration      integer (245) - duration in seconds                                                                                   
        studio        string (Warner Bros.) or list of strings (["Warner Bros.", "Disney", "Paramount"])                                    
        tagline       string (An awesome movie) - short description of movie                                                                
        writer        string (Robert D. Siegel) or list of strings (["Robert D. Siegel", "Jonathan Nolan", "J.K. Rowling"])                 
        tvshowtitle   string (Heroes)                                                                                                       
        premiered     string (2005-03-04)                                                                                                   
        status        string (Continuing) - status of a TVshow                                                                              
        set           string (Batman Collection) - name of the collection                                                                   
        setoverview   string (All Batman movies) - overview of the collection                                                               
        tag           string (cult) or list of strings (["cult", "documentary", "best movies"]) - movie tag                                 
        imdbnumber    string (tt0110293) - IMDb code                                                                                        
        code          string (101) - Production code                                                                                        
        aired         string (2008-12-07)                                                                                                   
        credits       string (Andy Kaufman) or list of strings (["Dagur Kari", "Quentin Tarantino", "Chrstopher Nolan"]) - writing credits  
        lastplayed    string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        album         string (The Joshua Tree)                                                                                              
        artist        list (['U2'])                                                                                                         
        votes         string (12345 votes)                                                                                                  
        path          string (/home/user/movie.avi)                                                                                         
        trailer       string (/home/user/trailer.avi)                                                                                       
        dateadded     string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        mediatype     string - "video", "movie", "tvshow", "season", "episode" or "musicvideo"                                              
        dbid          integer (23) - Only add this for items which are part of the local db. You also need to set the correct 'mediatype'!  
        ============= ===================================================================================================================== 

        **Music Values **:

        ======================== ==================================================================================================================== 
        Info label               Description                                                                                                          
        ======================== ==================================================================================================================== 
        tracknumber              integer (8)                                                                                                          
        discnumber               integer (2)                                                                                                          
        duration                 integer (245) - duration in seconds                                                                                  
        year                     integer (1998)                                                                                                       
        genre                    string (Rock)                                                                                                        
        album                    string (Pulse)                                                                                                       
        artist                   string (Muse)                                                                                                        
        title                    string (American Pie)                                                                                                
        rating                   float - range is between 0 and 10                                                                                    
        userrating               integer - range is 1..10                                                                                             
        lyrics                   string (On a dark desert highway...)                                                                                 
        playcount                integer (2) - number of times this item has been played                                                              
        lastplayed               string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                           
        mediatype                string - "music", "song", "album", "artist"                                                                          
        dbid                     integer (23) - Only add this for items which are part of the local db. You also need to set the correct 'mediatype'! 
        listeners                integer (25614)                                                                                                      
        musicbrainztrackid       string (cd1de9af-0b71-4503-9f96-9f5efe27923c)                                                                        
        musicbrainzartistid      string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)                                                                        
        musicbrainzalbumid       string (24944755-2f68-3778-974e-f572a9e30108)                                                                        
        musicbrainzalbumartistid string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)                                                                        
        comment                  string (This is a great song)                                                                                        
        ======================== ==================================================================================================================== 

        **Picture Values**:

        =========== ==================================================== 
        Info label  Description                                          
        =========== ==================================================== 
        title       string (In the last summer-1)                        
        picturepath string (``/home/username/pictures/img001.jpg``)      
        exif*       string (See kodi_pictures_infotag for valid strings) 
        =========== ==================================================== 

        **Game Values **:

        ========== ============================= 
        Info label Description                   
        ========== ============================= 
        title      string (Super Mario Bros.)    
        platform   string (Atari 2600)           
        genres     list (["Action","Strategy"])  
        publisher  string (Nintendo)             
        developer  string (Square)               
        overview   string (Long Description)     
        year       integer (1980)                
        gameclient string (game.libretro.fceumm) 
        ========== ============================= 

         @python_v14 Added new label**discnumber **. @python_v15**duration ** has to be
        set in seconds. @python_v16 Added new label**mediatype **. @python_v17 Added
        labels**setid **,**set **,**imdbnumber **,**code **,**dbid ** (video),**path **
        and**userrating **. Expanded the possible infoLabels for the option**mediatype **.
        @python_v18 Added new**game ** type and associated infolabels. Added
        labels**dbid ** (music),**setoverview **,**tag **,**sortepisode **,**sortseason **,**
        episodeguide **,**showlink **. Extended labels**genre **,**country **,**director**,*
        *studio **,**writer **,**tag **,**credits** to also use a list of strings.

        Example::

            ...
            listitem.setInfo('video', { 'genre': 'Comedy' })
            ...
        """
        pass
    
    def setCast(self, actors: List[Dict[str, str]]) -> None:
        """
        \python_func{ setCast(actors) } Set cast including thumbnails

        :param actors: list of dictionaries (see below for relevant keys)

        Keys:

        ========= ============================================= 
        Label     Description                                   
        ========= ============================================= 
        name      string (Michael C. Hall)                      
        role      string (Dexter)                               
        thumbnail string (http://www.someurl.com/someimage.png) 
        order     integer (1)                                   
        ========= ============================================= 

         @python_v17 New function added.

        Example::

            ...
            actors = [{"name": "Actor 1", "role": "role 1"}, {"name": "Actor 2", "role": "role 2"}]
            listitem.setCast(actors)
            ...
        """
        pass
    
    def setAvailableFanart(self, images: List[Dict[str, str]]) -> None:
        """
        \python_func{ setAvailableFanart(images) } Set available images (needed for
        video scrapers)

        :param images: list of dictionaries (see below for relevant keys)

        Keys:

        ======= ========================================================== 
        Label   Description                                                
        ======= ========================================================== 
        image   string (http://www.someurl.com/someimage.png)              
        preview [opt] string (http://www.someurl.com/somepreviewimage.png) 
        ======= ========================================================== 

        | colors | [opt] string (either comma separated Kodi hex values
        ("FFFFFFFF,DDDDDDDD") or TVDB RGB Int Triplets
        ("|68,69,59|69,70,58|78,78,68|")) @python_v18 New function added.

        Example::

            ...
            fanart = [{"image": path_to_image_1, "preview": path_to_preview_1}, {"image": path_to_image_2, "preview": path_to_preview_2}]
            listitem.setAvailableFanart(fanart)
            ...
        """
        pass
    
    def addAvailableArtwork(self, url: str,
                            art_type: str = "",
                            preview: str = "",
                            referrer: str = "",
                            cache: str = "",
                            post: bool = False,
                            isgz: bool = False,
                            season: int = -1) -> None:
        """
        \python_func{ addAvailableArtwork(images) } Add an image to available artworks
        (needed for video scrapers)

        :param url: string (image path url)
        :param art_type: string (image type)
        :param preview: [opt] string (image preview path url)
        :param referrer: [opt] string (referrer url)
        :param cache: [opt] string (filename in cache)
        :param post: [opt] bool (use post to retrieve the image, default false)
        :param isgz: [opt] bool (use gzip to retrieve the image, default false)
        :param season: [opt] integer (number of season in case of season thumb)
         @python_v18 New function added. @python_v19 New param added
        (preview).Example::

            ...
            listitem.addAvailableArtwork(path_to_image_1, "thumb")
            ...
        """
        pass
    
    def addStreamInfo(self, cType: str, dictionary: Dict[str, str]) -> None:
        """
        \python_func{ addStreamInfo(type, values) } Add a stream with details.

        :param type: string - type of stream(video/audio/subtitle).
        :param values: dictionary - pairs of { label: value }.

        Video Values:

        ======== ================= 
        Label    Description       
        ======== ================= 
        codec    string (h264)     
        aspect   float (1.78)      
        width    integer (1280)    
        height   integer (720)     
        duration integer (seconds) 
        ======== ================= 

        Audio Values:

        ======== ============ 
        Label    Description  
        ======== ============ 
        codec    string (dts) 
        language string (en)  
        channels integer (2)  
        ======== ============ 

        Subtitle Values:

        ======== =========== 
        Label    Description 
        ======== =========== 
        language string (en) 
        ======== =========== 

        Example::

            ...
            listitem.addStreamInfo('video', { 'codec': 'h264', 'width' : 1280 })
            ...
        """
        pass
    
    def addContextMenuItems(self, items: List[Tuple[str, str]],
                            replaceItems: bool = False) -> None:
        """
        \python_func{ addContextMenuItems([(label, action),*]) } Adds item(s) to the
        context menu for media lists.

        :param items: list - [(label, action),*] A list of tuples consisting of label and
            action pairs.  label string or unicode - item's label.action
            string or unicode - any available `built-in function` .

        .. note::
            You can use the above as keywords for arguments and skip certain
            optional arguments.  Once you use a keyword, all following
            arguments require the keyword.

         @python_v17 Completely removed previously available
        argument **replaceItems**.Example::

            ...
            listitem.addContextMenuItems([('Theater Showtimes', 'RunScript(special://home/scripts/showtimes/default.py,Iron Man)')])
            ...
        """
        pass
    
    def setProperty(self, key: str, value: str) -> None:
        """
        \python_func{ setProperty(key, value) } Sets a listitem property, similar to an
        infolabel.

        :param key: string - property name.
        :param value: string or unicode - value of property.

        .. note::
            Key is NOT case sensitive.  You can use the above as keywords for
            arguments and skip certain optional arguments.  Once you use a
            keyword, all following arguments require the keyword.   Some of
            these are treated internally by Kodi, such as the 'StartOffset'
            property, which is the offset in seconds at which to start
            playback of an item. Others may be used in the skin to add extra
            information, such as 'WatchedCount' for tvshow items

        Example::

            ...
            listitem.setProperty('AspectRatio', '1.85 : 1')
            listitem.setProperty('StartOffset', '256.4')
            ...
        """
        pass
    
    def setProperties(self, dictionary: Dict[str, str]) -> None:
        """
        \python_func{ setProperties(values) } Sets multiple properties for listitem's

        :param values: dictionary - pairs of``{ label: value }``.
        @python_v18 New function added.Example::

            ...
            # setProperties(values)
            listitem.setProperties({ 'AspectRatio': '1.85', 'StartOffset' : '256.4' })
            ...
        """
        pass
    
    def getProperty(self, key: str) -> str:
        """
        \python_func{ getProperty(key) } Returns a listitem property as a string,
        similar to an infolabel.

        :param key: string - property name.

        .. note::
            Key is NOT case sensitive.  You can use the above as keywords for
            arguments and skip certain optional arguments.  Once you use a
            keyword, all following arguments require the keyword.

        Example::

            ...
            AspectRatio = listitem.getProperty('AspectRatio')
            ...
        """
        return ""
    
    def setPath(self, path: str) -> None:
        """
        \python_func{ setPath(path) } Sets the listitem's path.

        :param path: string or unicode - path, activated when item is clicked.

        .. note::
            You can use the above as keywords for arguments.

        Example::

            ...
            listitem.setPath(path='/path/to/some/file.ext')
            ...
        """
        pass
    
    def setMimeType(self, mimetype: str) -> None:
        """
        \python_func{ setMimeType(mimetype) } Sets the listitem's mimetype if known.

        :param mimetype: string or unicode - mimetype

        If known prehand, this can (but does not have to) avoid HEAD requests
        being sent to HTTP servers to figure out file type.
        """
        pass
    
    def setContentLookup(self, enable: bool) -> None:
        """
        \python_func{ setContentLookup(enable) } Enable or disable content lookup for
        item.

        If disabled, HEAD requests to e.g determine mime type will not be sent.

        :param enable: bool to enable content lookup
         @python_v16 New function added.
        """
        pass
    
    def setSubtitles(self, subtitleFiles: List[str]) -> None:
        """
        \python_func{ setSubtitles(subtitleFiles) } Sets subtitles for this listitem.

        :param subtitleFiles: list with path to subtitle files

        Example::

            ...
            listitem.setSubtitles(['special://temp/example.srt', 'http://example.com/example.srt'])
            ...
         @python_v14 New function added.
        """
        pass
    
    def getPath(self) -> str:
        """
        \python_func{`getPath()` } Returns the path of this listitem.

        :return: [string] filename

         @python_v17 New function added.
        """
        return ""
    
    def getVideoInfoTag(self) ->InfoTagVideo:
        """
        \python_func{`getVideoInfoTag()` } Returns the VideoInfoTag for this item.

        :return: video info tag

         @python_v15 New function added.
        """
        return InfoTagVideo()
    
    def getMusicInfoTag(self) -> InfoTagMusic:
        """
        \python_func{`getMusicInfoTag()` } Returns the MusicInfoTag for this item.

        :return: music info tag

         @python_v15 New function added.
        """
        return InfoTagMusic()
    

class Action:
    """
    **`Action` class.**

    \python_class{ xbmcgui.Action(): }

    This class serves in addition to identify carried out kodi_key_action_ids of
    Kodi and to be able to carry out thereby own necessary steps.

    The data of this class are always transmitted by callback `Window::onAction` at a
    window.
    """
    
    def __init__(self) -> None:
        pass
    
    def getId(self) -> int:
        """
        \python_func{`getId()` } To get kodi_key_action_ids

        This function returns the identification code used by the explained order, it is
        necessary to determine the type of command from kodi_key_action_ids.

        :return: The action's current id as a long or 0 if no action is mapped in the xml's.

        Example::

            ..
            def onAction(self, action):
              if action.getId() == ACTION_PREVIOUS_MENU:
                print('action received: previous')
            ..
        """
        return 0
    
    def getButtonCode(self) -> int:
        """
        \python_func{`getButtonCode()` } Returns the button code for this action.

        :return: [integer] button code
        """
        return 0
    
    def getAmount1(self) -> float:
        """
        \python_func{`getAmount1()` } Returns the first amount of force applied to the
        thumbstick.

        :return: [float] first amount
        """
        return 0.0
    
    def getAmount2(self) -> float:
        """
        \python_func{`getAmount2()` } Returns the second amount of force applied to the
        thumbstick.

        :return: [float] second amount
        """
        return 0.0
    

class Window:
    """
    **GUI window class for Add-Ons.**

    This class allows over their functions to create and edit windows that can be
    accessed from an Add-On.

    Likewise, all functions from here as well in the other window
    classes `WindowDialog`,`WindowXML` and `WindowXMLDialog` with inserted and
    available.

    Constructor for window\python_class{ xbmcgui.Window([existingWindowId]): }

    Creates a new from Add-On usable window class. This is to create window for
    related controls by system calls.

    :param existingWindowId: [opt] Specify an id to use an existing window.
    :raises ValueError: if supplied window Id does not exist.
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and
    resets (not delete) all controls that are associated with this window.Example::

        ..
        win = xbmcgui.Window()
        width = win.getWidth()
        ..
    """
    
    def __init__(self, existingWindowId: int = -1) -> None:
        pass
    
    def show(self) -> None:
        """
        \python_func{`show()` } Show this window.

        Shows this window by activating it, calling `close()` after it wil activate the
        current window again.

        .. note::
            If your script ends this window will be closed to. To show it
            forever, make a loop at the end of your script or use `doModal()`
            instead.
        """
        pass
    
    def setFocus(self, pControl: Control) -> None:
        """
        \python_func{ setFocus(Control) } Give the supplied control focus.

        :param `Control`: `Control` class to focus
        :raises TypeError: If supplied argument is not a `Control` type
        :raises SystemError: On Internal error
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def setFocusId(self, iControlId: int) -> None:
        """
        \python_func{ setFocusId(ControlId) } Gives the control with the supplied focus.

        :param ControlId: [integer] On skin defined id of control
        :raises SystemError: On Internal error
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def getFocus(self) -> Control:
        """
        \python_func{ getFocus(Control) } Returns the control which is focused.

        :return: Focused control class

        :raises SystemError: On Internal error
        :raises RuntimeError: If no control has focus
        """
        return Control()
    
    def getFocusId(self) -> int:
        """
        \python_func{ getFocusId(int) } Returns the id of the control which is focused.

        :return: Focused control id

        :raises SystemError: On Internal error
        :raises RuntimeError: If no control has focus
        """
        return 0
    
    def removeControl(self, pControl: Control) -> None:
        """
        \python_func{ removeControl(Control) } Removes the control from this window.

        :param `Control`: `Control` class to remove
        :raises TypeError: If supplied argument is not a `Control` type
        :raises RuntimeError: If control is not added to this window

        This will not delete the control. It is only removed from the window.
        """
        pass
    
    def removeControls(self, pControls: List[Control]) -> None:
        """
        \python_func{ removeControls(List) } Removes a list of controls from this
        window.

        :param `List`: `List` with controls to remove
        :raises TypeError: If supplied argument is not a `Control` type
        :raises RuntimeError: If control is not added to this window

        This will not delete the controls. They are only removed from the
        window.
        """
        pass
    
    def getHeight(self) -> int:
        """
        \python_func{`getHeight()` } Returns the height of this `Window` instance.

        :return: `Window` height in pixels

         @python_v18 Function changed
        """
        return 0
    
    def getWidth(self) -> int:
        """
        \python_func{`getWidth()` } Returns the width of this `Window` instance.

        :return: `Window` width in pixels

         @python_v18 Function changed
        """
        return 0
    
    def setProperty(self, key: str, value: str) -> None:
        """
        \python_func{ setProperty(key, value) } Sets a window property, similar to an
        infolabel.

        :param key: string - property name.
        :param value: string or unicode - value of property.

        .. note::
            Key is NOT case sensitive. Setting value to an empty string is
            equivalent to clearProperty(key).  You can use the above as
            keywords for arguments and skip certain optional arguments.  Once
            you use a keyword, all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.setProperty('Category', 'Newest')
            ..
        """
        pass
    
    def getProperty(self, key: str) -> str:
        """
        \python_func{ getProperty(key) } Returns a window property as a string, similar
        to an infolabel.

        :param key: string - property name.

        .. note::
            Key is NOT case sensitive.  You can use the above as keywords for
            arguments and skip certain optional arguments. Once you use a
            keyword, all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            category = win.getProperty('Category')
            ..
        """
        return ""
    
    def clearProperty(self, key: str) -> None:
        """
        \python_func{ clearProperty(key) } Clears the specific window property.

        :param key: string - property name.

        .. note::
            Key is NOT case sensitive. Equivalent to setProperty(key,'') You
            can use the above as keywords for arguments and skip certain
            optional arguments. Once you use a keyword, all following
            arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperty('Category')
            ..
        """
        pass
    
    def clearProperties(self) -> None:
        """
        \python_func{`clearProperties()` } Clears all window properties.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperties()
            ..
        """
        pass
    
    def close(self) -> None:
        """
        \python_func{`close()` } Closes this window.

        Closes this window by activating the old window.

        .. note::
            The window is not deleted with this method.
        """
        pass
    
    def doModal(self) -> None:
        """
        \python_func{`doModal()` } Display this window until `close()` is called.
        """
        pass
    
    def addControl(self, pControl: Control) -> None:
        """
        \python_func{ addControl(Control) } Add a `Control` to this window.

        :param `Control`: `Control` to add
        :raises TypeError: If supplied argument is not a `Control` type
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)

        The next controls can be added to a window atm

        ==================== =============================================================================================== 
        Control-class        Description                                                                                     
        ==================== =============================================================================================== 
        `ControlLabel`       Label control to show text                                                                      
        `ControlFadeLabel`   The fadelabel has multiple labels which it cycles through                                       
        `ControlTextBox`     To show bigger text field                                                                       
        `ControlButton`      Brings a button to do some actions                                                              
        `ControlEdit`        The edit control allows a user to input text in Kodi                                            
        `ControlFadeLabel`   The fade label control is used for displaying multiple pieces of text in the same space in Kodi 
        `ControlList`        Add a list for something like files                                                             
        `ControlGroup`       Is for a group which brings the others together                                                 
        `ControlImage`       Controls a image on skin                                                                        
        `ControlRadioButton` For a radio button which handle boolean values                                                  
        `ControlProgress`    Progress bar for a performed work or something else                                             
        `ControlSlider`      The slider control is used for things where a sliding bar best represents the operation at hand 
        `ControlSpin`        The spin control is used for when a list of options can be chosen                               
        `ControlTextBox`     The text box is used for showing a large multipage piece of text in Kodi                        
        ==================== ===============================================================================================
        """
        pass
    
    def addControls(self, pControls: List[Control]) -> None:
        """
        \python_func{ addControls(List) } Add a list of Controls to this window.

        :param `List`: `List` with controls to add
        :raises TypeError: If supplied argument is not of `List` type, or a control is not
            of `Control` type
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)
        """
        pass
    
    def getControl(self, iControlId: int) -> Control:
        """
        \python_func{ getControl(controlId) } Gets the control from this window.

        :param controlId: `Control` id to get
        :raises Exception: If `Control` doesn't exist

        controlId doesn't have to be a python control, it can be a control id from a
        Kodi window too (you can find id's in the xml files.

        .. note::
            Not python controls are not completely usable yet You can only use
            the `Control` functions
        """
        return Control()
    
    def onAction(self, action: Action) -> None:
        """
        \python_func{ onAction(self, Action action) }**onAction method.**

        This method will receive all actions that the main program will send to this
        window.

        :param self: Own base class pointer
        :param action: The action id to perform, see `Action` to get use of them

        .. note::
              By default, only the ``PREVIOUS_MENU`` and ``NAV_BACK actions``
            are handled.Overwrite this method to let your script handle all
            actions.Don't forget to capture ``ACTION_PREVIOUS_MENU``
            or ``ACTION_NAV_BACK``, else the user can't close this window.

        Example::

            ..
            # Define own function where becomes called from Kodi
            def onAction(self, action):
              if action.getId() == ACTION_PREVIOUS_MENU:
                print('action received: previous')
                self.close()
              if action.getId() == ACTION_SHOW_INFO:
                print('action received: show info')
              if action.getId() == ACTION_STOP:
                print('action received: stop')
              if action.getId() == ACTION_PAUSE:
                print('action received: pause')
            ..
        """
        pass
    
    def onControl(self, control: Control) -> None:
        """
        \python_func{ onControl(self, Control) }**onControl method.**

        This method will receive all click events on owned and selected controls when
        the control itself doesn't handle the message.

        :param self: Own base class pointer
        :param control: The `Control` class

        Example::

            ..
            # Define own function where becomes called from Kodi
            def onControl(self, control):
              print("Window.onControl(control=[%s])"%control)
            ..
        """
        pass
    
    def onClick(self, controlId: int) -> None:
        """
        \python_func{ onClick(self, int controlId) }**onClick method.**

        This method will receive all click events that the main program will send to
        this window.

        :param self: Own base class pointer
        :param controlId: The one time clicked GUI control identifier

        Example::

            ..
            # Define own function where becomes called from Kodi
            def onClick(self,controlId):
              if controlId == 10:
                print("The control with Id 10 is clicked")
            ..
        """
        pass
    
    def onDoubleClick(self, controlId: int) -> None:
        """
        \python_func{ onDoubleClick(self, int controlId) }**onDoubleClick method.**

        This method will receive all double click events that the main program will send
        to this window.

        :param self: Own base class pointer
        :param controlId: The double clicked GUI control identifier

        Example::

            ..
            # Define own function where becomes called from Kodi
            def onDoubleClick(self,controlId):
              if controlId == 10:
                print("The control with Id 10 is double clicked")
            ..
        """
        pass
    
    def onFocus(self, controlId: int) -> None:
        """
        \python_func{ onFocus(self, int controlId) }**onFocus method.**

        This method will receive all focus events that the main program will send to
        this window.

        :param self: Own base class pointer
        :param controlId: The focused GUI control identifier

        Example::

            ..
            # Define own function where becomes called from Kodi
             def onDoubleClick(self,controlId):
               if controlId == 10:
                 print("The control with Id 10 is focused")
            ..
        """
        pass
    
    def onInit(self) -> None:
        """
        \python_func{ onInit(self) }**onInit method.**

        This method will be called to initialize the window

        :param self: Own base class pointer

        Example::

            ..
            # Define own function where becomes called from Kodi
            def onInit(self):
              print("Window.onInit method called from Kodi")
            ..
        """
        pass
    

class WindowDialog(Window):
    """
    **GUI window dialog class for Add-Ons.**

    \python_class{ xbmcgui.WindowDialog(int windowId): }

    Creates a new window from Add-On usable dialog class. This is to create window
    for related controls by system calls.

    :param windowId: [opt] Specify an id to use an existing window.
    :raises ValueError: if supplied window Id does not exist.
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and
    resets (not delete) all controls that are associated with this window.Example::

        ..
        dialog = xbmcgui.WindowDialog()
        width = dialog.getWidth()
        ..
    """
    
    def __init__(self) -> None:
        pass
    

class WindowXML(Window):
    """
    **GUI xml window class.**

    \python_class{ xbmcgui.WindowXML(xmlFilename, scriptPath[, defaultSkin,
    defaultRes]) }

    Creates a new xml file based window class.

    .. note::
        This class include also all calls from ```Window```.

    :param xmlFilename: string - the name of the xml file to look for.
    :param scriptPath: string - path to script. used to fallback to if the xml doesn't exist
        in the current skin. (eg
        xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
    :param defaultSkin: [opt] string - name of the folder in the skins path to look in for the
        xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution. (1080i, 720p, ntsc16x9, ntsc,
        pal16x9 or pal. default='720p')
    :param isMedia: [opt] bool - if False, create a regular window. if True, create a
        mediawindow. (default=False)
    :raises Exception: if more then 200 windows are created.

    Skin folder structure is e.g.**resources/skins/Default/720p **

    Deleting this window will activate the old window that was active and
    resets (not delete) all controls that are associated with this window. @python_v18 New param added**isMedia **.

    Example::

        ..
        win = xbmcgui.WindowXML('script-Lyrics-main.xml', xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'), 'default', '1080i', False)
        win.doModal()
        del win
        ..
    On functions defined input variable ``controlId`` (GUI control identifier)** is
    the on window.xml defined value behind type added with ``id="..."`` and used
    to identify for changes there and on callbacks.

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename: str,
                 scriptPath: str,
                 defaultSkin: str = "Default",
                 defaultRes: str = "720p",
                 isMedia: bool = False) -> None:
        pass
    
    def addItem(self, item: Union[str, ListItem],
                position: int = sys.maxsize) -> None:
        """
        \python_func{ addItem(item[, position]) } Add a new item to this `Window ``List`.

        :param item: string, unicode or `ListItem` - item to add.
        :param position: [opt] integer - position of item to add. (NO Int = Adds to bottom,0
            adds to top, 1 adds to one below from top,-1 adds to one above
            from bottom etc etc )  If integer positions are greater than list
            size, negative positions will add to top of list, positive
            positions will add to bottom of list
        Example::

            ..
            self.addItem('Reboot Kodi', 0)
            ..
        """
        pass
    
    def addItems(self, items: List[Union[str, ListItem]]) -> None:
        """
        \python_func{ addItems(items) } Add a list of items to to the window list.

        :param items: `List` - list of strings, unicode objects or ListItems to add.

        Example::

            ..
            self.addItems(['Reboot Kodi', 'Restart Kodi'])
            ..
        """
        pass
    
    def removeItem(self, position: int) -> None:
        """
        \python_func{ removeItem(position) } Removes a specified item based on position,
        from the `Window ``List`.

        :param position: integer - position of item to remove.

        Example::

            ..
            self.removeItem(5)
            ..
        """
        pass
    
    def getCurrentListPosition(self) -> int:
        """
        \python_func{`getCurrentListPosition()` } Gets the current position in
        the `Window ``List`.

        Example::

            ..
            pos = self.getCurrentListPosition()
            ..
        """
        return 0
    
    def setCurrentListPosition(self, position: int) -> None:
        """
        \python_func{ setCurrentListPosition(position) } Set the current position in
        the `Window ``List`.

        :param position: integer - position of item to set.

        Example::

            ..
            self.setCurrentListPosition(5)
            ..
        """
        pass
    
    def getListItem(self, position: int) -> ListItem:
        """
        \python_func{ getListItem(position) } Returns a given `ListItem` in
        this `Window ``List`.

        :param position: integer - position of item to return.

        Example::

            ..
            listitem = self.getListItem(6)
            ..
        """
        return ListItem()
    
    def getListSize(self) -> int:
        """
        \python_func{`getListSize()` } Returns the number of items in
        this `Window ``List`.

        Example::

            ..
            listSize = self.getListSize()
            ..
        """
        return 0
    
    def clearList(self) -> None:
        """
        \python_func{`clearList()` } Clear the `Window ``List`.

        Example::

            ..
            self.clearList()
            ..
        """
        pass
    
    def setContainerProperty(self, strProperty: str, strValue: str) -> None:
        """
        \python_func{ setContainerProperty(key, value) } Sets a container property,
        similar to an infolabel.

        :param key: string - property name.
        :param value: string or unicode - value of property.

        .. note::
            Key is NOT case sensitive. You can use the above as keywords for
            arguments and skip certain optional arguments. Once you use a
            keyword, all following arguments require the keyword.

         @python_v17 Changed function from **setProperty**
        to **setContainerProperty**.Example::

            ..
            self.setContainerProperty('Category', 'Newest')
            ..
        """
        pass
    
    def setContent(self, strValue: str) -> None:
        """
        \python_func{ setContent(value) } Sets the content type of the container.

        :param value: string or unicode - content value.
        **Available content types**

        =========== ========================================= 
        Name        Media                                     
        =========== ========================================= 
        actors      Videos                                    
        addons      Addons, Music, Pictures, Programs, Videos 
        albums      Music, Videos                             
        artists     Music, Videos                             
        countries   Music, Videos                             
        directors   Videos                                    
        files       Music, Videos                             
        games       Games                                     
        genres      Music, Videos                             
        images      Pictures                                  
        mixed       Music, Videos                             
        movies      Videos                                    
        Musicvideos Music, Videos                             
        playlists   Music, Videos                             
        seasons     Videos                                    
        sets        Videos                                    
        songs       Music                                     
        studios     Music, Videos                             
        tags        Music, Videos                             
        tvshows     Videos                                    
        videos      Videos                                    
        years       Music, Videos                             
        =========== ========================================= 

         @python_v18 Added new function.

        Example::

            ..
            self.setContent('movies')
            ..
        """
        pass
    
    def getCurrentContainerId(self) -> int:
        """
        \python_func{`getCurrentContainerId()` } Get the id of the currently visible
        container.

         @python_v17 Added new function.

        Example::

            ..
            container_id = self.getCurrentContainerId()
            ..
        """
        return 0
    

class WindowXMLDialog(WindowXML):
    """
    **GUI xml window dialog **

    \python_class{ xbmcgui.WindowXMLDialog(xmlFilename, scriptPath[, defaultSkin,
    defaultRes]) }

    Creates a new xml file based window dialog class.

    :param xmlFilename: string - the name of the xml file to look for.
    :param scriptPath: string - path to script. used to fallback to if the xml doesn't exist
        in the current skin.
        (eg `xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))`
    :param defaultSkin: [opt] string - name of the folder in the skins path to look in for the
        xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution. (1080i, 720p, ntsc16x9, ntsc,
        pal16x9 or pal. default='720p')
    :raises Exception: if more then 200 windows are created.

    .. note::
        Skin folder structure is e.g.**resources/skins/Default/720p **

    Example::

        ..
        dialog = xbmcgui.WindowXMLDialog('script-Lyrics-main.xml', xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'), 'default', '1080i')
        dialog.doModal()
        del dialog
        ..
    On functions defined input variable ``controlId`` (GUI control identifier)** is
    the on window.xml defined value behind type added with ``id="..."`` and used
    to identify for changes there and on callbacks.

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename: str,
                 scriptPath: str,
                 defaultSkin: str = "Default",
                 defaultRes: str = "720p") -> None:
        pass
    



def getCurrentWindowId() -> int:
    """
    \python_func{ xbmcgui.getCurrentWindowId() } Returns the id for the current
    'active' window as an integer.

    :return: The currently active window Id

    Example::

        ..
        wid = xbmcgui.getCurrentWindowId()
        ..
    """
    return 0


def getCurrentWindowDialogId() -> int:
    """
    \python_func{ xbmcgui.getCurrentWindowDialogId() } Returns the id for the
    current 'active' dialog as an integer.

    :return: The currently active dialog Id

    Example::

        ..
        wid = xbmcgui.getCurrentWindowDialogId()
        ..
    """
    return 0


def getScreenHeight() -> int:
    """
    \python_func{`getScreenHeight()` } Returns the height of this screen.

    :return: Screen height

     @python_v18 New function added.
    """
    return 0


def getScreenWidth() -> int:
    """
    \python_func{`getScreenWidth()` } Returns the width of this screen.

    :return: Screen width

     @python_v18 New function added.
    """
    return 0

