# Proyecto de Interacción con Google Gemini API

Este proyecto de ejemplo demuestra cómo interactuar con la API de Google Gemini (usando el modelo gemini-1.5-flash-latest) utilizando Python.

## Requisitos

* Python 3.10+ (recomendado usar `pyenv` o `venv` para entornos virtuales)
* Una clave API de Google AI Studio / Google Cloud para la API de Gemini.

## Configuración

1.  Clona este repositorio (si lo subes a Git).
2.  Navega al directorio del proyecto:
    ```bash
    cd nombre-de-la-carpeta
    ```
3.  (Opcional pero recomendado) Crea y activa un entorno virtual:
    ```bash
    # Usando venv (incorporado en Python 3.3+)
    python -m venv .venv
    source .venv/bin/activate # En Linux/macOS
    # .venv\Scripts\activate # En Windows

    # O usando pyenv (si lo usas para gestionar versiones de Python)
    # pyenv virtualenv 3.10.13 api-env # Crea el entorno si no existe
    # pyenv activate api-env
    ```
4.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt # Necesitarás crear este archivo después (ver abajo)
    ```
    O instalalas manualmente:
    ```bash
    pip install google-generativeai python-dotenv
    ```
5.  Crea un archivo `.env` en la raíz del proyecto y añade tu clave API:
    ```dotenv
    API_KEY="TU_CLAVE_API_AQUI"
    ```
    **¡No compartas tu archivo `.env` ni subas este archivo a Git!**

## Uso

Ejecuta el script principal:

```bash
python app.py
# api_ia

### Probando la app: Enviando prompt al modelo: '¿Puedes darme algunas ideas de proyectos en Python usando la apikey de IA de Google?'

Respuesta del modelo:
La API de IA de Google ofrece un amplio abanico de posibilidades para proyectos en Python.  Para darte ideas concretas, necesito saber qué APIs de Google Cloud AI específicamente te interesan (por ejemplo,  Natural Language, Vision, Translation, Speech-to-Text, etc.).  Sin embargo, aquí te doy algunas ideas, agrupadas por tipo de API, que puedes adaptar a tus intereses:

**Si usas la API de Google Cloud Natural Language:**

* **Análisis de sentimientos de reseñas de productos:**  Recolecta reseñas de productos de un sitio web (scraping web) y utiliza la API para determinar el sentimiento (positivo, negativo, neutral) expresado en cada reseña.  Puedes visualizar los resultados en un gráfico o generar un resumen general del sentimiento del producto.
* **Extracción de entidades nombradas:** Crea un programa que identifique personas, organizaciones, lugares y otros conceptos clave en un texto.  Esto podría ser útil para analizar noticias, artículos académicos o incluso literatura.
* **Análisis de temas en un corpus de texto:**  Utiliza la API para identificar los temas principales que se discuten en un conjunto de documentos.  Imagina analizar un conjunto de tweets sobre un tema en particular para identificar las tendencias de conversación.
* **Resumen automático de textos:** Crea una herramienta que resuma automáticamente artículos de noticias o documentos largos, utilizando las capacidades de la API para generar resúmenes concisos y relevantes.


**Si usas la API de Google Cloud Vision:**

* **Clasificador de imágenes:** Desarrolla un programa que clasifique imágenes según su contenido (ej: gato, perro, paisaje, etc.).  Puedes expandirlo para crear un sistema de etiquetado automático de imágenes.
* **Detección de objetos en imágenes:**  Crea una aplicación que detecte objetos específicos en imágenes (ej: coches, personas, señales de tráfico).  Esto podría utilizarse para aplicaciones de seguridad o automatización.
* **Reconocimiento de texto en imágenes (OCR):**  Desarrolla una herramienta que extraiga texto de imágenes, útil para digitalizar documentos o analizar imágenes con información textual.
* **Análisis de emociones en rostros:**  Utiliza la API para detectar y analizar las emociones expresadas en rostros humanos dentro de una imagen.


**Si usas la API de Google Cloud Translation:**

* **Traductor multilingüe:** Crea un traductor que pueda traducir texto entre varios idiomas.  Puedes agregar funciones adicionales, como la detección automática del idioma de origen.
* **Análisis de la traducción de textos literarios:** Compara traducciones de un texto literario en diferentes idiomas para analizar las diferencias en el estilo y la precisión.


**Si usas otras APIs (Speech-to-Text, Dialogflow, etc.):**

* **Transcripción automática de audio:**  Convierte archivos de audio a texto utilizando la API Speech-to-Text.  Puedes aplicarlo a podcasts, entrevistas o cualquier otro archivo de audio.
* **Chatbot inteligente:**  Integra Dialogflow para crear un chatbot con capacidades de conversación natural.  Este chatbot podría responder preguntas, realizar tareas o proporcionar información.


Recuerda que antes de comenzar cualquier proyecto, debes:

1. **Crear un proyecto en Google Cloud Platform (GCP).**
2. **Habilitar las APIs necesarias.**
3. **Obtener una clave de API.**
4. **Instalar la librería de cliente de Python para la API que estés utilizando.**


Estos son solo algunos ejemplos; las posibilidades son infinitas.  La clave está en identificar un problema que te interese resolver y explorar cómo las APIs de Google Cloud AI pueden ayudarte a lograrlo.  Recuerda consultar la documentación de cada API para entender sus capacidades y limitaciones.