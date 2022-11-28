# Zadeklaruj klasę `Colony` i `Ant`
# * Klasa `Colony` przyjmuje argument `name` podczas
#   instancjonowania
# * Obiekty klasy `Colony` posiadają atrybut `name`
#   co do wartości odpowiadający argumentowi przekazanemu podczas
#   instancjonowania
# * Obiekty klasy `Colony` posiadają metodę `spawn_ant` przyjmującą
#   argument `name` i zwracającą obiekt klasy `Ant`. Wartość atrybutu
#   `name` utworzonego obiektu odpowiada wartości przekazanego argumentu
# * Obiekty klasy 'Colony' posiadają atrybut 'ants' będący zbiorem
#   wszystkich obiektów typu `Ant` utworzonych przez wywołania metody
#   `spawn_ant`
# * Obiektu klasy `Ant` posiadają atrybuty `name` i `colony` odpowiadające
#   kolejno argumentowi `name` przekazanemu do `spawn_ant` oraz obiektowi
#   colony na którym ta metoda została wywołana
# * Kod testujący tworzy obiektu `Ant` tylko poprzez wywołania metody `spawn_ant`
#
#  Przykład:
#  colony = Colony("MyColony")
#  worker = colony.spawn_ant("worker")
#  worker.name == "worker"
#  worker.colony == colony
#  colony.ants == {worker}
#  worker2 = colony.spawn_ant("worker2")
#  colony.ants == {worker, worker2}

class Colony():
    def __init__(self, name):
        self.name = name


class Ant():
    pass

