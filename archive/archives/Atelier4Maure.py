# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs
def affichage(grille):
    x=0 #ligne
    y=0 #colonne
    i=1
    print("    A   B   C   D   E   F   G")  #permet l'affichage au dessus de la grille du nom des colonnes
    while x!=len(grille):  
        print("  +---+---+---+---+---+---+---+")
        print(i,end=' ')
        while y!=len(grille[0]):
            
            print('|',grille[x][y],'', end="")         #permet l'affichage de chaque symbole sur la même ligne grâce â  end=' '
            y=y+1
        print('|',end='')     #permet juste de rajouter la barre a la fin (pour faire plus propre)
        print()  # ce print permet une fois une colonne afficher de passer a la prochaine ligne
        i=1+i
        y=0                             # et donc je remet y=0 pour pouvoir commencer une nouvelle colonne
        x=x+1
    print("  +---+---+---+---+---+---+---+")

def test_est_dans_grille():                                                       #test pour voir si est_dans_grille fonctionne
    assert est_dans_grille('9Z')==False, 'Test colonne False'      #je vérifie d'abord avec une colonne en dehors
    assert est_dans_grille('-5B')==False, 'Test ligne False'       #puis une ligne fausse
    assert est_dans_grille('5A')==True, 'Test normalement True'    #enfin au cas oû, des coordonnées possibles
    print("test_est_dans_grille OK")


def est_dans_grille(saisie):                    #permet de vérifier la saisie, si un trop grand nombre de caractere est rentré ou trop peu etc...
    if len(saisie)>2:
        print(' -  Erreur trop de donnée saisie. Un nombre et une lettre attendue. Exemple: A1')
        return(False)
    elif len(saisie)<=1:
        print(' -  Erreur pas assez de donnée saisie. Un nombre et une lettre attendue. Exemple: A1')
        return(False)
    else:
        ligne=saisie[0]
        colonne=saisie[1]

    liste1=['1','2','3','4','5','6','7']
    liste2=['A','B','C','D','E','F','G']
    liste_erreur=[0,0]

    for elem in liste1:              #verifie si le premier chiffre saisie est bien dans la liste 1, si oui la liste erreur passe a 1
        if ligne==elem:
            liste_erreur[0]=1
            
    for elem in liste2:               #de meme avec la lettre, si elle est bien dans la liste 2, le deuxieme chiffre de la liste erreur passe a 1
        if colonne==elem:
            liste_erreur[1]=1

    if liste_erreur[0]==1 and liste_erreur[1]==1:           #si les 2 listes_erreur sont a 1 alors pas de probleme, sinon il est du coup facile de savoir ou est le probleme.
        return(True)
    else:
        if liste_erreur[0]==0:
            print()
            print(" -  Coordonnée de la ligne non valide. N'est pas dans la grille")
            print()
        if liste_erreur[1]==0:
            print()
            print(" -  Coordonnée de la colonne non valide. N'est pas dans la grille")
            print()
        return(False)


def saisir_coordonnees(grille):
    print("Quelle ligne et colonne voulez-vous choisir?  Coordonnées = ",end='' )
    saisie=input()
    
    while est_dans_grille(saisie)!=True:
        print("Quelle ligne et colonne voulez-vous choisir?  Coordonnées = ",end='' )
        saisie=input()
    else:
        ligne=saisie[0]
        colonne=saisie[1]
        ligne=int(ligne)
    
    liste2=['A','B','C','D','E','F','G']    #permet de transformer une colonne indiquée par une lettre ('A') en un chiffre (1). Utile pour les fonctions de l'atelier 3
    i=0
    while i!=len(liste2):
        if colonne==liste2[i]:
            colonne=i+1
        i=i+1
    
    return(ligne,colonne)






def verification_pion(ligne,colonne,grille,joueur):
    
    if joueur==grille[ligne-1][colonne-1]:
        return(True)
    else:
        print("Erreur, ce n'est pas votre pion")
        return(False)

def test_verification_pion():
    assert verification_pion(2,2,jeu_milieu_de_partie,'X')==True, "Erreur vérification pion 1" 
    assert verification_pion(3,1,jeu_milieu_de_partie,'X')==False, "Erreur vérification pion 2"
    assert verification_pion(3,3,jeu_milieu_de_partie,'X')==False, "Erreur vérification pion 3"
    print("test_verification_pion OK")



