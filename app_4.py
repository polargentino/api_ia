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

            # --- NUEVA LÓGICA para manejar la respuesta ---
            print("\nGemini:") # Imprimimos la etiqueta del modelo antes de la respuesta/mensaje de estado

            if response.text:
                # Si hay texto, lo imprimimos (esto es lo normal)
                print(response.text)
            else:
                # Si response.text está vacío, intentamos averiguar por qué
                print("[El modelo no proporcionó texto.]")

                # Verificar si el prompt fue bloqueado
                if response.prompt_feedback and response.prompt_feedback.block_reason:
                     print(f"  El prompt fue bloqueado por la razón: {response.prompt_feedback.block_reason.name}")
                     # Puedes imprimir más detalles si es necesario, como los ajustes de seguridad
                     # print("  Configuraciones de seguridad:", response.prompt_feedback.safety_settings)

                # Verificar si alguna respuesta candidata fue bloqueada
                elif response.candidates:
                    for i, candidate in enumerate(response.candidates):
                        print(f"  Candidato {i}:")
                        if candidate.finish_reason and candidate.finish_reason.name != 'STOP':
                             print(f"    La generación de la respuesta fue detenida por la razón: {candidate.finish_reason.name}")
                        if candidate.safety_ratings:
                            print("    Calificaciones de seguridad para esta respuesta:")
                            for rating in candidate.safety_ratings:
                                # 'severity' podría ser útil, pero 'probability' es más común
                                print(f"    - {rating.category.name}: {rating.probability.name}") # Muestra categoría y probabilidad de daño

                        # Si no hay texto y no hay razón obvia de bloqueo en finish_reason o safety_ratings
                        if not candidate.text and (not candidate.finish_reason or candidate.finish_reason.name == 'STOP') and (not candidate.safety_ratings or all(r.probability.name == 'NEGLIGIBLE' for r in candidate.safety_ratings)):
                             print("    [Respuesta del candidato sin texto y sin razón clara de bloqueo.]")

                else:
                    # Caso genérico si no hay texto y no hay feedback de bloqueo específico
                    print("  [No se encontraron candidatos de respuesta o feedback específico de bloqueo.]")

    except Exception as e:
        # Capturar otros errores durante el envío del mensaje (red, API, etc.)
        print(f"\nOcurrió un error al llamar a la API: {e}")
        print("Por favor, intenta tu mensaje de nuevo.")
        continue # Volver al inicio del bucle para pedir nueva entrada
    except EOFError: # Manejar Ctrl+D
        break

    # --- Impresión del historial completo después de cada turno exitoso (Mismo código que antes) ---
    # Esto se ejecuta SOLO si NO hubo una Exception arriba
    print("\n--- Historial de la Sesión ---")
    for message in chat.history:
        role = message.role.capitalize()
        content = message.parts[0].text if message.parts else "[Mensaje vacío o no textual]"
        print(f"{role}: {content}")
    print("----------------------------\n")


print("\n--- Sesión de chat terminada ---")

