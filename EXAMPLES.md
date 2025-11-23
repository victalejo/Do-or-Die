# Ejemplos de Uso - Do or Die API

Este archivo contiene ejemplos de cómo usar los módulos del sistema para desarrolladores que quieran extender la funcionalidad.

## 📚 Módulos Disponibles

### 1. Config (config.py)

Acceso a constantes y configuración global.

```python
from config import *

# Usar constantes de fuentes
titulo = sg.Text("Mi Título", font=FONT_TITLE)

# Usar constantes de colores
boton = sg.Button("OK", button_color=COLOR_SUCCESS)

# Acceder a rutas
print(f"Logo en: {LOGO_PATH}")
print(f"Icono en: {ICON_PATH}")

# Mensajes predefinidos
sg.popup_error(MSG_ERROR_EMPTY_EMAIL)
```

### 2. Utils (utils.py)

Funciones de utilidad para validación y formateo.

#### Validación de Email

```python
from utils import validar_email

# Validar un email
email = "usuario@ejemplo.com"
if validar_email(email):
    print("Email válido")
else:
    print("Email inválido")

# Ejemplos
validar_email("test@test.com")      # True
validar_email("invalido.com")        # False
validar_email("@test.com")          # False
validar_email("test@")              # False
```

#### Validación de Contraseña

```python
from utils import validar_password

# Validar con longitud por defecto (6)
valida, mensaje = validar_password("mi_password")
if valida:
    print("Contraseña válida")
else:
    print(f"Error: {mensaje}")

# Validar con longitud personalizada
valida, mensaje = validar_password("abc", min_length=8)
# valida = False
# mensaje = "La contraseña debe tener al menos 8 caracteres"
```

#### Formateo de Saldo

```python
from utils import formatear_saldo

# Formatear con moneda por defecto (USD)
saldo = formatear_saldo(1000)
# Resultado: "$1,000.00 USD"

# Formatear con moneda específica
saldo = formatear_saldo(2500.50, "EUR")
# Resultado: "$2,500.50 EUR"

# Números grandes
saldo = formatear_saldo(1000000, "GBP")
# Resultado: "$1,000,000.00 GBP"
```

#### Sistema de Logging

```python
from utils import log_evento

# Log de información
log_evento("Usuario inició sesión", "INFO")

# Log de advertencia
log_evento("Intento fallido de login", "WARNING")

# Log de error
log_evento("Error al conectar con API", "ERROR")

# El archivo app.log contendrá:
# [2025-11-23 14:30:15] [INFO] Usuario inició sesión
# [2025-11-23 14:30:20] [WARNING] Intento fallido de login
# [2025-11-23 14:30:25] [ERROR] Error al conectar con API
```

#### Gestión de Sesiones (Archivos)

```python
from utils import guardar_sesion, cargar_sesion, limpiar_sesion

# Guardar datos de sesión
datos = {
    "email": "usuario@test.com",
    "timestamp": "2025-11-23 14:30:00",
    "cuenta": "Demo"
}
guardar_sesion(datos)

# Cargar sesión guardada
sesion = cargar_sesion()
if sesion:
    print(f"Email: {sesion['email']}")
    print(f"Cuenta: {sesion['cuenta']}")

# Limpiar sesión
limpiar_sesion()
```

### 3. Session Manager (session_manager.py)

Gestión completa del estado de sesión del usuario.

#### Inicializar Session Manager

```python
from session_manager import SessionManager

# Crear instancia
session_mgr = SessionManager()

# Verificar estado inicial
print(f"Sesión iniciada: {session_mgr.sesion_iniciada}")  # False
print(f"Usuario: {session_mgr.usuario_actual}")           # None
```

#### Iniciar Sesión

```python
from session_manager import SessionManager

session_mgr = SessionManager()

# Intentar login
exito, mensaje = session_mgr.iniciar_sesion(
    email="usuario@test.com",
    password="mi_password"
)

if exito:
    print(mensaje)  # "Inicio de sesión exitoso"
    print(f"Usuario: {session_mgr.usuario_actual}")
else:
    print(f"Error: {mensaje}")
```

#### Gestionar Cuentas

```python
from session_manager import SessionManager

session_mgr = SessionManager()
session_mgr.iniciar_sesion("user@test.com", "password")

# Cambiar a cuenta Demo
session_mgr.cambiar_cuenta("Demo")
print(f"Saldo: {session_mgr.obtener_saldo()}")
# Resultado: "$10,000.00 USD"

# Cambiar a cuenta Real
session_mgr.cambiar_cuenta("Real")
print(f"Tipo: {session_mgr.cuenta_activa}")  # "Real"
```

