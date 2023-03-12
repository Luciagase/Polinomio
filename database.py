class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class polinomio(datoPolinomio):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if termino > polinomio.grado:
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None) and (termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while(aux is not None) and (aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while (aux is not None) and (aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None) and (aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
    
    def mostrar(polinomio):
        aux = polinomio.termino_mayor
        pol = ''
        if aux is not None:
            while aux is not None:
                signo = ' '
                if aux.info.valor >= 0:
                    signo = ' + '
                pol += signo + str(aux.info.valor) + 'x^' + str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def suma(polinomio1, polinomio2):
        paux = polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = obtener_valor(polinomio1, i) + obtener_valor(polinomio2, i)
            if total != 0:
                agregar_termino(paux, i, total)
        return paux
    
    def multiplicar(polinomio1, polinomio2):
        paux = polinomio()
        pol1 = polinomio1.termino_mayor
        while pol1 is not None:
            pol2 = polinomio2.termino_mayor
            while pol2 is not None:
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if obtener_valor(paux, termino) != 0):
                    valor += obtener_valor(paux, termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
    

        ''' def eliminar_termino(self, termino):
        aux = self.termino_mayor
        if (self.grado == termino):
            self.termino_mayor = aux.sig
            del aux
        else:
            while aux.sig is not None:
                if aux.sig.info.termino == termino:
                    aux.sig = aux.sig.sig
                    del aux.sig
                    return
                aux = aux.sig  '''

    def eliminar(polinomio, termino):
        pol = polinomio.termino_mayor
        while pol is not None:
            termino_pol = pol.info.termino
            if termino_pol == termino:
                pol.info.valor = 0
                print("Se elimino el término")
                return
            else:
                pol = pol.sig

    def existe(polinomio, termino):
        pol = polinomio.termino_mayor
        while pol is not None:
            termino_pol = pol.info.termino
            if termino_pol == termino:
                return pol.info.valor
            elif termino_pol is None:
                return False
            else:
                pol = pol.sig     

def ejercicio4():

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