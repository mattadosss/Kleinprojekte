import csv


pairs = []
with open('vocis.csv', newline='') as csvfile:

    spamreader = csv.DictReader(csvfile)
    print(spamreader)
    for row in spamreader:
        pairs.append(row)
        #print(row)
userinput = 0
counter = 0
laguageinp = 0
language1 = ""
language2 = ""

while not (laguageinp == "deutsch" or laguageinp == "englisch"):
    laguageinp = input('welche Sprach möchtest du lernen')
    if laguageinp == "deutsch":
        language1 = laguageinp
        language2 = "englisch"
    else:
        language1 = laguageinp
        language2 = "deutsch"

while True:
    for i in pairs:
        print(i[f"{language2}"])
        counter = 0
        while userinput != i[f"{language1}"]:
            if counter <= 3:
                print(i[f'{language1}'])
                userinput = input('gib die übersetzung\n')
                counter += 1
                print(counter)
            else:
                print("hier wäre die lösung: " + i[f'{language1}'])
                break


