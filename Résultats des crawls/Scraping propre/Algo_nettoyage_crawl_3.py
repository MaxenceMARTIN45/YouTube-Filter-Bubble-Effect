import csv
import ast

def main():
    file = open("resultats5.csv", "r")
    reader = csv.DictReader(file)
    line_count = 0
    nouveau_lien = []
    nouveau_noeuds= []

    for row in reader :
        # if line_count !=0 :
            to_add = row
            to_add["Id"] = row["URL"]
            for ord, tar in enumerate( ast.literal_eval(row['Suivant'])): 
                nouveau_lien.append({ "Source" : row['URL'], "Target" : tar , "Depth" : row["Profondeur"] , "Order" : ord+1})

            del to_add["Profondeur"]
            nouveau_noeuds.append( to_add )
            

        # line_count+=1



 #Traitement des noeuds

    file.close()

    new_file_noeuds = open("noeuds_resultats5.csv", "w")
    writer = csv.writer(new_file_noeuds)
    writer.writerow(nouveau_noeuds[0].keys())

    for vid in nouveau_noeuds :
        # print(vid)

        try:
            int(vid['Commentaires'])
        except:
            vid['Commentaires'] = '-1'
        

        if vid['Abonnes'].find("M") == -1 :
            if vid['Abonnes'].find("k") == -1 :# Il y a ni k ni M
                vid['Abonnes'] = vid['Abonnes'][:vid['Abonnes'].find("abo")].replace("&nbsp;", "").replace(",", "") 
                try : 
                    int( vid['Abonnes'])
                except Exception :
                    vid['Abonnes'] = "-1"
                # print("Pas k : ", vid['Abonnes'])
                
            else : #Il y a k
                vid['Abonnes'] = vid['Abonnes'][:vid['Abonnes'].find("k")+1].replace("&nbsp;", "").replace(",", ".").replace("k", "")
                vid['Abonnes'] = int (ast.literal_eval(vid['Abonnes']) * 1000)

                # print("K : ", vid['Abonnes'])
        else:
            vid['Abonnes'] = vid['Abonnes'][:vid['Abonnes'].find("M")].replace("&nbsp;", "").replace(",", ".").replace("M", "")
            vid['Abonnes'] = int (ast.literal_eval(vid['Abonnes']) * 1000000)
            # print("M : ", vid['Abonnes'])


        try :
            writer.writerow(vid.values())
        except UnicodeEncodeError:
            vid['Titre'] = "Erreur d'encodage"
            vid['Chaine'] = "Erreur d'encodage"
            writer.writerow(vid.values())

    new_file_noeuds.close()






 #Traitement des liens

    new_file = open("liens_resultats5.csv", "w")
    writer = csv.writer(new_file)
    writer.writerow(nouveau_lien[0].keys())

    for vid in nouveau_lien :
        try :
            writer.writerow(vid.values())
            print(vid)
        except UnicodeEncodeError:
            print("Erreur lors de l'écriture des données (table des liens)")

    new_file.close()

if __name__ == '__main__' :
    main()