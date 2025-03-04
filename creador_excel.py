import pandas as pd #pd es un acronimo de Pandas

#Dataframe es la informacion basica con el nombre de las piezas y cm de los componentes

data = {
    "Piezas: " : ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centímetros": [40, 90, 120, 60, 100]

}

df = pd.DataFrame(data)

# Guardar el dataframe en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)

#La gran diferencia entre Excel y CSV es que el CSV se genera en una sola columna y los valores estan separados por coma. Ademas, los caracteres especiales, como el acento en "centímetros" no los reconoce

