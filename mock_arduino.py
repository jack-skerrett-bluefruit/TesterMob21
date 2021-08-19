from typing import Text


def mock_arduino_response(text):
    if text == "ledon":
        return str("ledon")
    elif text == "ledoff":
        return str("ledoff")
    else:
        return str("I don't understand")
