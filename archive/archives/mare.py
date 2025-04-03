# -*- coding: utf-8 -*-  ## pour s'assurer de la compatibilté entre correcteurs
import random   #  pour tirage aleatoire   jeu joueur/ordi
random.seed()

"""
============ historique   du travail ===========================================
=========== MODIF faites ds l Atelier2 pour  atelier 3:
 -la dimension de la grille est fixe
 -j ai introduit une fonction de comptage des pions de chaque joueur (ne sert
    qu' a l initialisation des grilles; au cours du jeu, le nb de pions
     restants est actualisé lors des sauts)
 - les tests et affichages de l'atelier2  ont été  mis en commentaires
==========ATELIER 3
 - ajout de 2 grilles (config_test_deplacemnts et config_enchainement_sauts )
  pour les tests  deplacements et enchainement de saut

 - un tour de jeu   (on le realise que s'il reste au moins 6 pions de chaque couleur):
  1) on choisit une grille parmi les grilles définies ds le programme et un numero de joueur
  2) on choisit une case depart valide (case dans la grille et appartient au joueur)
    ds une liste de départ pourlesquels un mvt  (1 deplacement simple ou 1 saut) est possible
  3) le programme genere la liste des cases arrivees atteignables à partir de deplacements possibles
     (simple ou saut)  pour le joueur à partir de cette case depart
  4) 4a)si la liste est non vide: le  joueur choisit une de ces cases arrivees
         si choix  case arrivee par deplacement simple:
            mise a jour grille  et tour  fini
         si choix case arrivee  par saut:
            mise a jour de la grille
            definir case depart = case arrivee  (retour en 3) mais en  retentant UNIQUEMENT saut en 4)
            tour est fini quand plus de sauts possibles ou advesaire a moins de 6 pions
     4b)si la liste est vide et qu il n'a pas fait de saut: choix autre case depart (retour en 2)
       jusqu 'a deplacement possible   ou fin

==============MODIF faites ds atelier3 pour atelier 4:
- simplification de la fonction case_intermediaire pour calcul de case intermédiaire (si saut)
- modif choix de cases depart (pour le joueur "humain") :
-  ajout  "faire un  choix ds liste de cases disponibles" pour éviter temps reflexion choix case
 -amélioration des dialogues
"""
#____________CODE   RESULTANT   DES ATELIERS (eventuellement améliorés__________
#===============================================================================
# ##====     REPRESENTATION DES DONNEES ========================================
"""
variables  utilisées dans le programme:

n: dimension de la grille carrée -

pr: tableau de 2 entiers  représentant les pions restants
      pr[0] : nombre de pions restants (symbole '*') pour le joueur 1
              décroit de 24  à   >=5
      pr[1] : nombre de pions restants (symbole 'o') pour le joueur 2
              décroit de 24  à  >= 5
      fin de jeu quand pr[0]=5   ou pr[1] =5

grille: tableau nxn  de caractères '*', 'o'  et ' '
        grilles particulieres:
           config_init:   grille qui a la configuration du début du jeu
           config_milieu:  grille  environ milieu de jeu
           config_fin:     grille quelques coups avant la fin du jeu

joueur:entier, =1   joueur avec pions '*'
               =2   joueur  avec pions 'o'
"""

# --  initialisation des grilles et autres variables  de jeu -----------------
#==============================================================================
"""
Pour remplir les grilles nxn, i et j varient de 0 à n-1 inclus
pour affichage de  grille et aux opérations faisant intervenir   joueurs:
          i='A','B'...   et j=1,..n
"""
#=== fonctions pour passer d'une représentation à l'autre  des coordonnees des cases=
def coordonnees_entieres(case):
    """
     paramètre: case   chaine de caracteres lettre majuscule et chiffre
     retourne un tableau de 2 entiers, transformation de  case  en format
                       [i,j]  avec    0<= i < n   et  0<= j < n
    """
    return  [ord(case[0])-65,int(case[1])-1]
#==============================================================================
def coordonnees_lettrechiffre(case):
    """
     paramètre: case   format  [i,j]  avec    0<= i < n   et  0<= j < n
     retourne: case  chaine de caracteres lettre majuscule et chiffre
    """
    return  chr(case[0]+65) + str(case[1]+1)
#=============================================================================
def grille_vide(n):
    """   paramètre: n entier (dimension de la grille carree)
    valeur retournée:  tableau nxn réprésentant une  grille  de caractères vide:
    """
    grille = [[' ' for i in range(n)] for j in range(n)]
    return grille
