# Pablo Villalba Brisa

Mi nombre es Pablo Villalba Brisa, y soy estudiante del Doble Grado en Ingeniería Informática y Administración de Empresas. Mi interés en programación se focaliza en la minería de datos y la inteligencia artificial en Python, aunque también tengo experiencia en el desarrollo de código en R para análisis estadístico y visualización de datos.

Este repositorio contiene una serie de programas para realizar web scraping, descargar posts de Instagram, extraer conocimiento de imágenes, preparar datos, y realizar análisisn estadístico en R. Dichos programas están organizados en diferentes secciones según su fin.

## Código del TFG Integrado:

### Web Scraping

- **`ScraperATP.py`**: Realiza el scraping de la web de la ATP para obtener la información de los jugadores.
- **`AgeScraper.py`**: Obtiene mediante scraping la edad de los jugadores de la web de la ATP.
- **`ContadorDeMarcas.py`**: Cuenta la frecuencia de aparición de marcas en los equipamientos patrocinados. No es un programa de scraping como tal, pero se desarrolla en esta fase.
- **`followersScrap.py`**: Obtiene mediante scraping el número total de posts, seguidores y seguidos de las cuentas de Instagram de los jugadores.

### Descarga de Posts

- **`Instaloader.py`**: Realiza la descarga de posts. La descarga de imágenes, vídeo y texto se produce satisfactoriamente, pero falla la descarga de los metadatos asociados al post. Este último problema lo soluciona el siguiente programa, `MetadataExtractor.py`. 
- **`MetadataExtractor.py`**: Descarga metadatos de los posts. Permite conectar con Instagram a través del nombre de los usuarios en los directorios generados en la descarga con `Instaloader.py`.
- **`SingleExtractor.py`**: Mismo funcionamiento que `MetadataExtractor.py`, pero para algún jugador concreto que haya podido faltar.
- **`SingleExtractor.py`**: Mismo funcionamiento que `Instaloader.py`, pero para algún jugador concreto que haya podido faltar.

### Extracción de conocimiento de las imágenes

- **`TennisInstruments.ipynb`**: clasifica las imágenes según si aparecen instrumentos de tenis en ellas.
- **`TextoEnImagen.ipynb`**: clasifica las imágenes según si aparece texto en ellas.
- **`RostrosEmociones.ipynb`**: clasifica las imágenes según el número de rostros detectados y la emoción predominante en ellos.

### Preparación de la Tabla de Datos

- **`HashMentionEmoteCounter.py`**: Cuenta el número de hashtags, menciones y emoticonos en el texto de los posts.
- **`0rostrosEmocionNeutra.py`**: Asigna el valor "neutral" a la columna emoción si el valor en la columna rostros es 0.
- **`atp_depurador.py`**: Corrige las comas en los premios monetarios.
- **`CuentaJugadores.py`**: Cuenta el número de jugadores distintos en la tabla de datos.
- **`detectarIdioma.py`**: Añade una columna que indica el idioma del texto de cada post.
- **`EliminarDuplicados.py`**: Elimina los duplicados del archivo original de la primera descarga inicial. Fue el programa que permitió ver que `Instaloader.py` descargó de forma errónea los metadatos de los posts.
- **`GrandSlam.py`**: Determina si un post fue publicado durante un Grand Slam según la fecha.
- **`idDeFila.py`**: Agrega una columna con identificadores de fila a la tabla.
- **`NanOrEmptyFixer.py`**: Reemplaza valores vacíos o NaN en la columna sponsors por "No hay sponsors".
- **`NoInstagramDrop.py`**: Filtra los jugadores que tienen una URL de Instagram, ya sea válida o no.
- **`sacaFinde.py`**: Indica si el post fue publicado en un fin de semana según la fecha.
- **`SacaFranjaHoraria.py`**: Determina la franja horaria de publicación del post según la hora.
- **`VariablesMarcas.py`**: Crea columnas que indican si una marca se encuentra en el equipamiento patrocinado del jugador.
- **`WordCount.py`**: Cuenta el número de palabras en el texto del post.

### Programas de Concatenado de Columnas de Variables y Unión de Tablas

- **`Merge.ipynb`**: Concatena las tablas de Instrumentos de tenis, Rostros, Emoción y Texto Detectado, a la tabla de metadatos.
- **`ConcatenarCSV.py`**: Concatena archivos CSV.
- **`concatFollowers.py`**: Añade las columnas de las variables de número de posts, seguidores y seguidos a un CSV.
- **`csvsIdiomas.py`**: Genera un CSV con cada idioma detectado.

### Construcción y evaluación de modelos

- **`01 analisis imagenes.Rmd`**: Realiza la carga y preprocesamiento de datos, la exploración de variables categóricas, el preprocesamiento de variables continuas, el estudio de correlaciones, la exploración de variables continuas, la generación y la evaluación de los modelos 1 y 2.
- **`01 analisis imagenes_LIWC.Rmd`**: Realiza la carga y preprocesamiento de datos, la exploración de variables categóricas, el preprocesamiento de variables continuas, el estudio de correlaciones, la exploración de variables continuas, la generación y la evaluación de los modelos 3 y 4.
- **`script_LATEX_SIN_LIWC.Rmd`**: Hace lo mismo que `01 analisis imagenes.Rmd`, pero añade tablas de modelos adicionales y prepara dichas tablas para Latex. También prepara los gráficos para Latex.
- **`script_LATEX_CON_LIWC.Rmd`**: Hace lo mismo que `01 analisis imagenes_LIWX.Rmd`, pero añade tablas de modelos adicionales y prepara dichas tablas para Latex. También prepara los gráficos para Latex.

## Entorno de Desarrollo

Los programas han sido desarrollados y probados utilizando estos entornos:

- **PyCharm**
- **RStudio**
- **Google Colaboratory**



 
