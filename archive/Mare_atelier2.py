 # -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs

                    
                                      #  Atelier 2  #
#### REPRESENTATION DES DONNEES
###initialisation des grilles et autres variables du jeu
#Le joueur 1 a les pions noirs et le joueur 2 les pions blancs
#Attention à bien lire les instructions

 #### REPRESENTATION GRAPHIQUE
#Fonction permettant l'affichage du plateau
#Prends en argument un plateau sous forme de tableau de tableaux de charactères

def afficher_grille(grille):
    lettre = 65
    print()                        
    print('   ',1,' ',2,' ',3,' ',4,' ',5,' ',6,' ',7)     
    print('  —————————————————————————————')
    for tab_ligne in grille:        
        print(chr(lettre),end = " |")   
        for i_elt in tab_ligne:        
            print("",i_elt,end=" |")
        print()
        print('  —————————————————————————————')
        
        lettre += 1                                           
    print()
    
 #### REPRESENTATION DES DONNEES
 #initialisation de la grille 


grille_jeu=([['o', 'o', ' ', ' ', ' ', '•', '•'], 
             ['o', ' ', ' ', 'o', ' ', ' ', '•'], 
             ['o', ' ', 'o', ' ', 'o', '•', ' '], 
             ['o', ' ', ' ', ' ', ' ', '•', ' '], 
             ['o', '•', '•', ' ', ' ', ' ', ' '], 
             ['o', ' ', ' ', ' ', '•', '•', ' '], 
             ['o', ' ', '•', ' ', '•', ' ', ' ']])


"""

"""

#### SAISIE
###fonction de verification
#jeux de test

#test de la fonction est_dans_grille
def test_est_dans_grille():
    assert est_dans_grille("A5"),"erreur cas dans la grille"
    assert not est_dans_grille("a5"),"erreur hors ligne inferieure"
    assert not est_dans_grille("I5"),"erreur hors ligne superieure"
    assert not est_dans_grille("A-1"),"erreur hors colonne inferieure"
    assert not est_dans_grille("A8"),"erreur hors colonne superieure"
    print("est_dans_grille : OK")

    
#test de la fonction est_au_bon_format
def test_est_au_bon_format() :  
    assert est_au_bon_format("A1"), "erreur cas classique"
    assert est_au_bon_format("Z0"), "erreur cas classique, lettre sup"
    assert not est_au_bon_format("12"), "erreur lettre en 0 attendu"
    assert not est_au_bon_format("BB"), "erreur chiffre en 1 attendu"
    assert not est_au_bon_format("&("), "erreur symbole"
    print ("est_au_bon_format : OK")

#Vérifie si les coordonnées sont au bon format (format du type a1 ou B3)
#Prends en entrée les coordonnées de type char
#Retourne un booléen

def est_au_bon_format(chaine) : 
    if len(chaine)!=2 : 
        return False
    lettre = chaine[0]
    chiffre = chaine[1]
    if ord(lettre) not in range(65,91) and ord(lettre) not in range(97,123) : 
        return False
    if ord(chiffre) not in range(48,58) : 
        return False
    return True
    """
    on vérifie si les codes des caractères sont compris entre ceux de
    A à Z et 1 à 9, si c'est le cas, les coordonnées sont au bon format
    """


#verification dans grille
#Prends en entrée les coordonnées de type char
#Retourne un booléen

def est_dans_grille(coordonnees):
    
    if len(coordonnees)==2:
        code_X = ord(coordonnees[0])
        code_Y = ord(coordonnees[1])                 
        return (code_X>=65 and code_X<=71) and (code_Y>=49 and code_Y<=55)
    """
    on vérifie si les codes des caractères sont compris entre ceux de
    A à G et 1 à 7, si c'est le cas, les coordonnées sont dans la grille
    """
    return False

###fonctions de saisie

def saisir_coordonnees() :
    donne_pion = input('Saisir coordonnées : ').upper()
    # Entrees : demande à l'utilisateur les déplacements souhaités
    # la méthode .upper() 'met en majuscule' un caractère
    if est_au_bon_format(donne_pion) and est_dans_grille(donne_pion):
        coord1=donne_pion[0]
        coord2=donne_pion[1]
        message1=False
        message2=False
        lettre=65
        chiffre=49
        i=0
        p=0
        while message1==False:
            if ord(coord1)>lettre:
                i+=1
                lettre+=1
            else:
                coord1=i
                message1=True
        while message2==False:
            if ord(coord2)>chiffre:
                p+=1
                chiffre+=1
            else:
                coord2=p
                message2=True
        if (grille_jeu[coord1][coord2])=='•':
            print()
            print("Le pion choisit est en : ",donne_pion)
        else:
            print()
            print('Choisis un bon pion')
            saisir_coordonnees()
    else:
        print()
        print('Choisis un bon pion')
        saisir_coordonnees()
    donne_pion=[coord1,coord2]
    return(donne_pion)

#### CODE PRINCIPAL
# execution affichage sur les 3 grilles et autres variables de jeux
print()
afficher_grille(grille_jeu)
afficher_grille(grille_jeu)
afficher_grille(grille_jeu)



#execution fonction test unitaire
def run_test():
    test_est_dans_grille()
    test_est_au_bon_format()

#affichage des coordonnees saisies
print(saisir_coordonnees())


run_test()