#=============================================================================
def grille_init(n):   # grille  début jeu selon les règles
    """
    paramètre:    n entier (dimension de la grille carree) -
    valeur retournée: un tableau nxn réprésentant la grille au début du jeu
    grille[i][j]='*' (noir)   si  ( i+j < n-1)     ou   (i+j = n-1   et i >n//2)
                ='o' (blanc)  si  ( i+j > n-1)     ou   (i+j = n-1   et i <n//2)
    grille[n//2][n//2]=' '
    """
    grille = grille_vide(n)   # creation grille vide
    # placement des '*' et 'o' selon la definition de la grille initiale du jeu
    for i in range(n):
        for j in range(n):
            if i+j < n-1:
                grille[i][j] = '*'
            elif   i+j > n-1:
                grille[i][j] = 'o'
            else :   # i+j = n-1
                grille[i][j] = '*'  if i>=n//2 else 'o'
            if n % 2 == 1:
                grille[n//2][n//2]= ' '
    return grille
#=============================================================================
def placer_dans_ligne(ligne_grille,jdebut,jfin,jpas,symbole):
    """
    parametres ligne_grille  (tableau de caracteres): une ligne dans la grille
               jdebut,jfin,jpas  (entiers): colonnes j  jdebut<=j<jfin avec un pas jpas
               symbole (type caractere  '*' ou 'o')  a placer dans les cases (i,j)
    placement symbole ('*' ou  'o')  sur portion de ligne jdebut à jfin avec un pas jpas
    """
    for j in range(jdebut,jfin,jpas):
        ligne_grille[j] = symbole
#=============================================================================
def placer_dans_colonne(grille,j,idebut,ifin,ipas,symbole):
    """
    parametres  grille: une grille du jeu
                j  (entier): numero colonne dans la grille
               idebut,ifin,ipas  (entiers): lignes i  idebut<=i<ifin avec un pas ipas
               symbole (type caractere  '*' ou 'o')  a placer dans les cases (i,j)
    placement  symbole  ('*' ou  'o') sur  portion de colonne  idebut à ifin avec un pas ipas
;;;;;"""
    for i in range(idebut,ifin,ipas):
        grille[i][j] = symbole
#=============================================================================
def grille_milieu(n):
    """ grille milieu jeu
    paramètre: n entier (dimension de la grille carree)
    valeur retournée: un tableau nxn réprésentant la grille milieu jeu suivante

            0  1  2  3  4  5  6
         0  *  *  *        *
         1  *  *  *
         2        *     *                        15 pions '*'
         3           *  *  o  o                  15 pions 'o'
         4     *        o  o  o
         5  *  *     o  o  o  o
         6  *  o  o  o  o  o  o
    """
    grille = grille_vide(n)   # creation grille vide
    for i in range(2):    #pour (i,j)=(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)
        placer_dans_ligne(grille[i],0,3,1,'*')
    grille[0][5] = '*'
    placer_dans_ligne(grille[2],2,5,2,'*')  #pour (i,j)=(2,2),(2,4)
    placer_dans_ligne(grille[3],3,5,1,'*')  #pour (i,j)=(3,3),(3,4)
    placer_dans_ligne(grille[3],5,7,1,'o')  #pour (i,j)=(3,5),(3,6)
    placer_dans_colonne(grille,0,5,7,1,'*') #pour (i,j)=(5,0),(6,0)
    placer_dans_colonne(grille,1,4,6,1,'*') #pour (i,j)=(4,1),(5,1)
    placer_dans_ligne(grille[4],4,7,1,'o')  #pour (i,j)=(4,4),(4,5),(4,6)
    placer_dans_ligne(grille[5],3,7,1,'o')  #pour (i,j)=(5,3),(5,4),(5,5),(5,6)
    placer_dans_ligne(grille[6],1,7,1,'o')  #pour (i,j)=(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)
    return grille

#=============================================================================
def grille_fin(n):
    """ grille fin jeu (quelsques coups avant fin  du jeu)
    paramètre: n entier (dimension de la grille carree)
    valeur retournée: un tableau nxn réprésentant la grille proche de  fin suivante
            0  1  2  3  4  5  6
         0
         1              o
         2              o                         7 pions '*'
         3     *  *                              10 pions 'o'
         4  o
         5  *  *  o  o  o
         6  *  *  o  o  o  o  *
    """
    grille = grille_vide(n)   # creation grille vide
    placer_dans_colonne(grille,4,1,3,1,'o') #pour (i,j)=(1,4),(2,4)
    placer_dans_ligne(grille[3],1,3,1,'*')  #pour (i,j)=(3,1),(3,2)
    grille[4][0] = 'o'
    placer_dans_ligne(grille[5],2,5,1,'o')  #pour (i,j)=(5,2),(5,3),(5,4)
    placer_dans_ligne(grille[6],2,6,1,'o')  #pour (i,j)=(6,2),(6,3),(6,4),(6,5)
    for i in range(5,7):                    #pour (i,j)=(5,0),(5,1),(6,0),(6,1)
        placer_dans_ligne(grille[i],0,2,1,'*')
    grille[6][6]= '*'
    return grille
#==========================================================================
def grille_test_deplct(n):   # ajout atelier 3
    """
     retourne une grille pour tester la validité  des sauts et deplacements simples
    paramètre: n entier (dimension de la grille carree)
            0  1  2  3  4  5  6
         0  *           *
         1
         2           o  *  o                         6 pions '*'
         3        o  *  o                            6 pions 'o'
         4           o  o
         5     *
         6                    *
    """
    grille = grille_vide(n)   # creation grille vide
    grille[0] = ['*',' ',' ',' ','*',' ',' ']
    grille[2] = [' ',' ',' ','o','*','o',' ']
    grille[3] = [' ',' ','o','*','o',' ',' ']
    grille[4] = [' ',' ',' ','o','o',' ',' ']
    grille[5][1] = '*'
    grille[6][6] = '*'
    return grille
#=============================================================================
def grille_enchainement_saut(n):  # ajout atelier 3
    """
     retourne une grille pour tester la validité  des enchainements de sauts
    paramètre: n entier (dimension de la grille carree)
           1  2  3  4  5  6  F
      A
      B          o
      C          *  o     o                         8 pions '*'
      D       *     *     *  o                      9 pions 'o'
      E    *              o  *
      F                 o *  o
      G                 * o  o

    pour le joueur 2 (pions 'o', enchainement de sauts possibles:
          D7,D5,D3,D1,F1   en capturant les pions'*' en D6,D4,D2,E1
    (s'arretera en D1 car il ne restera plus que 5 pions '*')
    """
    grille = grille_vide(n)   # creation grille vide
    grille[1][2] = 'o'
    grille[2] = [' ',' ','*','o',' ','o',' ']
    grille[3] = [' ','*',' ','*',' ','*','o']
    grille[4] = ['*',' ',' ',' ',' ','o','*']
    grille[5] = [' ',' ',' ',' ','o','*','o']
    grille[6] = [' ',' ',' ',' ','*','o','o']
    return grille
# ======   bilan des pions (appelé en début  de partir)=======================
def comptage_pions(grille):
    """
    parametre: grille nxn de caracteres '*','o',' '
    retourne un tableau de  2 entiers pr   pr[0]: nb  pions  '*'  du joueur 1
                                           pr[1]: nb  pions 'o'   du joueur 2
    """
    pr=[0]*2
    n = len(grille[0])
    for i in range(n):
        for j in range(n):
            if grille[i][j] == '*':
                 pr[0] += 1
            elif grille[i][j] == 'o':
                 pr[1] += 1
    return pr

#=============================================================================
# ##====     REPRESENTATION GRAPHIQUE ========================================

def tracer_trait_horizontal(long):
    """
    paramètre: long (entier)   - le nombre de tirets qui composent la ligne
    trace  une trait horizontal composé de  tirets
    """
    print(" ",long * '-')

# ============================================================================
def afficher_ligne(x,ligne):
    """
    paramètres:   x : entier, code ASCII  d'une lettre majuscule
                  ligne:  tableau de caracteres (1 ligne de la grille)
    affiche 1 ligne  de la grille:   exemple pour la 1ere ligne: A|*|*|*|*|*|*|o|
    """
    n = len(ligne)
    print(chr(x), end='')        # chr(x) :  caractere  de code ASCII x
    for j in range(n):           # une ligne
            print ('|',ligne[j],end='')
    print('|')

# ===========================================================================
def afficher_grille(grille, joueur,pr):
    """
    paramètres: grille:  tableau  n x n  de caractères
                joueur: entier - prend la valeur 1 ou 2
                pr : tableau de 2 entiers
                     pr[0] : nombre de pions '*' restants au joueur 1
                     pr[1] : nombre de pions 'o'restants au joueur 2
    Pour afficher  dans 1ere colonne A,B, C,...on utilise :
         ord(caractere) :  code ASCII de la variable caractère
         chr(numero) :  caractere  correspondant au code ASCII 'numéro'

    affiche  grille selon la représentation de gauche de
        la figure 1  proposée  à la page 2 des consignes de l'Atelier 2
    """
    x = ord('A')          # code ASCII de 'A'
    n = len(grille[0])       # nombre de lignes  et colonnes de la grille

    ligne1 = [i for  i in range(1,n + 1)]  # pour afficher la ligne 1 2 ... n
    print('', end=' ')
    for j in range(n):
        print (' ',ligne1[j],end='')
    print()
    tracer_trait_horizontal(3*n)            # trait horizontal
    for i in range(n):   #  une ligne du  tableau
        afficher_ligne(x, grille[i])
        tracer_trait_horizontal(3*n)     # un trait horizontal
        x = x+1 # donnera la lettre majuscule suivante à partir du code ASCII x
    print()
    print('le joueur 1  a encore ',pr[0], ' pions * ')
    print('le joueur 2  a encore ',pr[1], ' pions o ')
    if pr[0]  <6    or  pr[1] < 6:
         print("partie finie - un  joueur a moins de 6 pions")
    else:
        print("C'est au tour  du joueur ", joueur)
    print(80* '*')   #  écriture ligne séparatrice composée d'étoiles

# ##====     PARTIE TESTS======================================================
#=======     fonctions de  test===============================================
def  test_affichage():
    """validation de la fonction d' affichage   sur un  carré 3x3"""
    print(" test affichage d'une grille  test 3 x 3")
    tab=[['o',' ','*'],['o','*','o'],['*','o','o']]
    afficher_grille(tab,1,[3,5])
#===========================================================================
def  test_affichage_grilles(n):
   print("grille  de départ du jeu Maré")
   afficher_grille(config_init,1, comptage_pions(config_init))
                 # grille de depart, numero du joueur, nb pions restant de chaque couleur
   print("grille milieu du jeu Maré")
   afficher_grille(grille_milieu(n),1,comptage_pions(config_milieu))
   print("grille  vers fin jeu Maré")
   afficher_grille(grille_fin(n),2,comptage_pions(config_fin))
   print("grille  pour test deplacements")
   afficher_grille(grille_test_deplct(n),1,comptage_pions(config_test_deplacemnts))

# ====  2   grilles   supplémentaires pour tester   le programme  =================
def  grille_pour_test_depl_simple(n):   #   pour fonction de test
    """
    grille apres  deplacement simple D3 à D4  sur  config_fin
    """
    grille =  grille_fin(7)
    grille[3][2] =' '  # le pion  '*' a quitte D3
    grille[3][3] ='*'  # il va en D4
    return grille
#=============================================================================
def  grille_pour_test_depl_saut(n):    #  pour fonction de test
    """
    grille apres saut  F1 à D1 sur  onfig_fin  (apres un  test deplacement  D3 à D4)
    """
    grille =  grille_fin(7)
    grille[5][0] =' '  # le pion '*'  a quitte F1
    grille[3][0] ='*' #  il va en D1
    grille[4][0] =' '  #  prise du   pion 'o' en E1
    return grille
#===========================================================================
def test_est_au_bon_format():
    """   True si 2 caracteres:  1er =lettre majuscule , 2ieme=chiffre
    """
    assert est_au_bon_format('ab1')== False, ">2 caractères"
    assert est_au_bon_format('a')  == False, "<2 caractères"
    assert est_au_bon_format('11') == False, "1er caractère n'est pas lettre majuscule"
    assert est_au_bon_format('Ab') == False, "2ieme   caractère n'est chiffre"
    assert est_au_bon_format('b4') == False, "1er caractère n'est pas lettre majuscule"
    assert est_au_bon_format('B4') == True,  "bon format"
#===========================================================================
def test_est_dans_grille():
    """
    est_dans_grille(l,c,n) True si  'A'<= l <chr(ord(A)+n-1)  et 0< int(c) <=n

    """
    assert est_dans_grille('B','3',7) == True, " est dans grille"
    assert est_dans_grille('L','3',7) == False, "ligne hors grille"
    assert est_dans_grille('A','0',7) == False, "colonne hors grille"
    assert est_dans_grille('C','8',7) == False, "colonne hors grille"
    assert est_dans_grille('S','9',7) == False, "ligne et colonne hors grille"
    #print("test_est_dans_grille  OK")
#==============================================================================
def test_coordonnees_entieres():
    assert coordonnees_entieres('A1')==[0,0], " bonne transformation"
    assert not coordonnees_entieres('B2')==[0,1], " mauvaise ligne"
    assert not coordonnees_entieres('B3')==[1,3], " mauvaise colonne"
    #print("test_coordonnees_entieres  OK")
#==============================================================================
def test_appartient_case_joueur():
    config_init = grille_init(7)
    assert appartient_case_joueur(coordonnees_entieres('A1'),config_init,1)==True, "case appartient joueur"
    assert appartient_case_joueur(coordonnees_entieres('D4'),config_init,1)==False, "case vide"
    assert appartient_case_joueur(coordonnees_entieres('G7'),config_init,1)==False, "case appartient à l'autre joueur"
    #print("test appartient_case_joueur OK")
#==============================================================================
def  test_distance():
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('C3'))==[0,0], "cases depart  et arrivee identiques"
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('B3'))==[-1,0], "deplacement simple vers haut"
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('D3'))==[1,0], "deplacement simple vers bas"
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('C4'))==[0,1], "deplacement simple vers droite"
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('C2'))==[0,-1], "deplacement simple vers gauche"
    assert distance(coordonnees_entieres('C5'),coordonnees_entieres('D6'))==[1,1], "deplacement bas et  droite - non valide"
    assert distance(coordonnees_entieres('C3'),coordonnees_entieres('A3'))==[-2,0], "saut vers haut"
    #print("test distance OK pour cases depart et arrivée valides")
