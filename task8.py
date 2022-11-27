# Zaimplementuj klasę Polynominal reprezentującą wielomian.
# https://en.wikipedia.org/wiki/Polynomial
#
# * Instancjonowanie odbywa się poprzez podanie kolejnych
#   współczynników wielomianu np.
#   Polynominal()  ->  0
#   Polynominal(1, 2, 3)  -> 1 + 2x + 3x^2
#   Polynominal(0, 0, 5)  -> 5x^2
#   Polynominal(1, -1, 1, -1)  -> 1 - x + x^2 - x^3
#
# * Instancje można rzutować na typ `string`, format podany w przykładach
#   str(Polynominal()) == ''
#   str(Polynominal(1, 2, 3)) == "1 + 2x + 2x^2"
#   str(Polynominal(0, 0, 5)) == "5x^2"
#   str(Polynominal(1, 1, 1, 1)) == "1 + x + x^2 + x^3"
#   str(Polynominal(0, 2, 0)) == "2x"
#   str(Polynominal(1, -1, 1, -1)) == "1 - x + x^2 - x^3"
#   str(Polynominal(-1)) == "-1"
#
# * Instancje mają metodę `get_degree` zwracającą stopień wielomianu
#   Polynominal().get_degree() == 0
#   Polynominal(1, 2, 3).get_degree() == 2
#
# * Instancje można porównywać ze sobą operatorem `==`
#   Polynominal() == Polynominal(0)  -> True
#   Polynominal(1, 2, 3) == Polynominal(1, 2, 3)  -> True
#   Polynominal(1, 1, 1) == Polynominal(2, 2, 2, 2)  -> False
#
# * Instancje można do siebie dodawać, w wyniku dodawania powstaje
#   nowy obiekt klasy Polynominal
#   Polynominal(1, 1, 1) + Polynominal(2, 2, 2) == Polynominal(3, 3, 3)
#
# * Klasa `Polynominal` posiada metodę `from_iterable` umożliwiającą
#   instancjonowanie obiektów z wykorzystaniem iterowalnych kolekcji
#   współczynników
#   Polynominal.from_iterable([1, 2, 3]) == Polynominal(1, 2, 3)
#   Polynominal.from_iterable((1, 1, 5)) == Polynominal(1, 1, 5)
#
# * Współczynniki są liczbami całkowitymi
