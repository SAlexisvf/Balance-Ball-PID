# import serial

# port = 'COM4'
# serial_comm = serial.Serial(port, 9600, timeout = 1)
# x = "90,90"

# while True:
#     serial_comm.write(x.encode())
#     x = str(input())

f = open("test_1_no holding.txt", "r")
x = 0
while True:
    x = f.readline()
    if not x:
        break
    print(x[0:18])