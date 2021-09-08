import serial
from time import sleep

def create_serial_connection(com, baud):
    return serial.Serial(com, int(baud), timeout = 1)

def write_to_serial(ser, command):
    ser.write(bytes(command + "\r", "utf-8"))

def read_from_serial(ser):
    return ser.read_until(b"\r")