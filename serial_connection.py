import serial
import sys
from time import sleep

ser = serial.Serial(sys.argv[1], sys.argv[2], timeout = 1)
sleep(3)
ser.write(bytes(sys.argv[3] + "\r", "utf-8"))