from Conjunto import Conjunto
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.test,
            '5':self.salir
        }
    def lanzarMenu(self,conjunto1):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para calcular la  union de dos conjuntos.')
            print('-Ingrese 2 para calcular la diferencia de dos conjuntos.')
            print('-Ingrese 3 para verificar si dos conjuntos son iguales.')
            print('-Ingrese 4 para ejecutar test.')
            print('-Ingrese 5 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='2' or opcion=='3':
                ejecutar(conjunto1)
            else:
                ejecutar()
    def opcion1(self,conjunto1):
        conjunto2=self.cargarConjunto()
        conjunto3=conjunto1+conjunto2
        print('A+B={}, con A={} y B={}'.format(conjunto3,conjunto1,conjunto2))
    def opcion2(self,conjunto1):
        conjunto2=self.cargarConjunto()
        conjunto3=conjunto1-conjunto2
        print('A-B={}, con A={} y B={}'.format(conjunto3,conjunto1,conjunto2))
    def opcion3(self,conjunto1):
        conjunto2=self.cargarConjunto()
        iguales=conjunto1==conjunto2
        if iguales:
            print('A es igual a B, A={},B={}'.format(conjunto1,conjunto2))
        else:
            print('A es distinto a B, A={},B={}'.format(conjunto1,conjunto2))
    def cargarConjunto(self):
        conjunto2=Conjunto()
        print('A continuacion se inicia la carga del Conjunto B, para finalizar la carga ingrese s')
        op='1'
        while(op!='s'):
            op=input('Ingrese un numero o s para salir:\n')
            if(op!='s'):
                conjunto2.agregarValor(int(op))
            else:
                print('Finalizo la carga del Conjunto B')
        return conjunto2
    def test(self):
        conjuntoT=Conjunto()
        conjuntoT.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')