class RestaurantSearch:
    """Permite buscar restaurantes do LocalEats pelo nome."""

    def __init__(self, restaurants: list[str] | None = None) -> None:
        self._restaurants: list[str] = list(restaurants) if restaurants else []

    def search(self, name: str) -> list[str]:
        """Retorna os restaurantes cujo nome e exatamente igual ao buscado."""
        return [restaurant for restaurant in self._restaurants if restaurant == name]
