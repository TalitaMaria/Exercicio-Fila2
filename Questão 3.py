from random import randint

def enqueue(queue,v):
    queue.append(v)
    return queue

tempos = []
clientes = []

tempo_atendimento = 0
soma = 0

for i in range(1000):
    tempos = enqueue(tempos,tempo_atendimento)
    clientes = enqueue(clientes,'a')
    auxiliar = randint(1,15)
    tempo_atendimento += auxiliar
    soma += auxiliar

print("TEMPO MEDIO DE ATENDIMENTO: %.2f"%(soma/1000))
