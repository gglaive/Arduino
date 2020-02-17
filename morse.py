import serial
import time

# set up the serial line
ser = serial.Serial('COM6', 9600)
data =[]	   # empty list to store the data

def translate(word):
	if (word == "01"):
		print("A")
	if (word == "1000"):
		print("B")
	if (word == "1010"):
		print("C")
	if (word == "100"):
		print("D")
	if (word == "0"):
		print("E")
	if (word == "0010"):
		print("F")
	if (word == "110"):
		print("G")
	if (word == "0000"):
		print("H")
	if (word == "00"):
		print("I")
	if (word == "0111"):
		print("J")
	if (word == "101"):
		print("K")
	if (word == "0100"):
		print("L")
	if (word == "11"):
		print("M")
	if (word == "10"):
		print("N")
	if (word == "111"):
		print("O")
	if (word == "0110"):
		print("P")
	if (word == "1101"):
		print("Q")
	if (word == "010"):
		print("R")
	if (word == "000"):
		print("S")
	if (word == "1"):
		print("T")
	if (word == "001"):
		print("U")
	if (word == "0001"):
		print("V")
	if (word == "011"):
		print("W")
	if (word == "1001"):
		print("X")
	if (word == "1011"):
		print("Y")
	if (word == "1100"):
		print("Z")
	if (word == "01"):
		print("A")
	if (word == "11111"):
		print("0")
	if (word == "01111"):
		print("1")
	if (word == "00111"):
		print("2")
	if (word == "00011"):
		print("3")
	if (word == "00001"):
		print("4")
	if (word == "00000"):
		print("5")
	if (word == "10000"):
		print("6")
	if (word == "11000"):
		print("7")
	if (word == "11100"):
		print("8")
	if (word == "11110"):
		print("9")
	
while 1:
	value = ser.readline()
	string_n = value.decode()  # decode byte string into Unicode  
	string = string_n.rstrip() # remove \n and \r
	#print(type(string))
	print(string)
	if (string == "2"):
		mot = ""
		for i in range(len(data)):
			mot = mot + data[i]
		print("/////////////////\n")
		translate(mot)
		data.clear()
	else:
		data.append(string)
