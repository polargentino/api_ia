import google.generativeai as genai
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Configura tu clave API leyendo la variable de entorno
API_KEY = os.getenv('API_KEY')

# Verifica si la clave API se cargó correctamente
if not API_KEY:
    print("Error: No se encontró la variable de entorno 'API_KEY'.")
    print("Asegúrate de tener un archivo .env con API_KEY='TU_CLAVE_API_AQUI'")
    print("O de haber exportado la variable de entorno en tu terminal.")
    exit()

genai.configure(api_key=API_KEY)

# Elige el modelo adecuado para chat
# 'gemini-pro' es un modelo comúnmente usado para tareas conversacionales
# 'gemini-1.5-flash-latest' también funciona
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Iniciar una sesión de chat ---
print("--- Iniciando sesión de chat (Escribe 'salir' o 'quit' para terminar) ---")
chat = model.start_chat(history=[])

# --- Bucle interactivo de chat ---
while True:
    try:
        # Pedir entrada al usuario
        user_message = input("Tú: ")

        # Verificar si el usuario quiere salir
        if user_message.lower() in ['salir', 'quit', 'exit']:
            break # Salir del bucle

        # Si el mensaje no está vacío
        if user_message:
            # Enviar el mensaje en el contexto de la conversación actual
            response = chat.send_message(user_message)

            # Imprimir la respuesta del modelo
            print("Gemini:")
            # Manejar respuestas que puedan no tener texto (ej: bloqueos de seguridad)
            if response.text:
                print(response.text)
            else:
                # Si no hay texto, imprimir detalles del bloqueo o la respuesta cruda
                # Esto es útil para depuración
                print("[El modelo no proporcionó texto. Posiblemente debido a un bloqueo de seguridad o un error.]")
                # print("Respuesta completa:", response) # Descomenta si quieres ver la respuesta cruda

    except Exception as e:
        # Capturar errores durante el envío del mensaje (red, API, etc.)
        print(f"\nOcurrió un error al enviar el mensaje: {e}")
        print("Por favor, intenta tu mensaje de nuevo.")
    except EOFError: # Manejar Ctrl+D
        break


print("\n--- Sesión de chat terminada ---")

# Opcional: Mostrar el historial completo al final
# print("\nHistorial completo de la sesión:")
# for message in chat.history:
#    print(f"{message.role}: {message.parts[0].text}")

'''
--- Iniciando sesión de chat (Escribe 'salir' o 'quit' para terminar) ---
Tú: sabes que es la API de Google Generative AI? ¿Qué proyectos .py puedo hacer con ella?
Gemini:
La API de Google Generative AI (anteriormente conocida como Generative Language API) es una interfaz de programación de aplicaciones que permite a los desarrolladores acceder y utilizar los potentes modelos de lenguaje grandes (LLM) de Google.  Estos modelos son capaces de generar texto, traducir idiomas, escribir diferentes tipos de contenido creativo y responder a tus preguntas de forma informativa.  En esencia, te permite integrar la inteligencia artificial generativa de Google en tus propias aplicaciones.

A diferencia de otras APIs de IA generativa,  Google Generative AI se centra en la calidad y la responsabilidad.  Esto significa que está diseñada para ser menos propensa a generar contenido inapropiado o dañino, aunque esto no elimina la necesidad de supervisión y buenas prácticas.


**Proyectos .py que puedes hacer con la API de Google Generative AI:**

Estos son algunos ejemplos, categorizados por nivel de complejidad:

**Nivel Principiante:**

* **Chatbot simple:** Crea un chatbot básico que responda a preguntas del usuario utilizando la API. Puedes enfocarlo en un tema específico (ej: un chatbot sobre historia, o uno que explique conceptos científicos).
* **Generador de historias:**  Un programa que genere historias cortas basadas en una frase o palabra clave que el usuario proporcione.
* **Traductor simple:**  Un traductor básico entre dos idiomas, utilizando la capacidad de traducción de la API.
* **Generador de resúmenes:**  Un script que toma un texto largo como entrada y genera un resumen conciso.

**Nivel Intermedio:**

* **Aplicación para escribir diferentes tipos de contenido:** Crea una herramienta que ayude a los usuarios a generar diferentes tipos de contenido, como poemas, código, guiones, correos electrónicos, etc., con diferentes estilos y tonos.
* **Aplicación para mejorar la escritura:** Un programa que analice la escritura del usuario y sugiera mejoras en gramática, estilo y claridad, utilizando la capacidad de la API para procesar lenguaje natural.
* **Herramienta para creación de preguntas y respuestas:** Genera preguntas y respuestas a partir de un texto dado, ideal para crear material de estudio.
* **Integración con otras APIs:** Combina la API de Google Generative AI con otras APIs (ej: una API de búsqueda de imágenes) para crear aplicaciones más complejas.  Por ejemplo, podrías crear una aplicación que genere descripciones de imágenes a partir de una imagen subida por el usuario.


**Nivel Avanzado:**

* **Asistente personal inteligente:**  Crea un asistente virtual más sofisticado que pueda realizar tareas complejas, como programar citas, enviar correos electrónicos, buscar información y generar reportes.
* **Sistema de recomendación personalizado:**  Utiliza la API para analizar las preferencias del usuario y recomendar contenido relevante (ej: películas, libros, música).
* **Herramienta para la creación de juegos de texto interactivos:** Genera historias y diálogos dinámicos basados en las elecciones del jugador.
* **Modelo de lenguaje personalizado (fine-tuning):**  Este es el nivel más avanzado y requiere un conocimiento profundo de machine learning.  Implica entrenar un modelo personalizado a partir de tus propios datos para lograr resultados más específicos y precisos.

**Consideraciones para tus proyectos:**

* **Costo:**  El uso de la API de Google Generative AI conlleva costos. Debes tener en cuenta el consumo de tokens (unidades de procesamiento de texto) y planificar tu presupuesto.
* **Límite de tokens:**  Hay un límite en la cantidad de tokens que puedes procesar por solicitud.  Debes segmentar las peticiones largas para evitar errores.
* **Autenticación:** Necesitarás una clave de API para poder usar los servicios.
* **Ingeniería de prompts:** La calidad de los resultados depende en gran medida de la calidad de las indicaciones (prompts) que le des al modelo.


Recuerda consultar la documentación oficial de la API de Google Generative AI para obtener información detallada sobre las funciones disponibles, las limitaciones y las mejores prácticas.  La documentación te guiará en la configuración, la autenticación y el uso de la API en tu código Python.

Tú: 
'''