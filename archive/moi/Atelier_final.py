# -*- coding: utf-8 -*-

###initialisation des grilles et autres variables de jeu
grille_debut_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", "●", "●", "●", "○"],
                       ["B", "●", "●", "●", "●", "●", "○", "○"],
                       ["C", "●", "●", "●", "●", "○", "○", "○"],
                       ["D", "●", "●", "●", " ", "○", "○", "○"],
                       ["E", "●", "●", "●", "○", "○", "○", "○"],
                       ["F", "●", "●", "○", "○", "○", "○", "○"],
                       ["G", "●", "○", "○", "○", "○", "○", "○"]]

grille_milieu_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", "●", "●", "●", "○"],
                       ["B", "●", "●", "●", "●", "●", "○", " "],
                       ["C", "●", "●", "●", "●", " ", " ", "○"],
                       ["D", "●", "●", " ", " ", "○", "○", "○"],
                       ["E", "●", " ", "●", "○", "○", "○", "○"],
                       ["F", "●", "●", "○", "○", "○", "○", "○"],
                       ["G", " ", "○", "○", "○", "○", "○", "○"]]

grille_fin_partie = [[" ", "1", "2", "3", "4", "5", "6", "7"],
                       ["A", "●", "●", "●", " ", "●", " ", " "],
                       ["B", "●", " ", " ", "●", " ", " ", " "],
                       ["C", "●", " ", " ", " ", " ", " ", " "],
                       ["D", " ", " ", " ", "●", " ", " ", " "],
                       ["E", " ", " ", " ", " ", " ", " ", "○"],
                       ["F", " ", " ", " ", "●", " ", "○", "○"],
                       ["G", " ", " ", " ", "○", "○", "○", "○"]]

tour = 1

#### REPRESENTATION GRAPHIQUE
def afficher_grille(grille) :
    resultat = ""
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            resultat += " " + grille[i][j] + " |"
        resultat += "\n"
    resultat +="    Joueur 1 = ●,   Joueur 2 = ○" + "\n"
    print(resultat)
    print(f"Pion du Joueur 1 restant : {nb_pion(grille)[0]} \nPion du Joueur 2 restant : {nb_pion(grille)[1]}")


### Fonction principale
def mare():
    rep = str(input("Quelle grille voulez vous ? \n(Pour celle du début tapez A, pour celle du milieu tapez B et pour celle de fin tapez C)\n").upper())
    valide = False
    while not valide:
        if rep == "A":
            grille_courante = grille_debut_partie
            valide = True
        elif rep == "B":
            grille_courante = grille_milieu_partie
            valide = True
        elif rep == "C":
            grille_courante = grille_fin_partie
            valide = True
        else:
            print("Veuillez saisir A, B ou C pour choisir la grille")
    afficher_grille(grille_courante)
    print(f"C'est le tour du Joueur {tour_joueur(tour)}")
    co1 = saisir_coordonnees(input("Veuillez saisir une coordonnée : "))
    co2 =  saisir_coordonnees(input("Veuillez saisir la coordonnée d'arrivé : "))
    co1 = saisir_deplacement(co1, co2, grille_courante)
    while est_possible_enchainement(co1, grille_courante) and rep != "n" and not est_fini_partie(nb_pion(grille_courante)[0], nb_pion(grille_courante)[1]):
        afficher_grille(grille_courante)
        rep = str(input("Voulez vous faire un enchainement ? \ny/n (oui tapez y, non tapez n.) : ").lower())
        if rep == "y":
            co2 = saisir_coordonnees(input("Veuillez saisir les coordonnées de votre enchainement :\n"))
            co1 = saisir_deplacement(co1, co2, grille_courante)
    afficher_grille(grille_courante)

def tour_joueur(tour):
    #Permet de savoir le tour est à quel joueur
    if tour%2 == 0:
        return 1
    elif tour%2 != 0:
        return 2

