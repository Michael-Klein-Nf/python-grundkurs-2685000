#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.
z1 = input("Geben Sie die erste Zahl ein: ")
z2 = input("Geben Sie die zweite Zahl ein: ")
operation = input("Wählen Sie die Operation (+, -, *, /): ")

result = 0
if operation == "+":
    result = float(z1) + float(z2)
elif operation == "-":
    result = float(z1) - float(z2)
elif operation == "*":
    result = float(z1) * float(z2)
elif operation == "/":
    if float(z2) == 0:
        result = "Fehler: Division durch Null ist nicht erlaubt."
    else:
        result = float(z1) / float(z2)

print("Das Ergebnis der Berechnung ist:", result)
