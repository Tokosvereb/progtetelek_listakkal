

def elsofeladat(szam_lista):
    listahossza = len(szam_lista)
    i:int = 0
    for i in range(0,listahossza,1):
        print(f"Számok: {szam_lista[i]}")

def masodikfeladat(szam_lista):
    osszeg = 0  
    for i in range(1,len(szam_lista),1):
        if szam_lista[i] > 0:
            osszeg += szam_lista[i]
          
    return osszeg

def harmadikfeladat(szam_lista):
    negativok = 0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i] < 0:
            negativok += 1
    return negativok

def negyedikfeladat(szam_lista):
    nemegeszek = 0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i] % 1 != 0:
            nemegeszek += 1

    return nemegeszek 

def otodikfeladat(szam_lista):
    harommaloszthatok = 0
    atlag = 0
    db = 0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i] % 3 == 0:
            harommaloszthatok += szam_lista[i]
            db += 1
            
    return harommaloszthatok/db 

def hatodikfeladat(szam_lista): 
    maxertek = szam_lista[0]
    for i in range(0,len(szam_lista),1):
        if maxertek < szam_lista[i]:  
            maxertek = szam_lista[i]

    return maxertek

def hetedikfeladat(szam_lista):
    minertek = szam_lista[0]
    for i in range (0,len(szam_lista),1):
        if minertek > szam_lista[i]:
            minertek = szam_lista[i]

    return minertek

def nyolcadikfeladat(szam_lista):
    minertek = 0
    maxertek = 0
    for i in range(0,len(szam_lista),1):
        if minertek > szam_lista [i]:
            minertek = szam_lista[i]
        if maxertek < szam_lista[i]:
            maxertek = szam_lista[i]
    kivonas = minertek - maxertek 
    
    return kivonas