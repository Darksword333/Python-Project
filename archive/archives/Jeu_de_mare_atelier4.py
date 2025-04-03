import random

"""                                                     ATELIER 2 !!!!                                                              """
"""                    Attention les Fonction de test etc sont commentés en bas du fichier !!!!!!!!!!!!                             """
"""                                             ATELIER 3 En bas du fichier !!!                                                     """

#____________________________________________ Fonction de vérification ________________________________________________#

nom_bot = ["Albert","Allen","Bert","Bob","Cecil","Clarence","Elliot","Elmer","Ernie","Eugene","Fergus"
           ,"Ferris","Frank","Frasier","Fred","George","Graham","Harvey","Irwin","Larry","Lester",
           "Marvin","Neil","Niles","Oliver","Opie","Ryan","Toby","Ulric","Ulysses","Uri","Waldo",
           "Wally","Walt","Wesley","Yanni","Yogi","Yuri"]


"""Création des différentes grilles"""

Grille_debut = [['○', '○', '○', '○', '○', '○', '●'],
               ['○', '○', '○', '○', '○', '●', '●'],
               ['○', '○', '○', '○', '●', '●', '●'],
               ['○', '○', '○', '', '●', '●', '●'],
               ['○', '○', '○', '●', '●', '●', '●'],
               ['○', '○', '●', '●', '●', '●', '●'],
               ['○', '●', '●', '●', '●', '●', '●']]

Grille_millieu = [['○', '○', '○', '○', '○', '', '●'],
                 ['○', '○', '', '○', '', '', '●'],
                 ['○', '', '', '●', '', '', '●'],
                 ['○', '', '', '●', '●', '●', '●'],
                 ['○', '', '', '○', '', '●', '●'],
                 ['○', '', '', '●', '', '●', '●'],
                 ['○', '', '●', '●', '●', '●', '●']]

Grille_fin =  [['○', '○', '', '', '', '', '●'],
              ['', '', '', '●', '', '', ''],
              ['', '○', '', '○', '', '○', ''],
              ['○', '', '', '', '○', '●', '●'],
              ['○', '', '○', '●', '', '', ''],
              ['', '○', '', '', '●', '●', ''],
              ['', '', '', '', '', '●', '']]



def nombre_de_pions(grille, pions):

    """prend en entrée une grille et un des deux type de pions
    et renvoie les nombre qu'il y en a dans la grille"""

    compt = 0

    for ligne in range(len(grille)):

        for colonne in range(len(grille[ligne])):       #Parcours la grille afin de compter les pions
            if grille[ligne][colonne] == pions:
                compt += 1

    return compt


def afficher_grille(grille,joueur1,joueur2,joueur_en_cours):

    """Prend en entré une grille le nom des deux joueurs
    et le nom du joueur qui doit jouer et affiche a la grille"""

    print("   1   2   3   4   5   6   7")
    alph = ["A", "B", "C", "D", "E", "F", "G"]

    for ligne in range(len(grille)):

        compt_joueur_1 = 0
        compt_joueur_2 = 0
        compteur_espace = 0
        aff = []

        for colonne in range(len(grille[ligne])):

            if grille[ligne][colonne] == "○":
                compt_joueur_1 += 1
                aff.append(" |○|")
            
            if grille[ligne][colonne] == "●":          #compte le nombre de pions a chaque ligne afin de les representer
                compt_joueur_2 += 1
                aff.append(" |●|")

            if grille[ligne][colonne] == '':
                compteur_espace += 1
                aff.append(" | |")

        print(alph[ligne] +str(aff[0])+str(aff[1])+str(aff[2])+str(aff[3])+str(aff[4])+str(aff[5])+str(aff[6]))

    print(str(joueur1) ," : "+str(nombre_de_pions(grille, "○")), "○", "          "+str(joueur2)," : "+str(nombre_de_pions(grille, "●")), "●")
    print("Au tour de "+str(joueur_en_cours), "!\n")
    


def est_au_bon_format(coordonees):

    """Prend en entrés des coordonnées de type str et renvoie
     True si les coordonnées sont au bon format sinon False """

    nbr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if coordonees == "" or len(coordonees) != 2:
        return False

    elif coordonees[0] not in alph:
        return False

    elif coordonees[1] not in nbr:
        return False

    return True


