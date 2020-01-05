import os
os.chdir("\youtube-gravitar_pythonuebungen\4-PI_grafisch_darstellen\")
with open("pi_as_hell.txt", "r") as f:
    pi = f.read()
print(pi[0:10])
print(pi[-10:])