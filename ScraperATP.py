import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(options=options)

#DIRECCION DE LA PAGINA WEB
driver.get('https://www.atptour.com/es/rankings/singles?RankRange=1-5000')

time.sleep(2)

html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

#OBTENCION DEL RANKING
xx = soup.find_all('td', class_='rank bold heavy')
ranking_list = [x.text for x in xx]
print(ranking_list)

#OBTENCION DEL NOMBRE
yy = soup.find_all('span', class_='lastName')
names_list = [y.text for y in yy]
print(names_list)

#OBTENCION DEL PUNTO
zz = soup.find_all('td', class_='points center bold extrabold')
points_list = [z.text.replace('\n', '').strip() for z in zz]
print(points_list)

#OBTENCION DE LOS JUGADORES
urls_list = ['https://www.atptour.com' + a['href'] for a in soup.select('.name a')]
print(urls_list)

#ELIMINACION DE DUPLICADOS
urls_set = set()
true_urls_list = []
true_ranking_list = []
for url, ranking in zip(urls_list, ranking_list):
    if url not in urls_set:
        urls_set.add(url)
        true_urls_list.append(url)
        true_ranking_list.append(ranking)
print(len(true_ranking_list))
print(len(true_urls_list))

#LISTA PARA ALMACENAR LOS DIFERENTES LINKS DE INSTAGRAM

instagram_list = []

#LISTA PARA ALMACENAR LOS PREMIOS DE LOS JUGADORES

prize_money_list = []

#LISTA PARA ALMACENAR LA FOTO DEL OVERVIEW DE CADA JUGADOR

photo_list = []

#LISTA PARA ALMACENAR LAS EQUIPACIONES DEL JUGADOR

equipment_list = []

#PARA CONTROLAR QUE URLS SE VAN A VISITAR, CADA BUCLE EXAMINA 500 ANTES DE GUARDAR EN CSV, EN TOTAL SON 2056 URLS
min_point = 0
max_point = 500
#min_point = 501
#max_point = 1000
#min_point = 1001
#max_point = 1500
#min_point = 1501
#max_point = 2000
#min_point = 2001
#max_point = 2055

contador_urls = 0

#PARA RECORRER LAS DIFERENTES URLS E IR OBTENIENDO INFORMACION DE LOS OVERVIEWS PARTICULARES DE CADA JUGADOR
for url in true_urls_list[min_point:]:
    contador_urls += 1
    if contador_urls > max_point:
        break
    driver.quit()
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    try:
        sencillos = driver.find_element(By.XPATH, "//a[text()='Sencillos']")
        sencillos.click()
    except Exception as e:
        print("Error al hacer clic en Sencillos:", e)
    time.sleep(2)
    pl_html = driver.page_source
    pl_soup = BeautifulSoup(pl_html, 'html.parser')
#OBTENCION DE LINK DE INSTAGRAM
    try:
        instagram_link = pl_soup.find("div", {"class": "social"})
        if instagram_link:
            try:
                instagram = instagram_link.find('a', {'href': re.compile(r'instagram', re.I)}).get('href')
                instagram_list.append(instagram)
                print(f"Instagram del Jugador: {instagram}")
            except AttributeError:
                instagram_list.append("El jugador no tiene Instagram")
                print("El jugador no tiene Instagram")
        else:
            instagram_list.append("El jugador no tiene Instagram")
            print("El jugador no tiene Instagram")
    except AttributeError:
        instagram_list.append("El jugador no tiene Instagram")
        print("El jugador no tiene Instagram")

#OBTENCION DE PREMIOS
    pp = pl_soup.find_all('div', class_='prize_money')

#SELECCION DE DATOS NUMERICOS GRACIAS AL MODULO RE
    prize_money = [re.sub(r'[^\d.]', '', p.text) for p in pp]

#CONCATENAMOS PRECIO ANUAL Y PRECIO DE CARRERA POR COMAS
    prize_money_list = ', '.join(prize_money)
    print(f"Premios: {prize_money_list}")

#OBTENCION DE IMAGENES DE JUGADORES
    try:
        photo = pl_soup.find("div", {"class": "player_image"})
        player_photo = photo.find('img', {'src': re.compile(r'player-gladiator-headshot', re.I)}).get('src')
        real_photo = ['https://www.atptour.com' + player_photo]
        print(real_photo)
        photo_list.append(real_photo)
    except AttributeError:
        photo_list.append("El jugador no tiene foto en el ATP")
        print("El jugador no tiene foto en el ATP")

    #OBTENCION DE EQUIPACION
    try:
        player_equipment = pl_soup.find("div", {"class": "atp_player-equipment"})
        equips = player_equipment.find_all("div", {"class": "atp_card small"})
        if equips:
            player_list = []
            for equip in equips:
                equipment = equip.find('h3', class_='title')
                text = equipment.text.strip()
                player_list.append(text)
            text = ", ".join(player_list)
            print(player_list)
            equipment_list.append(text)
        else:
                err_msg = "Se desconoce con que marcas trabaja el jugador"
                equipment_list.append(err_msg)
                print(err_msg)
    except AttributeError:
        err_msg = "Se desconoce con que marcas trabaja el jugador"
        equipment_list.append(err_msg)
        print(err_msg)
driver.quit()

#ESPECIFICAR LA RUTA DEL CSV
ruta_csv = r'C:\Users\Usuario\Documents\UPV.Documents\TFG INTEGRADO\atp_information.csv'

#CREACION DE DATAFRAME PARA ALMACENAR LOS DATOS OBTENIDOS
try:
    dataF = pd.read_csv(ruta_csv)
    min_length = min(len(true_ranking_list), len(names_list), len(points_list), len(true_urls_list),len(instagram_list), len(prize_money_list), len(photo_list), len(equipment_list))
    dataConc = pd.DataFrame({'Ranking': true_ranking_list[:min_length], 'Nombre': names_list[:min_length], 'Puntos': points_list[:min_length], 'URL': true_urls_list[:min_length],'Instagram': instagram_list[:min_length],'Premio monetario': prize_money_list[:min_length], 'Foto Jugador': photo_list[:min_length], 'Marcas Jugador': equipment_list[:min_length]})
    dataF = pd.concat([dataF, dataConc], ignore_index=True)

except FileNotFoundError:
    min_length = min(len(true_ranking_list), len(names_list), len(points_list), len(true_urls_list), len(instagram_list), len(prize_money_list), len(photo_list), len(equipment_list))
    dataF = pd.DataFrame({'Ranking': true_ranking_list[:min_length], 'Nombre': names_list[:min_length], 'Puntos': points_list[:min_length], 'URL': true_urls_list[:min_length],'Instagram': instagram_list[:min_length],'Premio monetario': prize_money_list[:min_length], 'Foto Jugador': photo_list[:min_length], 'Marcas Jugador': equipment_list[:min_length]})


#GUARDAR EL DATAFRAME EN EL ARCHIVO CSV ESPECIFICADO EN LA RUTA
dataF.to_csv(ruta_csv, index=False)

#PARA VER QUE LAS LISTAS TIENEN LA LONGITUD ADECUADA
print("Tamaño de true_ranking_list:", len(true_ranking_list))
print("Tamaño de names_list:", len(names_list))
print("Tamaño de points_list:", len(points_list))
print("Tamaño de true_urls_list:", len(true_urls_list))
print("Tamaño de instagram_list:", len(instagram_list))
print("Tamaño de prize_money_list:", len(prize_money_list))
print("Tamaño de photo_list:", len(photo_list))
print("Tamaño de equipment_list:", len(equipment_list))