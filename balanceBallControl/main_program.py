import serial

port = 'COM6'
serial_comm = serial.Serial(port, 9600, timeout = 1)
x = "hey"

while True:
    serial_comm.write(x.encode())
    x = input()
