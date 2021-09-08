import tkinter
from mock_arduino import mock_arduino_response
from serial_connection import create_serial_connection, read_from_serial, write_to_serial

class Application(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window 
        self.serial_port_state = False
        self.create_widgets()

    def connect_button_click(self):
        self.serial_port = create_serial_connection(self.com_box.get(), self.baud_box.get())
        self.serial_port_state = True

    def send_button_click(self, event = None):
        if self.serial_port_state:
            write_to_serial(self.serial_port, self.input_box.get())
            response = read_from_serial(self.serial_port)
        else: 
            response = mock_arduino_response(self.input_box.get())
        self.output_box.configure(text = response)

    def create_widgets(self):
        self.com_label = tkinter.Label(text = "Put a COM here please :)")
        self.com_label.grid(row = 0,column = 0)

        self.com_box = tkinter.Entry(width = 30)
        self.com_box.grid(row = 0, column = 1)

        self.baud_label = tkinter.Label(text = "Put a baudrate here please :)")
        self.baud_label.grid(row = 1,column = 0)

        self.baud_box = tkinter.Entry(width = 30)
        self.baud_box.grid(row = 1, column = 1)

        self.connect_button = tkinter.Button(self.main_window, text = "Connect", command = self.connect_button_click)
        self.connect_button.grid(row = 2, column = 0)
   
        self.my_label = tkinter.Label(text = "Put a message here please :)")
        self.my_label.grid(row = 3,column = 0)

        self.input_box = tkinter.Entry(width = 30)
        self.input_box.grid(row = 3, column = 1)
        self.input_box.bind("<Return>", self.send_button_click)

        self.message_button = tkinter.Button(self.main_window, text = "Send", command = self.send_button_click)
        self.message_button.grid(row = 4, column = 0)

        self.output_box = tkinter.Label(text = "This is the output message box")
        self.output_box.grid(row = 5)     

 

    
def main():
    main_window = tkinter.Tk()
    gui = Application(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()