def liste_cases_traverser(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):  # fonction qui permet de verifier si on peut aller d'un point a à un point b 
    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnes réelle de la liste du jeu
    
    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1                  
    colonne_arriver=colonne_arriver-1

    (x,y)=((ligne-ligne_arriver),(colonne-colonne_arriver))
    result=[]

    test1=0     #test1 et test2 servent a savoir si le deplacement est possible. Si test1 ou test2 est = 0 alors le deplacement est un déplcement en ligne droite
    test2=0                                        #sinon il faut que test1 et test2 soit a égalité, cela voudra dire que le deplacement est une diagonale.

    while x!=0 or y!=0:
        if x<0:
            ligne=ligne+1
            test1=test1+1
            x=x+1
        if y<0:
            colonne=colonne+1
            test2=test2+1
            y=y+1
        if x>0:
            ligne=ligne-1
            test1=test1+1
            x=x-1
        if y>0:
            colonne=colonne-1
            test2=test2+1
            y=y-1
        result.append(grille[ligne][colonne])    #tout ceci me permet au final d'avoir une liste avec toutes les cases traversées 
    
    #comme indiquer plus hauts si il ya un probleme avec test1 et test2, alors cela signifie que le deplacement n'est pas dans les regles du jeu.
    if test1!=test2:   # Car si test1 et test2 sont égaux, cela signifie que le movement est diagonale. 
        if test1!=0 and test2!=0:        #Et s'il ne sont pas égaux et qu'aucun des 2 n'est égales a 0. Alors il y a un probleme dans le déplacement.
            print("Erreur, le mouvement n'est pas possible")   
            return(False)
    return(result)
            
def test_liste_cases_traverser():

    assert liste_cases_traverser(2,2,8,9,jeu_milieu_de_partie,'X')==False, "Erreur liste_cases_traverser 1" 
    assert liste_cases_traverser(5,9,5,1,jeu_milieu_de_partie,'X')==[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], "Erreur liste_cases_traverser 2"
    assert liste_cases_traverser(1,4,7,4,jeu_milieu_de_partie,'X')==[' ', ' ', ' ', ' ', ' ', 'O'], "Erreur liste_cases_traverser 3"
    print("test_liste_cases_traverser OK")

  

def verification_elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):
    liste_cases=liste_cases_traverser(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)  
    if liste_cases==False:
        return(False)  
    joueur1='X'
    joueur2='O'

    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnées réelle de la liste du jeu
    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1           
    colonne_arriver=colonne_arriver-1

    #permet de savoir si les cases entre le départ et l'arrivé sont vides
    i=0
    t=0   
    if len(liste_cases)<=1:
        print("Erreur taille de trajet inférieur a 1 OU vous avez choisi la même case de départ et d'arrivée.")
        return(False)                       

    while i!=len(liste_cases)-1:       #si t reste a 0 alors toutes les cases entre la case de départ et d'arrivé sont vides.
        if liste_cases[i]!=' ':
            t=t+1
        i=i+1
    
    if t!=0:
        print("Erreur, il y a un autre pion sur la trajectoire d'élimination. Choisissez un autre pion a éliminer.")
        return(False)

    #vérifie que le pion éliminer est bien un pion adverse
    if joueur1==joueur:                                   #si c'est au tour du joueur 1 ou non
        if liste_cases[len(liste_cases)-1]==joueur2:
            return(True)
        else:
            print('Case impossible a prendre. Il y a déja un de vos pions dessus ou elle est vide')
            return(False)
    elif joueur2==joueur:
        if liste_cases[len(liste_cases)-1]==joueur1:
            return(True)
        else:
            print('Case impossible a prendre. Il y a déja un de vos pions dessus ou elle est vide')
            return(False)
    else:
        return(False)


def test_verification_elimination():

    assert verification_elimination(1,4,7,4,jeu_milieu_de_partie,'X')==True, "Erreur test_verification_elimination 1" 
    assert verification_elimination(1,4,8,4,jeu_milieu_de_partie,'X')==False, "Erreur test_verification_elimination 2"
    assert verification_elimination(5,3,5,4,jeu_milieu_de_partie,'X')==False, "Erreur test_verification_elimination 3"
    print("test_verification_elimination OK")


def elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):

    joueur1='X'
    joueur2='O'

    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1                  #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnes réelle de la liste du jeu
    colonne_arriver=colonne_arriver-1

                                     #si c'est au tour du joueur 1 ou non          
    grille[ligne][colonne]=' '                               #on enleve le pion du joueur 1 et on le remplace par une case vide du coup
    grille[ligne_arriver][colonne_arriver]=joueur           #et on met son pion a la place du joueur 2*
    return(grille)

def test_elimination():
    jeu_milieu_de_partie=[['X','X','X','X','X','X','O'],['X','X',' ',' ','X','X','O'],['O',' ','O',' ',' ','X','X'],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ','O','X',' ',' '],['O','X','O',' ','O',' ',' '],['O','O','O','O','O','O','O']]
    assert elimination(1,3,3,3,jeu_milieu_de_partie,'X')==[['X','X',' ','X','X','X','O'],['X','X',' ',' ','X','X','O'],['O',' ','X',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ','O','X',' ',' '],['O','X','O',' ','O',' ',' '],['O','O','O','O','O','O','O']], "Erreur test_elimination 1"
    jeu_milieu_de_partie=[['X','X','X','X','X','X','O'],['X','X',' ',' ','X','X',' '],['O',' ','O',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ','O','X',' ',' '],['O','X','O',' ','O',' ',' '],['O','O','O','O','O','O','O']]
    assert elimination(1,4,7,4,jeu_milieu_de_partie,'X')==[['X','X','X',' ','X','X','O'],['X','X',' ',' ','X','X','O'],['O',' ','O',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ','X','X',' ',' '],['O','X','O',' ','O',' ',' '],['O','O','O','O','O','O','O']], "Erreur test_elimination 2"
    print("test_elimination OK")




def verification_capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):
    liste_cases=liste_cases_traverser(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)  
    if liste_cases==False:
        return(False)  
    
    joueur1='X'
    joueur2='O'

    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnées réelle de la liste du jeu
    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1           
    colonne_arriver=colonne_arriver-1

    if len(liste_cases)<=1:
        print("Erreur taille de trajet inférieur à 2, pour capturer vous devez indiquer la case derriere le pion que vous capturer")
        return(False)

    #permet de savoir si les cases entre le départ et l'arrivé sont vides
    i=0
    t=0                         

    while i!=len(liste_cases)-2:       #si t reste a 0 alors toutes les cases entre la case de départ et d'arrivé -2 sont vides.
        if liste_cases[i]!=' ':
            t=t+1
        i=i+1
    
    # Je vérifie ensuite que l'avant derniere case est bien un pion adverse et que la case derriere est bien vide, pour respecter les regles de la capture
    if liste_cases[len(liste_cases)-2]!=joueur and liste_cases[len(liste_cases)-2]!=' ':
        if liste_cases[len(liste_cases)-1]==' ':
            t=t
        else:
            print("Erreur vous n'avez pas la place de capturer")
            t=t+1
    else:
        print("Erreur vous essayez de capturer votre propre pion probablement ou alors la case est vide ")
        t=t+1
    

    if t!=0:
        return(False)
    else:
        return(True)


def test_verification_capture():
    verification_capture(1,3,4,3,jeu_milieu_de_partie,'X')==True, "Erreur test_verification_capture 1"
    verification_capture(1,3,3,3,jeu_milieu_de_partie,'X')==False, "Erreur test_verification_capture 2"
    verification_capture(1,1,9,9,jeu_milieu_de_partie,'X')==False, "Erreur test_verification_capture 3"
    verification_capture(7,5,7,4,jeu_milieu_de_partie,'X')==False, "Erreur test_verification_capture 4"
    verification_capture(7,5,7,3,jeu_milieu_de_partie,'X')==True, "Erreur test_verification_capture 5"
    print("test_verification_capture OK")




def capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):

    joueur1='X'
    joueur2='O'

    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1                  #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnes réelle de la liste du jeu
    colonne_arriver=colonne_arriver-1
    
    # Calcul des coordonnées du pion a capturer
    # px,py sont les coordonnées du pion à capturer
    
    # je calcule les coordonnées grace a la difference négative ou positive, des coordonnées de départ - coordonnées d'arrivés
    (x,y)=((ligne-ligne_arriver),(colonne-colonne_arriver))
    
    if x==0:
        px=ligne_arriver+1+0               
    if y==0:
        py=colonne_arriver+1+0

    if x<0:
        px=ligne_arriver+1-1
    if y<0:
        py=colonne_arriver+1-1

    if x>0:
        px=ligne_arriver+1+1
    if y>0:
        py=colonne_arriver+1+1
    
                                
    grille[ligne][colonne]=' '                             #j'enleve le pion du joueur 1 et je le remplace par une case vide du coup
    grille[px-1][py-1]=joueur                              # je remplace le pion capturer par un pion du joueur
    grille[ligne_arriver][colonne_arriver]=joueur           #et je met son pion a la bonne position juste apres donc
    return(grille)

def fin_de_partie(grille):
    i1=0
    i2=0
    cpt_x=0
    cpt_o=0
    while i1!=len(grille):
        i2=0
        while i2!=7:
            if grille[i1][i2]=='X':
                cpt_x=cpt_x+1
            if grille[i1][i2]=='O':
                cpt_o=cpt_o+1
            i2=i2+1
        i1=i1+1
    if cpt_o<6:
        print("Jeu fini: le joueur aux pions X a gagné")
        return(True)
    if cpt_x<6:
        print("Jeu fini: le joueur aux pions O a gagné")
        return(True)
    else:
        return(False)

def test_fin_de_partie():
    assert fin_de_partie(jeu_milieu_de_partie)==False, "Erreur test_fin_de_partie 1"
    assert fin_de_partie(jeu_fin_de_partie)==False, "Erreur test_fin_de_partie 2"
    assert fin_de_partie(jeu_gagnant)==True, "Erreur test_fin_de_partie 3"
    print("test_fin_de_partie OK")

# Fonction qui me permet de saisir une valeur entre 1 et 3 et permet au programme de ne pas planter si le joueur décide de saisir n'importe quoi
def verifie_nombre():    # Du coup cette fonction est utilisée dès qu'il y a un choix a faire entre 1 et 3
    nombre=0
    t=0
    while t==0:
        nombre=input()
        x=0
        i=0
        liste=['1','2','3']   # Ne fonctionne qu'avec 3 choix. il serait possible de changer le nombre de choix avec une autre variable (def verifie_nombre(nombre,nombre_de_choix):)
        while i!=len(liste):
            if liste[i]==nombre:
                x=i+1
                return(x)
            i=i+1
        print("Erreur, seul 1,2 ou 3 sont accepter")
    return(nombre)


# Fonction qui permet d'exécuter un tour entier
def lancer_tour(joueur,grille):
    liste=[0,'A','B','C','D','E','F','G']
    # ca serait mieux qu'au lieu de demander a capturer ou a éliminer, le programme se rende compte qu'il s'agi d'une élimination ou d'une capture
    test=0
    while test==0:
        test=1
        affichage(grille)
        (ligne,colonne)=saisir_coordonnees(grille)
        while verification_pion(ligne,colonne,grille,joueur)==False:         #vérifie que le joueur choisi bien un de ces pions
            (ligne,colonne)=saisir_coordonnees(grille)    
        print('Ou souhaitez-vous vous déplacer ?')
        (ligne_arriver,colonne_arriver)=saisir_coordonnees(grille)

        # Je vérifie ensuite si un mouvement de capture ou d'élimination est possible, et du coup, j'en déduis ce que souhaite faire le joueur 
        
        # Ici si aucun des 2 n'est possible je dis au programme de re faire un tour ou permet au joueur d'abandonner
        if verification_capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==False and verification_elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==False:
            test=0
            print()
            print("Le mouvement n'est pas possible, voulez-vous abandonner ? ")
            print("1      pour Oui")
            print("2 ou 3 pour Non")
            x=verifie_nombre()
            if x==1:
                test=1
                if joueur=='X':
                    grille=jeu_gagnant_O
                else:
                    grille=jeu_gagnant_X
        
        # Mouvement de capture un peu long, du aux différents choix que je laisse au joueur
        elif verification_capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==True:  
            grille=capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)
            
            choix=0
            (ligne,colonne)=(ligne_arriver,colonne_arriver)
            while choix==0:    # Le joueur peut rejouer s'il le souhaite
                affichage(grille)
                print("Vous venez de capturer un pion, vous pouvez donc rejouer, seulement pour refaire une capture")
                print("Voulez-vous rejouer?    1      -> Oui")
                print("                        2 ou 3 -> Non")
                choix=verifie_nombre() 
                (ligne,colonne)=(ligne_arriver,colonne_arriver)  #Le programme récupere les coordonnées d'arriver du pion et les prends pour les coordonnées du pion a déplacer (cela évite la triche)
                while choix==1:       # Tant que le joueur veut rejouer, le programme lui redemande la ou il souhaite se déplacer
                    affichage(grille)
                    print("Vous étes sur la case (",ligne,",",liste[colonne],") (A CHANGER POUR UN CHIFFRE ET UNE LETTRE. OU ALORS un CODE COULEUR SUR LE PION DIRECTEMENT)")
                    print('Ou souhaitez-vous vous déplacer ?')
                    (ligne_arriver,colonne_arriver)=saisir_coordonnees(grille)

                    if verification_capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==True:  # Mouvement de capture
                        grille=capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)
                        choix=0
                    else:
                        print()
                        print("Voulez vous continuer la capture ? (répondez non (2 ou 3) si jamais vous vous etes rendu compte que vous ne pouvez plus capturer)")
                        print(" 1      -> Oui")
                        print(" 2 ou 3 -> Non")
                        choix=verifie_nombre()


        # Mouvement d'élimination beaucoup plus court du coup
        elif verification_elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==True:  # Mouvement d'élimination
            grille=elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)
        
    affichage(grille)
    print("Fin du tour du Joueur avec les pions",joueur)
    return(grille)   #retourne donc la grille avec le changement


# Fonction pour lancer la partie
def lancer_partie(grille):
    liste_joueur=[0,'X','O']       # cette liste me sert a changer de joueur, le joueur 1 a les pions 'X' et le joueur 2 a les pions 'O'
    joueur=1
    print("Le joueur",joueur,"va commencer avec les pions",liste_joueur[joueur])
    while fin_de_partie(grille)==False:               # Tant que la fonction fin_de_partie ne renvoie pas True , je repasse dans la boucle
        print("Au tour du joueur",joueur,"avec les pions",liste_joueur[joueur])
        grille=lancer_tour(liste_joueur[joueur],grille)

        if joueur==1:          # Si c'était au tour du joueur 1 je passe au joueur 2 et inversement
            joueur=2
        else:
            joueur=1

    return(print("Fin de partie"))







# Fonctions pour jouer contre l'ordinateur ----------------------------------------------------------------------------------------------------------------------------


# Fonctions pour jouer contre l'ordinateur ----------------------------------------------------------------------------------------------------------------------------


# Fonctions pour jouer contre l'ordinateur ----------------------------------------------------------------------------------------------------------------------------





# Les fonctions en dessous sont exactement les mêmes qu'au dessus, a ceci pres que j'ai enlever tout les 'print' d'erreur
# Car vu que la fonction lancer-tour_ordi teste toutes les possibilités, le nombre d'erreur affiché aurait été beaucoup trop grand 

# Les deux seuls nouvelles fonctions du coup sont: lancer_tour_ordi et lancer_partie_ordi   Elles sont en dernier du bloc des fonctions ordi


# Ajout pour permettre l'aléatoire (voir la fonction lancer_tour_ordi)
import random
random.seed()




def verification_pion_ordi(ligne,colonne,grille,joueur):
    if joueur==grille[ligne-1][colonne-1]:
        return(True)
    else:
        return(False)


def liste_cases_traverser_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):  # fonction qui permet de verifier si on peut aller d'un point a à un point b 
    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnes réelle de la liste du jeu
    
    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1                  
    colonne_arriver=colonne_arriver-1

    (x,y)=((ligne-ligne_arriver),(colonne-colonne_arriver))
    result=[]

    test1=0     #test1 et test2 servent a savoir si le deplacement est possible. Si test1 ou test2 est = 0 alors le deplacement est un déplcement en ligne droite
    test2=0                                        #sinon il faut que test1 et test2 soit a égalité, cela voudra dire que le deplacement est une diagonale.

    while x!=0 or y!=0:
        if x<0:
            ligne=ligne+1
            test1=test1+1
            x=x+1
        if y<0:
            colonne=colonne+1
            test2=test2+1
            y=y+1
        if x>0:
            ligne=ligne-1
            test1=test1+1
            x=x-1
        if y>0:
            colonne=colonne-1
            test2=test2+1
            y=y-1
        result.append(grille[ligne][colonne])    #tout ceci me permet au final d'avoir une liste avec toutes les cases traversées 
    
    #comme indiquer plus hauts si il ya un probleme avec test1 et test2, alors cela signifie que le deplacement n'est pas dans les regles du jeu.
    if test1!=test2:   # Car si test1 et test2 sont égaux, cela signifie que le movement est diagonale. 
        if test1!=0 and test2!=0:        #Et s'il ne sont pas égaux et qu'aucun des 2 n'est égales a 0. Alors il y a un probleme dans le déplacement.  
            return(False)
    return(result)



def verification_capture_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):
    liste_cases=liste_cases_traverser_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)  
    if liste_cases==False:
        return(False)  
    
    joueur1='X'
    joueur2='O'

    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnées réelle de la liste du jeu
    ligne=ligne-1
    colonne=colonne-1
    ligne_arriver=ligne_arriver-1           
    colonne_arriver=colonne_arriver-1

    if len(liste_cases)<=1:
        return(False)

    #permet de savoir si les cases entre le départ et l'arrivé sont vides
    i=0
    t=0                         
    while i!=len(liste_cases)-2:       #si t reste a 0 alors toutes les cases entre la case de départ et d'arrivé -2 sont vides.
        if liste_cases[i]!=' ':
            t=t+1
        i=i+1
    
    # Je vérifie ensuite que l'avant derniere case est bien un pion adverse et que la case derriere est bien vide, pour respecter les regles de la capture
    if liste_cases[len(liste_cases)-2]!=joueur and liste_cases[len(liste_cases)-2]!=' ':
        if liste_cases[len(liste_cases)-1]==' ':
            t=t
        else:
            t=t+1
    else:
        t=t+1
    
    if t!=0:
        return(False)
    else:
        return(True)



