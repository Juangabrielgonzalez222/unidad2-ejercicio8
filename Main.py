from Conjunto import Conjunto
from Menu import Menu

if __name__== '__main__':
    conjunto1=Conjunto()
    print('A continuacion se inicia la carga del Conjunto A, para finalizar la carga ingrese s')
    op='1'
    while(op!='s'):
        op=input('Ingrese un numero o s para salir:\n')
        if(op!='s'):
            valor=int(op)
            conjunto1.agregarValor(int(op))
        else:
            print('Finalizo la carga del Conjunto A')
    menu=Menu()
    menu.lanzarMenu(conjunto1)