#### Restaurar y Cerrar Sesión

```python
from session_manager import SessionManager

session_mgr = SessionManager()

# Restaurar sesión previa
if session_mgr.restaurar_sesion():
    print(f"Sesión restaurada: {session_mgr.usuario_actual}")
else:
    print("No hay sesión previa")

# Cerrar sesión
session_mgr.cerrar_sesion()
print(f"Sesión activa: {session_mgr.sesion_iniciada}")  # False
```

### 4. Aplicación Principal (main.py)

Uso de la clase principal de la aplicación.

#### Ejecutar la Aplicación Completa

```python
from main import DoOrDieApp

# Crear y ejecutar aplicación
app = DoOrDieApp()
app.ejecutar()

# Esto ejecutará:
# 1. Verificación de sesión previa
# 2. Login (si es necesario)
# 3. Ventana principal
# 4. Logging de eventos
```

#### Personalizar Componentes

```python
from main import DoOrDieApp
import PySimpleGUI as sg

class MiAppPersonalizada(DoOrDieApp):
    def mostrar_login(self):
        # Personalizar ventana de login
        sg.popup("Mi login personalizado")
        return super().mostrar_login()
    
    def mostrar_principal(self):
        # Personalizar ventana principal
        super().mostrar_principal()

# Usar versión personalizada
app = MiAppPersonalizada()
app.ejecutar()
```

## 🔧 Ejemplos Avanzados

### Validación de Formulario Completo

```python
from utils import validar_email, validar_password

def validar_formulario(datos):
    """
    Valida todos los campos de un formulario
    """
    errores = []
    
    # Validar email
    if not validar_email(datos['email']):
        errores.append("Email inválido")
    
    # Validar password
    valida, mensaje = validar_password(datos['password'])
    if not valida:
        errores.append(mensaje)
    
    # Validar monto
    try:
        monto = float(datos['monto'])
        if monto <= 0:
            errores.append("El monto debe ser positivo")
    except ValueError:
        errores.append("Monto inválido")
    
    return len(errores) == 0, errores

# Uso
datos = {
    'email': 'test@test.com',
    'password': 'password123',
    'monto': '100'
}

valido, errores = validar_formulario(datos)
if valido:
    print("Formulario válido")
else:
    for error in errores:
        print(f"- {error}")
```

### Sistema de Notificaciones con Logging

```python
from utils import log_evento
import PySimpleGUI as sg

def notificar(mensaje, tipo="INFO"):
    """
    Muestra un popup y registra en el log
    """
    # Registrar en log
    log_evento(mensaje, tipo)
    
    # Mostrar popup según tipo
    if tipo == "INFO":
        sg.popup_auto_close(mensaje, auto_close_duration=2)
    elif tipo == "WARNING":
        sg.popup_ok(mensaje, title="Advertencia")
    elif tipo == "ERROR":
        sg.popup_error(mensaje)
    
    return True

# Uso
notificar("Operación exitosa", "INFO")
notificar("Saldo bajo", "WARNING")
notificar("Error de conexión", "ERROR")
```

### Gestor de Trading Completo

```python
from session_manager import SessionManager
from utils import formatear_saldo, log_evento
from datetime import datetime

class TradingManager:
    def __init__(self, session_manager):
        self.session = session_manager
        self.historial = []
    
    def ejecutar_operacion(self, activo, tipo, monto):
        """
        Ejecuta una operación de trading
        """
        if not self.session.sesion_iniciada:
            return False, "Debe iniciar sesión primero"
        
        if monto <= 0:
            return False, "El monto debe ser positivo"
        
        if tipo not in ["CALL", "PUT"]:
            return False, "Tipo inválido (use CALL o PUT)"
        
        # Registrar operación
        operacion = {
            'timestamp': datetime.now(),
            'activo': activo,
            'tipo': tipo,
            'monto': monto,
            'cuenta': self.session.cuenta_activa
        }
        
        self.historial.append(operacion)
        
        # Log
        log_evento(
            f"Operación {tipo}: {activo} - {formatear_saldo(monto)}",
            "INFO"
        )
        
        return True, "Operación ejecutada"
    
    def obtener_historial(self, limite=10):
        """
        Retorna el historial de operaciones
        """
        return self.historial[-limite:]

# Uso
session = SessionManager()
session.iniciar_sesion("user@test.com", "password")
session.cambiar_cuenta("Demo")

trading = TradingManager(session)

# Ejecutar operaciones
trading.ejecutar_operacion("EUR/USD", "CALL", 100)
trading.ejecutar_operacion("BTC/USD", "PUT", 250)

# Ver historial
for op in trading.obtener_historial():
    print(f"{op['timestamp']} - {op['tipo']} {op['activo']}: ${op['monto']}")
```

