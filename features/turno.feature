Feature: Jugar un turno

Scenario: Gana el jugador
    Given el jugador tenía un total de 50 en su bolsa
    And la apuesta del jugador fue de 10
    When se juega un turno
    Then el jugador debe tener 70 en su bolsa

Scenario: Gana el crupier
    Given el jugador tenía un total de 50 en su bolsa
    And la apuesta del jugador fue de 10
    When se juega un turno
    Then el jugador debe tener 40 en su bolsa    

Scenario: Empate entre el jugador y el crupier
    Given el jugador tenía un total de 50 en su bolsa
    And la apuesta del jugador fue de 10
    When se juega un turno
    Then el jugador debe tener 45 en su bolsa
