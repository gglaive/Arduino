import serial
import time

# set up the serial line
ser = serial.Serial('COM3', 9600)
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

def to_morse(letter):
	trad = ""
	if (letter == "A"):
		trad = b"01"
	if (letter == "B"):
		trad = b"1000"
	if (letter == "C"):
		trad = b"1010"
	if (letter == "D"):
		trad = b"100"
	if (letter == "E"):
		trad = b"0"
	if (letter == "F"):
		trad = b"0010"
	if (letter == "G"):
		trad = b"110"
	if (letter == "H"):
		trad = b"0000"
	if (letter == "I"):
		trad = b"00"
	if (letter == "J"):
		trad = b"0111"
	if (letter == "K"):
		trad = b"101"
	if (letter == "L"):
		trad = b"0100"
	if (letter == "M"):
		trad = b"11"
	if (letter == "N"):
		trad = b"10"
	if (letter == "O"):
		trad = b"111"
	if (letter == "P"):
		trad = b"0110"
	if (letter == "Q"):
		trad = b"1101"
	if (letter == "R"):
		trad = b"010"
	if (letter == "S"):
		trad = b"000"
	if (letter == "T"):
		trad = b"1"
	if (letter == "U"):
		trad = b"001"
	if (letter == "V"):
		trad = b"0001"
	if (letter == "W"):
		trad = b"011"
	if (letter == "X"):
		trad = b"1001"
	if (letter == "Y"):
		trad = b"1011"
	if (letter == "Z"):
		trad = b"1100"
	return trad

'''	
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
'''


def split(word): 
    return [char for char in word]

while 1:
	value_input = input("Entrez votre texte : ")
	data = split(value_input.upper())
	binary_data = []
	for char in data:
		char2 = to_morse(char)
		#print(type(char2))
		binary_data.append(char2)
	binary_data.append(b"2")
	#print(binary_data)
	for elem in binary_data:
		print(elem)
		ser.write(elem)
		#time.sleep(0.5)
		#print(ser.readline())#.decode().rstrip())
ser.close()
	



