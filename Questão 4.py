from random import randint

def enqueue(queue,v):
    queue.append(v)
    return queue

def dequeue(queue):
    queue.pop(0)
    return queue
    
fila = []
for i in range(1000):
    fila = enqueue(fila,"Pessoa")

soma = 0
for i in range(1000):
    fila = dequeue(fila)
    soma += randint(1,15)

print("O tempo medio de espera foi de %.2f minutos(s) de espera"%(soma/1000))
