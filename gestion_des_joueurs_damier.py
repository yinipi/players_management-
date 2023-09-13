import sys

import json
import os

# declaration de la liste des matchs
all_matchs = []

# recuperation du chemin
CUR_DIR = os.path.dirname(__file__)

# jointure du chemin
liste_chemin = os.path.join(CUR_DIR, "liste_joueurs.json")
match_chemin = os.path.join(CUR_DIR, "liste matchs.json")

# # ouverture du fichier de sauvergarde pour les matchs
if os.path.exists(match_chemin):
    with open(match_chemin, "r") as file:
        all_matchs = json.load(file)
else:
    # declaration de la liste des courses
    all_matchs = []

# ouverture du fichier de sauvergarde pour les joueurs
if os.path.exists(liste_chemin):
    with open(liste_chemin, "r") as file:
        players_maks = json.load(file)
else:
    # declaration de la liste des courses
    players_maks = []


# focnton pour tester les donnees entrer par l'utilisateur
def test_Entier(nombre):
    try:
        nombre = int(nombre)
    except ValueError:
        print("Erreur : le nombre entré n'est pas un entier.")


# fonction pour l'affichage du menu principale
def menu_principale():
    print("*** MENU PRINCIPAL *** \n"
          "1. Gestion des joueurs\n"
          "2. Gestion des matchs \n"
          "3. Sauvegarder liste \n"
          "4. Classement final \n"
          "5. Quitter le programme"
          )


# fonction affichage du sous menu gestion des joueurs
def menu_gestion_joueurs():
    print("-->> GESTION DES JOUEURS <<-- \n"
          "1. Ajouter un joueur\n"
          "2. Modifier un joueur\n"
          "3. Option de suppression \n"
          "4. Lister les joueurs\n"
          "5. Retour au menu principale"
          )


# fonction menu gestion des matchs
def menu_gestion_matchs():
    print("-->> GESTION DES MATCHS <<-- \n"
          "1. Creer un  match\n"
          "2. Enregistrer les matchs \n"
          "3. Afficher les matchs \n"
          "4. Option de suppression \n"
          "5. Sauvegarder les resultats des matchs \n"
          "6. Retour au menu principale"
          )

# fonction  ajout des joueurs dans la liste
def add_players():

        nom = input("nom du joueur : ").upper()
        prenom = input(" prenom du joueur : ").capitalize()
        age = input("age du joueur : ")
        point = int(input(" points du joueur"))
        id_player = len(players_maks) + 1

        # ajout des element du joueurs dans son dictionnaire
        player= {"nom": nom, "prenom": prenom, "age": age, "id_player": id_player, "point": point}

        # ajout du joueur dans la liste des joueurs
        players_maks.append(player)
        print(f"{nom} {prenom} a ete ajouter avec success dans la liste ")


# fonction por la modification des joueurs
def upgrade_player():
    if len(players_maks) == 0:
        print("Il n'y a aucun joueur dans la liste.")
    id_upgrade = int(input("enter l'identifaint du joueur a modifier : "))
    for player in players_maks:
        if joueur["id_player"] == id_upgrade:
            while True:
                print("** menu modification ** \n"
                      "1. nom ?\n"
                      "2. prenom ? \n"
                      "3. age ? \n"
                      "4. point ? \n"
                      "5. retour  ")
                choice_upgrade = int(input("que voulez vous modifier sur le joueur ?"))
                if choice_upgrade == 1:
                    new_name = input("nouveau nom du joueur :  ")
                    joueur["name"] = new_name
                elif choice_upgrade == 2:
                    new_surname = input(" noyuveau prenom du joueur : ")
                    joueur["surname"] = new_surname
                elif choice_upgrade == 3:
                    new_age = int(input("nouveau nom du joueur :  "))
                    joueur["age"] = new_age
                elif choice_upgrade == 4:
                    new_point = int(input("nouveau nom du joueur :  "))
                    joueur["point"] = new_point
                elif choice_upgrade == 5:
                    break
        else:
            print("entrer un identifaint valide  ")

        print(f"joueur{id_upgrade} modifie avec succes")