#==============================================================================
def  test_case_vide():

    assert  case_vide(coordonnees_entieres('D4'),grille_init(7))== True,  "case  vide de la grille initiale"
    assert  case_vide(coordonnees_entieres('D7'),grille_milieu(7))== False,  "case  non  vide de la grille milieu"
    assert  case_vide(coordonnees_entieres('D3'),grille_fin(7))== False,  "case  non  vide de la grille fin"
    #print("test case vide OK")
#==============================================================================
def  test_comptage_pions():
    assert  comptage_pions(grille_init(7))==[24,24],  "test sur grille config_init"
    assert  comptage_pions(grille_milieu(7))==[15,15],  "test sur grille config_init"
    assert  comptage_pions(grille_fin(7))==[7,10],  "test sur grille config_init"
    #print("test comptage_pions ok")
#==============================================================================
def  test_case_intermediaire():
    assert case_intermediaire([0,1],[2,0])==[1,1],  'decalage 1 vers bas'
    assert case_intermediaire([3,1],[-2,0])==[2,1],  'decalage 1 vers haut'
    assert case_intermediaire([3,3],[0,2])==[3,4],  'decalage 1 vers droite'
    assert case_intermediaire([3,3],[0,-2])==[3,2],  'decalage 1 vers gauche'
    #print("test case_intermediaire ok ")
#==============================================================================
def  test_deplacements_simples_possibles():
    grille =  grille_milieu(7)
    assert deplacements_simples_possibles('D4',grille) == 'C4,E4,D3', 'case droite occupee'   #chaine HautBasGaucheDroite
    assert deplacements_simples_possibles('A1',grille) == '', 'en bord  gauche et haut, occupees bas et droite'
    assert deplacements_simples_possibles('D7',grille) == 'C7', 'en bord  droit, occupees bas et gauche'
    grille = grille_test_deplct(7)
    assert deplacements_simples_possibles('F2',grille) == 'E2,G2,F1,F3', 'cases haut, bas, gauche, droit accessibles'
    assert deplacements_simples_possibles('A1',grille) == 'B1,A2', 'angle haut gauche'
    assert deplacements_simples_possibles('G7',grille) == 'F7,G6', 'angle bas droit'
    assert deplacements_simples_possibles('D3',grille) == 'C3,E3,D2', 'droit occupé'
    assert deplacements_simples_possibles('D4',grille) == '', 'bas haut gauche et droit occupés'
    #print("test deplacements_simples_possibles ok")
#==============================================================================
def  test_sauts_possibles():
    assert sauts_possibles('B3',grille_milieu(7),1) == '', 'cases inaccesibles ou case intermediaire occupee par joueur' #chaine HautBasGaucheDroite
    grille = grille_fin(7)
    assert sauts_possibles('F1',grille,1) == 'D1', 'saut possible vers le haut'
    assert sauts_possibles('C5',grille,2) == '', 'cases intermediaires vides ou occupées par joueur'
    grille = grille_test_deplct(7)
    assert sauts_possibles('D4',grille,1) == 'B4,F4,D2,D6', 'sauts possibles ds les 4 directions'
    assert sauts_possibles('D3',grille,2) == '', 'sauts impossibles ds les 4 directions'
    assert sauts_possibles('G7',grille,1) == '', 'angle bas droit et sauts impossibles ds les 2 autres directions'
    assert sauts_possibles('C5',grille,1) == 'C3,C7', ' sauts impossibles haut et bas'
    #print("test sauts_possibles ok")
#==============================================================================
def  test_mise_a_jour_depl_simple():
    grille_apres = grille_pour_test_depl_simple(n)
    assert mise_a_jour_depl_simple('D3','D4',grille_fin(7),1)==grille_apres, 'erreur mise à jour deplacement simple'
    #print("test mise_a_jour_depl_simple:  ok")
