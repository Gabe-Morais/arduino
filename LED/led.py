from turtle import xcor
import pyfirmata
import time
import mysql.connector

pin = 7
port = 'COM4'
board = pyfirmata.Arduino(port)

dataBase = mysql.connector.connect(host = "localhost",user = "root",passwd = "",database = "arduino")
registro = dataBase.cursor()
query = "SELECT VALOR FROM LED"
registro.execute(query)
 
resultado = registro.fetchall()

for x in resultado:
    piscar = x[0]

dataBase.close()
print("Piscando " + str(piscar) + " vezes.")
 
for x in range(int(piscar)):
  board.digital[pin].write(1)
  time.sleep(1)
  board.digital[pin].write(0)
  time.sleep(1)