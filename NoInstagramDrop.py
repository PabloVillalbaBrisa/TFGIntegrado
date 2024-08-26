import pandas as pd

# Ruta del archivo CSV
csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/atp_information_R.csv'
output_csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/atp_only_insta.csv'

# Leer el archivo CSV
df = pd.read_csv(csv_path)

# Filtrar las filas que contienen el mensaje "El jugador no tiene Instagram"
df_filtered = df[df['Instagram'] != 'El jugador no tiene Instagram']

# Guardar el DataFrame filtrado en un nuevo archivo CSV
df_filtered.to_csv(output_csv_path, index=False)

print(f"Las filas sin links de Instagram han sido eliminadas y el resultado se ha guardado en {output_csv_path}")