# -*- coding: utf-8 -*-

### Representation des données
### initialisation des grilles et autres variable de jeu

config_defaut = [['●', '●', '●', '●', '●', '●', '○'],
                 ['●', '●', '●', '●', '●', '○', '○'],
                 ['●', '●', '●', '●', '○', '○', '○'],
                 ['●', '●', '●', ' ', '○', '○', '○'],
                 ['●', '●', '●', '○', '○', '○', '○'],
                 ['●', '●', '○', '○', '○', '○', '○'],
                 ['●', '○', '○', '○', '○', '○', '○']]

config_mil = [['●', '●', '●', '●', '●', '●', '○'],
              ['●', '●', '●', '●', '●', '○', '○'],
              ['●', '●', ' ', '●', '○', '○', '○'],
              ['●', '●', '●', '●', '○', '○', '○'],
              ['●', '●', '●', ' ', '○', '○', '○'],
              ['●', ' ', ' ', ' ', '○', '○', '○'],
              ['●', '○', '○', '○', '○', '○', '○']]

config_fin = [[' ', ' ', ' ', '●', '●', '○', '○'],
              [' ', '●', ' ', '○', '●', '●', '○'],
              ['●', ' ', ' ', '●', '○', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', '●', ' ', '●', '○', '●', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['●', '●', ' ', ' ', ' ', ' ', '○']]        

# Constante
LIGNE_MIN = 'A'
LIGNE_MAX = 'G'
COLONNE_MIN = '1'
COLONNE_MAX = '7'

### Représentation graphique 

def affichage_tour(joueur=True):
  """
  Permet d'afficher si c'est le tour du joueur 1 ou 2
  celon la variable global 'joueur'
  """
  if joueur :
    print("C'est au tour du joueur 1")
  if not joueur:
    print("C'est au tour du joueur 2")

def affichage_grille(conf):
  """
  prend en paramètre une configuration (matrices) de partie
  et l'affiche ligne par ligne
  """
  lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # lettres de placement

  for ligne in range(7):
    if ligne == 0: # cas spécial d'affichage de premiere ligne
      print("     1   2   3   4   5   6   7 \n   ┌───┬───┬───┬───┬───┬───┬───┐")
    print(f"  {lettres[ligne]}", end="") # affiche les lettres de placement du genre A B C D...

    for colonne in range(7) :
      if colonne == 0 : # cas spécial d'affichage de premiere colonne
        print(f"│ {conf[ligne][colonne]} │",end="") 
      else : # cas général d'affichage
        print(f" {conf[ligne][colonne]} │",end="")

    if ligne < 6 : # permet d'afficher les dernieres lignes
      print("\n   ├───┼───┼───┼───┼───┼───┼───┤")
    else :
      print("\n   └───────────────────────────┘\n")
  

def est_au_bon_format(message):
  """permet de verifier si un messages de joueur
   est au bon format"""

  if type(message) != str: # cas de mauvaise utilisation de fonction
    return False

  lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  l_message = len(message)

  if l_message != 2:
    return False
  elif message[0] not in lettres or message[1] not in chiffres:
    return False
  else:
    return True

def est_dans_grille(ligne, colonne):
  """permet de savoir si une position indiqué par le joueur
  est valide avec deux parametres ligne et colonne qui sont des chaines de caracteres.
  Ici le parametre "grille" n'est pas présent car inutile puisque
  la taille de la grille est constante."""

  if len(ligne) != 1 or len(colonne) != 1: # pour prendre seulement 1 caractere
    return False
  if ord(ligne) < ord(LIGNE_MIN) or ord(ligne) > ord(LIGNE_MAX):
    return False
  if ord(colonne) < ord(COLONNE_MIN) or ord(colonne) > ord(COLONNE_MAX) :
    return False
  else:
    return True
  
### Fonction de saisie

def saisie_coordonnee():
  """permet de lancer une saisie de déplacement d'une cordoonée a une autre.
  """
  est_valide = False
  while not est_valide:

    depart = input("Saisissez une coordonnée de depart : ")
    format_depart = est_au_bon_format(depart)
    grille_depart = est_dans_grille(depart[0], depart[1])

    arrive = input("Saisissez une coordonnée d'arrivé : ")
    format_arrive = est_au_bon_format(arrive)
    grille_arrive = est_dans_grille(arrive[0], arrive[1])

    if not format_depart and not grille_depart and not format_arrive and not grille_arrive:
      print("Le format et la position dans la grille ne sont pas correct")
    elif not format_depart or not format_arrive:
      print("Le format n'est pas correct")
    elif not grille_depart or not grille_arrive:
      print("La postion dans la grille n'est pas correct")
    else:
      est_valide = True

### Fonctions de Test

def test_est_bon_format():
  assert(est_au_bon_format("11") == False), "Deux chiffres"
  assert(est_au_bon_format("BB") == False), "Deux lettres"
  assert(est_au_bon_format("Z1") == False), "Ligne inexistante"
  assert(est_au_bon_format("A8") == True), "Bon format malgres que la colonne 8 ne doit pas exister"
  assert(est_au_bon_format("AAA") == False), "Troie lettres"
  assert(est_au_bon_format("A") == False), "Un seul caractere"
  assert(est_au_bon_format("213") == False), "Troie chiffres"
  assert(est_au_bon_format(12) == False), "Mauvais type"
  
def test_est_dans_grille():
    grille_vide = [[0]*8]*8 #façon pythonesque de creer une liste de liste vide
    assert est_dans_grille("A","5"),"erreur cas dans la grille"
    assert not est_dans_grille("a","5"),"erreur hors ligne inferieure"
    assert not est_dans_grille("I","5"),"erreur hors ligne superieure"
    assert not est_dans_grille("A","-1"),"erreur hors colonne inferieure"
    assert not est_dans_grille("A","8"),"erreur hors colonne superieure"
  
def test():
  print("Test")
  test_est_bon_format()
  test_est_dans_grille()
  print("OK !")

### CODE PRINCIPAL
# Execution de fonction de test
test()

# Execution affichage sur les 3 grilles
affichage_grille(config_defaut)
affichage_grille(config_mil)
affichage_grille(config_fin)
affichage_tour()

# Execution des coordonneés saisies
saisie_coordonnee()

