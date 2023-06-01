import random


def turn(player, name):
    while True:
        rabbit = player.count("królik")
        sheep = player.count("owca")
        pig = player.count("świnia")
        cow = player.count("krowa")
        horse = player.count("koń")
        small_dog = player.count("mały pies")
        big_dog = player.count("duży pies")
        print(f"{name}, posiadasz następujące zwierzęta: {rabbit}x królik, "
              f"{sheep}x owca, {pig}x świnia, {cow}x krowa, {horse}x koń oraz "
              f"{small_dog}x mały pies i {big_dog}x duży pies.")

        choice = input(f"{name}, rzucasz kośćmi (K), czy wymieniasz zwierzęta "
                       f"(W)? ")

        if choice == "K" or choice == "k":
            result_1 = random.choice(dice_1)
            result_2 = random.choice(dice_2)
            print(F"Twój wynik to: {result_1} i {result_2}")

            if result_1 == "wilk":
                if "duży pies" in player:
                    player.remove("duży pies")
                    print("Duży pies ratuje Twoje zwierzęta przed wilkiem. "
                          "Stan Twojego stada się nie zmienia, ale tracisz "
                          "dużego psa.")
                else:
                    print("Niestety, wilk atakuje prawie wszystkie zwierzęta :("
                          " Zostają Ci tylko króliki.")
                    rescued_rabbits = player.count('królik')
                    rescued_horses = player.count('koń')
                    player = []
                    for _ in range(0, rescued_rabbits):
                        player.append("królik")
                    for _ in range(0, rescued_horses):
                        player.append("koń")

            if result_2 == "lis" and result_1 != "wilk":
                if "mały pies" in player:
                    player.remove("mały pies")
                    print("Mały pies ratuje Twoje króliki przed lisem. Stan "
                          "Twojego stada się nie zmienia, ale tracisz małego "
                          "psa.")
                else:
                    print("Niestety, lis atakuje prawie wszystkie króliki :( "
                          "Zostaje Ci tylko jeden królik.")
                    for _ in range(0, player.count("królik")-1):
                        player.remove("królik")

            if result_2 != "lis" and result_1 != "wilk":
                animals_list = player.copy()
                animals_list.append(result_1)
                animals_list.append(result_2)
                if result_1 == result_2:
                    number = animals_list.count(result_1) // 2
                    print(f"Otrzymałeś {number}x {result_1}.")
                    for i in range(0, number):
                        player.append(result_1)

                else:
                    animal_1 = animals_list.count(result_1) // 2
                    if animal_1 == 0:
                        print(f"Niestety, nie otrzymujesz 1x {result_1}.")
                    else:
                        print(f"Otrzymujesz {animal_1}x {result_1}.")
                        for _ in range(0, animal_1):
                            player.append(result_1)

                    animal_2 = animals_list.count(result_2) // 2
                    if animal_2 == 0:
                        print(f"Niestety, nie otrzymujesz 1x {result_2}.")
                    else:
                        print(f"Otrzymujesz {animal_2}x {result_2}.")
                        for _ in range(0, animal_2):
                            player.append(result_2)

            rabbit = player.count("królik")
            sheep = player.count("owca")
            pig = player.count("świnia")
            cow = player.count("krowa")
            horse = player.count("koń")
            small_dog = player.count("mały pies")
            big_dog = player.count("duży pies")

            if rabbit >= 1 and sheep >= 1 and pig >= 1 and cow >= 1 and \
                    horse >= 1:
                print("Brawo, wygrałeś! Posiadasz po co najmniej jednym "
                      "przedstawicielu zwierząt z każdego gatunku.")
                print(f"Łącznie posiadasz: {rabbit}x królik, {sheep}x owca, "
                      f"{pig}x świnia, {cow}x krowa, {horse}x koń oraz "
                      f"{small_dog}x mały pies i {big_dog}x duży pies.")

            else:
                print(f"{name}, posiadasz następujące zwierzęta: "
                      f"{rabbit}x królik, "
                    f"{sheep}x owca, {pig}x świnia, {cow}x krowa, {horse}x koń "
                      f"oraz "
                    f"{small_dog}x mały pies i {big_dog}x duży pies.")

            print()
            break

        elif choice == "W" or choice == "w":
            print()
            print("Możesz wykonać jedną z poniższych wymian: ")
            print("A) Wymienić 6 królików na 1 owcę.")
            print("B) Wymienić 2 owce na 1 świnię.")
            print("C) Wymienić 3 świnie na 1 krowę.")
            print("D) Wymienić 2 krowy na 1 konia.")
            print("E) Wymienić 1 owcę na 1 małego psa. Mały pies chroni przed "
                  "lisem. ")
            print("F) Wymienić 1 krowę na 1 dużego psa. Duży pies chroni przed "
                  "wilkiem.")

            exchange = input(f"{name}, które zwierzęta chcesz wymienić (Wpisz "
                             f"A, B, C, D, E lub F)? ")

            if exchange == "A" or exchange == "a":
                exchanged_rabbits = player.count("królik") // 6
                if exchanged_rabbits == 0:
                    print("Masz za mało królików na wymianę!")

                elif exchanged_rabbits > 0:
                    print(f"Wymieniłeś {6*exchanged_rabbits}x królik na "
                          f"{exchanged_rabbits}x owca.")
                    for _ in range(0, 6*exchanged_rabbits):
                        player.remove("królik")
                    for _ in range(0, exchanged_rabbits):
                        player.append("owca")
                    rabbit = player.count("królik")
                    sheep = player.count("owca")
                    print(f"{name}, posiadasz teraz następujące zwierzęta: "
                          f"{rabbit}x królik, {sheep}x owca, {pig}x świnia, "
                          f"{cow}x krowa, {horse}x koń. ")
                    print()
                    break

            elif exchange == "B" or exchange == "b":
                exchanged_sheep = player.count("owca") // 2
                if exchanged_sheep == 0:
                    print("Masz za mało owiec na wymianę!")

                elif exchanged_sheep > 0:
                    print(f"Wymieniłeś {2*exchanged_sheep}x owca na "
                          f"{exchanged_sheep}x świnia.")
                    for _ in range(0, 2*exchanged_sheep):
                        player.remove("owca")
                    for _ in range(0, exchanged_sheep):
                        player.append("świnia")
                    sheep = player.count("owca")
                    pig = player.count("świnia")
                    print(f"{name}, posiadasz teraz następujące zwierzęta: "
                          f"{rabbit}x królik, {sheep}x owca, {pig}x świnia, "
                          f"{cow}x krowa, {horse}x koń. ")
                    print()
                    break

            elif exchange == "C" or exchange == "c":
                exchanged_pigs = player.count("świnia") // 3
                if exchanged_pigs == 0:
                    print("Masz za mało świń na wymianę!")

                elif exchanged_pigs > 0:
                    print(f"Wymieniłeś {3*exchanged_pigs}x świnia na "
                          f"{exchanged_pigs}x krowa.")
                    for _ in range(0, 3*exchanged_pigs):
                        player.remove("świnia")
                    for _ in range(0, exchanged_pigs):
                        player.append("krowa")
                    pig = player.count("świnia")
                    cow = player.count("krowa")
                    print(f"{name}, posiadasz teraz następujące zwierzęta: "
                          f"{rabbit}x królik, {sheep}x owca, {pig}x świnia, "
                          f"{cow}x krowa, {horse}x koń. ")
                    print()
                    break

            elif exchange == "D" or exchange == "d":
                exchanged_cows = player.count("krowa") // 2
                if exchanged_cows == 0:
                    print("Masz za mało krów na wymianę!")

                elif exchanged_cows > 0:
                    print(f"Wymieniłeś {3*exchanged_cows}x krowa na "
                          f"{exchanged_cows}x koń.")
                    for _ in range(0, 3*exchanged_cows):
                        player.remove("krowa")
                    for _ in range(0, exchanged_cows):
                        player.append("koń")
                    cow = player.count("krowa")
                    horse = player.count("koń")
                    print(f"{name}, posiadasz teraz następujące zwierzęta: "
                          f"{rabbit}x królik, {sheep}x owca, {pig}x świnia, "
                          f"{cow}x krowa, {horse}x koń. ")
                    print()
                    break

            elif exchange == "E" or exchange == "e":
                if player.count("owca") >= 1:
                    player.remove("owca")
                    player.append("mały pies")
                    print("Wymieniłeś owcę na małego psa.")
                    print()
                    break

                else:
                    print("Nie masz owcy, więc nie możesz dokonać wymiany!")

            elif exchange == "F" or exchange == "f":
                if player.count("krowa") >= 1:
                    player.remove("krowa")
                    player.append("duży pies")
                    print("Wymieniłeś krowę na dużego psa.")
                    print()
                    break

                else:
                    print("Nie masz krowy, więc nie możesz dokonać wymiany!")

            else:
                print("Wybierz literę z przedziału A-D!")

        else:
            print("Wybierz K lub W!")


dice_1 = ['królik', 'królik', 'królik', 'królik', 'królik', 'królik', 'owca',
          'owca', 'owca', 'świnia', 'krowa', 'wilk']
dice_2 = ['królik', 'królik', 'królik', 'królik', 'królik', 'królik', 'owca',
          'owca', 'świnia', 'świnia', 'koń', 'lis']

while True:
    start = input("Rozpocznij grę (S) lub wyświetl zasady gry (Z): ")
    if start == "S" or start == "s":
        name_1 = input("Imię pierwszego gracza: ")
        name_2 = input("Imię drugiego gracza: ")
        break

    elif start == "Z" or start == "z":
        with open('zasady_gry.txt', 'r', encoding="utf-8") as file:
            content = file.read()
        print(content)
        print()

    else:
        print("Wybierz S lub Z!")

player_1 = ['królik']
player_2 = ['królik']

while True:
    turn(player_1, name_1)
    turn(player_2, name_2)

