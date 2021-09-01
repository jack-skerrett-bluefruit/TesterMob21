import tkinter
from mock_arduino import mock_arduino_response


class Application(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.create_widgets()

    def send_button_click(self, event = None):
        print(event)
        self.output_box.configure(text = mock_arduino_response(self.input_box.get()))

    def create_widgets(self):
        self.my_label = tkinter.Label(text = "Put a message here please :)")
        self.my_label.grid(row = 0,column = 0)

        self.input_box = tkinter.Entry(width = 30)
        self.input_box.grid(row = 1)
        self.input_box.bind("<Return>", self.send_button_click)

        self.serial_connection_button = tkinter.Button(self.main_window, text = "Send", command = self.send_button_click)
        self.serial_connection_button.grid(row = 2, column = 0)

        self.output_box = tkinter.Label(text = "This is the output message box")
        self.output_box.grid(row = 4)     
    
def main():
    main_window = tkinter.Tk()
    gui = Application(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()