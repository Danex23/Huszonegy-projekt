import random

ktualis_szam_player = 0
aktualis_szam_ai = 0
player = 0
ai = 0
jatek = "y"
dontes = ""
dontes_ai = 0
k = 0
while jatek == "y":
    (input("Jó napot. Szeretne játszani?(y/n) "))
    if jatek == "y":
        for i in range(1,3):
            aktualis_szam_player = random.randint(2, 14)
            if aktualis_szam_player == 11:
                print (f"A számod bubi.")
                player = player + 10
            elif aktualis_szam_player == 12:
                print (f"A számod dáma.")
                player = player + 10
            elif aktualis_szam_player == 13:
                print (f"A számod király.")
                player = player + 10
            elif aktualis_szam_player == 14:
                print (f"A számod ász.")
                player = player + 10
            else:
                print (f"A számod {aktualis_szam_player}")
                player = player + aktualis_szam_player

            aktualis_szam_ai = random.randint(2, 14)
            if aktualis_szam_ai == 11:
                ai = ai + 10
            elif aktualis_szam_ai == 12:
                ai = ai + 10
            elif aktualis_szam_ai == 13:
                ai = ai + 10
            elif aktualis_szam_ai == 14:
                ai = ai + 10
            else:
                ai = ai + aktualis_szam_ai
            if k == 0:
                print(f"A gép kártyája: {aktualis_szam_ai}")
                k += 1

        print(f"A jelenlegi kártyáid összege: {player}")
        print(f"A gép jelenlegi kártyáinak összege: ???")
        dontes = input("Mit szeretne, ütni vagy tartani? (ü/t) ")
        while True:
            if dontes == "ü" and player < 21:
                aktualis_szam_player = random.randint(2, 14)
                if aktualis_szam_player == 11:
                    print (f"A számod bubi.")
                    player = player + 10
                elif aktualis_szam_player == 12:
                    print (f"A számod dáma.")
                    player = player + 10
                elif aktualis_szam_player == 13:
                    print (f"A számod király.")
                    player = player + 10
                elif aktualis_szam_player == 14:
                    print (f"A számod ász.")
                    player = player + 10
                else:
                    print (f"A számod {aktualis_szam_player}")
                    player = player + aktualis_szam_player
                print(f"A számaid összege: {player}")
            else:
                break
            dontes = input("Mit szeretne, ütni vagy tartani? (ü/t) ")

        dontes_ai = random.randint(1,2)
        if ai < 16 and ai != 17:
            while dontes_ai == 1 and dontes_ai < 21:
                aktualis_szam_ai = random.randint(2, 14)
                if aktualis_szam_ai == 11:
                    ai = ai + 10
                elif aktualis_szam_ai == 12:
                    ai = ai + 10
                elif aktualis_szam_ai == 13:
                    ai = ai + 10
                elif aktualis_szam_ai == 14:
                    ai = ai + 10
                else:
                 ai = ai + aktualis_szam_ai
                dontes_ai = random.randint(1,2)
        elif ai == 16:
            aktualis_szam_ai = random.randint(2, 14)
            if aktualis_szam_ai == 11:
                ai = ai + 10
            elif aktualis_szam_ai == 12:
                ai = ai + 10
            elif aktualis_szam_ai == 13:
                ai = ai + 10
            elif aktualis_szam_ai == 14:
                if ai + aktualis_szam_ai > 21:
                    ai = ai + 1
                else:
                    ai = ai + 10
            else:
                ai = ai + aktualis_szam_ai
        print(f"Kártyáid végleges összege: {player}.")
        print(f"A gép kártyáinak végleges összege: {ai}.")
        if player > 21:
            print("Vesztettél.")
        elif ai > 21:
            print("Nyertél.")
        elif player > ai:
            print("Nyertél.")
        else:
            print("Vesztettél.")