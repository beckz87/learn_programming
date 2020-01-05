from random import shuffle

liste = "amazing gorgeous blazing stunning stunning greatest best fantastic phenomenal \
    delightful ambitious outstanding incredible spectacular super cool magical \
        revolutionary beautiful jaw-dropping".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ",end='')
        print()
    print(liste.pop() +" SPAM, " + liste.pop()+" SPAM")
    print()
