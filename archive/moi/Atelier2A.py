# -*- coding: utf-8 -*-

###initialisation des grilles et autres variables de jeu
grille_debut_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "O", "O", "O", "O", "O", "O", "X"],
                       ["B", "O", "O", "O", "O", "O", "X", "X"],
                       ["C", "O", "O", "O", "O", "X", "X", "X"],
                       ["D", "O", "O", "O", " ", "X", "X", "X"],
                       ["E", "O", "O", "O", "X", "X", "X", "X"],
                       ["F", "O", "O", "X", "X", "X", "X", "X"],
                       ["G", "O", "X", "X", "X", "X", "X", "X"]]

grille_milieu_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "O", "O", "O", "O", "O", "O", "X"],
                       ["B", "O", "O", "O", "O", "O", "X", " "],
                       ["C", "O", "O", "O", "O", " ", " ", "X"],
                       ["D", "O", "O", " ", " ", "X", "X", "X"],
                       ["E", "O", " ", "O", "X", "X", "X", "X"],
                       ["F", "O", "O", "X", "X", "X", "X", "X"],
                       ["G", " ", "X", "X", "X", "X", "X", "X"]]

grille_fin_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "O", "O", "O", " ", "O", " ", " "],
                       ["B", "O", " ", " ", "O", " ", " ", " "],
                       ["C", "O", " ", " ", " ", " ", " ", " "],
                       ["D", " ", " ", " ", "O", " ", " ", " "],
                       ["E", " ", " ", " ", " ", " ", " ", "X"],
                       ["F", " ", " ", " ", "O", " ", "X", "X"],
                       ["G", " ", " ", " ", "X", "X", "X", "X"]]

#### REPRESENTATION GRAPHIQUE
def afficher_grille(grille) :
    resultat = ""
    pion_o, pion_x= 0, 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            resultat += " " + grille[i][j] + " |"
            if grille[i][j] == "X": #Compte le nombre de pion du joueur 2
                pion_x+=1
            elif grille[i][j] == "O": #Compte le nombre de pion du joueur 1
                pion_o+=1
        resultat += "\n"
    resultat +="    Joueur 1 = O,   Joueur 2 = X" + "\n" + "Pion du Joueur 1 restant : " + str(pion_o) + "\nPion du Joueur 2 restant : " + str(pion_x) #Affichage donnée complémentaire
    print(resultat)


### Fonction principale
def mare(grille):
    afficher_grille(grille)
    print(saisir_coordonnees(input("Veuillez saisir une coordonnée : ")))


### Saisi des coordonnées
def saisir_coordonnees(message):
    valide = False
    while not valide:
        if est_au_bon_format(message) and est_dans_grille(message):
            valide = True
        else:
            message = input("Veuillez saisir des coordonnées valide (comprise entre A-G et 1-7) : ")
    return ord(message[0])-ord("A")+1, int(message[1])

### Test du message
def est_au_bon_format(message):
    if (ord(message[0]) >= ord("A") and ord(message[0]) <= ord("Z")) and (ord(message[1]) >= ord("0") and ord(message[1]) <= ord("9")) and not len(message) > 2: #Test si la coordonnée est valide (premiere partie cotenue entre A et G 
        return True                                                                                                                                                                                 #seconde partie contenu entre 1 et 7)
    return False

def est_dans_grille(message):
    if (ord(message[0]) >= ord("A") and ord(message[0]) <= ord("G")) and (ord(message[1]) >= ord("1") and ord(message[1]) <= ord("7")) and not len(message) > 2: #Test si la coordonnée est valide (premiere partie cotenue entre A et G                                                                                                                                           
        return True                                                                                                                                                                                 #seconde partie contenu entre 1 et 7)
    return False

### Fonction de test
def test_est_au_bon_format() : 
    assert est_au_bon_format("A1"), "erreur cas classique"
    assert est_au_bon_format("Z0"), "erreur cas classique, lettre sup"
    assert not est_au_bon_format("12"), "erreur lettre en 0 attendu"
    assert not est_au_bon_format("BB"), "erreur chiffre en 1 attendu"
    assert not est_au_bon_format("&("), "erreur symbole"
    print('OK est_au_bon_format')

def test_est_dans_grille():
    grille_vide = [[0]*8]*8 #façon pythonesque de creer une liste de liste vide
    assert est_dans_grille("A",5,),"erreur cas dans la grille"
    assert not est_dans_grille("a",5,),"erreur hors ligne inferieure"
    assert not est_dans_grille("I",5,),"erreur hors ligne superieure"
    assert not est_dans_grille("A",-1,),"erreur hors colonne inferieure"
    assert not est_dans_grille("A",8,),"erreur hors colonne superieure"
    print('OK est_dans_grille')


# Appel de la fonction de démarrage
mare(grille_debut_partie)
#mare(grille_milieu_partie)
#mare(grille_fin_partie)

# Appel des fonctions de tests
def test():
    test_est_au_bon_format()
    test_est_dans_grille()

test()