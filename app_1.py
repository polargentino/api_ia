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
# Puedes listar modelos para ver cuáles soportan 'generateContent'
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
# El modelo gemini-1.5-flash-latest también soporta chat
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Iniciar una sesión de chat ---
# El historial ([]) inicial puede incluir mensajes previos si quieres dar contexto
print("--- Iniciando sesión de chat ---")
chat = model.start_chat(history=[])

# Lista de mensajes para enviar en la conversación
messages_to_send = [
    "Hola, ¿cómo estás?",
    "¿Puedes recordarme cuántos planetas hay en nuestro sistema solar?",
    "¿Y cómo se llama el más grande?",
    "Gracias!",
]

# Enviar mensajes y obtener respuestas en la conversación
for user_message in messages_to_send:
    print(f"\nUsuario: {user_message}")

    try:
        # Enviar el mensaje en el contexto de la conversación actual
        response = chat.send_message(user_message)

        # Imprimir la respuesta del modelo
        print("Modelo:")
        # Algunas respuestas pueden no tener directamente .text (ej: si hay bloqueos)
        if response.text:
            print(response.text)
        else:
             # Imprime información de depuración si no hay texto en la respuesta
             print("Respuesta sin texto. Detalles:")
             print(response)


    except Exception as e:
        print(f"\nOcurrió un error al enviar el mensaje: {e}")
        print("Saltando al siguiente mensaje...")
        # Puedes decidir si quieres salir o continuar en caso de error

print("\n--- Fin de la conversación ---")

# Opcional: Puedes ver el historial completo de la conversación
# print("\nHistorial completo:")
# for message in chat.history:
#    print(f"{message.role}: {message.parts[0].text}")

'''
--- Iniciando sesión de chat ---

Usuario: Hola, ¿cómo estás?
Modelo:
¡Hola! Estoy bien, gracias por preguntar. ¿Cómo estás tú?


Usuario: ¿Puedes recordarme cuántos planetas hay en nuestro sistema solar?
Modelo:
Hay ocho planetas en nuestro sistema solar.


Usuario: ¿Y cómo se llama el más grande?
Modelo:
El planeta más grande de nuestro sistema solar es Júpiter.


Usuario: Gracias!
Modelo:
¡De nada!  ¿Hay algo más en lo que pueda ayudarte?


--- Fin de la conversación ---
'''