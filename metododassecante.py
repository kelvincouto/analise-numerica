def funcao(i):
  funcao=(i**2)-100
  return(funcao)

def secante(xatual,xanterior,fxatual,fxanterior):
  secante=((xanterior*funcaoatual)-(xatual*funcaoanterior))/(funcaoatual-funcaoanterior)
  return(secante)


#Escolha Inicial
xanterior=1500 #x0 inicial
xatual=1100 #x1 inicial
funcaoanterior=funcao(xanterior)
funcaoatual=funcao(xatual)

for i in range (0,100): # 100 iterações no maximo
  if abs(xatual-xanterior) < 10**-5:
    break
  else:
    
    proximox=secante(xatual,xanterior,funcaoatual,funcaoanterior)
    funcaoanterior=funcaoatual
    xanterior=xatual
    xatual=proximox
    funcaoatual=funcao(xatual)


print(xatual)
