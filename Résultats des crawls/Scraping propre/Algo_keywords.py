import requests
from lxml import html
import pandas

pandas.options.mode.chained_assignment = None

filename = 'noeuds_resultats4.csv'

data = pandas.read_csv(filename,encoding='cp1252')

data["Keywords"]= ""

for i in range(len(data['Id'])):
    page = requests.get(data['Id'][i])
    tree = html.fromstring(page.content)
    keywords = tree.xpath("//meta[@name='keywords']/@content")
    data["Keywords"][i] = keywords[0]
    print(i)

data.to_csv(filename, index=False)

