import pandas as pd

csv1 = pd.read_csv('followers_data1.csv')
csv2 = pd.read_csv('English_LIWC.csv')

#SELECCIONAMOS LAS COLUMNAS QUE QUEREMOS CONCATENAR Y SE RENOMBRA POSTS
csv1_sel = csv1[['username', 'posts', 'followers', 'following']].rename(columns={'posts': 'publicaciones'})

#CONCATENAMOS POR NOMBRE DE USUARIO
merged_df = pd.merge(csv2, csv1_sel, on='username', how='left')

#CAMBIAMOS EL TIPO DE LAS 3 COLUMNAS A COMA FLOTANTE CON ASTYPE DE PANDAS
for column in ['publicaciones', 'followers', 'following']:
    merged_df[column] = merged_df[column].astype(float)

merged_df.to_csv('English_LIWC.csv', index=False)

