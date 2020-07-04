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

  for i in range(0,n):
    a[i]=(2/h)+(2*l*h/3)

  for i in range(0,n-1):
    b[i]=(-1/h)+(l*h/6)

  for i in range(0,n):
    d[i]=-12*h**3*(i+1)**2-2*h**3+12*h**2*(i+1)-2*h


  x=Thomas(a,b,d)




  erro=np.zeros(n)
  xi=np.zeros(n)
  u=np.zeros(n)
  for i in range (0,n):
    xi[i]=(i+1)*h
    u[i]=(xi[i]**2)*(xi[i]-1)**2

    #Plota X e U
  plt.plot(xi,x)
  plt.plot(xi,u)
  plt.xlabel("Valores de Xi")
  plt.ylabel("Valores de U")
  plt.title("Spline Linear")
  plt.legend(['Calculado','Original'])
  plt.show()    
  
  
  return()


calculoFuncao(255)