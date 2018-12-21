import time
import random 

class Fila_De_impressao:
  def __init__(self):
    self.fila = []
  
  def requerimento(self,documento):
    self.fila.append(documento)
  
  def isEmpty(self):
    return len(self.fila) == 0

  def impressao(self,numero):
    while not(self.isEmpty()):
      time.sleep(numero)
      print(self.fila[0])
      print('O documento foi impresso')
      self.fila.pop(0)

Impressora = Fila_De_impressao()
Impressora.requerimento('Talita')
Impressora.requerimento('Giulia')
Impressora.requerimento('Rhavy')
numero = random.randint(1,10)
Impressora.impressao(numero)
