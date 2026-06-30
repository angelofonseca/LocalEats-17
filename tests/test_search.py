from search import RestaurantSearch

RESTAURANTES = ["Restaurante Sabor 0", "Restaurante Sabor 1", "Restaurante Sabor 2"]


def test_buscar_restaurante_pelo_nome():
    busca = RestaurantSearch(RESTAURANTES)
    assert busca.search("Restaurante Sabor 0") == ["Restaurante Sabor 0"]


def test_buscar_restaurante_inexistente_retorna_lista_vazia():
    busca = RestaurantSearch(RESTAURANTES)
    assert busca.search("Restaurante Sabor 99") == []
