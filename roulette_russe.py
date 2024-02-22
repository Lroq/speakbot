import tkinter as tk
import random

# Fonction pour vérifier le nombre entré par l'utilisateur
def check_number(event=None):  # event=None pour permettre l'appel depuis le bouton ou la touche Entrée
    try:
        user_number = int(entry.get())
        if 1 <= user_number <= 10:
            if user_number == random_number:
                result_label.config(text="Correct! Closing window...")
                window.after(1500, window.destroy)
            else:
                result_label.config(text="Incorrect, try again.")
        else:
            result_label.config(text="Enter a number between 1 and 10.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Création de la fenêtre
window = tk.Tk()
window.title("Guess the Number")

# Mettre la fenêtre en mode plein écran
window.attributes('-fullscreen', True)

# Désactiver la fermeture de la fenêtre via la croix
window.protocol("WM_DELETE_WINDOW", lambda: None)

# Générer un nombre aléatoire entre 1 et 10
random_number = random.randint(1, 10)

# Ajout des widgets
entry = tk.Entry(window)
entry.pack()
entry.bind("<Return>", check_number)  # Lier la touche Entrée à la fonction check_number

result_label = tk.Label(window, text="")
result_label.pack()

# Lancement de la boucle d'événements
window.mainloop()