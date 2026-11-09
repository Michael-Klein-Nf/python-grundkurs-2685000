#!/usr/bin/env python3

# Einführung das Abfangen von Exceptions
print('Code snippet ohne try-except-Block')
user_input = input("Bitte geben Sie eine ganze Zahl ein: ")
number = int(user_input)  # Versuch, die Eingabe in einen Integer zu konvertieren
print(f'Die eingegebene Zahl ist: {number}')  # Ausgabe der eingegebenen Zahl

print('Code snippet mit try-except-Block')
try:
    user_input = input("Bitte geben Sie eine ganze Zahl ein: ")
    number = int(user_input)  # Versuch, die Eingabe in einen Integer zu konvertieren
    print(f'Die eingegebene Zahl ist: {number}')  # Ausgabe der eingegebenen Zahl
except ValueError:
    print("Ungültige Eingabe! Bitte geben Sie eine gültige ganze Zahl ein.")

# Einführung in das Auslösen von Exceptions

def überprüfe_positiven_wert(wert: int) -> None:
    """Überprüft, ob der übergebene Wert positiv ist. Löst eine Exception aus, wenn nicht."""
    if wert <= 0:
        raise ValueError(f"Der Wert {wert} ist nicht positiv! Der Wert muss größer als 0 sein.")
    print(f"Der Wert {wert} ist positiv.")

# Beispielverwendung
try:
    zahl = int(input("Bitte geben Sie eine positive Zahl ein: "))
    überprüfe_positiven_wert(zahl)
except ValueError as e:
    print(f"Fehler: {e}")

# Aufgabe: Ändern Sie den Code aus dem vorherigen Beispiel mit dem Bankkonto so
# ab, dass eine Exception ausgelöst wird, wenn der einzahlende Betrag negativ 
# ist, oder das Bankkonto negative Beträge enthält.
# Hier ist die vorherige Beispielimplementierung mit print-Statements:
#!/usr/bin/env python3

from typing import List, Tuple

class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos."""

    def __init__(self, inhaber: str, kontonummer: str, start_kontostand: float = 0.0):
        """Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand."""
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = start_kontostand
        self._transaktionen: List[Tuple[str, float]] = []

    def einzahlen(self, betrag: float) -> None:
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        if betrag > 0:
            self._kontostand += betrag
            self._transaktionen.append(("Einzahlung", betrag))
            print(f"{betrag} EUR wurden eingezahlt.")
        else:
            raise ValueError("Einzahlung fehlgeschlagen: Betrag muss positiv sein.")

    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand um den abgehobenen Betrag, wenn genügend Guthaben vorhanden ist."""
        if betrag > 0:
            if self._kontostand >= betrag:
                self._kontostand -= betrag
                self._transaktionen.append(("Abhebung", betrag))
                print(f"{betrag} EUR wurden abgehoben.")
            else:
                raise ValueError("Abhebung fehlgeschlagen: Unzureichendes Guthaben.")
        else:
            raise ValueError("Abhebung fehlgeschlagen: Betrag muss positiv sein.")

    def get_kontostand(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self._kontostand

    def get_transaktionen(self) -> List[Tuple[str, float]]:
        """Gibt eine Liste aller Transaktionen zurück."""
        return self._transaktionen

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Kontos zurück."""
        return (
            f"Konto von {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {self._kontostand:.2f} EUR"
        )

# Beispielverwendung
konto = BankAccount("Max Mustermann", "DE1234567890", 100.0)

print(konto)

try:
    konto.einzahlen(50)
except ValueError as e:
    print(f"Fehler bei Einzahlung: {e}")
try:
    konto.abheben(30)
except ValueError as e:
    print(f"Fehler bei Abhebung: {e}")
try:
    konto.abheben(150)
except ValueError as e:
    print(f"Fehler bei Abhebung: {e}")

print(f"Aktueller Kontostand: {konto.get_kontostand()} EUR")

# Transaktionen anzeigen
print("Transaktionsverlauf:")
for transaktion in konto.get_transaktionen():
    print(f"{transaktion[0]}: {transaktion[1]:.2f} EUR")


