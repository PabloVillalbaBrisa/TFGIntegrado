import pandas as pd
import instaloader
from instaloader import Post
import time

# Inicializar Instaloader
L = instaloader.Instaloader()

# Leer el archivo CSV original
df = pd.read_csv("C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/insta_posts_nodupes.csv")

# Crear una lista para almacenar los nombres de usuario
usernames = []

# Función para obtener el nombre de usuario de un shortcode
def get_username(shortcode):
    try:
        post = Post.from_shortcode(L.context, shortcode)
        username = post.owner_username
        print(f"Usuario encontrado para el shortcode {shortcode}: {username}")
        return username
    except Exception as e:
        print(f"Error al obtener el usuario para el shortcode {shortcode}: {e}")
        return None

# Iterar sobre cada shortcode y obtener el nombre de usuario correspondiente
for shortcode in df['shortcode']:
    username = get_username(shortcode)
    usernames.append(username)
    time.sleep(60)  # Añadir un retraso para evitar el rate limiting

# Añadir la nueva columna al DataFrame
df['username'] = usernames

# Guardar el DataFrame resultante en un nuevo archivo CSV
df.to_csv("C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/insta_users_posts.csv", index=False)