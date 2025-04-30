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
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Iniciar una sesión de chat ---
print("--- Iniciando sesión de chat (Escribe 'salir' o 'quit' para terminar) ---")
# Puedes iniciar con un mensaje del sistema si quieres darle contexto inicial
# chat = model.start_chat(history=[{'role':'user', 'parts':['Eres un asistente amigable y conciso.']},
#                                {'role':'model', 'parts':['Okay, seré amigable y conciso.']}])
chat = model.start_chat(history=[]) # Empezamos con historial vacío

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

            # --- NO imprimimos la respuesta aquí directamente ---
            # La respuesta se incluirá automáticamente en chat.history
            pass # No hacemos nada inmediatamente después de enviar

    except Exception as e:
        # Capturar errores durante el envío del mensaje
        print(f"\nOcurrió un error al enviar el mensaje: {e}")
        print("Por favor, intenta tu mensaje de nuevo.")
        # Si hay un error, no intentamos imprimir el historial de este turno fallido
        continue # Volver al inicio del bucle para pedir nueva entrada
    except EOFError: # Manejar Ctrl+D
        break

    # --- ¡NUEVA SECCIÓN! Imprimir el historial completo después de cada turno exitoso ---
    print("\n--- Historial de la Sesión ---")
    for message in chat.history:
        # 'role' puede ser 'user' o 'model'
        role = message.role.capitalize()
        # El contenido del mensaje está en message.parts (generalmente un solo elemento de texto)
        content = message.parts[0].text if message.parts else "[Mensaje vacío o no textual]"
        print(f"{role}: {content}")
    print("----------------------------\n") # Separador visual


print("\n--- Sesión de chat terminada ---")

# El historial completo ya se mostró al final del bucle, pero podrías descomentar esto si solo quisieras verlo al final
# print("\nHistorial completo al terminar:")
# for message in chat.history:
#    print(f"{message.role}: {message.parts[0].text}")

'''
--- Iniciando sesión de chat (Escribe 'salir' o 'quit' para terminar) ---
Tú: dime brevemente como hacer prompt efectivos

--- Historial de la Sesión ---
User: dime brevemente como hacer prompt efectivos
Model: Para prompts efectivos, sé **claro, conciso y específico**.  Define bien tu objetivo, usa palabras clave relevantes y proporciona contexto suficiente.  Experimenta con diferentes formulaciones y especifica el formato deseado (ej: lista, párrafo, código).  Cuanto más preciso seas, mejor será el resultado.

----------------------------

Tú: dame un ejemplo real de una persona que quiere hacer un C.V para impresionar a un reclutador

--- Historial de la Sesión ---
User: dime brevemente como hacer prompt efectivos
Model: Para prompts efectivos, sé **claro, conciso y específico**.  Define bien tu objetivo, usa palabras clave relevantes y proporciona contexto suficiente.  Experimenta con diferentes formulaciones y especifica el formato deseado (ej: lista, párrafo, código).  Cuanto más preciso seas, mejor será el resultado.

User: dame un ejemplo real de una persona que quiere hacer un C.V para impresionar a un reclutador
Model: Juan, un ingeniero de software con 5 años de experiencia en desarrollo web, quiere impresionar a un reclutador de una empresa de tecnología en auge.  Su objetivo no es sólo conseguir una entrevista, sino destacarse entre cientos de candidatos.  En lugar de un simple CV cronológico, Juan decide usar un formato moderno y visualmente atractivo.

Su CV incluye:

* **Un resumen impactante:** En lugar de una larga lista de responsabilidades,  Juan escribe un breve párrafo (3-4 líneas) destacando sus logros más importantes y cuantificables:  "Ingeniero de Software con 5 años de experiencia en desarrollo web, especializado en React y Node.js.  Aumenté la eficiencia del sitio web de [empresa anterior] en un 25% optimizando el código y reduciendo los tiempos de carga.  Lideré el desarrollo de una nueva API que incrementó las conversiones en un 15%."

* **Una sección de proyectos:**  Juan no solo lista sus trabajos, sino que describe 2-3 proyectos clave con detalles específicos de sus contribuciones, tecnologías utilizadas y resultados obtenidos.  Utiliza enlaces a repositorios de GitHub o sitios web en vivo para demostrar su trabajo.

* **Habilidades técnicas:**  Juan presenta sus habilidades con un formato visualmente atractivo, quizá un gráfico de barras o etiquetas, mostrando su nivel de dominio en cada tecnología (React, Node.js, SQL, Git, etc.).

* **Palabras clave:**  Juan incorpora palabras clave relevantes encontradas en las descripciones de trabajo de la empresa a la que aspira.

* **Diseño limpio y profesional:** El CV de Juan es conciso, fácil de leer y visualmente atractivo, usando una plantilla moderna y una tipografía profesional.  No está abarrotado de información innecesaria.

En resumen, el CV de Juan no solo enumera sus experiencias, sino que las presenta de forma estratégica para destacar sus logros y habilidades, usando un formato moderno y  palabras clave para optimizar su búsqueda por los reclutadores.

----------------------------

Tú: gracias

--- Historial de la Sesión ---
User: dime brevemente como hacer prompt efectivos
Model: Para prompts efectivos, sé **claro, conciso y específico**.  Define bien tu objetivo, usa palabras clave relevantes y proporciona contexto suficiente.  Experimenta con diferentes formulaciones y especifica el formato deseado (ej: lista, párrafo, código).  Cuanto más preciso seas, mejor será el resultado.

User: dame un ejemplo real de una persona que quiere hacer un C.V para impresionar a un reclutador
Model: Juan, un ingeniero de software con 5 años de experiencia en desarrollo web, quiere impresionar a un reclutador de una empresa de tecnología en auge.  Su objetivo no es sólo conseguir una entrevista, sino destacarse entre cientos de candidatos.  En lugar de un simple CV cronológico, Juan decide usar un formato moderno y visualmente atractivo.

Su CV incluye:

* **Un resumen impactante:** En lugar de una larga lista de responsabilidades,  Juan escribe un breve párrafo (3-4 líneas) destacando sus logros más importantes y cuantificables:  "Ingeniero de Software con 5 años de experiencia en desarrollo web, especializado en React y Node.js.  Aumenté la eficiencia del sitio web de [empresa anterior] en un 25% optimizando el código y reduciendo los tiempos de carga.  Lideré el desarrollo de una nueva API que incrementó las conversiones en un 15%."

* **Una sección de proyectos:**  Juan no solo lista sus trabajos, sino que describe 2-3 proyectos clave con detalles específicos de sus contribuciones, tecnologías utilizadas y resultados obtenidos.  Utiliza enlaces a repositorios de GitHub o sitios web en vivo para demostrar su trabajo.

* **Habilidades técnicas:**  Juan presenta sus habilidades con un formato visualmente atractivo, quizá un gráfico de barras o etiquetas, mostrando su nivel de dominio en cada tecnología (React, Node.js, SQL, Git, etc.).

* **Palabras clave:**  Juan incorpora palabras clave relevantes encontradas en las descripciones de trabajo de la empresa a la que aspira.

* **Diseño limpio y profesional:** El CV de Juan es conciso, fácil de leer y visualmente atractivo, usando una plantilla moderna y una tipografía profesional.  No está abarrotado de información innecesaria.

En resumen, el CV de Juan no solo enumera sus experiencias, sino que las presenta de forma estratégica para destacar sus logros y habilidades, usando un formato moderno y  palabras clave para optimizar su búsqueda por los reclutadores.

User: gracias
Model: De nada, ¡espero que te sea útil!

----------------------------

Tú: exit

--- Sesión de chat terminada ---
'''