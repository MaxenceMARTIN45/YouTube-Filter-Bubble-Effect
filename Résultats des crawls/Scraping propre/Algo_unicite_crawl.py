import csv

filename = "liens_resultats5.csv"

f = open(filename, "r", encoding="utf8")
reader = csv.reader(f, delimiter=',')
next(reader)

res = filename.replace(".csv", "") + "\n"
videos_uniques = []

next(reader)
ligne = next(reader)
videos_uniques.append(ligne[0])
nb_uniques = 1

f.close()

res += "\nCrawl 0 :\n"
res += "\tMaximum de videos uniques : 1\n"
res += "\tVideos uniques observees  : 1\n"

f = open(filename, "r", encoding="utf8")
reader = csv.reader(f, delimiter=',')
print(next(reader))

for i in range(6):
    res += "\nCrawl " + str(i+1) + " :\n"
    nb_lignes = 3**(i+1)
    for j in range(nb_lignes):
        next(reader)
        ligne = next(reader)
        if not(ligne[1] in videos_uniques):
            nb_uniques += 1
            videos_uniques.append(ligne[1])
    res += "\tVideos uniques observees  : " + str(nb_uniques) + "\n"
    res += "\tMaximum de videos uniques : " + str(sum(3**j for j in range(i+2))) + "\n"

f.close()

txt = open("unicite_" + filename.replace(".csv", ".txt"), "w", encoding="utf8")
txt.write(res)
txt.close()