'''
--- Iniciando sesión de chat (Escribe 'salir' o 'quit' para terminar) ---
Tú: Cual es el futuro de la IA?

Gemini:
El futuro de la IA es incierto, pero con un potencial enorme y transformador en múltiples áreas.  Es difícil predecir con exactitud, pero podemos hablar de tendencias y posibilidades:

**A corto plazo (próximos 5-10 años):**

* **Mayor integración en la vida cotidiana:** Veremos una proliferación de asistentes virtuales más sofisticados, automatización en más industrias (logística, atención al cliente, etc.), y avances en la personalización de experiencias (educación, entretenimiento, compras).
* **IA generativa más avanzada:** Modelos como GPT-4 continuarán mejorando, creando contenido más realista y coherente (texto, imágenes, vídeo, audio).  Esto impactará en áreas como el arte, la educación, y el desarrollo de software.
* **IA explicable y confiable:** Habrá un mayor enfoque en desarrollar modelos de IA más transparentes y comprensibles, para mitigar los sesgos y aumentar la confianza en sus decisiones.
* **Automatización de tareas cognitivas:** La IA se usará para automatizar tareas que requieren un cierto nivel de razonamiento y comprensión, como análisis de datos complejos o la toma de decisiones en contextos específicos.
* **Crecimiento de la IA en dispositivos de borde:** Más procesamiento de IA se llevará a cabo directamente en los dispositivos (teléfonos, autos, etc.), reduciendo la dependencia de la nube y mejorando la privacidad y la velocidad.


**A largo plazo (próximos 10-20 años y más):**

* **IA general artificial (AGI):** La posibilidad de desarrollar una IA con inteligencia comparable a la humana es un objetivo a largo plazo y altamente debatido.  Su llegada tendría un impacto inmenso en todos los aspectos de la sociedad.
* **Integración con otras tecnologías:** La IA se fusionará con otras tecnologías emergentes, como la biotecnología, la nanotecnología y la computación cuántica, creando nuevas posibilidades innovadoras.
* **Impacto en el mercado laboral:** La automatización impulsada por IA continuará cambiando el mercado laboral, requiriendo adaptaciones y nuevas habilidades en la fuerza de trabajo.
* **Desafíos éticos y sociales:** Se intensificarán los debates sobre temas éticos, como el sesgo algorítmico, la privacidad, la seguridad, y el potencial uso de la IA con fines dañinos.  La regulación de la IA será crucial.
* **Nuevas formas de interacción humano-computadora:** Se desarrollarán interfaces más naturales e intuitivas, permitiendo una interacción más fluida y efectiva con las máquinas.


**Riesgos y desafíos:**

* **Sesgos y discriminación:** Los modelos de IA pueden reflejar y amplificar los sesgos presentes en los datos de entrenamiento.
* **Desempleo y desigualdad:** La automatización podría desplazar a trabajadores en diversos sectores.
* **Mal uso de la IA:** La IA podría ser utilizada para fines malintencionados, como la creación de armas autónomas o la difusión de desinformación.
* **Control y gobernanza:** Es fundamental establecer marcos regulatorios y éticos para el desarrollo y uso responsable de la IA.


En resumen, el futuro de la IA está lleno de promesas y desafíos.  Su impacto será profundo y transversal, requiriendo una planificación cuidadosa y una atención constante a las implicaciones éticas y sociales.  El desarrollo responsable y ético de la IA será crucial para aprovechar al máximo su potencial y mitigar los riesgos.


--- Historial de la Sesión ---
User: Cual es el futuro de la IA?
Model: El futuro de la IA es incierto, pero con un potencial enorme y transformador en múltiples áreas.  Es difícil predecir con exactitud, pero podemos hablar de tendencias y posibilidades:

**A corto plazo (próximos 5-10 años):**

* **Mayor integración en la vida cotidiana:** Veremos una proliferación de asistentes virtuales más sofisticados, automatización en más industrias (logística, atención al cliente, etc.), y avances en la personalización de experiencias (educación, entretenimiento, compras).
* **IA generativa más avanzada:** Modelos como GPT-4 continuarán mejorando, creando contenido más realista y coherente (texto, imágenes, vídeo, audio).  Esto impactará en áreas como el arte, la educación, y el desarrollo de software.
* **IA explicable y confiable:** Habrá un mayor enfoque en desarrollar modelos de IA más transparentes y comprensibles, para mitigar los sesgos y aumentar la confianza en sus decisiones.
* **Automatización de tareas cognitivas:** La IA se usará para automatizar tareas que requieren un cierto nivel de razonamiento y comprensión, como análisis de datos complejos o la toma de decisiones en contextos específicos.
* **Crecimiento de la IA en dispositivos de borde:** Más procesamiento de IA se llevará a cabo directamente en los dispositivos (teléfonos, autos, etc.), reduciendo la dependencia de la nube y mejorando la privacidad y la velocidad.


**A largo plazo (próximos 10-20 años y más):**

* **IA general artificial (AGI):** La posibilidad de desarrollar una IA con inteligencia comparable a la humana es un objetivo a largo plazo y altamente debatido.  Su llegada tendría un impacto inmenso en todos los aspectos de la sociedad.
* **Integración con otras tecnologías:** La IA se fusionará con otras tecnologías emergentes, como la biotecnología, la nanotecnología y la computación cuántica, creando nuevas posibilidades innovadoras.
* **Impacto en el mercado laboral:** La automatización impulsada por IA continuará cambiando el mercado laboral, requiriendo adaptaciones y nuevas habilidades en la fuerza de trabajo.
* **Desafíos éticos y sociales:** Se intensificarán los debates sobre temas éticos, como el sesgo algorítmico, la privacidad, la seguridad, y el potencial uso de la IA con fines dañinos.  La regulación de la IA será crucial.
* **Nuevas formas de interacción humano-computadora:** Se desarrollarán interfaces más naturales e intuitivas, permitiendo una interacción más fluida y efectiva con las máquinas.


**Riesgos y desafíos:**

* **Sesgos y discriminación:** Los modelos de IA pueden reflejar y amplificar los sesgos presentes en los datos de entrenamiento.
* **Desempleo y desigualdad:** La automatización podría desplazar a trabajadores en diversos sectores.
* **Mal uso de la IA:** La IA podría ser utilizada para fines malintencionados, como la creación de armas autónomas o la difusión de desinformación.
* **Control y gobernanza:** Es fundamental establecer marcos regulatorios y éticos para el desarrollo y uso responsable de la IA.


En resumen, el futuro de la IA está lleno de promesas y desafíos.  Su impacto será profundo y transversal, requiriendo una planificación cuidadosa y una atención constante a las implicaciones éticas y sociales.  El desarrollo responsable y ético de la IA será crucial para aprovechar al máximo su potencial y mitigar los riesgos.

----------------------------

Tú: 
User: como seguir capacitandome para estar a la vanguardia de la creacion de App con python 
Model: Para mantenerte a la vanguardia en la creación de apps con Python, necesitas un plan de aprendizaje continuo y enfocado.  Aquí te doy algunas estrategias:

**1. Domina los fundamentos de Python:**

* **Profundiza en estructuras de datos:** Asegúrate de comprender completamente listas, diccionarios, conjuntos y tuplas.  Su uso eficiente es crucial para la optimización del código.
* **Manejo de archivos:** Aprende a leer, escribir y manipular diferentes formatos de archivos (JSON, CSV, XML, etc.).  Es fundamental para la persistencia de datos en tus apps.
* **Programación orientada a objetos (POO):**  La POO es esencial para construir aplicaciones robustas y escalables.  Practica con clases, objetos, herencia y polimorfismo.
* **Manejo de excepciones:** Aprende a gestionar errores de manera elegante para que tus apps sean más estables y resistentes a fallos.
* **Algoritmos y estructuras de datos:** Un buen conocimiento de algoritmos y estructuras de datos te permitirá escribir código eficiente y optimizar el rendimiento de tus aplicaciones.


**2. Frameworks y librerías para desarrollo de apps:**

* **Kivy:** Ideal para crear apps multiplataforma con interfaces gráficas atractivas.  Es una buena opción para aplicaciones que requieren una interfaz de usuario visualmente rica.
* **PyQt:** Un framework robusto y potente para desarrollar interfaces de usuario complejas.  Ofrece mayor control y flexibilidad que Kivy, pero tiene una curva de aprendizaje más pronunciada.
* **Tkinter:** Un framework más simple, ideal para prototipos rápidos o aplicaciones con interfaces menos complejas.  Es integrado con Python, por lo que es fácil de usar.
* **BeeWare:**  Un conjunto de herramientas para el desarrollo de aplicaciones nativas (iOS, Android, Desktop) con Python.  Facilita la creación de apps que se integran bien con el sistema operativo.
* **Flask o Django:** Aunque se utilizan principalmente para desarrollo web backend, pueden formar parte de aplicaciones móviles que interactúan con un servidor. Aprende al menos uno de ellos para crear aplicaciones completas.
* **Bibliotecas para acceso a datos:**  Familiarízate con bibliotecas como `sqlite3` (para bases de datos locales), o `psycopg2` (para PostgreSQL), o drivers para otras bases de datos según tus necesidades.


**3. Desarrollo de Backend:**

* **APIs y REST:** Aprende a construir y consumir APIs RESTful.  Esto es fundamental para la comunicación entre tu aplicación móvil y un servidor.
* **Bases de datos:** Profundiza en el diseño y la gestión de bases de datos relacionales y NoSQL.
* **Autenticación y autorización:** Implementa mecanismos seguros para la autenticación y autorización de usuarios en tus aplicaciones.


**4. Integración de servicios:**

* **Mapas:** Integración con APIs de mapas como Google Maps o Mapbox.
* **Pagos:** Integración con pasarelas de pago (Stripe, PayPal, etc.).
* **Notificaciones:** Implementación de sistemas de notificaciones push.
* **Redes sociales:** Integración con APIs de redes sociales (Facebook, Twitter, etc.).


**5. Práctica continua:**

* **Crea proyectos:**  La mejor manera de aprender es construyendo.  Empieza con proyectos pequeños y luego ve incrementando la complejidad.
* **Contribuye a proyectos open source:**  Participa en proyectos de código abierto para aprender de otros desarrolladores y mejorar tus habilidades.
* **Participa en la comunidad:**  Únete a foros, grupos de discusión y comunidades online de Python para interactuar con otros desarrolladores, compartir conocimientos y obtener ayuda.


**6. Mantente actualizado:**

* **Sigue blogs y sitios web:**  Lee blogs y sitios web dedicados al desarrollo de aplicaciones con Python.
* **Asiste a conferencias:**  Asiste a conferencias y eventos relacionados con Python y desarrollo de aplicaciones móviles.
* **Cursos online:**  Aprovecha los cursos online en plataformas como Coursera, edX, Udemy, etc.


**Herramientas adicionales:**

* **Sistemas de control de versiones (Git):**  Esencial para gestionar el código de tus proyectos.
* **Entornos virtuales (venv o conda):**  Permiten gestionar las dependencias de tus proyectos de forma aislada.
* **Depuradores:** Aprende a usar un depurador para identificar y solucionar errores en tu código.


Recuerda que el aprendizaje es un proceso continuo.  Prioriza la práctica, la participación en la comunidad y la búsqueda constante de nuevos conocimientos para mantenerte a la vanguardia en el desarrollo de aplicaciones con Python.

----------------------------

'''