import tkinter
from tkinter.constants import END
from typing import Text

#from serial_connection import write_to_serial
from mock_arduino import mock_arduino_response

main_window = tkinter.Tk()

def send_button_click():
    output_box.configure(text=mock_arduino_response(input_box.get("1.0", 'end-1c')))
    print(input_box.get("1.0", 'end-1c'))

my_label = tkinter.Label(text="Put a message here please :)")
my_label.grid(row=0,column=0)

input_box = tkinter.Text(height=1, width=30)
input_box.grid(row=1)

serial_connection_button = tkinter.Button(main_window, text = "Send", command = send_button_click)
serial_connection_button.grid(row=2, column=0)

output_box = tkinter.Label(text="This is the output message box")
output_box.grid(row=4)

main_window.mainloop()