def verification_elimination_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur):
    liste_cases=liste_cases_traverser_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)  
    if liste_cases==False:
        return(False)  
    joueur1='X'
    joueur2='O'

    #les coordonnées qui arrivent sont toutes selon la grille visuelle, donc il faut enlever 1, si on veut les coordonnées réelle de la liste du jeu
    #ligne=ligne-1
    #colonne=colonne-1
    #ligne_arriver=ligne_arriver-1           
    #colonne_arriver=colonne_arriver-1

    #permet de savoir si les cases entre le départ et l'arrivé sont vides
    i=0
    t=0   
    if len(liste_cases)<=1:
        return(False)                       

    while i!=len(liste_cases)-1:       #si t reste a 0 alors toutes les cases entre la case de départ et d'arrivé sont vides.
        if liste_cases[i]!=' ':
            t=t+1
        i=i+1
    
    if t!=0:
        
        return(False)

    #vérifie que le pion éliminer est bien un pion adverse
    if joueur1==joueur:                                   #si c'est au tour du joueur 1 ou non
        if liste_cases[len(liste_cases)-1]==joueur2:
            return(True)
        else:
            return(False)
    elif joueur2==joueur:
        if liste_cases[len(liste_cases)-1]==joueur1:
            return(True)
        else:
            return(False)


