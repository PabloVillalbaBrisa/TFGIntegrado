from bs4 import BeautifulSoup
import pandas as pd

#SE ABRE EL HTML QUE GUARDA LA PÁGINA DEL ATP DEL 2023
with open("Rankings _ Pepperstone ATP Rankings (Individual) _ ATP Tour _ Tenis _ ATP Tour _ Tennis.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

#SE TRABAJA CON BEAUTIFULSOUP PARA ENCONTRAR LOS ELEMENTOS QUE SE QUIEREN PARA EL DICCIONARIO
xx = soup.find_all('td', class_='age')
age_list = [x.text for x in xx]
print(age_list)

yy = soup.find_all('span', class_='lastName')
name_list = [y.text for y in yy]
print(name_list)

#CON ESTE DICCIONARIO, TENEMOS ASOCIADOS LOS JUGADORES CON SU EDAD
name_age_map = dict(zip(name_list, age_list))

df = pd.read_csv("atp_information_with_usernames.csv")
#AÑADIMOS LA COLUMNA EDAD
df["Edad"] = df["Nombre"].map(name_age_map)
df.to_csv("atp_information_with_age.csv", index=False)