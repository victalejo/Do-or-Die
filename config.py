"""
Módulo de configuración para Do or Die
Contiene constantes y configuraciones globales del sistema
"""
import os

# Rutas de recursos
RESOURCES_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(RESOURCES_DIR, 'Logo fondo transparente.png')
ICON_PATH = os.path.join(RESOURCES_DIR, 'do_or_die.ico')

# Configuración de tema
THEME = "Material2"

# Fuentes
FONT_TITLE = ("Magistral Regular", 24)
FONT_SUBTITLE = ("Magistral Regular", 16)
FONT_HEADING = ("Magistral Regular", 15)
FONT_TEXT = ("Magistral Regular", 13)
FONT_BUTTON = ("Magistral Regular", 12)
FONT_INPUT = ("Arial", 12)

# Colores
COLOR_SUCCESS = "green"
COLOR_ERROR = "red"
COLOR_WARNING = "orange"
COLOR_INFO = "LightCyan"

# Dimensiones de ventana
WINDOW_SIZE_LOGIN = (600, 400)
WINDOW_SIZE_MAIN = (900, 600)

# Configuración de cuenta
ACCOUNT_TYPES = ["Demo", "Real"]
DEFAULT_CURRENCY = "USD"

# Mensajes
MSG_ERROR_EMPTY_FIELDS = "Por favor, ingrese correo y contraseña"
MSG_ERROR_EMPTY_EMAIL = "Por favor, ingrese un correo válido"
MSG_ERROR_EMPTY_PASSWORD = "Por favor, ingrese una contraseña"
MSG_ERROR_INVALID_EMAIL = "El formato del correo electrónico no es válido"
MSG_ERROR_CONNECTION = "Error de conexión. Verifique su internet"
MSG_SUCCESS_LOGIN = "Inicio de sesión exitoso"

# Configuración de sesión
SESSION_FILE = os.path.join(RESOURCES_DIR, '.session')
LOG_FILE = os.path.join(RESOURCES_DIR, 'app.log')