def lancer_tour_ordi(joueur,grille):
    liste=[0,'A','B','C','D','E','F','G']
    liste_movement_elimination=[]         # Je crée 2 liste differentes qui recevront les coordonnées possibles de capture et d'élimination
    liste_movement_capture=[]                             

    # Tout les "for in range" me permette de tester toutes les cases pour le pion a choisir, et ensuite pour chaque pion choisi de tester toutes les cases d'arrivé possible
    

    for ligne in range(1,7):
        for colonne in range(1,7):
            if verification_pion_ordi(ligne,colonne,grille,joueur)==True:    # Pour alléger tout ca, je regarde au milieu si l'ordi est bien sur un de ses pions. 
                for ligne_arriver in range(1,7):
                    for colonne_arriver in range(1,7):
                        if verification_elimination_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==True:
                            liste_movement_elimination.append((ligne,colonne,ligne_arriver,colonne_arriver))                # Je rajoute donc les coordonnées possibles a chaques listes
                        if verification_capture_ordi(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)==True:
                            liste_movement_capture.append((ligne,colonne,ligne_arriver,colonne_arriver))

    a=1
    b=2
    choix = random.randint(a,b)             # le choix entre la liste capture et elimination est aléatoire. 1 pour la liste élimination et 2 pour la liste capture

    if choix==1:                            # Puis je choisi dans chaque liste, aléatoirement, les coordonnées a utilisés
        a=0
        b=len(liste_movement_elimination)-1
        choix = random.randint(a,b)         # Le choix sera en faite un indice entre 0 et la taille de la liste
        (ligne,colonne,ligne_arriver,colonne_arriver)=liste_movement_elimination[choix]
        elimination(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)
    else:
        a=0
        b=len(liste_movement_capture)-1
        choix = random.randint(a,b)
        (ligne,colonne,ligne_arriver,colonne_arriver)=liste_movement_capture[choix]
        capture(ligne,colonne,ligne_arriver,colonne_arriver,grille,joueur)
    
    print("L'ordinateur a joué son pion en (",ligne,liste[colonne],") et l'à déplacé en (",ligne_arriver,liste[colonne_arriver],") ")
    print()
    return(grille)  # Je retourne donc la grille une fois le mouvement de l'ordi effectuer
        


