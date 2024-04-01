"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.copy()
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_"," ").str.replace("-"," ")
    df["barrio"] = df["barrio"].str.lower().str.replace("_"," ").str.replace("-"," ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    def cambio_fecha(fecha):
        try:
            return datetime.strptime(fecha,"%d/%m/%Y")
        except:
            return datetime.strptime(fecha,"%Y/%m/%d")
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(lambda x:cambio_fecha(x)).dt.strftime("%d/%m/%Y")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$","").str.replace(".00","").str.replace(",","").astype(int)
    df["línea_credito"] = df["línea_credito"].str.lower().str.replace(" ","_").str.replace("-","_")
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    df.to_csv("prueba.csv")
    return df
clean_data()