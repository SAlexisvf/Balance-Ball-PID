import serial

port = 'COM4'
serial_comm = serial.Serial(port, 9600, timeout = 1)
x = "90,90"

while True:
    serial_comm.write(x.encode())
    x = str(input())
