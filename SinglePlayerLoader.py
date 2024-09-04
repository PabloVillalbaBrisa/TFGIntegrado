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

str_profile = 'player'

ruta_archivo_destino = r'C:\Users\pvill\OneDrive\Documentos\TFG INTEGRADO\insta_posts.csv'

###################################################################################

def saca_posts_entre_fechas_incluidas(str_profile, dt_fecha_inicio, dt_fecha_final):

    L = Instaloader()
    profile = Profile.from_username(L.context, str_profile)
    posts = profile.get_posts()
    return [post for post in takewhile(lambda p: p.date > dt_fecha_inicio,
                                       dropwhile(lambda p: p.date > dt_fecha_final + timedelta(1), posts))]

def descarga_posts_entre_fechas_incluidas(str_profile, dt_fecha_inicio, dt_fecha_final, str_directorio):

    L = Instaloader(compress_json=False, save_metadata=False)  # no queremos la información sobre el nodo de Instagram
    profile = Profile.from_username(L.context, str_profile)
    posts = profile.get_posts()

    lista_filas = []

    n = 0
    for post in takewhile(lambda p: p.date > dt_fecha_inicio,
                          dropwhile(lambda p: p.date > dt_fecha_final + timedelta(1), posts)):

        L.download_post(post, str_directorio)

        n += 1

        fila = {}
        fila['num'] = 0
        fila['post'] = post.date.strftime('%Y-%m-%d_%H-%M-%S_UTC')
        fila['shortcode'] = post.shortcode
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

    for n_fila, fila in enumerate(reversed(lista_filas)):
        fila['num'] = n_fila + 1
        writer_csv = csv.DictWriter(destino_csv, fieldnames=columns)
        writer_csv.writerows(reversed(lista_filas))
    return n

###################################################################################

# INTERVALO TEMPORAL DE DESCARGA: EN ESTE CASO SERA UNA DESCARGA DE POSTS DEL AÑO 2023
INICIO = datetime(2023, 1, 1)
FINAL = datetime(2023, 12, 31)

# INICIO DE SESION EN INSTAGRAM
user = '********'
password = '********'
loader = Instaloader()
loader.login(user, password)
if loader.context.is_logged_in:
    print("Se ha iniciado sesión correctamente.")
else:
    print("No se ha podido iniciar sesión.")

columns = ['player', 'num', 'post', 'shortcode', 'fecha', 'hora', 'video', 'likes', 'comentarios', 'texto',
           'hashtags', 'geotags', 'is_sponsored', 'sponsor_users']

#CHECKPOINT DE ESCRITURA PARA RETOMAR LA ESCRITURA DONDE TOCABA
checkpoint = 0

#CONTINUAR ESCRITURA EN EL CHECKPOINT
with open(ruta_archivo_destino, 'r', newline='', encoding='utf-8') as destino_csv:
        reader_csv = csv.DictReader(destino_csv)
        for row in reader_csv:
            checkpoint += 1

with open(ruta_archivo_destino, 'a', newline='', encoding='utf-8') as destino_csv:
    print('Descargando posts en el directorio {}...'.format(str_profile))
    # INTRODUCIMOS UN TIEMPO DE ESPERA ALEATORIO ENTRE 1 Y 15 SEGUNDOS PARA REDUCIR EL RITMO DE LA DESCARGA Y QUE ESTA NO SEA ANULADA
    time.sleep(random.uniform(60, 120))
    n_posts = descarga_posts_entre_fechas_incluidas(str_profile, INICIO, FINAL, str_profile)
    print('OPERACIÓN FINALIZADA\n  Se han descargado {} posts de la cuenta de Instagram de {}'.format(n_posts, str_profile))