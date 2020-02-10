Feature: Contar valor de la mano del jugador

Scenario: El as hace que se superen los 21 puntos con valor de 11
    Given el jugador tiene en su mano J de diamantes, K de treboles y A de picas
    When se determine el valor de la mano
    Then el valor de la mano del jugador debe ser 21

Scenario: El as no hace que se superen los 21 puntos con valor de 11
    Given el jugador tiene en su mano 2 de diamantes, 5 de corazones y A de picas
    When se determine el valor de la mano
    Then el valor de la mano del jugador debe ser 18
