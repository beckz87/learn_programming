import turtle as tu
import os  # MS-Struktur laden
# Wechsle ins Unterverzeichniss
os.chdir("youtube-gravitar_pythonuebungen\\4-PI_grafisch_darstellen")
with open("pi_as_hell.txt", "r") as f:
    pi = f.read()

# print(pi[0:10])  # zeigt die ersten 10 zeichen
# print(pi[-10:])  # zeigt die letzten 10 zeichen
# print(len(pi))  # zählt alle zeichen

lines = 100
for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(50)

tu.done()
