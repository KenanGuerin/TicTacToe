L1=[[],[],[]]
L2=[[],[],[]]
L3=[[],[],[]]
L=[L1,L2,L3]
print("           ",L[0])
print("           ",L[1])
print("           ",L[2])
Liste_rempli=[]
Liste_dispo=[1,2,3,4,5,6,7,8,9]
joueur=0
	
def ajout(Liste,nb):
    global Liste_rempli,Liste_dispo,joueur
    if joueur==0:
        joueur=1
    else:
        joueur=0
    if nb in Liste:
        print(" ERREUR la case ",nb," est deja remplie")
    elif nb < 1 or nb > 9:
        print(" ERREUR ",nb,"n'est pas compris entre 1 et 9")
    else:
        Liste_rempli.append(nb)
        Liste_dispo.remove(nb)
    if nb == 1:
        L[0][0]=joueur
    elif nb == 2:
        L[0][1]=joueur
    elif nb == 3:
        L[0][2]=joueur
    elif nb == 4:
        L[1][0]=joueur
    elif nb == 5:
        L[1][1]=joueur
    elif nb ==  6:
        L[1][2]=joueur
    elif nb == 7:
        L[2][0]=joueur
    elif nb == 8:
        L[2][1]=joueur
    elif nb == 9:
        L[2][2]=joueur
    return L


def verificateur(L): #verifie si la liste contient une combinaison gagnante , si oui retourne (joueur ," a gagné")
    global Liste_rempli,Liste_dispo,joueur,nb
    for i in range (0,3): # colonne
        if L[0][i]==L[1][i]==L[2][i]!=[]:
            return (joueur ," a gagné")
	
    for l in L : # ligne
        if l[0]==l[1]==l[2]!=[]:
            return (joueur ," a gagné")
    if L[0][0]==L[1][1]==L[2][2]!=[] or L[2][0]==L[1][1]==L[0][2]!=[]:
        return (joueur ," a gagné")
    return L


def jouer(L):
    global Liste_rempli,Liste_dispo,joueur,nb
    global Liste_dispo , joueur
    while len(Liste_dispo)!=0:
        print("Les cases libres sont : ",Liste_dispo)
        print(L[0])
        print(L[1])
        print(L[2])
        nb=int(input(" Entrez la case ou vous voulez jouer"))
        ajout(L,nb)
        result = verificateur(L)
        if isinstance(result, tuple):
            winner, _ = result
            print(L[0])
            print(L[1])
            print(L[2])
            return f"{winner} a gagné"
    return "Égalité"
jouer(L)