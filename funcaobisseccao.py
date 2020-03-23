## Este programa avalia o método numérico para definir a raiz de 2


def funcao(i):
	fx= (i**2)-2
	return (fx)


print("Entre um a tal que f(a).f(b)<0 (O b vem depois)")
a=int(input())
print("Entre um b tal que f(a).f(b)<0")
b=int(input())

fa=funcao(a)
fb=funcao(b)


for i in range (0,100): # 100 iterações no maximo
  p = (a+b)/2
  fp = funcao(p)
  if fp*fb>0:
    b=p
  else:
    a=p
  if abs(fp) < 10**-5:
    print("Uno")
    break
  elif abs(b-a) < 10**-5:
    print("Dos")
    break


print(p)