def conversion(co):
    #Permet de convertir les coordonnées utilisateur en indice
    new_co = []
    if str(co[0]) in 'ABCDEFG':
        new_co = (ord(str(co[0]))-ord("A")+1, int(co[1]))
        co = new_co
    return co

def nb_pion(grille):
    pion_j1 = 0
    pion_j2 = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == "●": #Compte le nombre de pion du joueur 1
                pion_j1+=1
            elif grille[i][j] == "○": #Compte le nombre de pion du joueur 2
                pion_j2+=1
    return pion_j1, pion_j2

### Saisis
def saisir_coordonnees(co):
    #Permet de saisir une coordonnée, l'utilisateur saisi la coordonnée tant qu'elle n'est pas valide
    valide = False
    while not valide:
        if est_au_bon_format(co) and est_dans_grille(co):
            valide = True
        else:
            co = input("Veuillez saisir des coordonnées valide (respectant la grille, respectant les règles) : ")
    return ord(co[0])-ord("A")+1, int(co[1])

def saisir_deplacement(co1, co2, grille):
    #Permet de saisir un déplacement, l'utilisateur saisi le déplacement tant qu'il n'est pas valide
    valide = False
    co3 = []
    while not valide:
        if not est_au_bon_joueur(co1, grille):
            co1 = input("Veuillez saisir des coordonnées avec un pion vous appartenant (si c'est un enchainement veuillez donner la co du pion à sauter): ")
        if co1 == co2:
            print("Veuillez saisir des coordonnées différentes")
            co1 = input("Veuillez resaisir les coordonnées de départ : ")
            co2 = input("Veuillez resaisir les coordonnées d'arrivées : ")
        elif est_possible_deplacement_simple(co1, co2, grille):
            co = deplacement_simple(co1, co2, grille)
            co = [conversion(co[0]), conversion(co[1])]
            grille[co[1][0]][co[1][1]] = grille[co[0][0]][co[0][1]]
            grille[co[0][0]][co[0][1]] = " "
            valide = True
        elif est_possible_deplacement_saut(co1, co2, grille):
            co3 = deplacement_saut(co1, co2, grille)
            grille[co3[0]][co3[1]] = grille[co1[0]][co1[1]]
            grille[co1[0]][co1[1]] = " "
            valide = True
        else: 
            co2 = input("Veuillez saisir des coordonnées valide (suivant le modèle des règles) : ")
    return co3

### Fonction de déplacement
def deplacement_simple(co1, co2, grille):
    #Permet d'effectuer les déplacements simple
    valide = False
    co3 = [0, 0]
    while not valide:
        if not est_libre(co1, grille) and est_libre(co2, grille):
            valide = True
        elif est_libre(co1, grille) and est_libre(co2, grille):
            print("Coordonnée de départ invalide veuillez vérifier que la case de départ contient un pion")
            co1 = saisir_coordonnees(input("Veuillez resaisir les coordonnées de départ : "))
            co2 = saisir_coordonnees(input("Veuillez resaisir les coordonnées d'arrivée : "))
        elif not est_libre(co1, grille) and not est_libre(co2, grille):
            co3 = deplacement_saut(co1, co2, grille)
            saisir_deplacement(co1, co3, grille)
            valide = True
        else:
            print("Coordonnée de départ et d'arrivé invalide veuillez vérifier que la case de départ contient un pion et la case d'arrivé est libre")
            co1 = saisir_coordonnees(input("Veuillez resaisir les coordonnées de départ : "))
            co2 = saisir_coordonnees(input("Veuillez resaisir les coordonnées d'arrivée : "))
    return co1, co2

def deplacement_saut(co1, co2, grille):
    #Permet d'effectuer les déplacements saut avec prises
    co3 = est_possible_deplacement_saut(co1, co2, grille)[1]
    co2 = conversion(co2)
    if est_possible_deplacement_saut(co1, co2, grille)[0]:
        print(co3)
        grille[co2[0]][co2[1]] = " "
    return co3