def lancer_partie_ordi(grille):
    liste_joueur=[0,'X','O']       # cette liste me sert a changer de joueur, le joueur 1 a les pions 'X' et le joueur 2 a les pions 'O'
    joueur=1
    print("Le joueur",joueur,"va commencer avec les pions",liste_joueur[joueur])
    while fin_de_partie(grille)==False:               # Tant que la fonction fin_de_partie ne renvoie pas True , je repasse dans la boucle
        if joueur==2:
            print()
            print("Au tour de l'ordinateur avec les pions",liste_joueur[joueur])
            print()
            grille=lancer_tour_ordi(liste_joueur[joueur],grille)
        else:
            print("Au tour du joueur",joueur,"avec les pions",liste_joueur[joueur])
            grille=lancer_tour(liste_joueur[joueur],grille)

        if joueur==1:          # Si c'était au tour du joueur 1 je passe au joueur 2 et inversement
            joueur=2
        else:
            joueur=1

    return(print("Fin de partie"))




# Fin des fonctions ordinateur ------------------------------------------------------------------------------------------------------------------------------------------

# Fin des fonctions ordinateur ------------------------------------------------------------------------------------------------------------------------------------------

# Fin des fonctions ordinateur ------------------------------------------------------------------------------------------------------------------------------------------

