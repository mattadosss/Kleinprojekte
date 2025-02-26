import random
from colorama import init
from termcolor import colored

words = [
    "Apfel", "Blume", "Boden", "Dachs", "Falke",
    "Fisch", "Fluss", "Glanz", "Grube", "Heide",
    "Hafen", "Herz", "Hirse", "Junge", "Kater",
    "Kranz", "Krone", "Kugel", "Lager", "Licht",
    "Mauer", "Mühle", "Nadel", "Rauch", "Regen",
    "Schaf", "Stein", "Stock", "Stuhl", "Tisch",
    "Traum", "Truhe", "Vater", "Waffe", "Weide",
    "Welle", "Wiese", "Winde", "Worte", "Zecke",
    "Zebra", "Zunge", "Zweig", "Zwing", "Eiche",
    "Birke", "Kamel", "Platz", "Stadt"
]

word = random.choice(words)
word = word.lower()
word = [*word]



print("Dies ist ein Wortrate Spiel")
print("🟩 steht für: dieser Buchstabe ist am richtigen Platz")
print("🟨 steht für: der Buchstabe ist im Wort enthalten aber am flaschen Platz")
print("🟥 steht für: der Buchstabe ist nicht im Wort enthalten")

init()

counter = 0
index = 0
tries = 0
output = ""
counter2 = 0
while tries <= 5 and counter2 != 5:
    intrput = input("Bitte gib ein 5 stelliges Wort ein:\n")
    intrput = [*intrput]
    tries += 1
    counter2 = 0
    if len(intrput) == 5:
        index = 0
        for i in intrput:
            a = intrput[index]
            b = word[index]
            tt = f" {a} "
            if a == b:
                output += colored(tt,"white","on_green")
                counter2 += 1
            elif i in word:
                output += colored(tt,"white","on_yellow")
            else:
                output += colored(tt,"white","on_red")
            index += 1
        print(output)
        index = 0
        output = ""
    else:
        print("Das eingegebene Wort ist nicht 5 Zeichen lang")


output = ""
for i in word:
    output += i
print(f'Das gesuchte Wort war {output}')
print(f'sie brauchten {tries} Versuche')