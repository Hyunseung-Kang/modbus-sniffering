import serial
import time

port = "COM12"
baud = 19200
ser = serial.Serial(port, baud, timeout=1)

def main():
    global ser
    prev_data = ""
    curr_data = ""
    data = []
    while True:
        if ser.readable():
            curr_data = ser.read().hex()
            if curr_data != "":
                data.append(curr_data)

            if curr_data == "" and prev_data != "":
                print("data: ", data)
                data = []
            prev_data = curr_data

    ser.close()

main()