# fonction pour la suppression
def delete_player():
    print("1. supprimer un joueurs \n"
          "2. vider la liste \n"
          "3.retour")
    delete_choice = int(input("Votre choix : "))

    # supprimer un joueur en particulier
    while True:
        if delete_choice == 1:
            if len(players_maks) == 0:
                print("Il n'y a aucun joueur dans la liste.")
            id_delete_player = int(input("Identifiant du joueur a supprimer  : "))
            for player in players_maks:
                if joueur["id_player"] == id_delete_player:
                    players_maks.remove(player)
                    print(f"Le joueur{id_delete_player} a été supprimé avec succès.")

            # vider la liste des joueurs
        elif delete_choice == 2:
            players_maks.clear()
            print("la liste a ete vider avec sucess ")

            # retour
        elif delete_choice == 3:
            break


# fonction pour lister les joueurs de la liste
def list_player():
    if len(players_maks) == 0:
        print("Il n'y a aucun joueur dans la liste.")
    for player in players_maks:
        print(
            f"{player['name']} {player['surname']} ({player['age']} ans, {player['point']} points) [id: {player['id_player']}]")


# programme principale
while True:
    menu_principale()
    choice_principal = int(input("Quel est votre choix entre 1-4 ? \n "))

    # gestion des joueurs
    if choice_principal == 1:
        while True:
            menu_gestion_joueurs()
            choice_player = int(input("Quel est votre choix dans le menu gestion ds joueur entre 1-6 ? \n "))

            # ajouter un joueur
            if choice_player == 1:
                add_players()

            # modifier un joueur
            elif choice_player == 2:
                upgrade_player()

            # option de suppression
            elif choice_player == 3:
                delete_player()

            # lister les joueurs
            elif choice_player == 4:
                list_player()

            # retour au menu principal
            elif choice_player == 5:
                break

    # gestion des matchs
    elif choice_principal == 2:
        while True:
            menu_gestion_matchs()
            choice_match = int(input("quel est votre choix : "))

            # recuperation des identifiants des joueurs et insertion dans une liste
            list_valeur_cle = []
            for dictionnaire in players_maks:
                for cle, valeur in dictionnaire.items():
                    if cle == "id_player":
                        list_valeur_cle.append(valeur)
            print(list_valeur_cle)

            # creation des matchs

            if choice_match == 1:
                if len(players_maks) == 0:
                    print("la liste des joueurs est  vide !!!")
                else:
                    id_player_1 = int(input("entrer l'identifiant du premier joueur du match: "))
                    id_player_2 = int(input(" entrer l'identifiant du second juouer du match : "))

                    if id_player_1 in list_valeur_cle:
                        if id_player_2 in list_valeur_cle:
                            if id_player_1 != id_player_2:
                                date_match = input("entrer  la date du match  : ")
                                id_match = len(all_matchs) + 1
                                # ajout des element du match dans son dictionnaire
                                match = {"id_player1": id_player_1, "id_player2": id_player_2, "date_match": date_match,
                                         "id_match": id_match}

                                # ajout du joueur dans la liste des match
                                all_matchs.append(match)
                                print(f"match {id_match} creer avec sucess ")
                                print(all_matchs)
                            else:
                                print("Entrer des identifiants differents pour creer un match ")
                        else:
                            print("identifiant du deuxieme joueur invalide")

                    else:
                        print("identifiant du premier  joueur invalide")

            # enregistrer les matchs creer dans un fichier json
            elif choice_match == 2:
                if len(all_matchs) == 0:
                    print("Aucun match enregistrer ")
                else:
                    print("voulez vous sauvegarder les matchs creer   ? ")
                    print(" 1. oui")
                    print(" 2. non")
                    save_match = int(input(" Quels est votre choix ? : "))

                    if save_match == 1:
                        # ecriture de la liste a l'interieur du fichier liste_joueurs.json
                        with open(match_chemin, "w") as file:
                            json.dump(all_matchs, file, indent=4)
                            print("sauvergarde des macths reussir reussir")
                    # retour au cas ou
                    elif save_match == 2:
                        break
                    elif save_match != 1 or save_match != 2:
                        break

            # affichage des matchs
            elif choice_match == 3:
                while True:
                    if len(all_matchs) == 0:
                        print("aucun match disponible")
                    else:
                        print("1. afficher un macth \n"
                              "2. afficher tout les matchs \n"
                              "3. retour ")
                        affiche_choice = int(input("Queles est votre choix ? : "))
                        if affiche_choice == 1:
                            display_match = int(input("enter l'identifiant du match a afficher : "))
                            for match in all_matchs:
                                if match['id_match'] == display_match:
                                    for joueur in players_maks:
                                        if joueur['id_player'] == match['id_player1']:
                                            name = joueur['name']
                                            surname = joueur['surname']
                                            for joueur in players_maks:
                                                if joueur['id_player'] == match['id_player2']:
                                                    name2 = joueur['name']
                                                    surname2 = joueur['surname']
                                                    print(
                                                        f"macth {match['id_match']} : {name} {surname} VS  {name2}  {surname2} le {match['date_match']}")

                                else:
                                    print("Aucun match n'a été trouvé avec cet identifiant. ")
                        # affiche tout les matchs creer
                        elif affiche_choice == 2:
                            for match in all_matchs:
                                for joueur in players_maks:
                                    if joueur['id_player'] == match['id_player1']:
                                        name = joueur['name']
                                        surname = joueur['surname']
                                        for joueur in players_maks:
                                            if joueur['id_player'] == match['id_player2']:
                                                name2 = joueur['name']
                                                surname2 = joueur['surname']
                                                print(
                                                    f"macth {match['id_match']} : {name} {surname} VS  {name2}  {surname2} le {match['date_match']}")

                        elif affiche_choice == 3:
                            break

            # option de suuppression
            elif choice_match == 4:
                print("1. supprimer un match \n"
                      "2. vider la liste \n"
                      "3.retour")
                del_match = int(input("Votre choix : "))

                # supprimer un match en particulier
                while True:
                    if del_match == 1:
                        if len(players_maks) == 0:
                            print("Il n'y a aucun match .")
                        del_identifiant = int(input("Identifiant du match  a supprimer  : "))
                        for match in all_matchs:
                            if match["id_match"] == del_identifiant:
                                all_matchs.remove(match)
                                print(f"Le match {del_identifiant} a été supprimé avec succès.")

                    # vider la liste des matchs
                    elif del_match == 2:
                        all_matchs.clear()
                        print("la liste  des matchs vider avec sucess ")

                        # retour
                    elif del_match == 3:
                        break

            # enregistrer les resultats avec les vainqueur de chaque match
            elif choice_match == 5:

                vainqueur = input("Identifiant du vainqueur : ")
                identifiant = int(input("Identifiant du match : "))
                for match in all_matchs:
                    if match["id_match"] == identifiant:
                        match["vainqueur"] = vainqueur
                        for joueur in players_maks:
                            if joueur["id_player"] == vainqueur:
                                joueur["point"] += 100
                            elif joueur["id_player"] != vainqueur:
                                joueur["point"] += 10
                        print("Résultat enregistré avec succès.")

                print("Aucun match trouvé avec cet identifiant.")

                # retour au menu principale
            elif choice_match == 6:
                break

    # sauvegarde sur la liste des joueurs dans un fichier json
    elif choice_principal == 3:
        print("voulez vous sauvegarder  ? ")
        print(" 1. oui")
        print(" 2. non")
        choice_save = int(input(" QUels est votre choix ? : "))

        if choice_save == 1:
            # ecriture de la liste a l'interieur du fichier liste_joueurs.json
            with open(liste_chemin, "w") as file:
                json.dump(players_maks, file, indent=4)
                print("sauvergarde reussir")
        # retour au cas ou
        elif choice_save == 2:
            break

    # classement des joueurs en fonction des points
    elif choice_principal == 4:

        if len(players_maks) == 0:
            print("la liste est vide , aucun joueur enregistrer ")
        else:
            player_classement = sorted(players_maks, key=lambda x: x["point"], reverse=True)
            for i, joueur in enumerate(player_classement):
                print("CLASSEMENT FINAL")
                print(f"{i + 1}. {joueur['name']} {joueur['surname']} ({joueur['age']} ans, {joueur['point']} points)")

    # quitter le programme
    elif choice_principal == 5:
        print("FIN DU PROGRAMME \n"
              "AU REVOIR !!!! "
              )
        sys.exit()
    
# class HomeMenu():
#     items = (
#         (1,'Match'),
#         (2,'Joeurs'),
#         (3,'Quitter')
#     )


