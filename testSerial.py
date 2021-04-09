import serial, time

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
ser.write("200") #200
print("set speed 1")
time.sleep(5)
ser.write("400") #400
print("set speed 2")
time.sleep(5)
ser.write("0") #1200
print("set speed 3")
while 1:
	line = ser.readline()
	print(line)
ser.close()
