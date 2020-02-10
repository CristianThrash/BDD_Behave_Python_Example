Feature: Determinar al ganador

Scenario: El valor de la mano del jugador supera el de la mano del crupier
    Given el valor de la mano del jugador es 20
    And el valor de la mano del crupier es 18
    Then el ganador debe ser el jugador

Scenario: El valor de la mano del crupier supera el de la mano del jugador
    Given el valor de la mano del jugador es 20
    And el valor de la mano del crupier es 21
    Then el ganador debe ser el crupier

Scenario: Las manos tienen igual valor
    Given el valor de la mano del jugador es 20
    And el valor de la mano del crupier es 20
    Then se decide un empate

Scenario: El jugador tiene 21 por blackjack
    Given el valor de la mano del jugador es 21 por blackjack
    And el valor de la mano del crupier es 21
    Then el ganador debe ser el jugador

Scenario: El crupier tiene 21 por blackjack
    Given el valor de la mano del jugador es 21
    And el valor de la mano del crupier es 21 por blackjack
    Then el ganador debe ser el crupier

Scenario: Crupier y jugador tienen 21 por blackjack
    Given el valor de la mano del jugador es 21 por blackjack
    And el valor de la mano del crupier es 21 por blackjack
    Then se decide un empate
