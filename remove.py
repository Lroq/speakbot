import os
from time import sleep
from colorama import Fore, Back, Style
import random

def remove():
    print("Creating file...")
    f = open("test.txt", "w+")
    f.close()
    print("Creation du fichier...")
    for i in range(1, 100):
        sleep(random.uniform(0.1, 0.9))  # ajuste le temps entre 0 et 1 seconde pour chaque itération
        print(f"Creation en cours... {i}%", end="\r", flush=True)

    print("File created." + " [OK]")
    sleep(1)
    print("Voulez-vous supprimer le fichier ?")
    print("1) Oui")
    print("2) Non")
    sleep(1)
    choix = input(">>> ")

    if choix == "1":
        print("Suppression du fichier...")
        for i in range(1, 100):
            sleep(random.uniform(0.1, 0.9))  # ajuste le temps entre 0 et 1 seconde pour chaque itération
            print(f"Suppression en cours... {i}%", end="\r", flush=True)
        os.remove("test.txt")
        print("Removing file..." + " [OK]")
    else:
        print("Suppression annulée.")

remove()
