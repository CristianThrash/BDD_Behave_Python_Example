Feature: Barajar monte de cartas

Scenario: Monte de cartas inicial debe quedar en distinto orden
	Given tengo un monte de cartas
	When el monte sea barajado
	Then el monte resultante no debe ser igual al inicial
