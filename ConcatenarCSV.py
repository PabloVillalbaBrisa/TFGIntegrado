import pandas as pd

csv1 = 'paolo_metadata.csv'
csv2 = 'atp_only_insta.csv'
output = 'paolo_metadata_2.csv'

df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

#SE AÑADEN ESTAS NUEVAS AL DF
cols_a_concatenar = ['Username', 'Puntos', 'Premio monetario', 'Edad', 'Marcas Jugador']
df2_ampliado = df2[cols_a_concatenar]

#CONCATENACIÓN POR NOMBRE DE USUARIO
merged_df = pd.merge(df1, df2_ampliado, left_on='username', right_on='Username', how='inner')

#ELIMINAR COLUMNAS DUPLICADAS
merged_df = merged_df.drop(columns=['Username'])

merged_df.to_csv(output, index=False)

print(f"GUARDADO EN: {output}")




