import turtle as tu
import os  # MS-Struktur laden
# Wechsle ins Unterverzeichniss
os.chdir("youtube-gravitar_pythonuebungen\\4-PI_grafisch_darstellen")

with open("pi_as_hell.txt", "r") as f:
    pi = f.read()

# print(pi[0:10])  # zeigt die ersten 10 zeichen
# print(pi[-10:])  # zeigt die letzten 10 zeichen
# print(len(pi))  # zählt alle zeichen

# TURTLE CONTROLING
lines = 100_000
tu.mode('logo')  # Turtle ausrichten sodass 0° oben ist
tu.tracer(False)  # False=speeed True=slow
tu.screensize(3000, 3000, 'black')
tu.colormode(255)

for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255, 255-color, color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(5)
    if n % 10_000 == 0: #Läd 10_000 Lines nach und nach und nicht alles aufeinmal
        tu.update()

tu.getcanvas().postscript(file='PI_Picture.ps')
tu.done()
