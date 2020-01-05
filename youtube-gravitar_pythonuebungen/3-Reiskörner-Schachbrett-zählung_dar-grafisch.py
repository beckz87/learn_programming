import matplotlib.pyplot as plt  # matplotlib.pyplot geladen und als "plt" aufrufbar
summe = 0
feldListe = []

for feld in range(64):
    reiskorn = 2**feld  # Aus doppelt * wird hoch
    feldListe.append(reiskorn)
    summe += reiskorn  # Durch "+=" werden der bestehenden Summme weitere Körner hinzugefügt
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damit insgesamt"
          f"{summe:>30,} Reiskörner")

gewicht = summe * 0.02 / 1000 / 1000
print()
print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten"
      f" Reiskörner {gewicht:,.0f} Tonnen")

plt.title("Anzahl von Reiskörner auf jeweiligen Feldern")
plt.xlabel("Anzahl der Schachfelder")
plt.ylabel("Anzahl der Reiskörner [in Trillionen]")
plt.grid(True)  # Hilfgitter ein-/ausblenden

plt.yscale('log')  # Achsenausrichtung an X oder Y logharithmisch ausrichten
# Syntax: plt.axis([xmin, xmax, ymin, ymax]) - eigene Skalierung festlegen
#plt.axis([0, 63, 0, 10**18])

plt.plot(feldListe, color="#1abc9c")
plt.show()
