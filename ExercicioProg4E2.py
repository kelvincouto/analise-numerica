import numpy as np
from matplotlib import pyplot as plt

def Thomas (a,b,d):
  z=len(a)
  for i in range (1,z):
    #Calcula a diagonal principal e o novo d
      a[i]=a[i]-(b[i-1]*b[i-1]/a[i-1])
      d[i]=d[i]-(b[i-1]*d[i-1]/a[i-1])
  
  #Calculo do vetor x
  x=np.zeros(z)
  x[-1]=d[-1]/a[-1]

  for i in range (z-2,-1,-1):
    x[i]=(d[i]-(b[i]*x[i+1]))/a[i]
  
  return x


def calculoFuncao (n):
  h=1/(n+1)
  l=0 # valor de lambda
  a=np.zeros(n)
  b=np.zeros(n-1)
  d=np.zeros(n)
  #Calculo de aii, aij, e di
  for i in range(0,n):
    a[i]=(2/h)+(2*l*h/3)

  for i in range(0,n-1):
    b[i]=(-1/h)+(l*h/6)

  for i in range(0,n):
     d[i]=-12*h**3*(i+1)**2-2*h**3+12*h**2*(i+1)-2*h


  x=Thomas(a,b,d)

  #Neste Ponto, calculamos os valores entre pontos usando as retas do spline linear.
  #Como nosso algoritmo não calcula originalmente x0 e xn, adicionamos os valores de borda



  c=x.copy()
  c=np.insert(c,0,0)
  c=np.append(c,0)

  erro=np.zeros(10*(n+1))
  xi=np.zeros(10*(n+1))
  u=np.zeros(10*(n+1))
  y=np.zeros(10*(n+1))

  
  for i in range (0,n+1):
    for j in range (0,10):
      #Valores de xi de 0 a 10n
      xi[(10*i)+j]=(10*i+j)/(10*(n))
      #Valores de u original
      u[(10*i)+j]=(xi[(10*i)+j]**2)*(xi[((10*i)+j)]-1)**2
      #Equacao calculada 
      y[(10*i)+j]=((c[i+1]-c[i])/h)*xi[(10*i)+j]-(c[i+1]-c[i])*(i)+c[i]
      erro[(10*i)+j]=abs(u[(10*i)+j]-y[(10*i)+j])
  

  

  return(erro.max())


valoresDeN=np.array([15,31,63,127,255])
valoresDeErro=np.zeros(len(valoresDeN))

for i in range (0,len(valoresDeN)):
  valoresDeErro[i]=calculoFuncao(valoresDeN[i])
  print(" Para o valor de n: ",valoresDeN[i], "temos o erro: ", valoresDeErro[i])

for i in range (0,(len(valoresDeN)-1)):
  print(" Entre n=",valoresDeN[i], " e n=", valoresDeN[i+1], "o erro caiu ", (valoresDeErro[i]/valoresDeErro[i+1]))

plt.yscale('log',basey=10) 
plt.plot(valoresDeN,valoresDeErro)
plt.xlabel("Valores de N")
plt.ylabel("Erro")
plt.title("Erro por N")
plt.show()