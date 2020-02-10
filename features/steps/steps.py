from behave import *
from blackjack import *

crupier=Crupier()
jugador=Jugador()

@given('tengo un monte de cartas')
def step_impl(context):
	context.result = crupier.getBaraja().copy()

@when('el monte sea barajado')
def step_impl(context):
	crupier.barajar()

@then('el monte resultante no debe ser igual al inicial')
def step_impl(context):
	assert context.result!=crupier.getBaraja()

@given('el jugador tiene en su mano J de diamantes, K de treboles y A de picas')
def step_impl(context):
	jugador.reiniciarMano()
	jugador.agregarCarta([('J','Dia')])
	jugador.agregarCarta([('K','Tre')])
	jugador.agregarCarta([('A','Pic')])

@when('se determine el valor de la mano')
def step_impl(context):
	context.result = jugador.getValorMano()

@then('el valor de la mano del jugador debe ser 21')
def step_impl(context):
	assert context.result==21

@given('el jugador tiene en su mano 2 de diamantes, 5 de corazones y A de picas')
def step_impl(context):
	jugador.reiniciarMano()
	jugador.agregarCarta([(2,'Dia')])
	jugador.agregarCarta([(5,'Cor')])
	jugador.agregarCarta([('A','Pic')])

@then('el valor de la mano del jugador debe ser 18')
def step_impl(context):
	assert context.result==18

@given('el valor de la mano del jugador es 20')
def step_impl(context):
	jugador.reiniciarMano()
	jugador.agregarCarta([('J','Dia')])
	jugador.agregarCarta([('K','Dia')])
	assert jugador.getValorMano()==20

@given('el valor de la mano del crupier es 18')
def step_impl(context):
	crupier.reiniciarMano()
	crupier.agregarCarta([(5,'Dia')])
	crupier.agregarCarta([(2,'Dia')])
	crupier.agregarCarta([('A','Dia')])
	assert crupier.getValorMano()==18

@then('el ganador debe ser el jugador')
def step_impl(context):
    assert crupier.ganaJugador(jugador)==1

@given('el valor de la mano del crupier es 21')
def step_impl(context):
	crupier.reiniciarMano()
	crupier.agregarCarta([('J','Dia')])
	crupier.agregarCarta([('K','Dia')])
	crupier.agregarCarta([('A','Dia')])
	assert crupier.getValorMano()==21

@then('el ganador debe ser el crupier')
def step_impl(context):
    assert crupier.ganaJugador(jugador)==2

@given('el valor de la mano del crupier es 20')
def step_impl(context):
	crupier.reiniciarMano()
	crupier.agregarCarta([('J','Dia')])
	crupier.agregarCarta([('K','Dia')])
	assert crupier.getValorMano()==20

@then('se decide un empate')
def step_impl(context):
    assert crupier.ganaJugador(jugador)==3

@given('el valor de la mano del jugador es 21 por blackjack')
def step_impl(context):
	jugador.reiniciarMano()
	jugador.agregarCarta([('J','Dia')])
	jugador.agregarCarta([('A','Dia')])
	assert jugador.getValorMano()==21

@given('el valor de la mano del jugador es 21')
def step_impl(context):
	jugador.reiniciarMano()
	jugador.agregarCarta([('J','Dia')])
	jugador.agregarCarta([('K','Dia')])
	jugador.agregarCarta([('A','Dia')])
	assert jugador.getValorMano()==21

@given('el valor de la mano del crupier es 21 por blackjack')
def step_impl(context):
	crupier.reiniciarMano()
	crupier.agregarCarta([('J','Dia')])
	crupier.agregarCarta([('A','Dia')])
	assert crupier.getValorMano()==21

@given('el jugador tenía un total de 50 en su bolsa')
def step_impl(context):
	jugador.setFichas(50)

@given('la apuesta del jugador fue de 10')
def step_impl(context):
	pass

@when('se juega un turno')
def step_impl(context):
	crupier.reiniciarMano()
	jugador.reiniciarMano()
	context.result=turno(jugador,crupier)

@then('el jugador debe tener 70 en su bolsa')
def step_impl(context):
	if(context.result==1):
		assert jugador.getFichas()==70
	else:
		pass

@then('el jugador debe tener 40 en su bolsa')
def step_impl(context):
	if(context.result==2):
		assert jugador.getFichas()==40
	else:
		pass

@then('el jugador debe tener 45 en su bolsa')
def step_impl(context):
	if(context.result==3):
		assert jugador.getFichas()==45
	else:
		pass
