import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyttsx3
import time
import subprocess

# Cargar variables desde el archivo .env
load_dotenv()