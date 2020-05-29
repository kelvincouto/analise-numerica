import numpy as np
from matplotlib import pyplot as plt

def metodoSOR(n,omega,tolerancia,matrizInicial):
  variacao = 100 # Variavel para garantirmos a primeira iteracao, salvamos posterirmente ||x-X0||
  numeroIteracoes=0
  matrizT=matrizInicial.copy()
  matrizTanterior=matrizInicial.copy()#matriz que sera alterada e salva x(n-1)

  while variacao>tolerancia and numeroIteracoes<500:
    numeroIteracoes=numeroIteracoes+1
    for i in range(1,n-1):
      for j in range(1,n-1):
       matrizT[i][j]=((1-omega)*(matrizT[i][j]))+(((omega/4)*(matrizT[i-1][j]+matrizT[i+1][j]+matrizT[i][j-1]+matrizT[i][j+1])))
    a=matrizT-matrizTanterior
    variacao=abs(max(a.min(), a.max(), key=abs)) #norma infinita de x-x0
    matrizTanterior=matrizT.copy()
  return(numeroIteracoes,matrizT)


n=64
tolerancia=1e-2
#Definimos T primeiramente com vetores nulos
T=np.zeros((n, n))

for i in range (0,n):
  T[i][0]=-3
  
for j in range (0,n):
  T[0][j]=-3

for i in range (1,n):
  T[i][n-1]=((6*(i)/n)-3)

for j in range (1,n):
  T[n-1][j]=((6*(j)/n)-3)

vetorOmega = np.zeros(100) #Valores de omega
vetorIterZero = np.zeros(100) # Quantidade de iteracoes com chute inicial zero
vetorIterAleatorio = np.zeros(100) # Quantidade de iteracoes com chute inicial com valores aleatorios
for i in range (0,100):
  omega=1+((i+1)/100)
  vetorOmega[i]=omega


for i in range (0,100):
  iteracoes,Z=metodoSOR(n,vetorOmega[i],tolerancia,T)
  vetorIterZero[i]=iteracoes
  print(i)
  print(Z)


#Redefinimos T de modo a ter o chute inicial com valores aleatórios
for i in range (1,n-1):
  for j in range (1,n-1):
    T[i][j]=np.random.random_sample()

for i in range (0,100):
  iteracoes,Z=metodoSOR(n,vetorOmega[i],tolerancia,T)
  vetorIterAleatorio[i]=iteracoes
  print(i)
  print(Z)


print(vetorIterZero)
print(vetorIterAleatorio)


plt.plot(vetorOmega,vetorIterZero)
plt.plot(vetorOmega, vetorIterAleatorio)
plt.xlabel("Valores de Omega")
plt.ylabel("Numero de Iteracoes")
plt.title("Numero de Iteracoes em Funcao de Omega")
plt.legend(['Chute Inicial Zero','Chute Inicial Valores Aleatorios'])
plt.show()