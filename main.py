szam_lista =[12,23,-56,82,12.23,69,-100] 
import feladatok
"""1.
Ird ki a kepernyore a lista elemeit
Irj metodust amely a parametereben kapott lista elemeit kiirja a kepernyore"""
print("***1.FELADAT***")
feladatok.elsofeladat(szam_lista)
"""2.
Mennyi a pozitiv szamok osszege?(osszegzes)"""
print("***2.FELADAT***")
masodik:float=feladatok.masodikfeladat(szam_lista)
print(f"Pozitív számok összege:{masodik}")
"""3.
Hany negativ szam van?(megszamlalas)"""
print("***3.FELADAT***")
harmadik:int=feladatok.harmadikfeladat(szam_lista)
print(f"Negatív számok:{harmadik}")
"""4.
Hany nem egesz szam van a szamok kozott?(szamlalas)
"""
print("***4.FELADAT***")
negyedik:int=feladatok.negyedikfeladat(szam_lista)
print(f"Nem egészek száma:{negyedik}")
"""5.
Mennyi a 3-al oszthato szamok atlaga?(osszegzes-szamlalas)"""
print("***5.FELADAT***")
otodik:float=feladatok.otodikfeladat(szam_lista)
print(f"Hárommal oszthatók átlaga:{otodik}")
"""6.
Mekkora a legnagyobb szam?(kivalasztas)"""
print("***6.FELADAT***")
hatodik:int=feladatok.hatodikfeladat(szam_lista)
print(f"A legnagyobb szám:{hatodik}")
"""7.
Mekkora a legkisebb szam?(kivalasztas)"""
print("***7.FELADAT***")
hetedik:int=feladatok.hetedikfeladat(szam_lista)
print(f"A legkisebb szám:{hetedik}")
"""8. 
Mekkora a legkisebb es a legnagyobb szam kulonbsege?(max/min kivalasztas)"""
print("***8.FELADAT***")
kivonas:int=feladatok.nyolcadikfeladat(szam_lista)
print(f" legkisebb és a legnagyobb szám különbsége:{kivonas}")





