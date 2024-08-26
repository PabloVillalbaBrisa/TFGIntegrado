# -*- coding: utf-8 -*-

#   Objetivo: pruebas con instagram

import csv
import time
import random
from instaloader import Instaloader, Profile
from instaloader.exceptions import *
from datetime import datetime
from datetime import timedelta
from itertools import dropwhile, takewhile
from os import listdir, mkdir

ruta_archivo_origen = r'C:\Users\pvill\OneDrive\Documentos\TFG INTEGRADO\atp_information.csv'
ruta_archivo_destino = r'C:\Users\pvill\OneDrive\Documentos\TFG INTEGRADO\insta_posts.csv'

# DEFINICION DE FUNCIONES QUE SE VAN A EMPLEAR PARA LA DESCARGA

def saca_posts_entre_fechas_incluidas(str_profile, dt_fecha_inicio, dt_fecha_final):
    # fecha_inicio y la fecha_final han de estar en datetime
    # devuelve una lista de posts

    L = Instaloader()
    profile = Profile.from_username(L.context, str_profile)
    posts = profile.get_posts()
    return [post for post in takewhile(lambda p: p.date > dt_fecha_inicio,
                                       dropwhile(lambda p: p.date > dt_fecha_final + timedelta(1), posts))]


def descarga_posts_entre_fechas_incluidas(str_profile, dt_fecha_inicio, dt_fecha_final, str_directorio):
    # OJO: la fecha_inicio y la fecha_final han de estar en datetime
    # guarda los posts entre las fechas indicadas (ambas inclusiva) y genera un archivo resumen en formato csv
    # devuelve el número de posts que se han grabado

    # gestor de instagram
    L = Instaloader(compress_json=False, save_metadata=False)  # no queremos la información sobre el nodo de Instagram
    profile = Profile.from_username(L.context, str_profile)
    posts = profile.get_posts()

    lista_filas = []

    # contador
    n = 0
    for post in takewhile(lambda p: p.date > dt_fecha_inicio,
                          dropwhile(lambda p: p.date > dt_fecha_final + timedelta(1), posts)):

        # grabamos el post
        L.download_post(post, str_directorio)

        # incrementamos el contador
        n += 1

        # preparamos la tabla resumen
        fila = {}
        fila['num'] = 0  # posteriormente lo actualizamos
        fila['post'] = post.date.strftime('%Y-%m-%d_%H-%M-%S_UTC')
        fila['shortcode'] = post.shortcode
        # ajustamos la hora de UTC a horario en España
        dt_post_corregido = post.date + timedelta(hours=1)
        fila['fecha'] = dt_post_corregido.strftime('%Y-%m-%d')
        fila['hora'] = dt_post_corregido.strftime('%H:%M:%S')
        if post.is_video:
            fila['video'] = 1
        else:
            fila['video'] = 0
        fila['likes'] = post.likes
        fila['comentarios'] = post.comments
        if post.caption is not None:
            fila['texto'] = post.caption.replace('\n', ' ').replace('\r', ' ')
        else:
            fila['texto'] = ""
        fila['hashtags'] = '; '.join(list(set(post.caption_hashtags)))
        try:
            geotags = post.location
            if geotags:
                fila['geotags'] = geotags.name
            else:
                fila['geotags'] = "Sin localización especificada"
        except InstaloaderException as ex:
            print(f"Error al obtener la localización geográfica del post: {ex}")
            fila['geotags'] = "Sin localización especificada"
        fila['is_sponsored'] = False
        fila['sponsor_users'] = []
        try:
            fila['is_sponsored'] = post.is_sponsored
            if fila['is_sponsored']:
                sponsor_users = post.sponsor_users
                if sponsor_users:
                    sponsored_users_list = []
                    for sponsor in sponsor_users:
                        sponsored_users_list.append(sponsor.username)
                    fila['sponsor_users'] = sponsored_users_list
        except Exception as e:
            print(f"Error al procesar el post: {e}")
            fila['is_sponsored'] = False
            fila['sponsor_users'] = []

        lista_filas.append(fila)

    # actualizamos el indice de los posts y guardamos el resumen
    for n_fila, fila in enumerate(reversed(lista_filas)):
        # Actualiza el número de la fila
        fila['num'] = n_fila + 1
        # Escribe la fila al archivo CSV destino
        writer_csv = csv.DictWriter(destino_csv, fieldnames=columns)
        writer_csv.writerows(reversed(lista_filas))
    return n