def est_dans_grille(ligne, colonne, grille):

    coordonnees_possible = []
    nbr = ["1", "2", "3", "4", "5", "6", "7"]
    alph = []

    for nbr_ligne in range(len(grille)):
        alph.append(chr(65+nbr_ligne))

        for nbr_colonne in range(len(grille[0])):
            coordonnees_possible.append(str(alph[nbr_ligne-1]) + str(nbr[nbr_colonne-1]))

    if colonne not in nbr:
        return False

    if ligne not in alph:
        return False
    return True


def saisie_de_coordonnees(grille):
    coordonees = input(str("Rentrez les coordonées désiré "))  #Attention pour certain ide il faut cliquer en bas pour
                                                               # rentrer les valeurs de inputs
    print("\n")
    while est_au_bon_format(coordonees) == False:
        coordonees = input(str("Rentrez les coordonées désiré car les anciennes n'étais pas au bon format "))
    
    while est_dans_grille(coordonees[0], coordonees[1], grille) == False:
    
        coordonees = input(str("Rentrez les coordonées désiré car les anciennes n'appartenais pas a la grille "))
    return coordonees



#_______________________________________________________TEST___________________________________________________________#

def test_est_dans_grille(grille):
    assert est_dans_grille("A", "1",grille) == True
    assert est_dans_grille("", "", grille) == False
    assert est_dans_grille("1", "A", grille) == False
    assert est_dans_grille("A", "A", grille) == False
    assert est_dans_grille("a", "1", grille) == False
    assert est_dans_grille("", "1", grille) == False


def test_est_au_bon_format():
    assert est_au_bon_format("A1") == True
    assert est_au_bon_format("X2") == True
    assert est_au_bon_format("11") == False
    assert est_au_bon_format("AA") == False
    assert est_au_bon_format("") == False
    assert est_au_bon_format("B12") == False

test_est_dans_grille(Grille_debut)
test_est_au_bon_format()

"""                                                         ATELIER 3 ET 4                                                           """

def transfo_coord(coordonne):

    """Prend en entrées des coordonnées de type str et renvoie
    une lise de deux éléments"""

    new_coord = [0,0]

    for nombre_de_ligne_dans_grille in range(0,7):

        if coordonne[1] == str(nombre_de_ligne_dans_grille+1):
            new_coord[1] = nombre_de_ligne_dans_grille

        if coordonne[0] == chr(65+nombre_de_ligne_dans_grille):
            new_coord[0] = nombre_de_ligne_dans_grille

    return new_coord

def verif_case_depart(grille, coord_dep, pion_joueur):

    """Prend en entrée une grille , des coordonnées et le pion du joueur
    qui joue et vérifie que dans la case de départ il y a bien un pion a lui"""

    if grille[coord_dep[0]][coord_dep[1]] == pion_joueur:
        return True
    
    return False

def verif_case_arr(grille, coord_arr):

    """Prend en entrée une grille , des coordonnées et vérifie que
    la case d'arrivée est vide"""

    if grille[coord_arr[0]][coord_arr[1]] == "":
        return True
    
    return False

