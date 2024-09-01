import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import random

options = Options()
#DRIVER DE SELENIUM
driver = webdriver.Chrome(options=options)


#ESTA FUNCIÓN LIMPIA EL TEXTO, CONVIERTE LOS NÚMEROS EN NOTACIÓN K A MILES
# Y LOS NÚMEROS EN NOTACIÓN M A MILLONES
def clean_text(text):
    text = text.replace(',', '').replace('.', '')
    text = re.sub(r'[^\dKM]', '', text)
    if 'K' in text:
        return str(int(float(text.replace('K', '')) * 1000))
    elif 'M' in text:
        return str(int(float(text.replace('M', '')) * 1000000))
    else:
        return text


#ESTA FUNCIÓN OBTIENE EL PERFIL DEL USUARIO
def get_profile_info(username):
    url = f'https://www.instagram.com/{username}/'
    driver.get(url)

    time.sleep(5)

    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    profile_data = {}
    profile_data['username'] = username

    #USAMOS BEAUTIFULSOUP PARA SELECCIONAR LOS ELEMENTOS QUE QUEREMOS SCRAPEAR
    try:
        stats = soup.select('ul.x78zum5 li.xl565be button._acan span._ac2a')
        profile_data['posts'] = clean_text(stats[0].text) if len(stats) > 0 else 'N/A'
        profile_data['followers'] = clean_text(stats[1].text) if len(stats) > 1 else 'N/A'
        profile_data['following'] = clean_text(stats[2].text) if len(stats) > 2 else 'N/A'
    except Exception as e:
        profile_data['posts'] = 'N/A'
        profile_data['followers'] = 'N/A'
        profile_data['following'] = 'N/A'
        print(f"Error retrieving profile data for {username}: {e}")

    return profile_data


#CARGA DEL CSV
file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_8.csv'
data = pd.read_csv(file_path)

#CARGA DE LA LISTA DE USUARIOS
usernames_list = data['username'].unique().tolist()

#EN ESTE CSV VAMOS GUARDANDO LOS DATOS DE LAS ITERACIONES
output_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/provisional.csv'

if os.path.exists(output_path):
    processed_data = pd.read_csv(output_path)
    processed_usernames = processed_data['username'].tolist()
else:
    processed_data = pd.DataFrame(columns=['username', 'posts', 'followers', 'following'])
    processed_usernames = []

#SE VAN EXAMINANDO LOS USUARIOS
for username in usernames_list:
    #LOS USUARIOS PROCESADOS SE SALTAN
    if username in processed_usernames:
        continue

    profile_info = get_profile_info(username)
    profile_info_df = pd.DataFrame([profile_info])
    processed_data = pd.concat([processed_data, profile_info_df], ignore_index=True)

    #GUARDADO DE LOS DATOS
    processed_data.to_csv(output_path, index=False)
    #SE IMPRIME EL USUARIO PROCESADO
    print(f"Processed user: {username}")
    #TIEMPO DE ESPERA PRUDENCIAL ENTRE 1 Y 2 MINS
    wait_time = random.randint(60, 120)
    time.sleep(wait_time)

#SE CIERRA EL DRIVER DE SELENIUM
driver.quit()

# Guardar los datos completos en un nuevo archivo CSV
final_output_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/followers_data.csv'
processed_data.to_csv(final_output_path, index=False)

#MOSTRAR LOS DATOS QUE SE HAN PROCESADO
print(processed_data.head())





