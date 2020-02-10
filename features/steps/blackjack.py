from random import shuffle

class Jugador:
    __mano=[]
    __fichas=0
    __apuesta=0

    def __init__(self):
        pass

    def getNumeroCartas(self):
        return len(self.__mano)

    def getMano(self):
        return self.__mano

    def setFichas(self,fichas):
        self.__fichas=fichas

    def getFichas(self):
        return self.__fichas

    def agregarCarta(self, carta):
        self.__mano=self.__mano+carta

    def reiniciarMano(self):
        self.__mano=[]

    def apostar(self, apuesta):
        self.__fichas-=apuesta
        self.__apuesta=apuesta

    def resolverApuesta(self,resultado):
        if(resultado==1):
            self.__fichas+=self.__apuesta*2
            self.__apuesta=0
        elif(resultado==2):
            self.__apuesta=0
        else:
            self.__fichas+=self.__apuesta/2
            self.__apuesta=0

    def getValorMano(self):
        valor=0
        for carta in self.__mano:
            if(carta[0]=='J' or carta[0]=='Q' or carta[0]=='K'):
                valor+=10
            elif(carta[0]=='A' and valor+11<=21):
                valor+=11
            elif(carta[0]=='A' and valor+11>21):
                valor+=1
            else:
                valor+=carta[0]
                
        return valor

class Crupier(Jugador):
	__baraja=[(x,y) for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] for y in ['Dia','Tre','Pic','Cor']]

	def __init__(self):
		pass

	def barajar(self):
		shuffle(self.__baraja)

	def getBaraja(self):
		return self.__baraja

	def ganaJugador(self,jugador):
		if(self.getValorMano()<jugador.getValorMano()):
			return 1
		elif(self.getValorMano()>jugador.getValorMano()):
			return 2
		elif(self.getValorMano()==21):
			if(self.getNumeroCartas()==2 and jugador.getNumeroCartas()>2):
				return 2
			elif(self.getNumeroCartas()>2 and jugador.getNumeroCartas()==2):
				return 1
			else:
				return 3
		else:
			return 3

def turno(jugador,crupier):
	crupier.barajar()
	jugador.apostar(int(input("Apuesta: ")))
	crupier.agregarCarta([crupier.getBaraja().pop()])
	print("Mano del crupier"+str(crupier.getMano()))
	jugador.agregarCarta([crupier.getBaraja().pop()])
	jugador.agregarCarta([crupier.getBaraja().pop()])
	print("Mano del jugador"+str(jugador.getMano()))
	opcion = input("1. Plantarse \n2. Pedir carta")
	while(opcion==2 and jugador.getValorMano()<21):
		jugador.agregarCarta([crupier.getBaraja().pop()])
		print("Mano del jugador"+str(jugador.getMano()))
		if(jugador.getValorMano()<21):
			opcion = input("1. Plantarse \n2. Pedir carta")
	if(jugador.getValorMano()<=21):
		crupier.agregarCarta([crupier.getBaraja().pop()])
		print("Mano del crupier"+str(crupier.getMano()))
		while(crupier.getValorMano()<=16):
			crupier.agregarCarta([crupier.getBaraja().pop()])
			print("Mano del crupier"+str(crupier.getMano()))
		if(crupier.getValorMano()>21):
			resultado=1
		else:
			resultado=crupier.ganaJugador(jugador)
	else:
		resultado=2
	jugador.resolverApuesta(resultado)
	return resultado
