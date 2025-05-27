import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyttsx3
import time
import subprocess

# Cargar variables desde el archivo .env
load_dotenv()

# Configura tu clave API
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("Error: No se encontró 'API_KEY' en .env o variables de entorno.")
    print("Solución: Crea un archivo .env con API_KEY='tu_clave' o exporta la variable.")
    exit()

# Configurar Gemini AI
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    print(f"Error al configurar Gemini: {e}")
    print("Verifica tu conexión a internet y la validez de tu API_KEY")
    exit()

# Configuración avanzada de texto a voz para Kali Linux
def init_tts_engine():
    try:
        # Intento directo con espeak
        engine = pyttsx3.init('espeak')
        print("\nMotor TTS: espeak (configuración directa)")
        
        # Configurar voz en español si está disponible
        voices = engine.getProperty('voices')
        spanish_voices = [v for v in voices if 'spanish' in v.name.lower() or 'es' in v.languages]
        
        if spanish_voices:
            engine.setProperty('voice', spanish_voices[0].id)
        else:
            print("No se encontró voz en español, usando voz predeterminada")
        
        return engine
        
    except Exception as e:
        print(f"\nError al inicializar espeak directamente: {e}")
        print("Intentando configuración alternativa...")
        
        try:
            # Configuración alternativa para Kali Linux
            engine = pyttsx3.init()
            
            # Forzar el uso de espeak si está disponible
            voices = engine.getProperty('voices')
            for voice in voices:
                if 'espeak' in voice.id.lower():
                    engine.setProperty('voice', voice.id)
                    print(f"Motor TTS: {voice.name} (configuración alternativa)")
                    break
            
            return engine
            
        except Exception as e:
            print(f"\nError crítico al inicializar TTS: {e}")
            print("La funcionalidad de voz no estará disponible.")
            return None

# Inicializar motor de voz
engine = init_tts_engine()

# Función mejorada para leer texto
def speak(text):
    if not engine:
        return
        
    try:
        # Limpiar texto para evitar errores en TTS
        clean_text = text.replace('"', '').replace("'", "")
        
        # Configuración para Kali Linux
        engine.setProperty('rate', 160)  # Velocidad moderada
        engine.setProperty('volume', 0.9)  # Volumen alto
        
        print("\nLeyendo respuesta...")
        engine.say(clean_text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"\nError al reproducir voz: {e}")
        print("Intentando método alternativo...")
        
        # Método alternativo usando espeak directamente
        try:
            subprocess.run(['espeak', '-v', 'es', text])
        except Exception as sub_e:
            print(f"No se pudo usar espeak directamente: {sub_e}")

# Bucle principal de chat mejorado
def main_chat_loop():
    chat = model.start_chat(history=[])
    print("\n--- Chat con Gemini AI (escribe 'salir' para terminar) ---")
    print("--- Comandos especiales: /clear (limpiar historial) ---\n")
    
    while True:
        try:
            user_input = input("Tú: ").strip()
            
            # Manejo de comandos
            if user_input.lower() in ['salir', 'quit', 'exit']:
                break
                
            if user_input.lower() == '/clear':
                chat = model.start_chat(history=[])
                print("\n--- Historial de chat limpiado ---")
                continue
                
            if not user_input:
                continue
                
            # Procesar mensaje
            try:
                print("\nProcesando...")
                response = chat.send_message(user_input)
                
                # Mostrar respuesta
                print("\nGemini:")
                if response.text:
                    print(response.text)
                    speak(response.text)
                else:
                    print("[No se recibió respuesta válida]")
                    
            except Exception as api_error:
                print(f"\nError en la API: {api_error}")
                time.sleep(1)  # Esperar antes de reintentar
                
        except KeyboardInterrupt:
            print("\nSesión terminada por el usuario")
            break
            
        except Exception as e:
            print(f"\nError inesperado: {e}")
            continue

# Ejecución principal
if __name__ == "__main__":
    # Verificar dependencias del sistema
    print("Verificando dependencias...")
    try:
        subprocess.run(['espeak', '--version'], check=True)
        print("espeak está instalado correctamente")
    except:
        print("\nAdvertencia: espeak no está instalado correctamente")
        print("Para mejor compatibilidad, ejecuta:")
        print("sudo apt-get install espeak espeak-data libespeak1")
    
    # Iniciar chat
    main_chat_loop()
    
    # Limpieza final
    if engine:
        engine.stop()
    print("\n--- Sesión terminada ---")