# Définition des fonctions pour les sous-menus
def afficher_info_linux():
    print("Informations sur Linux")

def afficher_info_cpu():
    print("Informations sur le processeur")

def afficher_info_memoire():
    print("Informations sur la mémoire")

def afficher_info_disque():
    print("Informations sur le disque")

def afficher_info_reseau():
    print("Informations sur le réseau")

# Définition du menu principal
menu_principal = {
    "1": {"label": "Afficher des informations sur Linux", "action": afficher_info_linux},
    "2": {"label": "Afficher des informations sur le processeur", "action": afficher_info_cpu},
    "3": {"label": "Afficher des informations sur la mémoire", "action": afficher_info_memoire},
    "4": {"label": "Afficher des informations sur le disque", "action": afficher_info_disque},
    "5": {"label": "Afficher des informations sur le réseau", "action": afficher_info_reseau},
}

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    print("Menu principal :")
    for key, value in menu_principal.items():
        print(f"{key} - {value['label']}")
    choix = input("Choisissez une option : ")
    if choix in menu_principal:
        menu_principal[choix]["action"]()
    else:
        print("Option invalide")

# Programme principal
if __name__ == "__main__":
    while True:
        afficher_menu_principal()