#==============================================================================
def  test_mise_a_jour_depl_saut():
    pr=[7,10]
    grille_apres = grille_pour_test_depl_saut(n)
    assert mise_a_jour_depl_saut('F1','D1',grille_fin(7),1,pr)==(grille_apres,[7,9]), 'erreur mise à jour saut'
    #print("test mise_a_jour_depl_saut:  ok")
#==============================================================================
def  test_test_fin_partie():
    assert test_fin_partie([12,24])==False, 'les 2 joueurs ont au moins 6 pions'
    assert test_fin_partie([5,10])==True, 'le  joueur 1 a moins de 6 pions'
    assert test_fin_partie([13,5])==True, 'le  joueur 2 a moins de 6 pions'
    #print("test test_fin_partie OK")
#=============================================================================
def tour_de_jeu_joueur_impose(grille,pr):  # pour test enchainement de sauts
    """
    parametres : grille nxn
                  pr: pr[0] nb de pionsrestants joueur 1, pr[1] nb pions restant  joueur 2
    organise un enchainement sauts du joueur 2 à partir de case D7
    """
    saut = 0  # saut vaudra 1   dès que lon a validé un 1er saut;
              #seul un enchainement de  sauts sera possible
    joueur = 2  #   test se fait sur joueur 2
    depart = 'D7'
    fin =  False
    while not  fin   :  # le joueur peut jouer
        if saut == 1:    # on enchaine un saut    sur la case d'arrivee
              depart = arrivee
        choix1,choix2 = choix_arrivee(depart,grille,joueur)
        if   choix2=='[]' or  test_fin_partie(pr):
            fin = True  # le joueur ne peut plus enchainer de sauts
            print("fin des sauts  du joueur")
        else:    #  enchainement de sauts
            arrivee =  choix_saut(choix2)
            print("saut joueur 2    depart:",depart,"  arrivee:",arrivee)
        if not fin: #  deplacement sur case arrivee et mise à jour de la grille
            saut,fin, pr = mise_a_jour(depart,arrivee,grille,pr,joueur,choix1,choix2,saut,fin)
    newjoueur = 1     # le joueur 2 a joué; c'est au joueur 1
    return (grille,newjoueur,pr)
#===============================================================================
def validation_enchainement_sauts():
    """
    pour le joueur 2 (pions 'o'), enchainement de sauts possibles:
          D7,D5,D3,D1,F1   en capturant les pions'*' en D6,D4,D2,E1
    (s'arretera en D1 car il ne restera plus que 5 pions '*'
    """
    grille = grille_enchainement_saut(n)
    pr = comptage_pions(grille)
    print("avant le tour du joueur:")
    afficher_grille(grille,2,pr)
    print("le joueur 2 ('o') joue; departs successifs D7, D5, D3, D1 pour succession de sauts")
    grille,joueur,pr = tour_de_jeu_joueur_impose(grille,pr) # le tour d'un joueur
    print("apres le tour du joueur:")
    afficher_grille(grille,joueur,pr)   # affichage apres le tour du joueur
#===============================================================================
def test_coordonnees_lettrechiffre():
    assert coordonnees_lettrechiffre([0,0])=='A1', 'case haut, gauche'
    assert coordonnees_lettrechiffre([6,6])=='G7', 'case bas, droit'
    assert coordonnees_lettrechiffre([3,3])=='D4', 'case milieu'
    #print("test coordonnees_lettrechiffre OK")
#===============================================================================
def test_possibilites_tour_de_jeu_ordi():
    config_fin = grille_fin(n)
    resultat = [['D2', 'C2,E2,D1', ''], ['D3', 'C3,E3,D4', ''], ['F1', '', 'D1'], ['F2', 'E2', ''], ['G7', 'F7', '']]
    assert possibilites_tour_de_jeu_ordi(config_fin,1)== resultat, 'test config_fin , joueur 1'
    config_fin = grille_fin(n)
    resultat = [['B5', 'A5,B4,B6', ''], ['C5', 'D5,C4,C6', ''], ['E1', 'D1,E2', ''], ['F3', 'E3', ''], ['F4', 'E4', ''], ['F5', 'E5,F6', ''], ['G6', 'F6', '']]
    assert possibilites_tour_de_jeu_ordi(config_fin,2)== resultat, 'test config_fin , joueur 2'
    #print("possibilites_tour_de_jeu_ordi ok")
#===============================================================================
def test_liste_choix_ordi():
    possibilites = [['B5', 'A5,B4,B6',''], ['C5', 'D5,C4,C6', ''], ['E1', 'D1,E2', ''], ['F3', 'E3', ''], ['F4', 'E4', ''], ['F5', 'E5,F6', ''], ['G6', 'F6', '']]
    choix_simple =  [('B5', 'A5'), ('B5', 'B4'), ('B5', 'B6'), ('C5', 'D5'), ('C5', 'C4'), ('C5', 'C6'), ('E1', 'D1'), ('E1', 'E2'), ('F3', 'E3'), ('F4', 'E4'), ('F5', 'E5'), ('F5', 'F6'), ('G6', 'F6')]
    choix_saut = []
    assert(liste_choix_ordi(possibilites))== (choix_simple, choix_saut), ' validte joueur2 config_fin'
    possibilites = [['D2', 'C2,E2,D1', ''], ['D3', 'C3,E3,D4', ''], ['F1', '', 'D1'], ['F2', 'E2', ''], ['G7', 'F7', '']]
    choix_simple =  [('D2', 'C2'), ('D2', 'E2'), ('D2', 'D1'), ('D3', 'C3'), ('D3', 'E3'), ('D3', 'D4'), ('F2', 'E2'), ('G7', 'F7')]
    choix_saut = [('F1', 'D1')]
    assert(liste_choix_ordi(possibilites))== (choix_simple, choix_saut), ' validte joueur1 config_fin'
    #print("liste_choix_ordi  ok")
#===============================================================================
def test_complete_choix():
    assert(complete_choix('A5','B5,A6',[]))==[('A5','B5'),('A5','A6')], "depart liste vide"
    avant = [('A5','B5'),('A5','B6')]
    apres =  [('A5','B5'),('A5','B6'),('C2','C1'),('C2','C3'),('C2','D2')]
    assert(complete_choix('C2','C1,C3,D2',avant))== apres, "depart liste  non vide"
   # print("complete_choix ok")
#============================================================================
#=========   execution des tests    ===========================================

def  generale_tests():
  print("Vous commencez les tests - certains demandent des réponses du joueur")
  test_affichage()           #  verification sur grille 3x3
  test_affichage_grilles(7)  #  verification des grilles
  test_est_au_bon_format()   #  mise au point atelier2
  test_est_dans_grille()     #   mise au point atelier2
  #  atelier 3
  test_coordonnees_entieres()
  test_appartient_case_joueur()
  test_distance()
  test_case_vide()
  test_comptage_pions()
  test_case_intermediaire()
  test_deplacements_simples_possibles()
  test_sauts_possibles()
  test_mise_a_jour_depl_simple()
  test_mise_a_jour_depl_saut()
  test_test_fin_partie()
  validation_enchainement_sauts()
  #  atelier 4, 5
  test_coordonnees_lettrechiffre()
  test_possibilites_tour_de_jeu_ordi()
  test_liste_choix_ordi()
  test_complete_choix()
  print("=========   tous les  tests ok   ==============")

