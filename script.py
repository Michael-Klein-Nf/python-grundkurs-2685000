#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.
class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos."""
    def __init__(self, inhaber, kontonummer, anfangs_kontostand=0):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.__kontostand = anfangs_kontostand
        self.__transaktionen = []

    def einzahlen(self, betrag):
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        if betrag > 0:
            self.__kontostand += betrag
            self.__transaktionen.append(f"Einzahlung: {betrag}")
        else:
            print("Betrag muss positiv sein.")

    def abheben(self, betrag):
        """Verringert den Kontostand um den abgehobenen Betrag."""
        if betrag > 0:
            if self.__kontostand >= betrag:
                self.__kontostand -= betrag
                self.__transaktionen.append(f"Abhebung: {betrag}")
            else:
                print("Nicht genügend Guthaben.")
        else:
            print("Betrag muss positiv sein.")

    def get_kontostand(self):
        """Gibt den aktuellen Kontostand zurück."""
        return self.__kontostand

    def get_transaktionen(self):
        """Gibt die Liste der Transaktionen zurück."""
        return self.__transaktionen

    def __str__(self):
        return f"Bankkonto von {self.inhaber}, Kontonummer: {self.kontonummer}, Kontostand: {self.__kontostand}"

konto = BankAccount("Max Mustermann", "1234567890", 1000)
konto.einzahlen(500)
konto.abheben(200)
print(konto)
