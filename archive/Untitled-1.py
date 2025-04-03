# -*- coding: utf-8 -*-

#Representation de donnes 

joueur_1 = "⚫"
joueur_2 = "⚪"

#Creation de la grile de depart  
grille_1  = ([" ", 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
             ["A",joueur_1,joueur_1,joueur_1,joueur_1,joueur_1,joueur_1,joueur_2],
             ["B",joueur_1,joueur_1,joueur_1,joueur_1,joueur_1,joueur_2,joueur_2],
             ["C",joueur_1,joueur_1,joueur_1,joueur_1,joueur_2,joueur_2,joueur_2],
             ["D",joueur_1,joueur_1,joueur_1,"  ",joueur_2,joueur_2,joueur_2],
             ["E",joueur_1,joueur_1,joueur_1,joueur_2,joueur_2,joueur_2,joueur_2],
             ["F",joueur_1,joueur_1,joueur_2,joueur_2,joueur_2,joueur_2,joueur_2],
             ["G",joueur_1,joueur_2,joueur_2,joueur_2,joueur_2,joueur_2,joueur_2])

#representation d'une grille du millieu du jeu 
grille_2 = ([" ", 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
            ["A",joueur_1,"  " , joueur_1 , "  " , joueur_1 , joueur_1 , joueur_2],
            ["B",joueur_1,joueur_1,"  " , "  " , "  " , "  ", joueur_2],
            ["C",joueur_1,"  " , "  " , "  " , "  ", "  " , "  "],
            ["D",joueur_1,"  ",joueur_2, "  " , "  ", "  ","  "],
            ["E",joueur_1,joueur_2,"  " , "  " , "  " , "  " , "  "],
            ["F",joueur_1,"  " , "  " , "  " , "  ", "  ",joueur_2],
            ["G",joueur_1,joueur_2,"  ", "  " ,joueur_2,joueur_2,joueur_2])

#representation de la  grille de fin de partie
grille_3 = ([" ", 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
            ["A",joueur_1,"  " , joueur_1,"  ", "  " , "  " , "  "],
            ["B",joueur_1,"  " , "  ", "  " , "  " , "  " , joueur_2],
            ["C",joueur_1,"  " , joueur_1,"  " , "  " , joueur_1, "  "],
            ["D",joueur_1,"  " , "  " , joueur_1, "  " , "  " , "  "],
            ["E","  " , "  " , joueur_1, "  ", joueur_2 , "  " , joueur_2],
            ["F","  ","  ","  " , "  ", "  ", "  ","  "],
            ["G",joueur_1,"  ","  ","  ", joueur_2,"  " , joueur_2])

#representation graphique 
def afficher_grille(grille) : 
    for j in range(len(grille[0])):           #creation de la ligne de la numerotation des colonnes sans separation
        print(grille[0][j],end="  ")
    print()
    for i in range(1,len(grille)) :           #creation du reste de la grille avec separation '|' entre chaque case 
        for j in range(len(grille[i])):
            print(grille[i][j],end="|" )     
        print()
            

#saisie des donnees 
#fonction de test est au bon format 

def test_est_au_bon_format():

    assert est_au_bon_format("A1"), "erreur cas classique"
    assert est_au_bon_format("Z0"), "erreur cas classique, lettre sup"
    assert not est_au_bon_format("12"), "erreur lettre en 0 attendu"
    assert not est_au_bon_format("BB"), "erreur chiffre en 1 attendu"
    assert not est_au_bon_format("&("), "erreur symbole"

#fonction de test est dans la grille

def test_est_dans_grille():
    
    assert est_dans_grille("A",5,grille_2),"erreur cas dans la grille"
    assert not est_dans_grille("a",5,grille_2),"erreur hors ligne inferieure"
    assert not est_dans_grille("I",5,grille_2),"erreur hors ligne superieure"
    assert not est_dans_grille("A",-1,grille_2),"erreur hors colonne inferieure"
    assert not est_dans_grille("A",8,grille_2),"erreur hors colonne superieure"

#fonction qui verifie si le pion choisie est au bon format 

def est_au_bon_format(pion):

    #si le choix ne contient pas deux caracteres
    if len(pion)<=1 :     
        return False
    #si le choix a au moins deux caracteres mais n'est pas sous forme lettre-chiffres 
    elif len(pion)>1 and  (ord(pion[0])<65 or ord(pion[0])>90 or ord(pion[1])< 48 or ord(pion[1])>57) :   
        return False
    #si le choix contient au moins deux caracteres avec le bon ordre : lettre-chiffre
    else :
        return True
    
#fonction qui verifie si le pion choisi est dans la grille 

def est_dans_grille(ligne,colonne,grille): 

    if int(colonne) not in grille[0] or ligne > grille[len(grille)-1][0] : 
        return False 
    else : 
        return True

#fonction qui compte le nb de pion dans chaque equipe 

def nb_de_pion(grille) : 
    nb_de_pion_j1 = 0 
    nb_de_pion_j2 = 0 
    
    for i in range(len(grille)) : 
        for j in range(len(grille[i])): 
            #parcours la grille est compte le nombre de fois qu'il rencontre la chaine de car joueur_1 ou joueur_2      
            if grille[i][j] == joueur_1:
                nb_de_pion_j1 += 1        
            elif grille[i][j] == joueur_2 : 
                nb_de_pion_j2 += 1

    #le message a afficher 
    message = "Le nombre de pions du joueur 1 est " , nb_de_pion_j1 , "Le nombre de pions du joueur 2 est " , nb_de_pion_j2
    return message 

#saisie de coordonnee

def saisie_de_coordonnes(grille): 
    valeur = False 

    #tant que la valeur est False et que la fonction est_au_bon_format / est_dans_grille est fausse , on redemende un nouveau choix
    pion = input("Veuillez choisir un pion")
    while valeur == False : 
           
        ligne = pion[0]
        colonne = pion[1]
        if est_au_bon_format(pion) == False : 
            pion = input("Veuillez entrer un pion au bon format")
        elif est_dans_grille(ligne,colonne,grille) == False : 
            pion = input("Veuillez choisir un pion dans la grille")
        elif est_dans_grille(ligne,colonne,grille) == True and est_au_bon_format(pion) == True : 
            valeur = True 

    #on retourne les coordonnes du pion choisi
    return pion


### code principal ###

#affichage des 3 grilles 
print("Le joueur 1 est : " , joueur_1)
print("Le joueur 2 est : ", joueur_2)
print("La grille de départ est : ")
afficher_grille(grille_1)
print(nb_de_pion(grille_1))
print("La grille du millieu de jeu est : ")
afficher_grille(grille_2)
print(nb_de_pion(grille_2))
print("La grille de fin de partie est : ")
afficher_grille(grille_3)
print(nb_de_pion(grille_3))

#appel de la fonction test 

test_est_dans_grille()
test_est_au_bon_format()

#affichage des coordonnees 

print(saisie_de_coordonnes(grille_1))
