import numpy as np
import zmq
import time
import datetime
import logging

# robolab123
file_name = "arduino_zlata/data_zlata.txt"

logging.basicConfig(filename='arduino_zlata/zlata.log', encoding='utf-8',
                     level=logging.CRITICAL, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

connected = False
start = time.time()
while not connected:
    try:
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt(zmq.SUBSCRIBE, b"")
        socket.connect("tcp://192.168.0.102:5555")

        connected = True
    except:
        logging.critical("Unabled to connect to server")
        time.sleep(0.05)


while True:
    try:
        mes = socket.recv_string()
        data = mes.split()
        if len(data) < 1:
            logging.critical("Received message has len=0")
        else:
            print(f"received event: {mes}")
            if data[0] in ['p', 't', 'm']:
                with open(file_name, 'a') as file:
                    file.write(f"{datetime.datetime.now()}\t{mes}\n")
            else:
                logging.critical("Unknown data")

    except Exception as e:
        logging.critical(str(e))
        time.sleep(0.05)
    