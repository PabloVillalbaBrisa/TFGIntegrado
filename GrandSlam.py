import pandas as pd
from datetime import datetime, timedelta

#AUSTRALIAN OPEN: 8 al 29 de ene de 2023
#ROLAND GARROS: 22 de may al 11 de jun de 2023
#WIMBLEDON : 26 de jun al 16 de jul de 2023
#US OPEN: 22 de ago al 10 de sept de 2023

csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_5.csv'
data = pd.read_csv(csv_path)
# Convertir la columna 'fecha' a tipo datetime
data['fecha'] = pd.to_datetime(data['fecha'], format='%Y-%m-%d', errors='coerce')

# Fechas de los Grand Slams en 2023
grand_slams = {
    'Australian_Open': (datetime(2023, 1, 8), datetime(2023, 1, 29)),
    'Roland_Garros': (datetime(2023, 5, 22), datetime(2023, 6, 11)),
    'Wimbledon': (datetime(2023, 6, 26), datetime(2023, 7, 16)),
    'US_Open': (datetime(2023, 8, 22), datetime(2023, 9, 10))
}

# Añadir un margen de 7 días antes y después de cada Grand Slam
margen = timedelta(days=7)
for slam, (start, end) in grand_slams.items():
    data[slam] = data['fecha'].apply(lambda x: 1 if x and (start - margen <= x <= end + margen) else 0)

data.to_csv( 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_6.csv', index=False)
