# README.MD
Este proyecto fue planeado para el evento Hackaton by UDLA.  
Equipo: Números primos

## Problema
Datos de entrada: Información sobre los negocios de Quito.  

Datos de salida: Representación visual de la información y los diferentes análisis para las parroquias y barrios de la ciudad de Quito. 

## Plan de resolución
* Se utilizará el lenguaje de programación Python para obtener los datos de negocios de Quito con la API de Google: Google Places. Los datos serán colocados en un archivo “.csv” para su uso práctico.
* Construcción un mapa interactivo en python para mostrar la información obtenida con la API de Google.
* Integración de python en R para el futuro despliegue en https://www.shinyapps.io 

## Implementación
* Se utilizó un código de ejemplo para probar la API de Google Places.
* Se utilizó un archivo geojson para obtener la división administrativa y poder graficar un mapa interactivo dentro de python.
* Fue necesario generar un csv a partir del archivo JSON para el correcto funcionamiento del mapa en python (obtener_datos_csv.py).

## Problemas Implementación
* La API de Google Places sólo se encuentra disponible si se utiliza una tarjeta de crédito. 
* El tiempo disponible antes de la entrega final no fue suficiente para este equipo.


