class Conjunto:
    __listaConjunto=[]
    def __init__(self):
        self.__listaConjunto=[]
    def agregarValor(self,valor):
        if type(valor)==int:
            if valor not in self.__listaConjunto:
                self.__listaConjunto.append(valor)
        else:
            print('Error, no se pudo agregar un valor al conjunto, el tipo de datos es incorrecto.')
    def cantidadElementos(self):
        return len(self.__listaConjunto)
    def comprobarValor(self,valor):
        return valor in self.__listaConjunto
    def cargarOtroConjunto(self,otroConjunto):
        for numero in self.__listaConjunto:
            otroConjunto.agregarValor(numero)
    def __add__(self,conjunto2):
        conjuntoResultado=Conjunto()
        self.cargarOtroConjunto(conjuntoResultado)
        conjunto2.cargarOtroConjunto(conjuntoResultado)
        return conjuntoResultado
    def __sub__(self,conjunto2):
        conjuntoResultado=Conjunto()
        for numero in self.__listaConjunto:
            if not conjunto2.comprobarValor(numero):
                conjuntoResultado.agregarValor(numero)
        return conjuntoResultado
    def __eq__(self,conjunto2):
        resultado=False
        if len(self.__listaConjunto)==conjunto2.cantidadElementos():
            bandera=True
            i=0
            longitudConjunto=len(self.__listaConjunto)
            while i< longitudConjunto and bandera:
                if conjunto2.comprobarValor(self.__listaConjunto[i]):
                    i+=1
                else:
                    bandera=not bandera
            if i==longitudConjunto:
                resultado=True
        return resultado
    def __str__(self):
        cadena=''
        bandera=True
        for numero in self.__listaConjunto:
            if bandera:
                cadena+=str(numero)
                bandera=not bandera
            else:
                cadena='{},{}'.format(cadena,numero)
        return '{'+cadena+'}'
    def test(self):
        print('Comienza test Conjunto')
        conjuntoA=Conjunto()
        conjuntoB=Conjunto()
        conjuntoC=Conjunto()
        conjuntoD=Conjunto()
        print('Metodo agregarValor()')
        for i in range(1,5):
            conjuntoA.agregarValor(i)
        for i in range(4,0,-1):
            conjuntoC.agregarValor(i)
        for i in range(3,10,3):
            conjuntoB.agregarValor(i)
        print('A={},B={},C={},D={}'.format(conjuntoA,conjuntoB,conjuntoC,conjuntoD))
        print('Metodo cantidadElementos()')
        print(conjuntoB.cantidadElementos())
        print('Metodo comprobarValor()')
        print(conjuntoA.comprobarValor(1))
        print(conjuntoA.comprobarValor(22))
        print('Metodo cargarOtroConjunto()')
        conjuntoE=Conjunto()
        conjuntoA.cargarOtroConjunto(conjuntoE)
        print('E=',conjuntoE)
        print('Union')
        print('A+B=',conjuntoA+conjuntoB)
        print('A+C=',conjuntoA+conjuntoC)
        print('B+D=',conjuntoB+conjuntoD)
        print('Diferencia')
        print('A-B=',conjuntoA-conjuntoB)
        print('C-A=',conjuntoC-conjuntoA)
        print('A-D=',conjuntoA-conjuntoD)
        print('D-A=',conjuntoD-conjuntoA)
        print('Igualdad')
        print('A=B,',conjuntoA==conjuntoB)
        print('A=C,',conjuntoA==conjuntoC)
        print('B=D,',conjuntoB==conjuntoD)
        print('Fin test Conjunto. \n')