#######################################################################################################################

# INTERVALO TEMPORAL DE DESCARGA: EN ESTE CASO SERA UNA DESCARGA DE POSTS DEL AÑO 2023
INICIO = datetime(2023, 1, 1)
FINAL = datetime(2023, 12, 31)

# INICIO DE SESION EN INSTAGRAM
user = 'pwindTennis2024'
password = 'paoloposts2024'
loader = Instaloader()
loader.login(user, password)
if loader.context.is_logged_in:
    print("Se ha iniciado sesión correctamente.")
else:
    print("No se ha podido iniciar sesión.")

# Nombres de las columnas del CSV
columns = ['player', 'num', 'post', 'shortcode', 'fecha', 'hora', 'video', 'likes', 'comentarios', 'texto',
           'hashtags', 'geotags', 'is_sponsored', 'sponsor_users']

#PARA CONTROLAR QUE CUENTAS SE VAN A VISITAR, CADA EJECUCIÓN EXAMINA 15 ANTES DE GUARDAR EN CSV, EN TOTAL SON 507 CUENTAS
#min_point = 0 max_point = 15
#min_point = 15 max_point = 30
#min_point = 30 max_point = 45
#min_point = 45 max_point = 60
#min_point = 60 max_point = 75
#min_point = 75 max_point = 90
#min_point = 90 max_point = 105
#min_point = 120 max_point = 135
#min_point = 135 max_point = 150
#min_point = 150 max_point = 165
#min_point = 165 max_point = 180
#min_point = 180 max_point = 195
#min_point = 195 max_point = 210
#min_point = 210 max_point = 225
#min_point = 225 max_point = 240
#min_point = 240 max_point = 255
#min_point = 255 max_point = 270
#min_point = 270 max_point = 285
#min_point = 285 max_point = 300
#min_point = 300 max_point = 315
#min_point = 315 max_point = 330
#min_point = 330 max_point = 345
#min_point = 345 max_point = 360
#min_point = 360 max_point = 375
#min_point = 375 max_point = 390
#min_point = 390 max_point = 405
#min_point = 405 max_point = 420
#min_point = 420 max_point = 435
#min_point = 435 max_point = 450
#min_point = 450 max_point = 465
#min_point = 465 max_point = 480
#min_point = 480 max_point = 495
min_point = 1921
max_point = 2056


#CHECKPOINT DE ESCRITURA PARA RETOMAR LA ESCRITURA DONDE TOCABA
checkpoint = 0

#CONTINUAR ESCRITURA EN EL CHECKPOINT
with open(ruta_archivo_destino, 'r', newline='', encoding='utf-8') as destino_csv:
        reader_csv = csv.DictReader(destino_csv)
        for row in reader_csv:
            checkpoint += 1

with open(ruta_archivo_destino, 'a', newline='', encoding='utf-8') as destino_csv:
    # LECTURA DE ATP INFORMATION Y LLAMADA A LA FUNCION QUE DESCARGA LOS POSTS
    counter = 0
    with open(ruta_archivo_origen, 'r', newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        # SE ABRE PARA ESCRITURA EL ARCHIVO DESTINO
        for _ in range(min_point):
            next(lector_csv)
        while counter < max_point:
            for fila in lector_csv:
                if 'instagram.com' in fila['Instagram']:
                    counter += 1
                    player_name = fila['Nombre']
                    str_profile = fila['Instagram'].split("instagram.com/")[1].split("/")[0]
                    if '?' in str_profile:
                        str_profile = str_profile.split("?")[0]
                    print(player_name)
                    print(str_profile)
                    if str_profile not in listdir('.'):
                        mkdir(str_profile)
                    print('Descargando posts en el directorio {}...'.format(str_profile))
                    # INTRODUCIMOS UN TIEMPO DE ESPERA ALEATORIO ENTRE 1 Y 15 SEGUNDOS PARA REDUCIR EL RITMO DE LA DESCARGA Y QUE ESTA NO SEA ANULADA
                    time.sleep(random.uniform(60, 120))
                    n_posts = descarga_posts_entre_fechas_incluidas(str_profile, INICIO, FINAL, str_profile)
                    print('OPERACIÓN FINALIZADA\n  Se han descargado {} posts de la cuenta de Instagram de {}'.format(n_posts, str_profile))
                if counter >= max_point:
                    break
        print('Descarga de posts de todos los jugadores de la tanda finalizada')

print("Cuentas de Instagram obtenidas:", (counter))