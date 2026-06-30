from pytest_bdd import scenarios, given, when, then, parsers
from search import RestaurantSearch

scenarios("features/busca_nome.feature")

RESTAURANTES = ["Restaurante Sabor 0", "Restaurante Sabor 1", "Restaurante Sabor 2"]


@given(
    parsers.parse('que eu busco por "{nome}"'),
    target_fixture="contexto",
)
def buscar_por_nome(nome):
    return {"busca": RestaurantSearch(RESTAURANTES), "nome_buscado": nome, "resultado": None}


@when("o sistema busca pela lista de restaurantes")
def executar_busca(contexto):
    contexto["resultado"] = contexto["busca"].search(contexto["nome_buscado"])


@then(parsers.parse('o resultado deve ser somente o "{nome}"'))
def verificar_resultado(contexto, nome):
    assert contexto["resultado"] == [nome]
