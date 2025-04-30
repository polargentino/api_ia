
import google.generativeai as genai
import os
from dotenv import load_dotenv # Importa load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Configura tu clave API leyendo la variable de entorno
# Si la variable API_KEY no existe en el entorno o en el archivo .env, esto será None
API_KEY = os.getenv('API_KEY')

# Verifica si la clave API se cargó correctamente
if not API_KEY:
    print("Error: No se encontró la variable de entorno 'API_KEY'.")
    print("Asegúrate de tener un archivo .env con API_KEY='TU_CLAVE_API_AQUI'")
    print("O de haber exportado la variable de entorno en tu terminal.")
    exit() # Sale del script si no encuentra la clave

genai.configure(api_key=API_KEY)

# Elige el modelo que quieres usar
# Puedes usar 'gemini-1.0-pro', 'gemini-1.5-flash-latest', etc.
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Envía un mensaje al modelo
prompt = "¿Puedes darme algunas ideas de proyectos en Python usando la apikey de IA de Google?"

print(f"Enviando prompt al modelo: '{prompt}'")

try:
    response = model.generate_content(prompt)

    # Imprime la respuesta
    print("\nRespuesta del modelo:")
    # Algunas respuestas pueden no tener directamente .text (ej: si hay bloqueos)
    if response.text:
        print(response.text)
    else:
        # Imprime información de depuración si no hay texto en la respuesta
        print("Respuesta sin texto. Detalles:")
        print(response)


except Exception as e:
    print(f"\nOcurrió un error al llamar a la API: {e}")
    print("Esto podría ser un problema de sobrecarga, autenticación o un error en la solicitud.")
    print("Verifica tu clave API y vuelve a intentarlo más tarde si el error persiste.")

'''
Enviando prompt al modelo: '¿Puedes explicar brevemente qué es la inteligencia artificial?'

Respuesta del modelo:
La inteligencia artificial (IA) es un campo de la informática que se centra en crear máquinas capaces de realizar tareas que normalmente requieren inteligencia humana.  Esto incluye el aprendizaje, la resolución de problemas, el razonamiento, la percepción y la comprensión del lenguaje natural.  En esencia, se trata de simular la inteligencia humana en máquinas.

'''