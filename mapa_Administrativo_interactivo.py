import pandas as pd
import requests
import plotly.express as px

df=pd.read_csv('quitoData.csv')
repo_url = 'https://raw.githubusercontent.com/flandrade/quito-crime-map/master/data/zonales_quito.geojson' #Archivo GeoJSON
quito_p = requests.get(repo_url).json()


fig = px.choropleth(df, geojson=quito_p, locations='id', color='Habitantes',
                           color_continuous_scale="burg", #greens                           
                           projection="mercator",featureidkey="id",
                           hover_name="Zonas"
                          )
fig.update_geos(fitbounds="locations", visible=False)                          
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

