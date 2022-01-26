def marque_tableau(symbole,tableau,coup):
    ligne = 5
    for i in range(6):
        if tableau[ligne][coup] == '_':
            tableau[ligne][coup] = symbole
            break
        else :
            ligne = ligne - 1
    return tableau

def verification_collone(tableau,symbole,victoire):
    for i in range(7):
        valeur = 0
        for s in tableau:
            if s[i] == symbole:
                valeur = valeur + 1
                if valeur >= 4:
                    victoire = 1
            else:
                valeur = 0
    return victoire
                    
def verification_ligne(tableau,symbole,victoire):
    for i in tableau:
        valeur = 0
        for s in i:
            if s == symbole:
                valeur = valeur + 1
                if valeur >= 4:
                    victoire = 1
            else:
                valeur = 0
    return victoire

def verification_diagonale_descendante(tableau,symbole,victoire,nbr_1,nbr_2,nbr_3):
    valeur = 0
    for i in range(nbr_1):
        v = i
        v = v + nbr_2
        k = i
        k = k + nbr_3
        if tableau[v][k] == symbole:
            valeur = valeur + 1
            if valeur >= 4:
                victoire = 1
        else:
            valeur = 0
    return victoire

def verification_diagonale_montante(tableau,symbole,victoire,nbr_1,nbr_2):
    v = nbr_2
    valeur = 0
    for i in reversed(range(nbr_1)):
        v = v + 1
        if v == 7:
            break
        if tableau[i][v] == symbole:
            valeur = valeur + 1
            if valeur >= 4:
                victoire = 1
        else:
            valeur = 0      
    return victoire

def verification_diagonale_descendante_g(tableau,symbole,victoire):
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,6,0,0)
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,5,1,0)
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,4,2,0)
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,6,0,1)
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,5,0,2)
    victoire = verification_diagonale_descendante(tableau,symbole,victoire,4,0,3)
    return victoire

def verification_diagonale_montante_g(tableau,symbole,victoire):
    victoire = verification_diagonale_montante(tableau,symbole,victoire,6,-1)
    victoire = verification_diagonale_montante(tableau,symbole,victoire,6,0)
    victoire = verification_diagonale_montante(tableau,symbole,victoire,6,1)
    victoire = verification_diagonale_montante(tableau,symbole,victoire,5,-1)
    victoire = verification_diagonale_montante(tableau,symbole,victoire,4,-1)
    victoire = verification_diagonale_montante(tableau,symbole,victoire,6,2)
    return victoire
    
def verification_general(tableau,symbole,victoire):
    victoire = verification_ligne(tableau,symbole,victoire)
    victoire = verification_collone(tableau,symbole,victoire)
    victoire = verification_diagonale_descendante_g(tableau,symbole,victoire)
    victoire = verification_diagonale_montante_g(tableau,symbole,victoire)
    return victoire

def error_coup_joueur(joueur):
    continuer = False
    while not continuer:
        coup = int(input(joueur + " Entrez une colonne entre 1-7 : ")) - 1
        if coup<=6 and coup>=0:
            continuer=True
            print(joueur +" joue " + str(coup))
        else:
            print("veuillez entrer une colonne qui correspond au jeu !!! ")
    return coup


    

def play(joueur_1,joueur_2):
    import random as rd
    tableau=[['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_']]
    temp= 2
    victoire = 0
    print(joueur_1 + " joue les O")
    print(joueur_2 + " Joue les X")
    while victoire != 1:
        if temp%2 == 1:
            symbole = "X"
            joueur = joueur_2
            if joueur_2 == "ordi":
                coup = rd.randint(0,6)
                print("l'ordi joue: "+ str(coup+1))
            else:
                coup = int(input(joueur_2 + " Entrez une colonne entre 1-7 : ")) - 1
                print(joueur_2 +" joue " + str(coup))
                coup = error_coup_joueur(joueur)
        else:
            symbole = "O"
            joueur = joueur_1
            coup = error_coup_joueur(joueur)
        marque_tableau(symbole,tableau,coup)

        victoire = verification_general(tableau,symbole,victoire)

        temp = temp+ 1
        for ligne in tableau:
            print(ligne)
    return joueur + " a gagné"



    
     