def verif_case_inter(grille, coord_dep, coord_arr, pion_joueur, pion_ennemi):

    """Prend en entrée une grille , des coordonnées de départ et d'arrivé,
    le pion du joueur qui joue et de son adversaire vérifie que lors d'un saut
    la intermediaire est un pion ennemi"""

    coord_inter = [(coord_dep[0]+coord_arr[0])//2,(coord_dep[1]+coord_arr[1])//2]
    
    if grille[coord_inter[0]][coord_inter[1]] == "" or grille[coord_inter[0]][coord_inter[1]] == pion_joueur: 
         return False
    
    return True

def dist_entre_case_saut(grille,coord_dep,coord_arr):
    if not est_dans_grille(coord_dep[0],coord_dep[1],grille) and est_dans_grille(coord_arr[0],coord_arr[1],grille):
        return False
 
    if coord_dep[0] == coord_arr[0] and coord_dep[1] == coord_arr[1]:
        return False
    
    if dist_entre_case_depl(grille,coord_dep,coord_arr) == True:
        return False
    
    elif not 2 >= (coord_dep[0] - coord_arr[0]) >= -2 and direction_entre_deux_cases(coord_dep,coord_arr) == True:
        return False
    
    elif not 2 >= (coord_dep[1] - coord_arr[1]) >= -2 and direction_entre_deux_cases(coord_dep,coord_arr) == True:
        return False
    
    return True
    

def dist_entre_case_depl(grille,coord_dep,coord_arr):
    if not est_dans_grille(coord_dep[0],coord_dep[1],grille) and est_dans_grille(coord_arr[0],coord_arr[1],grille):
        return False
    
    if coord_dep[0] == coord_arr[0] and coord_dep[1] == coord_arr[1]:
        return False
    
    elif not 1 >= (coord_dep[0] - coord_arr[0]) >= -1 and direction_entre_deux_cases(coord_dep,coord_arr) == True:
        return False
    
    elif not 1 >= (coord_dep[1] - coord_arr[1]) >= -1 and direction_entre_deux_cases(coord_dep,coord_arr) == True:
        return False
    
    return True


def direction_entre_deux_cases(coord_dep,coord_arr):

    """Prend en entrée des coordonnées de départ et d'arrivée 
    et vérifie que le déplacement est orthogonale"""
    
    if coord_dep[0] != coord_arr[0] and coord_dep[1] != coord_arr[1]:
        return False
    
    return True

def saut_possible(grille, coord, pion_ennemi):
    if coord[0] <= 4:
        if grille[coord[0]+2][coord[1]] == "" and grille[coord[0]+1][coord[1]] == pion_ennemi :
            return True

    if coord[0] >= 4:
        if grille[coord[0]-2][coord[1]] == "" and grille[coord[0]-1][coord[1]] == pion_ennemi :
            return True

    if coord[1] <= 4:
        if grille[coord[0]][coord[1]+2] == "" and grille[coord[0]][coord[1]+1] == pion_ennemi :
            return True
    
    if coord[1] >= 4:
        if grille[coord[0]][coord[1]-2] == "" and grille[coord[0]][coord[1]-1] == pion_ennemi :
            return True
        
    return False
    
def tour_joueur(tour, grille, joueur1, joueur2, depl = ""):
        
    coord_dep,coord_arr = [0,0]
    dist_depl,dist_saut,case_arr,case_dep,case_inter = False,False,False,False,False
    
    if tour%2 != 0:
        afficher_grille(grille, joueur1, joueur2, joueur1)
        pion_ennemi,pion_joueur = "●","○"
    
    if tour%2 == 0:
        afficher_grille(grille, joueur1, joueur2, joueur2)
        pion_ennemi,pion_joueur = "○","●"

    while depl != "saut" and depl != "deplacement":
        depl = str(input("Quel déplacement voulez vous effectuer ?\nSaisissez le mot 'saut' pour effectuer un saut\nSaisissez le mot 'deplacement' pour effectuer un deplacement simple\n"))
        print("\n")
    
    if depl == "saut":
        print("Rentrez les coordonnées du pions que vous voulez déplacer\nLes coordonnées rentrer doivent etre de la forme xy \n x est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
        coord_dep=transfo_coord(saisie_de_coordonnees(grille))
        print("Rentrez les coordonnées de la case ou vous voulez aller\nLes coordonnées rentrer doivent etre de la forme xy \n x est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
        coord_arr=transfo_coord(saisie_de_coordonnees(grille))
        dist_saut = dist_entre_case_saut(grille, coord_dep, coord_arr)
        case_arr =  verif_case_arr(grille, coord_arr)
        case_dep = verif_case_depart(grille, coord_dep, pion_joueur)
        case_inter = verif_case_inter(grille, coord_dep, coord_arr, pion_joueur, pion_ennemi)
        coord_inter = [(coord_dep[0]+coord_arr[0])//2,(coord_dep[1]+coord_arr[1])//2]
        
        while dist_saut == False or (case_arr == False or case_dep == False or case_inter == False):
            print("Les coordonnées rentrées precedemment ne sont pas valide veuillez réessayer.")
            print("Rentrez les coordonnées du pions que vous voulez déplacer\nLes coordonnées rentrer doivent etre de la forme xy \n x est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
            coord_dep=transfo_coord(saisie_de_coordonnees(grille))
            print("Rentrez les coordonnées de la case ou vous voulez aller\nLes coordonnées rentrer doivent etre de la forme xy \nx est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
            coord_arr=transfo_coord(saisie_de_coordonnees(grille))
            dist_saut = dist_entre_case_saut(grille, coord_dep, coord_arr)
            case_arr =  verif_case_arr(grille, coord_arr)
            case_dep = verif_case_depart(grille, coord_dep, pion_joueur)
            case_inter = verif_case_inter(grille, coord_dep, coord_arr, pion_joueur, pion_ennemi)
            coord_inter = [(coord_dep[0]+coord_arr[0])//2,(coord_dep[1]+coord_arr[1])//2]
        
        grille[coord_arr[0]][coord_arr[1]] = grille[coord_dep[0]][coord_dep[1]]
        grille[coord_dep[0]][coord_dep[1]] = ""
        grille[coord_inter[0]][coord_inter[1]] = ""
        
        if saut_possible(grille, coord_arr, pion_ennemi) == True:
            continu = str(input("Un saut est encore possible voulez vous continuer\n oui ou non ?"))
            print("\n")
            
            if continu == "oui":
                tour_joueur(tour, grille, joueur1, joueur2, depl = "saut")
            continu = "non"
            
            

    if depl == "deplacement":
        
        print("Rentrez les coordonnées du pions que vous voulez déplacer\nLes coordonnées rentrer doivent etre de la forme xy \nx est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
        coord_dep=transfo_coord(saisie_de_coordonnees(grille))
        print("Rentrez les coordonnées de la case ou vous voulez aller\nLes coordonnées rentrer doivent etre de la forme xy \nx est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
        coord_arr=transfo_coord(saisie_de_coordonnees(grille))
        dist_depl = dist_entre_case_depl(grille, coord_dep, coord_arr)
        case_arr =  verif_case_arr(grille, coord_arr)
        case_dep = verif_case_depart(grille, coord_dep, pion_joueur)
        
        while dist_depl == False or (case_arr == False or case_dep == False):
            print("Les coordonnées rentrées precedemment ne sont pas valide veuillez réessayer.\n")
            print("Rentrez les coordonnées du pions que vous voulez déplacer\nLes coordonnées rentrer doivent etre de la forme xy \nx est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
            coord_dep=transfo_coord(saisie_de_coordonnees(grille))
            print("Rentrez les coordonnées de la case ou vous voulez aller\nLes coordonnées rentrer doivent etre de la forme xy \ny est une lettre en majucsule entre A et G\ny un nombre compris entre 1-9\n")
            coord_arr=transfo_coord(saisie_de_coordonnees(grille))
            dist_depl = dist_entre_case_depl(grille,coord_dep,coord_arr)
            case_arr =  verif_case_arr(grille, coord_arr)
            case_dep = verif_case_depart(grille, coord_dep, pion_joueur)


        save =  grille[coord_arr[0]][coord_arr[1]]
        grille[coord_arr[0]][coord_arr[1]] = grille[coord_dep[0]][coord_dep[1]]
        grille[coord_dep[0]][coord_dep[1]] = save
    return grille
    
def tour_IA(grille, joueur1, joueur2, choix_depl = 0):
    afficher_grille(grille, joueur1, joueur2, joueur2)
    depl_saut = []
    depl_simpl = []
    for nb_ligne in range(len(grille)):
        for nb_colonne in range(1,len(grille[0])+1):
            coord_dep = transfo_coord(chr(65+nb_ligne)+str(nb_colonne))
            if verif_case_depart(grille, coord_dep, "●") == True:

                coord_arr_depl_gauche = transfo_coord(chr(65+nb_ligne)+str(nb_colonne-1))
                if dist_entre_case_depl(grille, coord_dep, coord_arr_depl_gauche)==True:
                    if verif_case_arr(grille, coord_arr_depl_gauche) == True:
                        depl_simpl.append((coord_dep, coord_arr_depl_gauche))

                coord_arr_depl_droite = transfo_coord(chr(65+nb_ligne)+str(nb_colonne+1))
                if dist_entre_case_depl(grille, coord_dep, coord_arr_depl_droite)==True:
                    if verif_case_arr(grille, coord_arr_depl_droite) == True:
                        depl_simpl.append((coord_dep, coord_arr_depl_droite))

                coord_arr_depl_haut = transfo_coord(chr(65+nb_ligne-1)+str(nb_colonne))
                if dist_entre_case_depl(grille, coord_dep, coord_arr_depl_haut)==True:
                    if verif_case_arr(grille, coord_arr_depl_haut) == True:
                        depl_simpl.append((coord_dep, coord_arr_depl_haut))

                coord_arr_depl_bas = transfo_coord(chr(65+nb_ligne+1)+str(nb_colonne))
                if dist_entre_case_depl(grille, coord_dep, coord_arr_depl_bas)==True:
                    if verif_case_arr(grille, coord_arr_depl_bas) == True:
                        depl_simpl.append((coord_dep, coord_arr_depl_bas))

                coord_arr_saut_gauche = transfo_coord(chr(65+nb_ligne)+str(nb_colonne-2))
                coord_inter = [(coord_dep[0]+coord_arr_saut_gauche[0])//2,(coord_dep[1]+coord_arr_saut_gauche[1])//2]
                if dist_entre_case_saut(grille, coord_dep, coord_arr_saut_gauche)==True:
                    if verif_case_arr(grille, coord_arr_saut_gauche) == True and verif_case_inter(grille, coord_dep , coord_arr_saut_gauche,  "●", "○") == True:
                        depl_saut.append((coord_dep,coord_arr_saut_gauche))

                coord_arr_saut_droite = transfo_coord(chr(65+nb_ligne)+str(nb_colonne+2))
                coord_inter = [(coord_dep[0]+coord_arr_saut_droite[0])//2,(coord_dep[1]+coord_arr_saut_droite[1])//2]
                if dist_entre_case_saut(grille, coord_dep, coord_arr_saut_droite)==True:
                    if verif_case_arr(grille, coord_arr_saut_droite) == True and verif_case_inter(grille, coord_dep , coord_arr_saut_droite,  "●", "○") == True:
                        depl_saut.append((coord_dep,coord_arr_saut_droite))

                coord_arr_saut_haut = transfo_coord(chr(65+nb_ligne-2)+str(nb_colonne))
                coord_inter = [(coord_dep[0]+coord_arr_saut_haut[0])//2,(coord_dep[1]+coord_arr_saut_haut[1])//2]
                if dist_entre_case_saut(grille, coord_dep, coord_arr_saut_haut)==True:
                    if verif_case_arr(grille, coord_arr_saut_haut) == True and verif_case_inter(grille, coord_dep , coord_arr_saut_haut,  "●", "○") == True:
                        depl_saut.append((coord_dep,coord_arr_saut_haut))

                coord_arr_saut_bas = transfo_coord(chr(65+nb_ligne+2)+str(nb_colonne))
                coord_inter = [(coord_dep[0]+coord_arr_saut_bas[0])//2,(coord_dep[1]+coord_arr_saut_bas[1])//2]
                if dist_entre_case_saut(grille, coord_dep, coord_arr_saut_bas)==True:
                    if verif_case_arr(grille, coord_arr_saut_bas) == True and verif_case_inter(grille, coord_dep , coord_arr_saut_bas,  "●", "○") == True:
                        depl_saut.append((coord_dep,coord_arr_saut_bas))

    print(depl_simpl)
    print(depl_saut)

    if depl_simpl == []:
        choix_depl = 2
    elif depl_saut == []:
        choix_depl = 1
    else:   
        choix_depl = random.randint(1,2)

    if choix_depl == 1:
        coup = depl_simpl[random.randint(0,len(depl_simpl)-1)]
        save =  grille[coup[1][0]][coup[1][1]]
        grille[coup[1][0]][coup[1][1]] = grille[coup[0][0]][coup[0][1]]
        grille[coup[0][0]][coup[0][1]] = save
        
    if choix_depl == 2:
        coup = depl_saut[random.randint(0,len(depl_saut)-1)]
        coord_inter = [(coup[0][0]+coup[1][0])//2,(coup[0][1]+coup[1][1])//2]
        grille[coup[1][0]][coup[1][1]] = grille[coup[0][0]][coup[0][1]]
        grille[coup[0][0]][coup[0][1]] = ""
        grille[coord_inter[0]][coord_inter[1]] = ""

        if saut_possible(grille, [coup[1][0]//2,coup[1][1]], "○") == True:
            if random.randint(1,2) == 2:
                tour_IA(grille, joueur1, joueur2, choix_depl = 2)

    print("\n")
    return grille
        


def choix_grille():
    grille = str(input("Avec quel grille voulez vous jouez?:\n  -Tapez 1 pour la grille du début\n  -Tapez 2 pour la grille du millieu\n  -Tapez 3 pour la grille de fin\n"))
    print("\n")
    while grille != "1" and grille !="2" and grille != "3":
         grille = str(input("Avec quel grille voulez vous jouez?:\n  -Tapez 1 pour la grille du début\n  -Tapez 2 pour la grille du millieu\n  -Tapez 3 pour la grille de fin\n"))
         print("\n")
    if grille == "1":
        return Grille_debut
    if grille == "2":
        return Grille_millieu
    if grille == "3":
        return Grille_fin

def choix_partie():
        Type_partie = int(input("A quel mode de jeu voulez vous jouez?: \n    -Tapez 1 pour une partie Joueur contre Joueur\n    -Tapez 2 si vous voulez jouer contre un ordinateur\n"))
        return Type_partie


def Partie(tour = 1,joueur1 ="Player1", joueur2="Bot_"+str(nom_bot[random.randint(0,len(nom_bot))])):
    Type_partie = choix_partie()
    grille = choix_grille()
    if Type_partie == 1:
        joueur1 = input("Quel est le nom du joueur n°1 ")
        print("\n")
        joueur2 = input("Quel est le nom du joueur n°2 ")
        print("\n")
        while nombre_de_pions(grille,"○") >= 6 and nombre_de_pions(grille,"●") >= 6:
            grille = tour_joueur(tour, grille, joueur1, joueur2)
            tour+=1
        if nombre_de_pions(grille,"○") < 6:
            afficher_grille(grille, joueur1, joueur2, joueur2)
            print("Fin de la partie, " +str(joueur2)," a gagné la partie!!!!!!!!")
        if nombre_de_pions(grille,"●") < 6:
            afficher_grille(grille, joueur1, joueur2, joueur1)
            print("Fin de la partie, " +str(joueur1)," a gagné la partie!!!!!!!!")
        return 0
       
    joueur1 = input("Quel est votre nom ?\n")
    print("\n")
    while nombre_de_pions(grille,"○") >= 6 and nombre_de_pions(grille,"●") >= 6:
            if tour % 2 != 0:
                grille = tour_joueur(tour, grille, joueur1, joueur2)
            else:
                grille = tour_IA(grille, joueur1, joueur2)
            tour+=1
    if nombre_de_pions(grille,"○") < 6:
        afficher_grille(grille, joueur1, joueur2, joueur2)
        print("Fin de la partie, " +str(joueur2)," a gagné la partie!!!!!!!!")
    if nombre_de_pions(grille,"●") < 6:
        afficher_grille(grille, joueur1, joueur2, joueur1)
        print("Fin de la partie, " +str(joueur1)," a gagné la partie!!!!!!!!")
    return 0
       
       
#_______________________________________________________TEST___________________________________________________________#
def test_transfo_coord():
    assert transfo_coord("A1") == [0,0]
    assert transfo_coord("B1") == [1,0]
    assert transfo_coord("F4") == [5,3]

def test_dist_entre_case_depl():
    assert dist_entre_case_depl(Grille_debut,[0,0],[0,0]) == False
    assert dist_entre_case_depl(Grille_debut,[2,1],[0,1]) == False
    assert dist_entre_case_depl(Grille_debut,[10,0],[9,0])
    assert dist_entre_case_depl(Grille_debut,[2,3],[2,4])

def test_dist_entre_case_saut():
    assert dist_entre_case_saut(Grille_debut,[0,0],[0,0]) == False
    assert dist_entre_case_saut(Grille_debut,[2,1],[0,1])
    assert dist_entre_case_saut(Grille_debut,[10,0],[9,0]) == False
    assert dist_entre_case_saut(Grille_debut,[2,3],[2,4]) == False
    assert dist_entre_case_saut(Grille_debut,[0,1],[0,3])
    assert dist_entre_case_saut(Grille_debut,[3,4],[3,2])

def test_direction_entre_deux_cases():
    assert direction_entre_deux_cases([0,0],[0,0])
    assert direction_entre_deux_cases([2,1],[0,1])
    assert direction_entre_deux_cases([10,0],[9,0])
    assert direction_entre_deux_cases([2,3],[2,4])

#__________________________________________________Fonction Générale de test___________________________________________#

def Test():
    test_est_dans_grille(Grille_debut)
    test_est_au_bon_format()
    test_transfo_coord()
    test_dist_entre_case_depl()
    test_direction_entre_deux_cases()
    test_dist_entre_case_saut()

#___________________________________________________Fonction début de partie____________________________________________#

Partie()
Test()