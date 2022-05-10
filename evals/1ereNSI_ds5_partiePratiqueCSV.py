import csv

fichier=open("1ereNSI_ds5_notesEleves.csv", encoding="utf8")
table=list(csv.DictReader(fichier,delimiter=","))

def convert (dico) :
    note1= int(dico["Note1"])
    note2 = int(dico["Note2"])
    note3 = int(dico["Note3"])
    moyenne = (note1+note2+note3)/3
    return { 'Eleve' : dico["Eleve"], 'Note1' : note1, 'Note2' : note2, 'Note3' : note3, 'Moyenne':moyenne}
def moy(t):
    a=0
    for i in table_valide:
        a+=int(i[t])
    return a/4
table_valide=[convert(x) for x in table]
table_valide.append({"Eleve":"Moyenne","Note1":moy("Note1"),"Note2":moy("Note2"),"Note3":moy("Note3"),"Moyenne":moy("Moyenne")})
#Les quatre lignes suivantes permettent de réécrire le contenu de "1ereNSI_ds5_notesEleves.csv"
#dans un nouveau fichier "1ereNSI_ds5_notesElevesMoyennes.csv"
with open ( "1ereNSI_ds5_notesElevesMoyennes.csv" , "w" ) as sortie :
    objet=csv.DictWriter ( sortie, [ 'Eleve' , 'Note1' , 'Note2' , 'Note3','Moyenne' ])
    objet.writeheader ( )
    objet.writerows(table_valide)

#Ajouter une colonne qui contient les moyennes par élèves :


#Ajouter une ligne qui contient les moyennes par matière :

