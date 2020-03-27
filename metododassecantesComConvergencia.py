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
  funcao=(i**2)-2
  return(funcao)

def secante(xatual,xanterior,fxatual,fxanterior):
  secante=((xanterior*funcaoatual)-(xatual*funcaoanterior))/(funcaoatual-funcaoanterior)
  return(secante)


#Escolha Inicial
xanterior=1500 #x0 inicial
xatual=1100 #x1 inicial
funcaoanterior=funcao(xanterior)
funcaoatual=funcao(xatual)
resultados=[]

for i in range (0,100): # 100 iterações no maximo
  if abs(xatual-xanterior) < 10**-5:
    break
  else:
    
    proximox=secante(xatual,xanterior,funcaoatual,funcaoanterior)
    funcaoanterior=funcaoatual
    xanterior=xatual
    xatual=proximox
    funcaoatual=funcao(xatual)
    resultados.append(funcaoatual)


print("O resultado e: ",xatual)

ordemDeConvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])