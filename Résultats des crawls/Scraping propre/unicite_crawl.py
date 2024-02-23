import csv
import pandas

# Renseigner les noms de fichier

filename_liens = "liens_resultats5.csv"    # Fichier des liens
filename_noeuds = "noeuds_resultats5.csv"  # Fichier des noeuds
filename_res = "unicite_liens_resultats5.txt"    # Fichier des résultats

# Ouverture fichier noeuds

data = pandas.read_csv(filename_noeuds)
data.drop_duplicates(subset = "Id", keep = 'first', inplace = True)

# Premiere ouverture des liens pour gerer le crawl 0

f = open(filename_liens, "r", encoding="utf8")
reader = csv.reader(f, delimiter=',')
next(reader)

res = filename_liens.replace(".csv", "") + "\n" # En-tete fichier

videos_uniques = []     # Stocker les vidéos uniques
chaines_uniques = []    # Stocker les chaines uniques
genres_uniques = []     # Stocker les genres uniques

# Crawl 0 manuel

next(reader)
ligne = next(reader)

videos_uniques.append(ligne[0])
chaines_uniques.append(data[ data['Id'] == ligne[0] ]['Chaine'].values[0])
genres_uniques.append(data[ data['Id'] == ligne[0] ]['Genre'].values[0])

nb_vid_uniques = 1
nb_cha_uniques = 1
nb_gen_uniques = 1

f.close()

res += "\nCrawl 0 :\n"
res += "\tVideos uniques observees  : 1\n"
res += "\tMaximum de videos uniques : 1\n\n"
res += "\tChaines uniques observees : 1\n"
res += "\tGenres uniques observees  : 1\n"

# Deuxieme ouverture du fichier des liens pour les crawls 1 à n

f = open(filename_liens, "r", encoding="utf8")
reader = csv.reader(f, delimiter=',')
next(reader)

# Parametres

crawl = 6
plage = 3

for i in range(crawl):
    # Afficher le niveau de profondeur
    res += "\nCrawl " + str(i+1) + " :\n"
    # Combien de lignes va-t-on lire ? On suppose le csv trié par ordre croissant de crawl
    nb_lignes = plage**(i+1)
    for j in range(nb_lignes):  # On lit les lignes
        next(reader)
        ligne = next(reader)
        if not(ligne[1] in videos_uniques): # Si la vidéo est unique,
            nb_vid_uniques += 1             # on la compte,
            videos_uniques.append(ligne[1]) # et on la stocke
            chaine = data[ data['Id'] == ligne[1] ]['Chaine'].values[0] # On récupère sa chaine
            genre = data[ data['Id'] == ligne[1] ]['Genre'].values[0]   # et son genre
            if not(chaine in chaines_uniques):  # Si la chaine est unique,
                nb_cha_uniques += 1             # on la compte,
                chaines_uniques.append(chaine)  # et on la stocke
            if not(genre in genres_uniques):    # Si le genre est unique,
                nb_gen_uniques += 1             # on le compte,
                genres_uniques.append(genre)  # et on le stocke
    # Afficher le resultat
    res += "\tVideos uniques observees  : " + str(nb_vid_uniques) + "\n"
    res += "\tMaximum de videos uniques : " + str(sum(plage**j for j in range(i+2))) + "\n\n"
    res += "\tChaines uniques observees : " + str(nb_cha_uniques) + "\n"
    res += "\tGenres uniques observees  : " + str(nb_gen_uniques) + "\n"
    

f.close()

print(res)

txt = open(filename_res, "w", encoding="utf8")
txt.write(res)
txt.close()

