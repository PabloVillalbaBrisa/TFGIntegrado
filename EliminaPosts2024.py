import pandas as pd

# Nombre del archivo CSV
csv_file = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata.csv'

try:
    df = pd.read_csv(csv_file, on_bad_lines='skip')
    print("CSV file loaded successfully")

    # Eliminar filas donde la columna 'post' contenga '2024'
    df.drop(df[df['post'].str.contains('2024', na=False)].index, inplace=True)

    # Guardar el DataFrame filtrado en un nuevo archivo CSV
    output_csv_file = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_final.csv'
    df.to_csv(output_csv_file, index=False)

    print(f"Filtered CSV file saved to {output_csv_file}")
except pd.errors.ParserError as e:
    print(f"Error reading the CSV file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
