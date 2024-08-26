import pandas as pd

# Cargar el CSV con el que hemos trabajado
file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_7.csv'  # Actualiza esta ruta con la ruta correcta
data = pd.read_csv(file_path)

# Agregar la columna de identificador de fila
data.insert(0, 'ID', range(1, len(data) + 1))

# Guardar el DataFrame actualizado
data.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_8.csv', index=False)  # Actualiza esta ruta con la ruta deseada

# Verificar el resultado
print(data.head())
