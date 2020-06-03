import numpy as np
from matplotlib import pyplot as plt

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


n=512
tolerancia=1e-6
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

vetorOmega = np.zeros(100) #Valores de omega
vetorIterZero = np.zeros(100) # Quantidade de iteracoes com chute inicial zero
vetorIterAleatorio = np.zeros(100) # Quantidade de iteracoes com chute inicial com valores aleatorios
#Valores de Omega dados pelo exercicio
for i in range (0,100):
  omega=1+((i+1)/100)
  vetorOmega[i]=omega

#omega = 2 nao apresentou menos de 100000 iteracoes para nenhum N testado, pode ser que nao ha convergencia 

#Calculo de Iterações para Cada Omega com Chute Inicial Nulo
for i in range (0,100):
  iteracoes,Z1=metodoSOR(n,vetorOmega[i],tolerancia,T)
  vetorIterZero[i]=iteracoes
  print("Omega: ",vetorOmega[i]," Iterações: ",iteracoes)
  print(Z1)



#Redefinimos T de modo a ter o chute inicial com valores aleatórios
for i in range (1,n-1):
  for j in range (1,n-1):
    T[i][j]=np.random.random_sample()

#Calculo de Iterações para Cada Omega com Chute Inicial Aleatorio
for i in range (0,100):
  iteracoes,Z2=metodoSOR(n,vetorOmega[i],tolerancia,T)
  vetorIterAleatorio[i]=iteracoes
  print("Omega: ",vetorOmega[i]," Iterações: ",iteracoes)
  print(Z2)

#Podemos observar a quantidade de iteracoes de cada omega
print("Iteraçoes com chute nulo \n")
for i in range(0,100):
  print(vetorIterZero[i])

#Podemos observar a quantidade de iteracoes de cada omega
print("Iteraçoes com chute aleatorio\n")
for i in range(0,100):
  print(vetorIterAleatorio[i])


plt.plot(vetorOmega,vetorIterZero)
plt.plot(vetorOmega, vetorIterAleatorio)
plt.xlabel("Valores de Omega")
plt.ylabel("Numero de Iteracoes")
plt.title("Numero de Iteracoes em Funcao de Omega")
plt.legend(['Chute Inicial Zero','Chute Inicial Valores Aleatorios'])
plt.show()