import numpy as np
import matplotlib.pyplot as plt


def metodoSOR(n,omega,tolerancia,matrizInicial):
  variacao = 100 # Variavel para garantirmos a primeira iteracao, salvamos posterirmente ||x-X0||
  numeroIteracoes=0
  matrizT=matrizInicial.copy()
  matrizTanterior=matrizInicial.copy()#matriz que sera alterada e salva x(n-1)

  while variacao>tolerancia and numeroIteracoes<100000:
    numeroIteracoes=numeroIteracoes+1
    for i in range(1,n):
      for j in range(1,n):
       matrizT[i][j]=((1-omega)*(matrizT[i][j]))+(((omega/4)*(matrizT[i-1][j]+matrizT[i+1][j]+matrizT[i][j-1]+matrizT[i][j+1])))
    a=matrizT-matrizTanterior
    variacao=abs(max(a.min(), a.max(), key=abs)) #norma infinita de x-x0
    matrizTanterior=matrizT.copy()
  return(numeroIteracoes,matrizT)




n=128
tolerancia=1e-6
omega=1.95 #Omega Otimo, Segundo Planilha do Excel
#Definimos T primeiramente com vetores nulos
T=np.zeros(((n+1), (n+1)))

for i in range (0,(n+1)):
  T[i][0]=-3
  
for j in range (0,(n+1)):
  T[0][j]=-3

for i in range (1,(n+1)):
  T[i][n]=((6*(i)/n)-3)

for j in range (1,(n+1)):
  T[n][j]=((6*(j)/n)-3)


iteracoes,Z1=metodoSOR(n,omega,tolerancia,T)



x=np.zeros(n+1)
y=np.zeros(n+1)
for i in range (0,n+1):
  x[i]=i
  y[i]=i



plt.contourf(x,y,Z1, cmap='bwr')
plt.colorbar()
plt.show()