def respect_distance(co1, co2):
    #Permet de vérifier si la distance d'un déplacement est possible
    co1 = conversion(co1)
    co2 = conversion(co2)
    delta_ligne = co1[0]-co2[0]
    delta_colonne = co1[1]-co2[1]
    if delta_ligne == 0 and delta_colonne == 1:
        return True, "Droite"
    elif delta_ligne == 0 and delta_colonne == -1:
        return True, "Gauche"
    elif delta_ligne == 1 and delta_colonne == 0:
        return True, "Bas"
    elif delta_ligne == -1 and delta_colonne == 0:
        return True, "Haut"
    return False

### Test des inputs
def est_au_bon_format(co):
    #Vérifie si les coordonnées sont au bon format ou non
    if len(co) != 2:
        return False
    elif (ord(co[0]) < ord("A") or ord(co[0]) > ord("Z")) or (ord(co[1]) < ord("0") or ord(co[1]) > ord("9")): #Test si la coordonnée est valide (premiere partie contenue entre A et G seconde partie contenu entre 1 et 7)
        return False                                                                                                                                                                               
    return True

def est_dans_grille(co):
    #Vérifie si les coordonnées sont dans la grille ou non
    if len(co) != 2:
        return False
    co = conversion(co)
    if (ord(str(co[0])) < ord("1") or ord(str(co[0])) > ord("7")) or (int(co[1]) < 1 or int(co[1]) > 7): #Test si la coordonnée est valide (premiere partie contenue entre A et G seconde partie contenu entre 1 et 7)                                                                                                                                        
        return False
    return True

def est_possible_deplacement_simple(co1, co2, grille):
    #Vérifie si le déplacement est possible
    if est_libre(co2, grille) and respect_distance(co1, co2):
        return True
    return False

def est_possible_deplacement_saut(co1, co2, grille):
    #Vérifie si le déplacement saut avec prise est possible
    co3 = list(co2)
    co1 = conversion(co1)
    co2 = conversion(co2)
    if not est_libre(co2, grille) and respect_distance(co1, co2) and not est_au_bon_joueur(co2, grille):
        if respect_distance(co1, co2)[1] == "Haut":
            co3[0] = co3[0] + 1
            co3[1] = co3[1]
            return True, co3
        elif respect_distance(co1, co2)[1] == "Bas":
            co3[0] = co3[0] - 1
            co3[1] = co3[1]
            return True, co3
        elif respect_distance(co1, co2)[1] == "Gauche":
            co3[0] = co3[0]
            co3[1] = co3[1] + 1
            return True, co3
        elif respect_distance(co1, co2)[1] == "Droite":
            co3[0] = co3[0]
            co3[1] = co3[1] - 1
            return True, co3
    return False, co1

def est_possible_enchainement(co, grille):
    if co == []:
        return False
    if est_dans_grille((co[0]+2, co[1])):
        if not est_au_bon_joueur((co[0]+1, co[1]), grille) and est_libre((co[0]+2, co[1]), grille):
            return True
    if est_dans_grille((co[0]-2, co[1])):
        if not est_au_bon_joueur((co[0]-1, co[1]), grille) and est_libre((co[0]+2, co[1]), grille):
            return True
    if est_dans_grille((co[0], co[1]+2)):
        if not est_au_bon_joueur((co[0], co[1]+1), grille) and est_libre((co[0]+2, co[1]), grille):
            return True 
    if est_dans_grille((co[0], co[1]-2)):
        if not est_au_bon_joueur((co[0], co[1]-1), grille) and est_libre((co[0]+2, co[1]), grille):
                return True
    return False

def est_libre(co, grille):
    #Vérifie si la case actuelle est libre ou non
    if str(co[0]) in 'ABCDEFG':
        new_co = (ord(str(co[0]))-ord("A")+1, int(co[1]))
        co = new_co
    if est_dans_grille(co):
        if grille[co[0]][co[1]] == "●" or  grille[co[0]][co[1]] == "○":
            return False
    return True

