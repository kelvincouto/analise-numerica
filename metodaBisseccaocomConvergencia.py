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

def funcao(i):
	fx= (i**2)-100
	return (fx)


a=1
b=20

fa=funcao(a)
fb=funcao(b)
resultados = []
for i in range (0,100): # 100 iterações no maximo
  p = (a+b)/2
  fp = funcao(p)
  resultados.append(p)
  if fp*fb>0:
    b=p
  else:
    a=p
  if abs(fp) < 10**-5:
    print("Saida um")
    break
  elif abs(b-a) < 10**-5:
    print("Saida dois")
    break


print("Sua Raiz sera: ",p)


ordemDeConvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])