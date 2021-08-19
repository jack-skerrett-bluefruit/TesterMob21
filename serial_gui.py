import tkinter

#from serial_connection import write_to_serial
from mock_arduino import mock_arduino_response

main_window = tkinter.Tk()

serial_connection_button = tkinter.Button(main_window, text = "Hello", command = mock_arduino_response)
serial_connection_button.pack()
main_window.mainloop()
