def mock_arduino_response(text):
    if text == "ledon":
        return ("ledon")
    elif text == "ledoff":
        return ("ledoff")
    else:
        return ("I don't understand")
