"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.copy()
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["barrio"] = df["barrio"].str.lower()
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"],format="mixed")
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].dt.strftime('%m/%d/%Y')
    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$","").str.replace(".00","").str.replace(",","").astype(int)
    df["línea_credito"] = df["línea_credito"].str.lower()
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["tipo_de_emprendimiento","barrio"],inplace=True)
    return df

