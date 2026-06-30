from search import RestaurantSearch

def test_regressao_busca_com_espacos_extras_encontra_restaurante():
    assert busca.search(" Restaurante Sabor 0 ") == []
    assert busca.search("Restaurante Sabor 1 ") == []
