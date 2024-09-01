# TFGIntegrado

Este repositorio contiene una serie de programas para realizar web scraping, descargar posts de Instagram, extraer conocimiento de imágenes, preparar datos, y realizar análisis en R. Dichos programas están organizados en diferentes secciones según su funcionalidad.

## Código del proyecto:

### Web Scraping

- **`ScraperATP.py`**: Realiza el scraping inicial.
- **`AgeScraper.py`**: Obtiene la edad de los jugadores.
- **`ContadorDeMarcas.py`**: Cuenta la frecuencia de aparición de marcas en los equipamientos patrocinados.
- **`followersScrap.py`**: Obtiene el número total de posts, seguidores y seguidos.

### Descarga de Posts

- **`Instaloader.py`**: Descarga de posts. La descarga de metadatos falló, pero los posts se guardan en directorios con los nombres de los usuarios.
- **`MetadataExtractor.py`**: Descarga metadatos de los posts. Permite conectar con Instagram a través del nombre de los usuarios en los directorios.

### Preparación de la Tabla de Datos

- **`HashMentionEmoteCounter.py`**: Cuenta el número de hashtags, menciones y emoticonos en el texto de los posts.
- **`0rostrosEmocionNeutra.py`**: Asigna el valor "neutral" a la columna emoción si el valor en la columna rostros es 0.
- **`atp_depurador.py`**: Corrige las comas en los premios monetarios.
- **`CuentaJugadores.py`**: Cuenta el número de jugadores distintos en la tabla de datos.
- **`detectarIdioma.py`**: Añade una columna que indica el idioma del texto de cada post.
- **`EliminarDuplicados.py`**: Elimina duplicados del archivo original de la primera descarga.
- **`GrandSlam.py`**: Determina si un post fue publicado durante un Grand Slam basado en la fecha.
- **`idDeFila.py`**: Agrega un identificador de fila a la tabla.
- **`NanOrEmptyFixer.py`**: Reemplaza valores vacíos o NaN en la columna sponsors por "No hay sponsors".
- **`NoInstagramDrop.py`**: Filtra los jugadores que tienen una URL de Instagram, ya sea válida o no.
- **`sacaFinde.py`**: Indica si el post fue publicado en un fin de semana según la fecha.
- **`SacaFranjaHoraria.py`**: Determina la franja horaria de publicación del post según la hora.
- **`VariablesMarcas.py`**: Crea columnas que indican si una marca se encuentra en el equipamiento patrocinado del jugador.
- **`WordCount.py`**: Cuenta el número de palabras en el texto del post.

### Programas de Concatenado de Columnas de Variables y Unión de Tablas

- **`ConcatenarCSV.py`**: Une archivos CSV.
- **`concatFollowers.py`**: Añade variables de posts, seguidores y seguidos a un CSV.
- **`csvsIdiomas.py`**: Genera un CSV con cada idioma detectado.

## Entorno de Desarrollo

Los programas han sido desarrollados y probados utilizando estos entornos:

- **PyCharm**
- **RStudio**
- **Google Colaboratory**

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas:

- `requests`
- `beautifulsoup4`
- `pandas`
- `instaloader`

Puedes instalar las dependencias usando pip:

```bash
pip install requests beautifulsoup4 pandas instaloader

 
