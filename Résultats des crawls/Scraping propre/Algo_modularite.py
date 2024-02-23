import pandas

def info_classe(data) :
    res = ""
    res += "\nCommentaires :\n"
    res += "\tMoyenne       = " + str(data['commentaires'].mean()) + "\n"
    res += "\tEcart-type    = " + str(data['commentaires'].std()) + "\n"
    res += "\tMinimum       = " + str(data['commentaires'].min()) + "\n"
    res += "\t1er quartile  = " + str(data['commentaires'].quantile(0.25)) + "\n"
    res += "\tMediane       = " + str(data['commentaires'].quantile(0.5)) + "\n"
    res += "\t3eme quartile = " + str(data['commentaires'].quantile(0.75)) + "\n"
    res += "\tMaximum       = " + str(data['commentaires'].max()) + "\n"
    res += "\tEcart IQ      = " + str(data['commentaires'].quantile(0.75) - data['commentaires'].quantile(0.25)) + "\n"

    res += "\nVues :\n"
    res += "\tMoyenne       = " + str(data['vues'].mean()) + "\n"
    res += "\tEcart-type    = " + str(data['vues'].std()) + "\n"
    res += "\tMinimum       = " + str(data['vues'].min()) + "\n"
    res += "\t1er quartile  = " + str(data['vues'].quantile(0.25)) + "\n"
    res += "\tMediane       = " + str(data['vues'].quantile(0.5)) + "\n"
    res += "\t3eme quartile = " + str(data['vues'].quantile(0.75)) + "\n"
    res += "\tMaximum       = " + str(data['vues'].max()) + "\n"
    res += "\tEcart IQ      = " + str(data['vues'].quantile(0.75) - data['vues'].quantile(0.25)) + "\n"

    res += "\nDates :\n"
    res += "\tMoyenne       = " + str(pandas.to_datetime(data['date']).mean()) + "\n"
    res += "\tEcart-type    = " + str(pandas.to_datetime(data['date']).std()) + "\n"
    res += "\tMinimum       = " + str(pandas.to_datetime(data['date']).min()) + "\n"
    res += "\t1er quartile  = " + str(pandas.to_datetime(data['date']).quantile(0.25)) + "\n"
    res += "\tMediane       = " + str(pandas.to_datetime(data['date']).quantile(0.5)) + "\n"
    res += "\t3eme quartile = " + str(pandas.to_datetime(data['date']).quantile(0.75)) + "\n"
    res += "\tMaximum       = " + str(pandas.to_datetime(data['date']).max()) + "\n"
    res += "\tEcart IQ      = " + str(pandas.to_datetime(data['date']).quantile(0.75) - pandas.to_datetime(data['date']).quantile(0.25)) + "\n"

    res += "\nFamilyFriendly :\n"
    res += "\t" + str(data['familyfriendly'].sum()) + " sur " + str(data['Id'].count()) + " vidéos.\n"

    res += "\nGenres :\n"
    res += "\tUniques = " + str(len(data['genre'].unique())) + "\n"
    for i in data['genre'].value_counts().index :
        res += "\t   " + str(data['genre'].value_counts()[i]) + "\t: " + i + "\n"


    temp = ""
    for i in data['keywords'].index :
        temp += data['keywords'][i]
        temp += ", "
    kw = temp.split(", ")

    res += "\nKeywords :\n"
    res += "\tUniques = " + str(len(pandas.Series(kw).unique())) + "\n"
    for i in pandas.Series(kw).value_counts().index :
        res += "\t    " + str(pandas.Series(kw).value_counts()[i]) + "\t: " + i + "\n"

    res += "\nChaines :\n"
    res += "\tUniques = " + str(len(data['chaine'].unique())) + "\n"
    for i in data['chaine'].value_counts().index :
        res += "\t    " + str(data['chaine'].value_counts()[i]) + "\t: " + i + "\n"

    res += "\nAbonnés :\n"
    res += "\tMoyenne       = " + str(data['abonnes'].mean()) + "\n"
    res += "\tEcart-type    = " + str(data['abonnes'].std()) + "\n"
    res += "\tMinimum       = " + str(data['abonnes'].min()) + "\n"
    res += "\t1er quartile  = " + str(data['abonnes'].quantile(0.25)) + "\n"
    res += "\tMediane       = " + str(data['abonnes'].quantile(0.5)) + "\n"
    res += "\t3eme quartile = " + str(data['abonnes'].quantile(0.75)) + "\n"
    res += "\tMaximum       = " + str(data['abonnes'].max()) + "\n"
    res += "\tEcart IQ      = " + str(data['abonnes'].quantile(0.75) - data['abonnes'].quantile(0.25)) + "\n"

    return res




filename = 'data5.csv'
new_filename = "classes_" + filename.replace(".csv", ".txt")

data = pandas.read_csv(filename)
data.drop_duplicates(subset = "Id", keep = 'first', inplace = True)
data = data[data['vues'] > 0]

#
for i in data['date'].index :
    data['date'] = data['date'].replace(data['date'][i], data['date'][i].replace("<[",""))
    data['date'] = data['date'].replace(data['date'][i], data['date'][i].replace("]>",""))
data['date'] = pandas.to_datetime(data['date'], utc=True, unit='ms')
#

res = filename.replace(".csv", "") + "\n"

txt = open(new_filename, "a", encoding="utf8")
txt.write(res)
txt.close()

for i in sorted(data["modularity_class"].unique()) :
    classe = data[data['modularity_class'] == i]
    res = "\n--------------- Classe " + str(i) + " : " + str(classe['Id'].count()) + " vidéos ---------------\n"
    res += info_classe(classe)
    txt = open(new_filename, "a", encoding="utf8")
    txt.write(res)
    txt.close()