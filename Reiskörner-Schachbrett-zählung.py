summe = 0
for feld in range(64):
    reikorn = 2**feld
    print("Feld {}. = {} Reiskörner und damit insgesamt {} Reiskörner" \
        .format(feld+1,reiskorn,summe))