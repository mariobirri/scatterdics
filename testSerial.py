import serial, time

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
ser.write("100")
time.sleep(5)
ser.write("200")
time.sleep(5)
ser.write("1200") 
while 1:
	line = ser.readline()
	print(line)
ser.close()