# ##====     PETITES FONCTIONS  DE VERIFICATION ============================
#===========================================================================
def est_au_bon_format(message):
    """
    parametre:  message:  case  format chaine de 2 caractères (majuscule+chiffre)

    retourne True  si len(message)==2  et le format est: lettre majuscule+ chiffre
    """
    if len(message) != 2 :  # on doit saisir 2  caractères
        return False
    if message[0] < 'A' or  message[0] > 'Z': # n'est pas une lettre majuscule
        return False
    if message[1] < '0' or  message[1] > '9': # n'est pas un caractere representant un chiffre
        return False
    return True
#=============================================================================
def est_dans_grille(rep0,rep1,n):
    """ paramètres rep0:  type str, lettre majuscule  numero  de ligne
                   rep1:  type str, chiffre  numero  de colonne
                   n:  dimension d'une grille carree
     retourne True  si case reperee par rep0 et rep1   est dans  grille:
    """
    col = int(rep1)                     # on doit avoir 0<col<=n
    lettre_max = chr(ord('A') + n -1)   # ligne doit varier de A à lettre_max inclus
    return  rep0 >= 'A'  and rep0 <= lettre_max   and   col >0   and    col<=n

#=============================================================================
# ## ===================  SAISIE =============================================
def saisir_coordonnees(grille):
    """
    paramètre: grille:    grille carrée

    valeur retournee: les coordonnees (valides) d'une case
          format: lettre majuscule  (A,B...) suivie d'un chiffre (1...n) exemple: B3
    """
    n = len(grille[0])  #  dimension de la grille carree nxn
    l_max = chr(ord('A') + n -1)   # ligne doit varier de A à l_max
    doit_saisir = True
    while doit_saisir:  #True   tant que  joueur ne donne pas  de bonnes coordonnées
       #  utilisation fstring : valeurs de l_max et n  affichées  pour guider le joueur
       reponse = input(f"entrez 1 lettre majuscule A..{l_max} suivie d'1 chiffre de 1 à {n} (exemple: B3) - ma reponse:")
       doit_saisir  = not est_au_bon_format(reponse)
       if  doit_saisir == False: # si format ok   on verifie appartenance grille
           doit_saisir = not est_dans_grille(reponse[0],reponse[1],n)
       if doit_saisir: #  le joueur recommence la saisie
          print("erreur de saisie -  hors grille  ou mauvais format - recommencez")
    return reponse
#===============================================================================
def chercher_case_depart_joueur(grille,joueur):
    """
    parametres   grille:la grille nxn de caracteres
                 joueur=1 (pions '*')   ou 2 (pions 'o')
    retourne une case de depart appartenant  au joueur  (format lettre majuscule+chiffre)
    """
    ma_liste = possibilites_depart_humain(grille,joueur)
          # liste cases appartenant au joueur à partir desquelles un deplacement  possible
    valide = False
    c = '*'  if joueur ==1    else 'o'
    while not  valide:   # recherche iterative d'une case appartenant au joueur
        print(f" choisir case depart  (qui contient  {c}) dans  {ma_liste}")
        case = saisir_coordonnees(grille) #  bon format, case dans grille
        valide =  case  in ma_liste
        if not valide:
            print(" choisissez  dans liste fournie")
    #print("la case  est dans la grille et appartient au joueur")
    return case
#===============================================================================
def choix_simple_ou_saut(choix1,choix2):
    """
    parametres: choix1:  cases arrivees possibles par deplacement simple
                choix2:  cases arrivees possibles par saut
    retourne une case arrivee format lettre+chiffre   choisie  dans choix1 ou choix2
    """
    arrivee=input(f" choisir  case arrivee dans {choix1} (deplacement simple) ou dans {choix2} (saut) - ma reponse:")
    while arrivee not in choix1  and  arrivee not in choix2:
       print("erreur saisie - recommencez")
       arrivee = input(f" choisir  une case arrivee dans {choix1} (deplacement simple)  OU  dans {choix2} (saut) - ma reponse :")
    return arrivee
#===============================================================================
def choix_saut(choix2):
    """
    parametres:  choix2:  cases arrivees possibles par saut
    retourne une case arrivee format lettre+chiffre   choisie  dans  choix2
    """
    arrivee = input(f" choisir une case arrivee dans {choix2}  (saut) - ma reponse:")
    while arrivee  not in choix2:
        print("erreur saisie - recommencez")
        arrivee = input(f" choisir une case arrivee dans  {choix2}  (saut)  - ma reponse:")
    return arrivee
#===============================================================================
# ## ===================  DEPLACEMENTS==========================================
#==== fonctions sur l'occupation des cases =================================
def case_vide(case,grille):
    """
    parametres: case: case    en format  [i,j] 0<= i < n   et  0<= j < n
                grille: un grile de jeu nxn
     retourne True si   case de la  grille contient  " " (case non occupee)
     """
    return  grille[case[0]][case[1]] == ' '
#==========================================================================
def appartient_case_joueur(case,grille,joueur):
    """
      case: position ds  grille   dans  format   [i,j] 0<= i < n   et  0<= j < n
      grille: tableau nxn de caracteres;  la grille de jeu considérée
      joueur:  numero du joueur  =1 si pions '*', =2 si pions 'o'
    retourne True si case  appartient au joueur  si non False
    """
    i = case[0]
    j = case[1]
    return  (joueur==1  and grille[i][j]=='*')  or (joueur==2  and grille[i][j]=='o')
#==================================================================================
# == fonctions sur positions  cases arrivee, depart,  intermediaire (si  saut) ===
def distance(depart,arrivee):
    """
    parametres:
         depart et arrivee:   cases depart et arrivee  sous le format [i,j]
                        [i,j] 0<= i < n   et  0<= j < n
    retourne  tableau de 2 entiers: 1ere coordonnee: distance entre  lignes des 2 cases
                                   2ieme coordonnee: distance entre  colonnes des 2 cases

    selon les règles: si la distance depart-arrivee n'est   pas une des valeurs  suivantes
        [1,0], [-1,0], [0,1], [0,-1]   pour deplacement simple
        [2,0], [-2,0] [0,2], [0,-2]    pour saut
    alors la case arrivee n'est pas atteignable à partie de la case depart
    """
    return  [arrivee[0] -  depart[0], arrivee[1] -  depart[1]]