# Fin des fonctions ordinateur ------------------------------------------------------------------------------------------------------------------------------------------


jeu_de_depart=[['X','X','X','X','X','X','O'],['X','X','X','X','X','O','O'],['X','X','X','X','O','O','O'],['X','X','X',' ','O','O','O'],['X','X','X','O','O','O','O'],['X','X','O','O','O','O','O'],['X','O','O','O','O','O','O']]
jeu_milieu_de_partie=[['X','X','X','X','X','X','O'],['X',' ',' ',' ',' ',' ','O'],['X',' ',' ',' ',' ',' ','O'],['X',' ',' ',' ',' ',' ','O'],['X',' ',' ','X',' ',' ','O'],[' ',' ',' ','O','X','O','O'],['X','X','X','O','O','O','O']]
jeu_fin_de_partie=[['X',' ',' ','X',' ',' ',' '],[' ',' ',' ',' ','X','O',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ','O'],['X','O',' ','X','O','O','O']]
jeu_gagnant=[['X',' ',' ','X',' ',' ',' '],[' ',' ',' ',' ','X','O',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ','O'],[' ','O',' ','X','O','O','O']]
jeu_gagnant_O=[['X',' ',' ',' ',' ',' ','O'],['X','X',' ',' ',' ','O','O'],[' ',' ',' ',' ',' ',' ',' '],['X','X',' ',' ','O','O','O'],[' ',' ',' ','O','O','O','O'],[' ',' ',' ','O','O','O','O'],[' ',' ',' ','O','O','O','O']]
jeu_gagnant_X=[['X','X','X','X',' ',' ',' '],['X','X','X',' ','X',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ','O','O','O','O','O']]
# Les variables du jeu sont des listes de listes, chaque sous listes et une ligne, a l'interieur ce sont des varibles types str, qui contiennent ce que la fonction affichage va montrer.
# jeu gagnant est un jeu ou les pions X ont perdu (pratique pour certain test)

# Fonction qui lance tout les tests
# Les test des fonctions sont juste en dessous de la fonction qu'elle test 
def different_test():
    test_est_dans_grille()
    test_liste_cases_traverser()
    test_verification_elimination()
    test_verification_pion()
    test_elimination()
    test_verification_capture()
    test_fin_de_partie()
    print()         
    print("Tous les test se sont bien déroulé")       
    print()


# Code principale a 3 choix possibles: lancer le programme des tests ou jouer un tour avec 3 set de jeux différents ou jouer une partie complete, contre humain ou ordi
def code_principale():
    print("Si vous voulez lancer un tour de jeu       --> 1")
    print("Si vous voulez lancer la fonction de test  --> 2")
    print("Si vous voulez lancer une partie complete  --> 3")
    x=verifie_nombre()
    
    if x==1:
        print("Lancer un tour avec le jeu de début de partie   --> 1")
        print("Lancer un tour avec le jeu de milieu de partie  --> 2")
        print("Lancer un tour avec le jeu de fin de partie     --> 3")  # Il est possible de gagner en jouant ce jeu
        x=verifie_nombre()
        
        print('Joueur 1 aura les pions en forme de X et le joueur 2 les pions en forme de O')
        joueur='X'
        print('Au tour du joueur 1')
        if x==1:
            (lancer_tour(joueur,jeu_de_depart))
            x=0
        if x==2:
            (lancer_tour(joueur,jeu_milieu_de_partie))
            x=0
        if x==3:
            (lancer_tour(joueur,jeu_fin_de_partie))
            x=0
    if x==2:
        different_test()
    
    if x==3:
        print("Si vous voulez jouer contre un humain (ou vous même)  --> 1")
        print("Si vous voulez jouer contre l'ordinateur (c'est juste de l'aléatoire)  --> 2 ou 3")
        x=verifie_nombre()

        if x==2 or x==3:
            print("Lancer une partie avec le jeu de début de partie   --> 1")
            print("Lancer une partie avec le jeu de milieu de partie  --> 2")
            print("Lancer une partie avec le jeu de fin de partie     --> 3")  # Il est possible de gagner en un tour avec ce jeu
            x=verifie_nombre()
            if x==1:
                lancer_partie_ordi(jeu_de_depart)
                x=0
            if x==2:
                lancer_partie_ordi(jeu_milieu_de_partie)
                x=0
            if x==3:
                lancer_partie_ordi(jeu_fin_de_partie)
                x=0

        if x==1:
            print("Lancer une partie avec le jeu de début de partie   --> 1")
            print("Lancer une partie avec le jeu de milieu de partie  --> 2")
            print("Lancer une partie avec le jeu de fin de partie     --> 3")  # Il est possible de gagner en un tour avec ce jeu
            x=verifie_nombre()
            if x==1:
                (lancer_partie(jeu_de_depart))
                x=0
            if x==2:
                (lancer_partie(jeu_milieu_de_partie))
                x=0
            if x==3:
                (lancer_partie(jeu_fin_de_partie))
                x=0


# Tableau pratique avec les coordonnées autour:

                    #   1   2   3   4   5   6   7
                    #   A   B   C   D   E   F   G
jeu_milieu_de_partie=[['X','X','X','X','X','X','O'], #1
                      ['X','X',' ',' ','X','X',' '], #2
                      ['O',' ','O',' ',' ',' ',' '], #3
                      [' ',' ',' ',' ',' ',' ',' '], #4
                      [' ',' ',' ',' ',' ',' ',' '], #5
                      [' ',' ',' ',' ','O',' ',' '], #6
                      [' ',' ','O','O','O','O','O'], #7
                      ]
code_principale()


#print(lancer_tour_ordi('X',jeu_milieu_de_partie))


