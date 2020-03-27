import math
import numpy as np

def ordemDeConvergencia(x0,x1,x2,x3):
  e2=abs((x3-x2))
  e1=abs((x2-x1))
  e0=abs((x1-x0))
  ordemConvergencia1 = np.log(e2/e1)
  ordemConvergencia2 = np.log(e1/e0)
  ordemConvergencia = ordemConvergencia1/ordemConvergencia2
  constanteAssintotica= (e2/(e1**ordemConvergencia))
  print("A ordem de Convergencia sera", ordemConvergencia)
  print("A constante Assintotica sera", constanteAssintotica)
  return()


def funcaonewton(i):
  funcao= ((i**2)-100*i)
  derivada= (2*i)-100
  newton= i-(funcao/derivada)
  #print(newton)

  return(newton)




#Escolha Inicial
x0=1500
a=x0

resultados=[]

for i in range (0,100): # 100 iterações no maximo
  fa=funcaonewton(a)
  resultados.append(fa)
  if abs(fa-a) < 10**-5:
    break
  else:
    a=fa

print("Sua raiz sera : ",fa)

ordemDeConvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])