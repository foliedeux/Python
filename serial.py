import serial

ser = serial.Serial('\\.\COM3', 9600)

print(ser.name)