### Integración con API Externa (Plantilla)

```python
from session_manager import SessionManager
from utils import log_evento
import requests  # Requiere: pip install requests

class IQOptionAPI:
    def __init__(self, session_manager):
        self.session = session_manager
        self.api_url = "https://api.iqoption.com"  # Ejemplo
    
    def conectar(self):
        """
        Conecta con la API de IQ Option
        """
        if not self.session.sesion_iniciada:
            return False, "No hay sesión iniciada"
        
        try:
            # Aquí iría la lógica real de conexión
            # Este es solo un ejemplo
            log_evento("Conectando con API de IQ Option", "INFO")
            
            # response = requests.post(
            #     f"{self.api_url}/login",
            #     json={
            #         'email': self.session.usuario_actual,
            #         'password': '...'  # Nunca almacenar passwords
            #     }
            # )
            
            return True, "Conectado exitosamente"
            
        except Exception as e:
            log_evento(f"Error al conectar: {str(e)}", "ERROR")
            return False, str(e)
    
    def obtener_saldo(self):
        """
        Obtiene el saldo de la cuenta
        """
        # Implementación de ejemplo
        pass
    
    def colocar_orden(self, activo, tipo, monto):
        """
        Coloca una orden en la plataforma
        """
        # Implementación de ejemplo
        pass
```

## 🎨 Personalización de UI

### Crear Tema Personalizado

```python
import PySimpleGUI as sg

# Definir tema personalizado
sg.LOOK_AND_FEEL_TABLE['DoOrDieTheme'] = {
    'BACKGROUND': '#1a1a2e',
    'TEXT': '#eee',
    'INPUT': '#16213e',
    'TEXT_INPUT': '#fff',
    'SCROLL': '#16213e',
    'BUTTON': ('#fff', '#0f3460'),
    'PROGRESS': ('#01FF70', '#01FF70'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

# Usar tema
sg.theme('DoOrDieTheme')
```

### Componentes Reutilizables

```python
import PySimpleGUI as sg
from config import FONT_TEXT, COLOR_SUCCESS

def crear_campo_input(label, key, password=False):
    """
    Crea un campo de input reutilizable
    """
    return [
        [sg.Text(label, size=(15, 1), font=FONT_TEXT)],
        [sg.Input(key=key, size=(30, 1), 
                 password_char='•' if password else '')]
    ]

def crear_boton_accion(texto, key, color=COLOR_SUCCESS):
    """
    Crea un botón de acción estilizado
    """
    from config import FONT_BUTTON
    return sg.Button(texto, key=key, button_color=color, 
                    font=FONT_BUTTON, size=(12, 1))

# Uso
layout = [
    crear_campo_input("Email:", "email"),
    crear_campo_input("Password:", "password", password=True),
    [crear_boton_accion("Ingresar", "login")]
]
```

## 📊 Testing (Ejemplos)

```python
# test_utils.py
import pytest
from utils import validar_email, validar_password, formatear_saldo

def test_validar_email():
    assert validar_email("test@test.com") == True
    assert validar_email("invalido") == False
    assert validar_email("@test.com") == False

def test_validar_password():
    valida, _ = validar_password("password123")
    assert valida == True
    
    valida, mensaje = validar_password("abc")
    assert valida == False
    assert "6 caracteres" in mensaje

def test_formatear_saldo():
    assert formatear_saldo(1000) == "$1,000.00 USD"
    assert formatear_saldo(100.5, "EUR") == "$100.50 EUR"

# Ejecutar: pytest test_utils.py
```

---

## 📝 Notas Importantes

1. **Seguridad**: Nunca almacenes contraseñas en texto plano
2. **API Keys**: Usa variables de entorno para credenciales
3. **Logging**: Evita registrar información sensible
4. **Validación**: Siempre valida inputs del usuario
5. **Manejo de Errores**: Usa try-except para operaciones críticas

## 🔗 Referencias

- [Documentación PySimpleGUI](https://pysimplegui.readthedocs.io/)
- [README.md](README.md) - Documentación principal
- [USER_GUIDE.md](USER_GUIDE.md) - Guía del usuario
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guía de contribución

---

**Última actualización**: Noviembre 2025  
**Versión**: 2.0
