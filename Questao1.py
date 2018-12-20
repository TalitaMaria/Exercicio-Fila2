class Fila():
 def __init__(self):
   self.fila = []
 
 def isEmpty(self):
   return self.lenght() == 0
 
 def lenght(self):
   return len(self.fila)
 
 def peek(self):
   return self.fila[0]
 
 def enqueue(self,item):
   self.fila.append(item)
 
 def dequeue(self):
   if not(self.isEmpty()):
     self.fila.pop(0)

 def inverter(self):
    pilha = Pilha()
    for i in range(self.lenght()-1,-1,-1):
      pilha.push(self.fila[i])
    print(pilha.pilha)

class Pilha():
 def __init__(self):
   self.pilha = []

 def lenght(self):
   return len(self.pilha)

 def isEmpyt(self):
   return self.lenght()==0

 def push(self, elemento):
   self.pilha.append(elemento)

 def pop():
   self.pilha  
     
fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
print(fila.fila)
fila.inverter()
