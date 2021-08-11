import tkinter
from serial_connection import write_to_serial

main_window = tkinter.Tk()

serial_connection_button = tkinter.Button(main_window, text = "Hello", command = write_to_serial)
serial_connection_button.pack()
main_window.mainloop()