#=============================================================================
def case_intermediaire(depart,distance):
    """
    paramètres
      depart:  case de depart  sous le format [i,j]  [i,j] 0<= i < n  et  0<= j < n
      distance: un élément  des distances possibles ([-2,0],[2,0],[0,-2],[0,2] correspondant
                     à saut vertical haut ou bas,saut horizontal gauche ou droite
    retourne les coodonnées en format [i,j]   0<= i < n   et  0<= j < n
                de la case intermediaire   qui sera sautée
    """
    return [depart[0] + distance[0]//2,  depart[1] + distance[1]//2]
# ================   etude des deplacements   ===============================
def possibilites_depart_humain(grille,joueur):
    """
    parametres: grille nxn tableau de caracterees 'o','*'  et ' '
                joueur = 1  (pions '*')   ou 2   pions 'o')
    retourne liste cases depart du joueur a partir desquelles un tour de jeu est possible
              format: [depart1,depart2,,...],  chaque depart  dans format type 'B5'
    """
    possibilites = []
    n=len(grille[0])
    for i in range(n):
       for j in range(n):
            if appartient_case_joueur([i,j],grille,joueur):
                depart = coordonnees_lettrechiffre([i,j]) #case en format lettre chiffre
                choix1 = deplacements_simples_possibles(depart,grille)
                choix2 = sauts_possibles(depart,grille,joueur)
                if choix1 !='' or choix2 != '':
                     possibilites.append(depart)
    return possibilites
#=============================================================================
def mise_a_jour_depl_simple(depart,arrivee,grille,joueur):
    """
    parametres  depart, arrivee  coordonnes des cases  depart et   arrivee
                          format  lettre majuscumle + chiffre
                grille: tableau nxn de caractères '*','o'   et ' '
                joueur =1   si pions '*',  =2   si pions 'o')
    met a jour   cases depart et arrivée  lors d'un deplacemnt simple de joueur
    """
    [i,j] = coordonnees_entieres(depart)
    grille[i][j]= ' '
    [i,j] =  coordonnees_entieres(arrivee)
    grille[i][j] = '*'  if joueur==1   else 'o'
    return grille
#=============================================================================
def mise_a_jour_depl_saut(depart,arrivee,grille,joueur,pr):
    """
    parametres  depart, arrivee   cases  depart et   arrivee
                          format chaine de caracteres lettre majuscumle + chiffre
                grille: tableau nxn de caractères '*','o'   et ' '
                joueur =1   si pions '*', =2   si pions 'o')
                pr: tableau de 2 entiers , pions restants au joueur 1 et au joueur 2
    met a jour   cases depart, arrivée, case sautée, pions restants   lors d'un saut
    """
    mise_a_jour_depl_simple(depart,arrivee,grille,joueur)
    #  l'adversaire perd le  pion de  la case sautée
    distant = distance(coordonnees_entieres(depart),coordonnees_entieres(arrivee))
    case_sautee = case_intermediaire(coordonnees_entieres(depart),distant)
    grille[case_sautee[0]][case_sautee[1]] = ' '
    adversaire =  1 if joueur==2  else 2
    pr[adversaire - 1] -= 1
    return (grille,pr)
#==============================================================================
def  mise_a_jour(depart,arrivee,grille,pr,joueur,choix1,choix2,saut,fin):
    """
    parametres  depart, arrivee: cases depart et  arrivee en format lettre+chiffre
                choix1  chaine str    - cases arrivees possibles par deplacement simple
                choix2  chaine str    - cases arrivees possibles par saut
               saut=0  deplacement simple 'et fin des deplacements du joueur
                   =1   saut
                fin booleen ; True si fin deplacement sinon False
    fait la mise  à jour de la grille apres le deplacement
    """
    if arrivee in choix1  and  saut==0:  # deplacement simple
        mise_a_jour_depl_simple(depart,arrivee,grille,joueur)
        fin = True
        print("le joueur a fait son deplacement simple")
    elif arrivee in choix2:  #  saut
        mise_a_jour_depl_saut(depart,arrivee,grille,joueur,pr)
        saut =1
    return saut, fin, pr

#=============================================================================
def  deplacements_simples_possibles(case,grille):
    """
     case:   case de départ ds grille - format lettre majuscule+chiffre
     grille: grille nxn    de caracteres '*', 'o' et ' '
     retourne chaine de caracteres (choix) donnant cases d'arrivee  (au max 4)
           atteignables en  1 deplacement simple
           (format exemple:   A1,A3,B2  si 3 cases atteignables
    """
    I = ord(case[0])   #I, J servent à definir case d'arrivee en format lettre+chiffre
    J= int(case[1])
    [i,j] = coordonnees_entieres(case)  #( dans 0...n-1)
    choix = ""
    n = len(grille[0])
    if i >=1  and grille[i-1][j] == ' ':   # deplacement haut
        choix +=  chr(I-1) + case[1]
    if i <n-1  and  grille[i+1][j] == ' ':  #  deplacement bas
        if choix != "":
             choix += ','
        choix += chr(I+1) + case[1]
    if j >= 1  and  grille[i][j-1] == ' ':  # deplacement gauche
        if choix != "":
             choix += ','
        choix += case[0] + str(J-1)
    if j < n-1 and  grille[i][j+1] == ' ':  # deplacementdroite
        if choix != "":
            choix += ','
        choix += case[0] + str(J+1)
    return choix
#============================================================================
def  sauts_possibles(case,grille,joueur):
    """
     case:   case de départ ds grille - format lettre majuscule+chiffre
     grille: grille nxn    de caracteres '*', 'o' et ' '
     joueur =1   si pions '*',  =2   si pion 'o'
     retourne chaine de caracteres (choix) donnant les cases arrivee  (au max 4)
        atteignables en 1 saut (arrivee vide et  intermediaire  occupee par adversaire)
        (en format du   type A1,A3,B2  si 3 cases possibles )
    """
    I = ord(case[0])   #  I, J   servent à definir la case d'arrivee en format lettre+chiffre
    J= int(case[1])
    [i,j] = coordonnees_entieres(case)  #( dans 0...n-1)
    n = len(grille[0])
    adversaire = 1 if joueur == 2  else 2
    choix = ""
    if i >=2  and grille[i-2][j] == ' ' and  appartient_case_joueur([i-1,j],grille,adversaire) :
        choix +=  chr(I-2) + case[1]
    if i <n-2  and grille[i+2][j] == ' ' and appartient_case_joueur([i+1,j],grille,adversaire):
        if choix != "":
          choix += ','
        choix += chr(I+2) + case[1]
    if j >= 2  and grille[i][j-2] == ' ' and appartient_case_joueur([i,j-1],grille,adversaire):
        if choix != "":
          choix += ','
        choix +=  case[0] +  str(J-2)
    if j < n-2  and grille[i][j+2] == ' '  and  appartient_case_joueur([i,j+1],grille,adversaire):
        if choix != "":
          choix += ','
        choix += case[0] + str(J+2)
    return choix
#=============================================================================
def choix_arrivee(depart,grille,joueur):
    """
    parametres: depart   case de depart formet lettre majuscule + chiffre
    grille: grille nxn de caracteres '*','o',' '
    joueur : =1   si pions '*',  =2   si pion 'o'
    retourne:
      - choix1  (format [A1,....]) :  cases arrivees atteignables par deplacement simple
      - choix2  (format[B1,....]) ;   cases arrivee atteignables par saut
    """
    choix1 =  '['+deplacements_simples_possibles(depart,grille)+']'
    choix2 = '[' + sauts_possibles(depart,grille,joueur) +']'
    return choix1,choix2
#=============================================================================
#==========       PARTIE JEU    =============================================
#============   joueur/joueur ==============================================
def tour_de_jeu_joueur(grille,joueur,pr):
    """
    parametres : grille nxn
                joueur =1   si pions '*', =2   si pions 'o'
                pr: pr[0]=nb de pions restants joueur 1, pr[1]=nb pions restant  joueur 2
    organise un tour de jeu du joueur:
            1 deplacement simple   ou un enchainement   de sauts tant que c'est possible
            stopper le mvt si fin de jeu
    """

    saut = 0  # saut vaudra 1   dès que lon a validé un 1er saut;
              #seul un enchainement de  sauts sera possible
    fin =  False
    while not  fin   :  # le joueur peut jouer
        if saut == 0:
            depart   = chercher_case_depart_joueur(grille,joueur)
        else: # on enchaine un saut    sur la case d'arrivee
            depart = arrivee
        choix1,choix2 = choix_arrivee(depart,grille,joueur)
        if choix1=='[]' and  choix2=='[]':
            if saut == 1 : # le joueur a deja fait un saut et ne peut plus en faire
                fin = True  # le joueur ne peut plus enchainer de sauts
                print("fin des sauts  du joueur")
            #else : # le joueur n a pas encore joue
            #    print("pas de  deplacement possible  - choisir une autre case depart")
        else:    # choisir un deplacemt qq ou un enchainement de sauts si saut =1
            if saut==0: # choix deplacement simple ou saut
                arrivee = choix_simple_ou_saut(choix1,choix2)
                print("joueur:",joueur,"  depart:",depart,"  arrivee:",arrivee)
            else: #  on a deja fait un saut -  on tente un enchainement de sauts
                if choix2=='[]'  or test_fin_partie(pr): #enchainement impossible ou fin_partie
                    fin = True
                    print("le joueur ne peut plus  sauter")
                else: # on peut continuer les sauts'
                    arrivee =  choix_saut(choix2)
                    print("joueur:",joueur,"  depart:",depart,"  arrivee:",arrivee)
            if not fin: #  deplacement sur case arrivee et mise à jour de la grille
                saut,fin,pr = mise_a_jour(depart,arrivee,grille,pr,joueur,choix1,choix2,saut,fin)
    newjoueur = 2  if joueur==1  else 1    # le joueur a joué; c'est à son adversaire
    return (grille,newjoueur,pr)
#===============================================================================
def jeu_joueur_joueur(grille):
   """ paramètre   grille tableau nxn de caracteres ' ', '*', 'o'
   fait une partie entre 2 joueurs   """
   joueur = ' '
   while joueur not in ['1','2']:
       joueur = input("choisir le joueur 1   (pions '*')  ou le joueur 2 (pions 'o') - ma réponse: ")
   joueur = int(joueur)
   pr = comptage_pions(grille)
   print("avant le tour du joueur ",joueur)
   afficher_grille(grille,joueur,pr)
   while  not test_fin_partie(pr):  # la partie n 'est pas finie, on  fait jouer 1 joueur
      grille,joueur,pr = tour_de_jeu_joueur(grille,joueur,pr) # le tour d'un joueur
      print("apres le tour du joueur")
      afficher_grille(grille,joueur,pr)   # affichage apres le tour du joueur
   print(" le joueur 1  a ",pr[0], " pions  *, le joueur 2  a ",pr[1]," pions o;  la partie est finie ")
   vainqueur = 2 if pr[0] <6   else 1
   print( " le joueur ", vainqueur, "  a  gagné")
# =======   test    fin de partie   ===========================================
def test_fin_partie(pr):
    """
    parametre: pr  tableau  de dimension 2  du nb de pions restant à chaque joueur
    retourne True si un des 2 joueurs a moins de 6 pions
    """
    return pr[0] < 6    or   pr[1] < 6
#============================================================================
def menu_utilisateur():
   """ retourne 2 entiers   rep1 (=1 ou 2)  choix joueur/joueur   ou joueur/ordi
                            rep2   =1   ou part de la grille début
                                   =2   on part de la grille  milieu
                                   =3   on part de la grille fin
   """
   rep1 =  rep2 = ''
   while rep1 not in {'1','2'}:
       rep1  =  input("choisir  jeu joueur/joueur: taper 1    OU    jeu joueur/ordi: taper 2 - ma réponse:")
   while rep2 not in {'1','2','3'}:
       rep2  =  input("choisir  grille debut: taper 1   OU  grille milieu: taper 2   OU  grille fin: taper 3 - ma réponse:")
   return  int(rep1), int(rep2)
#===============================================================================
#=========== partie  joueur/ordi               =================================
def possibilites_tour_de_jeu_ordi(grille,joueur):
    """
    version naive  - paragraphe 2.3   enoncé atelier 4
    parametres : grille nxn
                  joueur =1   si pions '*', =2   si pions 'o'
    retourne les possibilites de jeu à partir  de chaque case depart possible du joueur
    format: [[depart1,depl_simples,sauts],[depart2,depl_simples,sauts],...]
          depart1    sous le format   de type 'B5'
          depl_simples (cases atteignables par deplacement simple) format  exemple: 'B4,B6'
          sauts (cases atteignables par saut)  format exemple; 'B3,B7'
    """
    possibilites = []
    n=len(grille[0])
    for i in range(n):
       for j in range(n):
            if appartient_case_joueur([i,j],grille,joueur):
                depart = coordonnees_lettrechiffre([i,j]) #case en format lettre chiffre
                choix1 = deplacements_simples_possibles(depart,grille)
                choix2 = sauts_possibles(depart,grille,joueur)
                if choix1 !='' or choix2 != '':
                     possibilites.append([depart,choix1,choix2])
    return possibilites
#===============================================================================
def liste_suite_choix_ordi(depart, possibilites):
    """
    arguments:
    depart : case depart (= arrivee du saut precedent)
      possibilités:  liste des possibilites en format de type
          [[depart1,depl_simples,sauts],[depart2,depl_simples,sauts],...]
          depart1    sous le format   de type 'B5'
          depl_simples (cases atteignables par deplacement simple) format  exemple: 'B4,B6'
          sauts (cases atteignables par saut)  format exemple; 'B3,B7'
       (retournee par la fonction possibilites_tour_de_jeu_ordi(grille,joueur,pr)

    retourne les  couples (depart,arrivee) par sauts
    """
    nb_cases_depart = len(possibilites)
    nb_choix_saut = 0
    choix_saut = []
    for j in range(nb_cases_depart):
        if possibilites[j][0] == depart:  # case depart imposee  en argument
            # exemple  pour  'A2,B3'   il y a   (5+1)//3= 2   arrivées possibles A2  et B3
            len2  = len(possibilites[j][2])
            if len2  >  0:
                nb_choix_saut +=   (len2 +1) //3 # nb cases atteignables par saut
                i = 0
                for k in range((len2 +1)//3) :
                      choix_saut.append((possibilites[j][0],possibilites[j][2][i:i+2] ))
                      i +=3
    #print("choix_saut:",choix_saut)
    return choix_saut
#==============================================================================
def complete_choix(depart, liste_possible,choix):
    """
    arguments
        depart; case départ     dans format   de type 'B5'
        liste_possible: cases atteignables par deplacement simple ou  saut
         (selon l'appel   dans fonction liste_choix_ordi)
               format  exemple: 'B4,B6'
    retourne  la mise à jour de choix:  liste   des couples (départ,arrivée) ( par
         deplacement simple ou saut  selon l'appel   dans fonction liste_choix_ordi=
                 (départ et arrivée en format lettre suivie d'une chiffre)
    """
    dim  = len(liste_possible)
    # compte tenu du format, pour la chaine  A2,B3 il y a  (5+1)//3= 2   arrivées possibles
    # chaque arrivee codee sur 2 caracteres
    i = 0
    for k in range((dim +1)//3) :
        choix.append((depart,liste_possible[i:i+2]))
        i +=3
    return  choix
#===============================================================================
def liste_choix_ordi(possibilites):
    """
    arguments  possibilités:  liste des possibilites en format de type
         [[depart1,depl_simples,sauts],[depart2,depl_simples,sauts],...]
          depart1    sous le format   de type 'B5'
          depl_simples (cases atteignables par deplacement simple) format  exemple: 'B4,B6'
          sauts (cases atteignables par saut)  format exemple; 'B3,B7'
       (retournee par la fonction possibilites_tour_de_jeu_ordi(grille,joueur,pr)
    retourne 2 listes: choix_simple: liste   des couples (départ,arrivée)   par déplacement simple
                       choix_saut: liste   des couples (départ,arrivée)  par saut
                 (départ et arrivée en format lettre suivie d'une chiffre)
    """
    nb_cases_depart = len(possibilites)
    choix_simple = []
    choix_saut = []
    for j in range(nb_cases_depart):
        depart = possibilites[j][0]
        if  len(possibilites[j][1]) > 0:
           choix_simple =complete_choix(depart,possibilites[j][1],choix_simple )
        if  len(possibilites[j][2]) > 0:
           choix_saut =complete_choix(depart, possibilites[j][2], choix_saut )
    return choix_simple,choix_saut
#===============================================================================
def choix_aleatoire(liste_choix):
    """
    arguments :  liste_choix liste des couples (depart,arrivées) possibles pour
               le déplacement selectionné
    valeur retounée: le couple (départ,arrivée) tiré aléatoirement dans la liste
        depart et arrivee sont dans le format lettre suivie de chiffre
        numéro des couples 0, 1 .... nb_de_couples - 1
    """
    n = len(liste_choix)
    i = random.randint(0,n-1)
    #print("choix_aleatoire:", liste_choix,n,i,liste_choix[i] )
    return  liste_choix[i]
#===============================================================================
def  tour_de_jeu_ordi(grille,joueur,pr):  # le tour du  joueur ordi
    """
    parametres : grille nxn
                  joueur ordi  =1   si pions '*', =2   si pions 'o'
    organise un tour de jeu de l'ordi :
            en priorité  un saut (voire un enchainement)  sinon 1 deplacement simple
    stopper le mvt si fin de jeu
    """
    saut = 0
    fin =  False
    while not  fin  :  # l'ordi peut jouer
        possibilites = possibilites_tour_de_jeu_ordi(grille,joueur)
        if saut == 0:  # tirage aleatoire saut / deplacement simple
            liste1,liste2= liste_choix_ordi(possibilites)
        else:
            liste2= liste_suite_choix_ordi(depart,possibilites)
        if liste2 != []:
            choix_saut_ou_simple = 1   # l'ordi va faire un saut  avec prise
            couple_dep_arrivee= choix_aleatoire(liste2)
            saut = 1
            print(" ordi  depart=",couple_dep_arrivee[0], "arrivee=",couple_dep_arrivee[1] )
            grille, pr = mise_a_jour_depl_saut(couple_dep_arrivee[0],couple_dep_arrivee[1],grille,joueur,pr)
            #  preparer saut suivant  si  possible
            depart = couple_dep_arrivee[1]
        else:
            if saut == 0:  # on n a pas fait de saut, on peut essayer deplacement simple
                if    liste1  !=[] :  # l'ordi va faire un deplacement simple
                    choix_saut_ou_simple = 0
                    couple_dep_arrivee= choix_aleatoire(liste1)   #  choix depart et arrivee deplacement simple
                    saut = 0
                    print(" ordi  depart=",couple_dep_arrivee[0], "arrivee=",couple_dep_arrivee[1] )
                    grille = mise_a_jour_depl_simple(couple_dep_arrivee[0],couple_dep_arrivee[1],grille,joueur)
                fin = True
            else:  #  on ne peut plus sauter
                fin = True

    newjoueur = 2  if joueur==1  else 1    # l ordi a joué; c'est à l'humain
    return   (grille,newjoueur,pr)

#===============================================================================
def jeu_joueur_ordi(grille):
    """
     paramètres   grille tableau nxn de caracteres ' ', '*', 'o'
    """

    #le joueur humain  peut  etre 1 (avec pions *)   ou 2 (avec pions o)
    #il  commence le jeu

    rep = ''
    while rep not in {'1','2'}:
       rep  =  input("vous voulez etre  joueur 1: taper 1   OU   joueur  2: taper 2  - ma réponse:")
    if rep == '1':
        print("vous etes le joueur 1,pions *    et  l'ordi le joueur 2 ,pions o ")
    else:  # rep = '2'
        print("vous etes le joueur 2,pions o    et l'ordi le joueur 1 ,pions * ")
    print("le joueur humain commence")
    joueur = int(rep)

    pr = comptage_pions(grille)
    print("avant le tour du joueur ",joueur)
    afficher_grille(grille,joueur,pr)
    while  not test_fin_partie(pr):  # la partie n 'est pas finie, on  fait jouer 1 joueur
         if  joueur == int(rep) :  #l'humain joue
             grille,joueur,pr = tour_de_jeu_joueur(grille,joueur,pr) # le tour d'un joueur humain
         else: # l'ordi joue
             grille,joueur,pr = tour_de_jeu_ordi(grille,joueur,pr) # le tour du  joueur ordi
         print("apres le tour du joueur")
         afficher_grille(grille,joueur,pr)   # affichage apres le tour du joueur
    print(" le joueur 1  a ",pr[0], " pions  *, le joueur 2  a ",pr[1]," pions o;  la partie est finie ")
    vainqueur = 2 if pr[0] <6   else 1
    print( " le joueur ", vainqueur, "  a  gagné")

#=============================================================================
def faire_un_tour_de_jeu():   #  1 tour joueur   tel   que demandé   atelier 3
   #  les grilles disponibles
   config_init = grille_init(n)
   config_milieu = grille_milieu(n)
   config_fin = grille_fin(n)
   #  on va  faire un choix  de grille   et un choix de joueur pour faire un tour de joueur
   grille = grille_vide(n)
   choix = 0
   while choix  not in [1,2,3]:
       choix= int(input("votre choix de grille:   config_init: taper 1   OU    config_milieu: taper 2   OU  config_fin: taper 3 - ma réponse:"))
   if choix == 1:
       grille = config_init
   elif  choix == 2:
       grille = config_milieu
   else:  # choix =3
      grille = config_fin
   joueur = 0
   while joueur !=1 and joueur !=2:
       joueur= int(input("choisir le joueur 1   (pions '*')  OU   le joueur 2 (pions 'o') - ma réponse: "))
   pr = comptage_pions(grille)
   print("avant le tour du joueur")
   afficher_grille(grille,joueur,pr)
   if  not test_fin_partie(pr):  # la partie n 'est pas finie, on  fait jouer 1 joueur
      grille,joueur,pr = tour_de_jeu_joueur(grille,joueur,pr) # le tour d'un joueur
      print("apres le tour du joueur")
      afficher_grille(grille,joueur,pr)   # affichage apres le tour du joueur
   else:
      print(" au moins un des 2 joueurs a moins de 6 pions;  la partie est finie ")
#==============================================================================
# ## ================  CODE PRINCIPAL   ======================================
#  dimension de la grille carrée
n =7

config_init = grille_init(n)
config_milieu = grille_milieu(n)
config_fin = grille_fin(n)
config_test_deplacemnts=grille_test_deplct(n)
#afficher_grille(config_test_deplacemnts,1,comptage_pions(config_test_deplacemnts))

rep=''
while rep not in ['oui','non']:
     rep  =  input(" vous voulez  lancer la fonction generale de test:  taper oui    SINON   non  - ma réponse: ")
if rep == 'oui':
     generale_tests()
rep=''
while rep not in ['oui','non']:
    rep  =  input("vous voulez faire un tour de jeu de joueur:  taper oui    SINON   non - ma réponse: ")
if rep == 'oui':
   faire_un_tour_de_jeu()

#=====   faire une partie houeur/ joueur   ou   joueur/ordi  avec choix grille depart et joueur
choix_jeu, choix_grille = menu_utilisateur()
if choix_grille == 1:
    print("le jeu commence par la grille du début")
    grille = grille_init(n)
elif   choix_grille == 2:
    print("le jeu commence par la grille du milieu")
    grille  =  grille_milieu(n)
else:   #choix_grille == 3:
    print("le jeu commence par la grille de la fin")
    grille = grille_fin(n)
if choix_jeu == 1:
    print("jeu  joueur contre joueur")
    jeu_joueur_joueur(grille)
else:  # choix_jeu == 2
    print("jeu  joueur contre ordinateur")
    jeu_joueur_ordi(grille)








