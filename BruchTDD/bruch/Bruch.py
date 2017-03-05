"""
Created on 23.10.2016

@author: mmuehlehner
"""

class Bruch:

    def __init__(self, zaehler = 0, nenner = 1):
        """
        Konstruktor für den Bruch

        :raise ZeroDivisionError: Der Nenner darf nicht 0 sein
        :raise TypeError: Nenner und Zaehler muessen von Typ int sein (bzw. Bruch beim Zaehler)
        :param zaehler: Der Zaehler des Bruchs, oder ein Bruch
        :param nenner:  Der Nenner des Bruchs, wird dieser nicht angegeben, wird der default Wert 1 angenommen
        """
        if isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        elif nenner == 0:
            raise ZeroDivisionError("Division durch 0 ist nicht erlaubt! -> Nenner darf nicht 0 sein!")
        elif type(zaehler) is not int:
            raise TypeError("Inkompatibler Datentyp bei Zaehler: "+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError("Inkompatibler Datentyp bei Nenner: "+type(nenner).__name__)
        else:
            self.zaehler = zaehler
            self.nenner = nenner

    def __float__(self):
        """
        Gibt den Bruch als Gleitkommazahl zurueck

        :return: float: Bruch als Gleitkommazahl
        """
        return self.zaehler / float(self.nenner)

    def __int__(self):
        """
        Gibt den Bruch als int (ganze Zahl) zurueck

        :return: int: Bruch als ganze Zahl
        """
        return int(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Gibt den Bruch als komplexe Zahl zurueck

        :return: complex: Bruch als komplexe Zahl
        """
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Gibt den invertierten Bruch zurueck

        :return: Bruch: invertierter Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        Gibt den Bruch als formatierten String zurueck

        :return: String: Bruch als String
        """
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1
        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __pow__(self, power):
        """
        Gibt den mit 'power' exponierten Bruch zurueck

        :raise TypeError: Falscher Datentyp
        :param power: Der Exponent
        :return: Bruch: exponierter Bruch
        """
        if type(power) is int:
            return Bruch(self.zaehler ** power,self.nenner ** power)
        else:
            raise TypeError("Datentyp muss int sein!")

    def __makeBruch(value):
        """
        Dient dazu um einen unbekannten Parameter in einen Bruch umzuwandeln

        :raise TypeError: Falscher Datentyp
        :param: value: ein unbekannter Parameter welcher Falls möglich in einen Bruch umgewandelt wird
        :return: Bruch: neu erzeugter Bruch
        """
        if isinstance(value, Bruch):
            return value
        elif type(value) is int:
            return Bruch(value, 1)
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")

    def __abs__(self):
        """
        Gibt den Absolutbetrag des Bruches zurueck, also einen positiven Bruch

        :return: Bruch: der Absolutbetrag eines Bruchs (positiver Bruch)
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        Negiert den Bruch

        :return: Bruch: negierter Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __eq__(self, other):
        """
        Ueberprueft die Gleichheit des Bruches mit einem anderen Wert

        :param other: anderer unbekannter Wert
        :return: boolean: gleich oder nicht gleich
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner

    def __ne__(self, other):
        """
        Ueberprueft die Ungleichheit des Bruches mit einem anderen Wert

        :param other: anderer unbekannter Wert
        :return: boolean: ungleich oder nicht ungleich
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner != other.zaehler * self.nenner

    def __ge__(self, other):
        """
        Ueberprueft ob der Bruch groesser oder gleich ist als ein anderer Wert

        :param other: anderer unbekannter Wert
        :return: boolean: groesser gleich oder kleiner
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    def __le__(self, other):
        """
        Ueberprueft ob der Bruch kleiner oder gleich ist als ein anderer Wert

        :param other: anderer unbekannter Wert
        :return: boolean: kleiner gleich oder groesser
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    def __lt__(self, other):
        """
        Ueberprueft ob der Bruch kleiner ist als ein anderer Wert

        :param other: anderer unbekannter Wert
        :return: boolean: kleiner oder nicht kleiner
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    def __gt__(self, other):
        """
        Ueberprueft ob der Bruch groesser ist als ein anderer Wert

        :param other: anderer unbekannter Wert
        :return: boolean: groesser oder nicht groesser
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    def __add__(self, other):
        """
        Addiert zwei Brueche
        Bruch + other

        :raise TypeError: Falscher Datentyp
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Summe der zwei Brueche
        """
        if isinstance(other, Bruch):
            zaehler2 = other.zaehler
            nenner2 = other.nenner
        elif type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        return Bruch(self.zaehler * nenner2 + zaehler2 * self.nenner, self.nenner * nenner2)

    def __radd__(self, other):
        """
        Addiert ebenfalls zwei Brueche
        other + Bruch
        Gleich wie __add__ aufgrund des Kommutativgesetzes

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Summe der zwei Brueche
        """
        return self.__add__(other)

    def __iadd__(self, other):
        """
        Addiert ebenfalls zwei Brueche
        Bruch += other

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Summe der zwei Brueche
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Subtrahiert zwei Brueche
        Bruch - other

        :raise TypeError: Falscher Datentyp
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Differenz der zwei Brueche
        """
        if isinstance(other, Bruch):
            zaehler2 = other.zaehler
            nenner2 = other.nenner
        elif type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        return Bruch(self.zaehler * nenner2 - zaehler2 * self.nenner, self.nenner * nenner2)

    def __rsub__(self, other):
        """
        Subtrahiert zwei Brueche
        other - Bruch

        :raise TypeError: Falscher Datentyp
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Differenz der zwei Brueche
        """
        if type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        return Bruch(zaehler2 * self.nenner - self.zaehler * nenner2, self.nenner * nenner2)

    def __isub__(self, other):
        """
        Subtrahiert zwei Brueche
        Bruch-=other

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Differenz der zwei Brueche
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """
        Multipliziert zwei Brueche
        Bruch * other

        :raise TypeError: Falscher Datentyp
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Produkt der zwei Brueche
        """
        if isinstance(other, Bruch):
            zaehler2 = other.zaehler
            nenner2 = other.nenner
        elif type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        return Bruch(zaehler2 * self.zaehler, nenner2 * self.nenner)

    def __rmul__(self, other):
        """
        Multipliziert zwei Brueche
        other * Bruch
        Gleich wie __mul__ aufgrund des Kommutativgesetzes

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Produkt der zwei Brueche
        """
        return self.__mul__(other)

    def __imul__(self, other):
        """
        Multipliziert zwei Brueche
        Bruch *= other

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Produkt der zwei Brueche
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Dividiert zwei Brueche
        Bruch / other

        :raise TypeError: Falscher Datentyp
        :raise ZeroDivisionError: Division durch 0 nicht erlaubt
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Quotient der zwei Brueche
        """
        if isinstance(other, Bruch):
            zaehler2 = other.zaehler
            nenner2 = other.nenner
        elif type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        if zaehler2 == 0:
            raise ZeroDivisionError("Division durch 0 nicht erlaubt!")
        return Bruch(self.zaehler * nenner2, zaehler2 * self.nenner)

    def __itruediv__(self, other):
        """
        Dividiert zwei Brueche
        Bruch /= other

        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Quotient der zwei Brueche
        """
        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        Dividiert zwei Brueche
        other / Bruch

        :raise TypeError: Falscher Datentyp
        :param other: anderer Wert welcher, falls noch nicht, zu einem Bruch gemacht wird (wenn moeglich)
        :return: Bruch: Quotient der zwei Brueche
        """
        if type(other) is int:
            zaehler2 = other
            nenner2 = 1
        else:
            raise TypeError("Datentyp muss int oder Bruch sein!")
        return Bruch(zaehler2 * self.nenner, self.zaehler * nenner2)

    def __iter__(self):
        """
        Ermoeglicht das iterieren des Bruchs
        """
        return (self.zaehler, self.nenner).__iter__()
