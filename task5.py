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

class Bee():
    instances = []
    def __init__(self, name, identifier):
        self.__class__.instances.append(self)
        self.name = name
        self.identifier = identifier

    def __str__(self):
        return str(self.identifier) +' '+ str(self.name)

    def get_hive(self):
        for instance in self.instances:
            return str(self.identifier) +' '+ str(self.name)



foo = Bee(2, "as")
foo2 = Bee(8, "xyz")
print(str(foo))
print(str(foo2))
