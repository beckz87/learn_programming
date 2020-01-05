import os  # MS-Struktur laden
os.chdir("youtube-gravitar_pythonuebungen\\4-PI_grafisch_darstellen")
import turtle as tu

lines = 100_000

with open("Teil_04_1_million_digits_of_pi.txt", "r") as f:
  pi = f.read()

tu.mode('logo')
tu.tracer(True)
tu.screensize(6000, 6000, 'black')
tu.colormode(255)


for n in range(lines):
  color = int(n/(lines/255))
  tu.pencolor(255, 255-color, color)
  zahl = int(pi[n])
  rotation = zahl * 36
  tu.setheading(rotation)
  tu.forward(50)
  if n % 10_000 == 0:
    tu.update()

tu.getcanvas().postscript(file='PI_Picture.ps')
tu.done()