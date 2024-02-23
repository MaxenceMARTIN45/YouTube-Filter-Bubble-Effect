import pandas

filename = 'noeuds_resultats4.csv'

data = pandas.read_csv(filename)

data.drop_duplicates(subset = "Id", keep = 'first', inplace = True)

res = filename.replace(".csv", "") + "\n"

res += "\nCommentaires :\n"
res += "\tMoyenne       = " + str(data['Commentaires'].mean()) + "\n"
res += "\tEcart-type    = " + str(data['Commentaires'].std()) + "\n"
res += "\tMinimum       = " + str(data['Commentaires'].min()) + "\n"
res += "\t1er quartile  = " + str(data['Commentaires'].quantile(0.25)) + "\n"
res += "\tMediane       = " + str(data['Commentaires'].quantile(0.5)) + "\n"
res += "\t3eme quartile = " + str(data['Commentaires'].quantile(0.75)) + "\n"
res += "\tMaximum       = " + str(data['Commentaires'].max()) + "\n"
res += "\tEcart IQ      = " + str(data['Commentaires'].quantile(0.75) - data['Commentaires'].quantile(0.25)) + "\n"

res += "\nVues :\n"
res += "\tMoyenne       = " + str(data['Vues'].mean()) + "\n"
res += "\tEcart-type    = " + str(data['Vues'].std()) + "\n"
res += "\tMinimum       = " + str(data['Vues'].min()) + "\n"
res += "\t1er quartile  = " + str(data['Vues'].quantile(0.25)) + "\n"
res += "\tMediane       = " + str(data['Vues'].quantile(0.5)) + "\n"
res += "\t3eme quartile = " + str(data['Vues'].quantile(0.75)) + "\n"
res += "\tMaximum       = " + str(data['Vues'].max()) + "\n"
res += "\tEcart IQ      = " + str(data['Vues'].quantile(0.75) - data['Vues'].quantile(0.25)) + "\n"

res += "\nDates :\n"
res += "\tMoyenne       = " + str(pandas.to_datetime(data['Date']).mean()) + "\n"
res += "\tEcart-type    = " + str(pandas.to_datetime(data['Date']).std()) + "\n"
res += "\tMinimum       = " + str(pandas.to_datetime(data['Date']).min()) + "\n"
res += "\t1er quartile  = " + str(pandas.to_datetime(data['Date']).quantile(0.25)) + "\n"
res += "\tMediane       = " + str(pandas.to_datetime(data['Date']).quantile(0.5)) + "\n"
res += "\t3eme quartile = " + str(pandas.to_datetime(data['Date']).quantile(0.75)) + "\n"
res += "\tMaximum       = " + str(pandas.to_datetime(data['Date']).max()) + "\n"
res += "\tEcart IQ      = " + str(pandas.to_datetime(data['Date']).quantile(0.75) - pandas.to_datetime(data['Date']).quantile(0.25)) + "\n"

res += "\nFamilyFriendly :\n"
res += "\t" + str(data['FamilyFriendly'].sum()) + " sur " + str(data['Id'].count()) + " vidéos.\n"

res += "\nGenres :\n"
res += "\tUniques = " + str(len(data['Genre'].unique())) + "\n"
for i in data['Genre'].value_counts().index :
    res += "\t   " + str(data['Genre'].value_counts()[i]) + "\t: " + i + "\n"


temp = ""
for i in data['Keywords'].index :
    temp += data['Keywords'][i]
    temp += ", "
kw = temp.split(", ")

res += "\nKeywords :\n"
res += "\tUniques = " + str(len(pandas.Series(kw).unique())) + "\n"
for i in pandas.Series(kw).value_counts().index :
    res += "\t    " + str(pandas.Series(kw).value_counts()[i]) + "\t: " + i + "\n"

res += "\nChaines :\n"
res += "\tUniques = " + str(len(data['Chaine'].unique())) + "\n"
for i in data['Chaine'].value_counts().index :
    res += "\t    " + str(data['Chaine'].value_counts()[i]) + "\t: " + i + "\n"

res += "\nAbonnés :\n"
res += "\tMoyenne       = " + str(data['Abonnes'].mean()) + "\n"
res += "\tEcart-type    = " + str(data['Abonnes'].std()) + "\n"
res += "\tMinimum       = " + str(data['Abonnes'].min()) + "\n"
res += "\t1er quartile  = " + str(data['Abonnes'].quantile(0.25)) + "\n"
res += "\tMediane       = " + str(data['Abonnes'].quantile(0.5)) + "\n"
res += "\t3eme quartile = " + str(data['Abonnes'].quantile(0.75)) + "\n"
res += "\tMaximum       = " + str(data['Abonnes'].max()) + "\n"
res += "\tEcart IQ      = " + str(data['Abonnes'].quantile(0.75) - data['Abonnes'].quantile(0.25)) + "\n"

print(res)

'''
txt = open("desc_4" + filename.replace(".csv", ".txt"), "w", encoding="cp1252")
txt.write(res)
txt.close()
'''