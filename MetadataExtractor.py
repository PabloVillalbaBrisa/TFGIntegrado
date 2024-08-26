import os
import csv
import random
import time
from datetime import timedelta
from instaloader import Instaloader, Profile
import instaloader.exceptions

# Ruta del directorio base donde se encuentran los subdirectorios
base_directory = 'PycharmProjects/TFG'

# Archivo CSV de salida
output_csv = 'metadata.csv'

# Archivo de registros para evitar duplicados
log_file = 'log.csv'

user = '********'
password = '********'

# Configurar Instaloader
L = Instaloader(compress_json=False, save_metadata=False)

def iniciar_sesion():
    L.login(user, password)
    if L.context.is_logged_in:
        print("Se ha iniciado sesión correctamente.")
    else:
        print("No se ha podido iniciar sesión.")
        raise Exception("Error al iniciar sesión")

iniciar_sesion()

# Leer los identificadores de posts ya procesados
processed_posts = set()
if os.path.exists(log_file):
    with open(log_file, 'r', newline='', encoding='utf-8') as logfile:
        reader = csv.reader(logfile)
        for row in reader:
            processed_posts.add(row[0])

# Función para guardar los posts procesados en el archivo de registros
def guardar_log():
    with open(log_file, 'w', newline='', encoding='utf-8') as logfile:
        writer = csv.writer(logfile)
        for post_id in processed_posts:
            writer.writerow([post_id])

# Lista de usuarios a excluir
usuarios_excluir = {'camilougo', 'cem.ilkel', 'dmitrypopko', 'ferverdasco', 'bernard_tomic', 'roko_horvat1'}

# Inicializar CSV en modo 'append'
with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['username', 'post', 'shortcode', 'fecha', 'hora', 'video', 'likes', 'comentarios', 'texto', 'hashtags', 'is_sponsored', 'sponsors']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Si el archivo CSV está vacío, escribir los encabezados
    if os.path.getsize(output_csv) == 0:
        writer.writeheader()

    # Recorrer subdirectorios
    for root, dirs, files in os.walk(base_directory):
        for subdir in dirs:
            username = subdir
            if username in usuarios_excluir:
                print(f"Usuario {username} excluido, saltando.")
                continue
            user_directory = os.path.join(root, subdir)
            try:
                # Verificar si hay posts por procesar para este usuario
                posts_por_procesar = False
                for image_file in os.listdir(user_directory):
                    if (image_file.endswith('UTC.jpg') or image_file.endswith('UTC_1.jpg')) and \
                       not any(f"{username}_" in post_id for post_id in processed_posts):
                        posts_por_procesar = True
                        break

                if not posts_por_procesar:
                    print(f"No hay posts por procesar para el usuario {username}, saltando.")
                    continue

                # Obtener el perfil del usuario
                profile = Profile.from_username(L.context, username)
                print(f"Perfil obtenido para {username}")

                # Almacenar los posts del perfil en una variable
                user_posts = list(profile.get_posts())

                for image_file in os.listdir(user_directory):
                    if image_file.endswith('UTC.jpg') or image_file.endswith('UTC_1.jpg'):
                        post_identifier = f"{username}_{image_file.split('_UTC')[0]}"
                        if post_identifier in processed_posts:
                            print(f"Post {post_identifier} ya procesado, saltando.")
                            continue
                        if '2024' in image_file:
                            print(f"Post {post_identifier} es del 2024, saltando.")
                            continue
                        print(f"Procesando imagen: {image_file}")
                        try:
                            # Buscar el post correspondiente a la imagen
                            for post in user_posts:
                                if post.date.strftime('%Y-%m-%d_%H-%M-%S_UTC') in image_file:
                                    # Obtener los metadatos del post
                                    is_sponsored = False
                                    sponsors = []
                                    try:
                                        is_sponsored = post.is_sponsored
                                        sponsors = [user.username for user in post.sponsor_users]
                                    except AttributeError:
                                        print(f"El post {post.shortcode} no tiene información de patrocinio disponible.")

                                    post_data = {
                                        'username': username,
                                        'post': post.date.strftime('%Y-%m-%d_%H-%M-%S_UTC'),
                                        'shortcode': post.shortcode,
                                        'fecha': (post.date + timedelta(hours=1)).strftime('%Y-%m-%d'),
                                        'hora': (post.date + timedelta(hours=1)).strftime('%H:%M:%S'),
                                        'video': 1 if post.is_video else 0,
                                        'likes': post.likes,
                                        'comentarios': post.comments,
                                        'texto': post.caption.replace('\n', ' ').replace('\r', ' ') if post.caption else '',
                                        'hashtags': '; '.join(list(set(post.caption_hashtags))),
                                        'is_sponsored': is_sponsored,
                                        'sponsors': '; '.join(sponsors)
                                    }
                                    # Escribir los metadatos en el CSV
                                    writer.writerow(post_data)
                                    processed_posts.add(post_identifier)
                                    guardar_log()  # Guardar el log después de cada post
                                    # Esperar un tiempo aleatorio entre 1 y 20 segundos entre posts
                                    time.sleep(random.uniform(1, 20))
                                    break  # Salir del bucle después de encontrar el post correspondiente
                        except instaloader.exceptions.QueryReturnedNotFoundException:
                            print(f"Post no encontrado para {username} con imagen {image_file}")
                        except instaloader.exceptions.LoginRequiredException:
                            print("Redirigido a la página de inicio de sesión. Entrando en modo sleep.")
                            guardar_log()  # Guardar el log antes de detener el programa
                            exit()
                        except Exception as e:
                            if 'redirected to login' in str(e).lower() or '400' in str(e).lower():
                                print("Detectado redireccionamiento a la página de inicio de sesión. Deteniendo el programa.")
                                guardar_log()  # Guardar el log antes de detener el programa
                                exit()  # Detener el programa
                            elif '401' in str(e).lower():
                                guardar_log()
                                exit()
                            else:
                                print(f"Error al obtener metadatos para {os.path.join(user_directory, image_file)}: {e}")
                # Esperar un tiempo aleatorio entre 1 y 2 minutos entre usuarios
                time.sleep(random.uniform(60, 180))

            except instaloader.exceptions.ProfileNotExistsException:
                print(f"Perfil no encontrado para el usuario {username}")
            except Exception as e:
                print(f"Error al obtener el perfil de {username}: {e}")
                exit()

    print(f"Metadatos guardados en {output_csv}")