def est_au_bon_joueur(co, grille):
    #Vérifie si la case contient un pion qui est au bon joueur
    J1 = "●"
    J2 = "○"
    co = conversion(co)
    if grille[co[0]][co[1]] == J1 and tour_joueur(tour) == 1:
        return True
    elif grille[co[0]][co[1]] == J2 and tour_joueur(tour) == 2:
        return True
    return False

def est_fini_partie(x, o):
    if x < 6:
        print("Le joueur 2 a gagné !")
        return True
    elif o < 6:
        print("Le joueur 1 a gagné !")
        return True
    return False

### Fonction de test
def test_est_au_bon_format():
    assert est_au_bon_format("A0") == True, "Test classique 1"
    assert est_au_bon_format("Z9") == True, "Test classique 2"
    assert est_au_bon_format("A22") == False, "Test erreur message trop long"
    print('OK est_au_bon_format')

def test_est_dans_grille():
    assert est_dans_grille("A1") == True, "Test classique 1"
    assert est_dans_grille("G7") == True, "Test classique 2"
    assert est_dans_grille("H7") == False, "Test classique 3"
    assert est_dans_grille("A22") == False, "Test erreur message trop long"
    print('OK est_dans_grille')

def test_est_possible_deplacement_simple():
    assert est_possible_deplacement_simple((5, 4), (4, 4), grille_debut_partie) == True, "Test classique 1"
    assert est_possible_deplacement_simple((4, 2), (4, 3), grille_milieu_partie) == True, "Test classique 2"
    assert est_possible_deplacement_simple((6, 4), (6, 3), grille_fin_partie) == True, "Test classique 3"
    print('OK est_possible_deplacement_simple')

def test_est_possible_deplacement_saut():
    assert est_possible_deplacement_saut((5, 3), (6, 3), grille_debut_partie)[0] == False, "Test classique 1"
    assert est_possible_deplacement_saut((5, 4), (5, 3), grille_milieu_partie)[0] == True, "Test classique 2"
    assert est_possible_deplacement_saut((7, 4), (6, 4), grille_fin_partie)[0] == True, "Test classique 3"
    print('OK est_possible_deplacement_saut')

def test_est_possible_enchainement():
    #Nécessite la modification de la variable ligne 31 pour effectuer des bons tests (réglé pour l'instant au joueur 2)
    assert est_possible_enchainement((5, 4), grille_debut_partie) == False, "Test classique 1"
    assert est_possible_enchainement((7, 2), grille_milieu_partie) == True, "Test classique 2"
    assert est_possible_enchainement((7, 4), grille_fin_partie) == True, "Test classique 3"
    print('OK est_possible_enchainement')

def test_est_libre():
    assert est_libre((4, 4), grille_debut_partie) == True, "Test classique 1"
    assert est_libre((1, 1), grille_milieu_partie) == False, "Test classique 2"
    assert est_libre((2, 3), grille_fin_partie) == True, "Test classique 3"
    print('OK est_libre')

def test_est_au_bon_joueur():
    #Nécessite la modification de la variable ligne 31 pour effectuer des bons tests (réglé pour l'instant au joueur 2)
    assert est_au_bon_joueur((7, 7), grille_debut_partie) == True, "Test classique 1"
    assert est_au_bon_joueur((1, 1), grille_milieu_partie) == False, "Test classique 2"
    assert est_au_bon_joueur((2, 3), grille_fin_partie) == False, "Test case vide"
    print('OK est_au_bon_joueur')

def test_est_fini_partie():
    assert est_fini_partie(6, 5) == True, "Test classique 1"
    assert est_fini_partie(5, 6) == True, "Test classique 2"
    assert est_fini_partie(6, 6) == False, "Test case vide"
    print('OK est_fini_partie')

# Appel des fonctions de tests
def test():
    test_est_au_bon_format()
    test_est_dans_grille()
    test_est_possible_deplacement_simple()
    test_est_possible_deplacement_saut()
    test_est_possible_enchainement()
    test_est_libre()
    test_est_au_bon_joueur()
    test_est_fini_partie()
    print("Les test sont tous OK")

# Appel de la fonction de démarrage
test()
mare()