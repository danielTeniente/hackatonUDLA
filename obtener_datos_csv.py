import json
import pandas as pd

id_zona=[]
lista_zonas=[]
habitantes = []
with open('zonales_quito.json') as file:
    data = json.load(file)
    for zonal in data['features']:
        id_zona.append(zonal['id'])
        lista_zonas.append(zonal['properties']['zonal'])
        habitantes.append(zonal['properties']['habitantes'])

diccionario = {
    "id":id_zona,
    "Zonas":lista_zonas,
    "Habitantes":habitantes
}

df = pd.DataFrame(diccionario)
df.to_csv (r'quitoData.csv', index = False, header=True)