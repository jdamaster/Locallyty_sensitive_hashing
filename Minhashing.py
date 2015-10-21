import numpy
import random

#la siguiente clase representa una funcion hash,
# dicha funcion cambia aleatoriamente, para realizar
#el proceso de minhashing
class FuncionHash(object):

    def getHash(self,x):
        return ((self.a*x)+self.b) % self.n
    def __init__(self,n):
        self.n=n
        self.a=random.randint(1,n-1)
        self.b=random.randint(0,n-1)
    def newHash(self):
        self.a=random.randint(1,self.n-1)
        self.b=random.randint(0,self.n-1)

#----------------------------------------------------

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#metodo para calcular primo mas cercano
def nextPrime(n):
    prime=isPrime(n)
    if prime==True:
        return n
    else: 
        return nextPrime(n+1)
class Minhash(object):
   
    def __init__(self,filas,columnas,matriz,hashes):
    
        self.filas=filas
        self.columnas=columnas
        self.matriz=matriz
        self.hashes=hashes
        self.n=nextPrime(filas)
        self.infinito=self.filas+1
        """
        representacion del infinito, esta representacion se necesita
        para inicializar la matriz de minhash y posee un valor mayor al numero de filas
        dado que el valor que almacena la matriz de minhashing pose valores desde 0 hasta filas-1
        """
        #matriz que simula las permutaciones de las filas
        self.matrizHashes =numpy.zeros((self.filas,self.hashes))
        #matri que almacena los hashes minimos obtenidos de los sets
        self.minhashMatriz =numpy.zeros((self.hashes,self.columnas))



    #filas es el numero de palabras
    #   filas = 0

    #columnas representa el numero de sets
    #   columnas = 0

    #matriz de sets
    #   matriz=numpy.zeros(filas,columnas)

    #numero de hashes que se haran
    #   hashes = 100

    #numero primo mayor que las filas para
    # que la funcion hash sea efectiva
    # (en caso de que las filas sean un numero primo
    # n es el numero de filas)
    #   n=filas


    #inizializando la matriz con todos los hashes
    def CrearHashes(self):
        i=0
        j=0
        miFuncion=FuncionHash(self.n)
        while j< self.hashes:
            i=0
            while i< self.filas:
                self.matrizHashes[i][j]=miFuncion.getHash(i);
                i+=1
            j+=1
            miFuncion.newHash()

    def InitMinhash(self):
        i=0
        j=0
        while i<self.hashes:
            j=0
            while j<self.columnas:
                self.minhashMatriz[i][j]=self.infinito
                j+=1
            i+=1

    def ConstruirMinhas(self):
        i=0
        j=0
        while i<self.filas:
            j=0
            while j<self.columnas:
                if self.matriz[i][j]==1:
                    k=0
                    while k<self.hashes:
                        if(self.matrizHashes[i][k]<self.minhashMatriz[k][j]):
                            self.minhashMatriz[k][j]=self.matrizHashes[i][k]
                        k+=1
                j+=1
            i+=1
        return self.minhashMatriz






matriz=[[1,0,0,1],[0,0,1,0],[0,1,0,1],[1,0,1,1],[0,0,1,0]]
minH=Minhash(5,4,matriz,5)
minH.InitMinhash()
minH.CrearHashes()
signatures=minH.ConstruirMinhas()
print(minH.matrizHashes)
print(signatures)
