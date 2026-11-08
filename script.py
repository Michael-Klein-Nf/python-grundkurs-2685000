#!/usr/bin/env python3
import argparse
# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.
parser = argparse.ArgumentParser(description="Analysiere den Text und liefere Details darüber.")
parser.add_argument("text", help="Eingabe Text")
parser.add_argument("--details", action="store_true", help="Zeige nähere Details an")
args = parser.parse_args()

text = args.text
characters = len(text)
words = len(text.split())

print(f"Zeichen: {characters}")
if args.details:
    print(f"Wörter: {words}")

    vowels = "aeiou"
    sum_vowels = sum(1 for char in text if char.lower() in vowels)
    print(f"Vokale: {sum_vowels}")

    consonants = "bcdfghjklmnpqrstvwxyz"
    sum_consonants = sum(1 for char in text if char.lower() in consonants)
    print(f"Konsonanten: {sum_consonants}")