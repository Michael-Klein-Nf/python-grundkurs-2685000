#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division)
# eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis
# der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional: 
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen,
# bis der Benutzer das Programm beendet.
def add_numbers(number1: float, number2: float) -> float:
    """Addiert zwei Zahlen."""
    return number1 + number2

def subtract_numbers(number1: float, number2: float) -> float:
    """Subtrahiert die zweite Zahl von der ersten."""
    return number1 - number2

def multiply_numbers(number1: float, number2: float) -> float:
    """Multipliziert zwei Zahlen."""
    return number1 * number2

def divide_numbers(number1: float, number2: float) -> float:
    """Dividiert die erste Zahl durch die zweite.
    
    Gibt eine Fehlermeldung aus, wenn die Division durch Null erfolgt.
    """
    if number2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        return None
    return number1 / number2


def main():
    """Hauptfunktion, die den Benutzer durch die Berechnungen führt."""
    try:
        number1 = float(input("Geben Sie die erste Zahl ein: "))
        number2 = float(input("Geben Sie die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        return

    print("Wählen Sie die gewünschte Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    operation = input("Geben Sie die Nummer der Operation ein (1-4): ")

    if operation == '1':
        result = add_numbers(number1, number2)
        print(f"Ergebnis: {result}")
    elif operation == '2':
        result = subtract_numbers(number1, number2)
        print(f"Ergebnis: {result}")
    elif operation == '3':
        result = multiply_numbers(number1, number2)
        print(f"Ergebnis: {result}")
    elif operation == '4':
        result = divide_numbers(number1, number2)
        if result is not None:
            print(f"Ergebnis: {result}")
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und 4.")

if __name__ == "__main__":
    main()
