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
