#Damian Bermudez Lara
#Contador


#crear la clase
class Contador_Seguro:
    #constructor
    def __init__(self):
        self._n = 0  

    #metodo para incrementar
    def inc(self):
        self._n += 1
        self.__log()

    #metodo de solo lectura
    @property
    def n(self):
        return self._n  

    def __log(self):
        print("tick")  

def main():

    contador = Contador_Seguro()
    contador.inc()  
    print("Valor final:", contador.n)
    contador.inc()  
    print("Valor final:", contador.n)  

if __name__ == "__main__":
    
    main()
