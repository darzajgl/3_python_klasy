# Zadeklaruj klasę `Bee`
# * Klasa przyjmuje dwa argumenty `name` i `identifier` podczas
#   instancjonowania
# * Klasa jest konwertowalna do typu `string`, to znaczy wywołanie
#   `str(bee)` zwraca wartość typu `string` o określonym formacie
#   i zawartości
# * Format wyżej wymienionej wartości wygląda następująco: `{identifier} {name}`,
#   dla `bee = Bee(name='Bumble', identifier=1)` wywołanie `str(bee)` zwróci `"1 Bumble"`
# * Obiekty klasy `Bee` mają metodę `get_hive()` zwracającą zbiór tekstowych
#   reprezentacji wszyskich utworzonych instancji klasy Bee
