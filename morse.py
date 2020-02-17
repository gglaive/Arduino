import serial
import time

# set up the serial line
ser = serial.Serial('COM6', 9600)
time.sleep(2)

# Read and record the data
data =[]	   # empty list to store the data
for i in range(50):
	b = ser.readline()	 # read a byte string
	string_n = b.decode()  # decode byte string into Unicode  
	string = string_n.rstrip() # remove \n and \r
	try:
		flt = float(string)	# convert string to float
		print(flt)
		data.append(flt)	   # add to the end of data list
	except:
		pass
	time.sleep(0.1)	# wait (sleep) 0.1 seconds

ser.close()

'''
while True:
	sw = board.digital[10].read()
	if sw is True:
		board.digital[13].write(1)
	else:
		board.digital[13].write(0)
	time.sleep(0.1)
'''

# show the data

for line in data:
	print(line)