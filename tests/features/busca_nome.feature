Feature: Busca restaurante pelo nome
  Como cliente do LocalEats,
  desejo que o sistema encontre o restaurante,
  quando eu busco pelo nome dele.
 
  Scenario: Encontrar restaurante pelo nome
    Given que eu busco por "Restaurante Sabor 0"
    When o sistema busca pela lista de restaurantes
    Then o resultado deve ser somente o "Restaurante Sabor 0"
