from funciones import *

def ejemplo():

    #Creamos los polinomios vacios
    polinomio1 = polinomio()
    polinomio2 = polinomio()
    
    #Les añadimos terminos
    agregar_termino(polinomio1, 3, 5)
    agregar_termino(polinomio2, 3, 1)

    agregar_termino(polinomio1, 1, 7)
    agregar_termino(polinomio2, 1, 4)    

    #Mostramos los polinomios
    print("Este es el polinomio 1:")
    print(mostrar(polinomio1))
    print("\n")
    print("Este es el polinomio 2:")
    print(mostrar(polinomio2))
    print("\n")

    #Restamos ambos terminos
    print("Polinomio 1 menos polinomio 2:")
    print(mostrar(sumar(polinomio1, polinomio2)))
    print("\n")

    #Dividimos ambos terminos
    print("Polinomio 1 entre polinomio 2:")
    print(mostrar(multiplicar(polinomio1, polinomio2)))
    print("\n")

    #Eliminamos un termino
    print("Eliminamos el coeficiente del termino de grado 1:")
    print(mostrar(polinomio1))
    print(eliminar(polinomio1, 1))
    print(mostrar(polinomio1))
    print("\n")
    
    #Vemos si existe 5
    print(existe(polinomio1, 3))

ejemplo()