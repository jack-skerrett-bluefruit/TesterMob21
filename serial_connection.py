import serial
import sys
from time import sleep

def write_to_serial():
    ser.write(bytes(sys.argv[3] + "\r", "utf-8"))


ser = serial.Serial(sys.argv[1], sys.argv[2], timeout = 1)
sleep(3)
print("hello")

#response = ser.read_until("\r").decode("utf-8")
#print(response)