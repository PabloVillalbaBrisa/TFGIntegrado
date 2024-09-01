import pandas as pd
from datetime import datetime, timedelta

#AUSTRALIAN OPEN: 8 AL 29 DE ENERO DE 2023
#ROLAND GARROS: 22 DE MAYO AL 11 DE JUNIO DE 2023
#WIMBLEDON : 26 DE JUNIO AL 16 DE 2023
#US OPEN: 22 DE AGOSTO AL 10 DE SEPTIEMBRE AL 2023

csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_5.csv'
data = pd.read_csv(csv_path)
#FECHA A FORMATO DATETIME
data['fecha'] = pd.to_datetime(data['fecha'], format='%Y-%m-%d', errors='coerce')

#FECHAS GRAND SLAMS
grand_slams = {
    'Australian_Open': (datetime(2023, 1, 8), datetime(2023, 1, 29)),
    'Roland_Garros': (datetime(2023, 5, 22), datetime(2023, 6, 11)),
    'Wimbledon': (datetime(2023, 6, 26), datetime(2023, 7, 16)),
    'US_Open': (datetime(2023, 8, 22), datetime(2023, 9, 10))
}

#MARGEN DE UNA SEMANA ANTES Y DESPUÉS
#ESTO AÑADE UNO A LA FILA DE LA COLUMNA SI LA FECHA DEL POST CAE DENTRO DEL MARGEN DEL SLAM
#LO HACE PARA CADA SLAM
margen = timedelta(days=7)
for slam, (start, end) in grand_slams.items():
    data[slam] = data['fecha'].apply(lambda x: 1 if x and (start - margen <= x <= end + margen) else 0)

data.to_csv( 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_6.csv', index=False)
