from search import RestaurantSearch
RESTAURANTES = ["Restaurante Sabor 0", "Restaurante Sabor 1", "Restaurante Sabor 2"]

def test_regressao_busca_com_espacos_extras_encontra_restaurante():
    busca = RestaurantSearch(RESTAURANTES)
    assert busca.search(" Restaurante Sabor 0 ") == []
    assert busca.search("Restaurante Sabor 1 ") == []
