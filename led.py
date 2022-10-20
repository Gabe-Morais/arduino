import pyfirmata
import time
pin = 13
port = 'COM4'
board = pyfirmata.Arduino(port)
 
numeroBlink = input('Insira o número de vezes que o LED deve piscar: ')
print("Piscando " + numeroBlink + " vezes.")
 
for x in range(int(numeroBlink)):
  board.digital[13].write(1)
  time.sleep(5)
  board.digital[13].write(0)
  time.sleep(5)
