import sys
import requests
import time

## Declaration of Global Variables

hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }


def Main():
	fp = open('/dev/hidraw0', 'rb')
	ss = ""
	shift = False
	url = "http://192.168.1.50:3000/PostBarcode?barcode="
	with open("log.txt", "a") as log_file: 
		try:
			while True:
				buffer = fp.read(8)
				for c in buffer:
					if ord(c) > 0:
						if int(ord(c)) == 40:
							with open("Output.txt", "a") as text_file:
								text_file.write("Barcode : %s" % ss)
								print(ss)
								log_file.write(str(time.ctime()) +" - " + "Barcode : " + ss)
								send_url = url + ss
								r = requests.get(send_url)
								log_file.write(str(time.ctime()) +" - " + "API Cal Result :" + r)
							ss = ""
						if int(ord(c)) != 40:
							if shift:
								if int(ord(c)) == 2 :
									shift=True
								else:
									ss += hid2[ int(ord(c)) ]
									shift = False
							else:
								if int(ord(c)) == 2 :
									shift=True
								else:
									ss += hid[ int(ord(c)) ]
									shift = False
		except Exception as err:
			log_file.write(str(time.ctime()) +" - " + "Error : " + str(err))
			Main()

if __name__ == "__main__":
	Main()