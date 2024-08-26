import csv
import os
import random
import time
from datetime import timedelta
from instaloader import Instaloader, Profile
import instaloader.exceptions
base_directory = 'C:/Users/pvill/PycharmProjects/TFG'

output_csv = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_limpio.csv'

# Configurar Instaloader
L = Instaloader(compress_json=False, save_metadata=False)
user = 'moonveilren18'
password = 'rellana19'
def iniciar_sesion():
    L.login(user, password)
    if L.context.is_logged_in:
        print("Se ha iniciado sesión correctamente.")
    else:
        print("No se ha podido iniciar sesión.")
        raise Exception("Error al iniciar sesión")

iniciar_sesion()

usuario_especifico = 'niki_kpoonacha'

# Inicializar CSV en modo 'append'
with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['username', 'post', 'shortcode', 'fecha', 'hora', 'video', 'likes', 'comentarios', 'texto', 'hashtags', 'is_sponsored', 'sponsors']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Si el archivo CSV está vacío, escribir los encabezados
    if os.path.getsize(output_csv) == 0:
        writer.writeheader()

    # Obtener el perfil del usuario
    try:
        profile = Profile.from_username(L.context, usuario_especifico)
        print(f"Perfil obtenido para {usuario_especifico}")

        # Almacenar los posts del perfil en una variable
        user_posts = list(profile.get_posts())

        # Ruta del directorio del usuario
        user_directory = os.path.join(base_directory, usuario_especifico)

        for image_file in os.listdir(user_directory):
            if image_file.endswith('UTC.jpg') or image_file.endswith('UTC_1.jpg'):
                if '2024' in image_file:
                    print(f"Post {image_file} es del 2024, saltando.")
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
                                'username': usuario_especifico,
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
                            # Esperar un tiempo aleatorio entre 1 y 20 segundos entre posts
                            time.sleep(random.uniform(1, 20))
                            break  # Salir del bucle después de encontrar el post correspondiente
                except instaloader.exceptions.QueryReturnedNotFoundException:
                    print(f"Post no encontrado para {usuario_especifico} con imagen {image_file}")
                except instaloader.exceptions.LoginRequiredException:
                    print("Redirigido a la página de inicio de sesión. Entrando en modo sleep.")
                    exit()
                except Exception as e:
                    if 'redirected to login' in str(e).lower() or '400' in str(e).lower():
                        print("Detectado redireccionamiento a la página de inicio de sesión. Deteniendo el programa.")
                        exit()  # Detener el programa
                    elif '401' in str(e).lower():
                        exit()
                    else:
                        print(f"Error al obtener metadatos para {os.path.join(user_directory, image_file)}: {e}")

        print(f"Metadatos guardados en {output_csv}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Perfil no encontrado para el usuario {usuario_especifico}")
    except Exception as e:
        print(f"Error al obtener el perfil de {usuario_especifico}: {e}")
        exit()
