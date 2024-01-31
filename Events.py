import uinput

# https://github.com/tuomasjjrasanen/python-uinput/blob/master/src/ev.py
events = (
    uinput.ABS_X + (0, 1000, 0, 0),   # Left joystick X-axis
    uinput.ABS_Y + (0, 1000, 0, 0),   # Left joystick Y-axis
    uinput.BTN_THUMBL,                # Left joystick button
    uinput.ABS_RX + (0, 1000, 0, 0),  # Right joystick X-axis
    uinput.ABS_RY + (0, 1000, 0, 0),  # Right joystick Y-axis
    uinput.BTN_THUMBR,                # Right joystick button
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT
)

# The order of events handled must match the events tuple above
def eventHandler(gamepad, values, prevValues):
    # Left Joystick
    gamepad.emit(uinput.ABS_X, values[0], syn=False)
    gamepad.emit(uinput.ABS_Y, values[1], syn=False)

    # Right Joystick
    gamepad.emit(uinput.ABS_RX, values[3], syn=False)
    gamepad.emit(uinput.ABS_RY, values[4], syn=False)
    
    if values[2] != prevValues[2]:
        gamepad.emit_click(uinput.BTN_THUMBL, values[2])
    if values[5] != prevValues[5]:
        gamepad.emit_click(uinput.BTN_THUMBR, values[5])
    
    # A, B, X, Y Buttons
    if values[6] != prevValues[6]:
        gamepad.emit(uinput.BTN_A, values[6])
    if values[7] != prevValues[7]:
        gamepad.emit(uinput.BTN_B, values[7])
    if values[8] != prevValues[8]:
        gamepad.emit(uinput.BTN_X, values[8])
    if values[9] != prevValues[9]:
        gamepad.emit(uinput.BTN_Y, values[9])
    
    # UP, DOWN, LEFT, RIGHT
    if values[10] != prevValues[10]:
        gamepad.emit(uinput.BTN_DPAD_UP, values[10])
    if values[11] != prevValues[11]:
        gamepad.emit(uinput.BTN_DPAD_DOWN, values[11])
    if values[12] != prevValues[12]:
        gamepad.emit(uinput.BTN_DPAD_LEFT, values[12])
    if values[13] != prevValues[13]:
        gamepad.emit(uinput.BTN_DPAD_RIGHT, values[13])