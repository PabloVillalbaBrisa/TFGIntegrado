import pandas as pd

file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_7.csv'  # Actualiza esta ruta con la ruta correcta
data = pd.read_csv(file_path)

data.insert(0, 'ID', range(1, len(data) + 1))

data.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_8.csv', index=False)  # Actualiza esta ruta con la ruta deseada
