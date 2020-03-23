def funcaonewton(i):
  funcao=(i**2)-100
  derivada= (2*i)
  newton= i-(funcao/derivada)
  print(newton)

  return(newton)




#Escolha Inicial
a=1500


for i in range (0,100): # 100 iterações no maximo
  fa=funcaonewton(a)
  if abs(fa-a) < 10**-5:
    break
  else:
    a=fa

print(fa)