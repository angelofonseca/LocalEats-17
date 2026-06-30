from search import RestaurantSearch

RESTAURANTES = ["Restaurante Sabor 0", "Restaurante Sabor 1", "Restaurante Sabor 2"]


def test_regressao_busca_com_espacos_extras_encontra_restaurante():
    """
    Defeito: busca por nome não encontrava o restaurante quando o termo
    buscado continha espaços extras no inicio ou no fim (ex: " Restaurante Sabor 0 ").
    Correcao: RestaurantSearch.search agora aplica strip() no termo buscado
    antes de comparar com a lista de restaurantes.
    """
    busca = RestaurantSearch(RESTAURANTES)
    assert busca.search(" Restaurante Sabor 0 ") == ["Restaurante Sabor 0"]
    assert busca.search("Restaurante Sabor 1\n") == ["Restaurante Sabor 1"]
