def Play(J1,J2):
    cst=[['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_']]
    T = 2
    Win = 0
    print(J1 + " joue les O")
    print(J2 + " Joue les X")
    while Win != 1:
        Diag = 0
        L=5
        if T%2 == 1:
            Tour = "X"
            Player = J2
        else:
            Tour = "O"
            Player = J1

        Coup = int(input(Player + " Entrez une colonne entre 1-7")) - 1
        for i in range(6):
            if cst[L][Coup] == '_':
                cst[L][Coup] = Tour
                break
            else :
                L = L - 1

        for i in cst:
            Val = 0
            for s in i:
                if s == Tour:
                    Val = Val + 1
                    if Val >= 4:
                        Win = 1
                else:
                    Val = 0

        for i in range(7):
            Val = 0
            for s in cst:
                if s[i] == Tour:
                    Val = Val + 1
                    if Val >= 4:
                        Win = 1
                else:
                    Val = 0

        for i in range(6):
            if cst[i][i] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
        Val = 0
        for i in range(5):            
            v = i
            v = v + 1
            if cst[v][i] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                Val = 0
        Val = 0        
        for i in range(4):            
            v = i
            v = v + 2
            if cst[v][i] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                Val = 0
        Val = 0        
        for i in range(6):            
            v = i
            v = v + 1
            if cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                Val = 0
        Val = 0        
        for i in range(5):            
            v = i
            v = v + 2
            if cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                Val = 0
        Val = 0        
        for i in range(4):            
            v = i
            v = v + 3
            if cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                Val = 0
        Val = 0        
        v = -1
        for i in reversed(range(6)):
            v = v + 1
            if cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
        
        Val = 0        
        v = 0
        for i in reversed(range(6)):
            v = v + 1
            if cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
                    
        Val = 0        
        v = 1
        for i in reversed(range(6)):
            v = v + 1
            if v  == 7:
                break
            elif cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
                    
        Val = 0        
        v = 1
        for i in reversed(range(6)):
            v = v + 1
            if v  == 7:
                break
            elif cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
                    
        Val = 0        
        v = -1
        for i in reversed(range(5)):
            v = v + 1
            if v == 7:
                break
            elif cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0
                    
        Val = 0        
        v = -1
        for i in reversed(range(4)):
            v = v + 1
            if v == 7:
                break
            elif cst[i][v] == Tour:
                Val = Val + 1
                if Val >= 4:
                    Win = 1
            else:
                    Val = 0

        T = T + 1
        for ligne in cst:
            print(ligne)
    return Player + " a gagné"