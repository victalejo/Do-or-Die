"""
Módulo de utilidades para Do or Die
Funciones de validación, formateo y helpers generales
"""
import re
import json
import os
from datetime import datetime
from config import SESSION_FILE


def validar_email(email):
    """
    Valida el formato de un correo electrónico
    
    Args:
        email (str): Correo electrónico a validar
        
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def validar_password(password, min_length=6):
    """
    Valida que la contraseña cumpla con requisitos mínimos
    
    Args:
        password (str): Contraseña a validar
        min_length (int): Longitud mínima requerida
        
    Returns:
        tuple: (bool, str) - (es_válida, mensaje_error)
    """
    if not password:
        return False, "La contraseña no puede estar vacía"
    
    if len(password) < min_length:
        return False, f"La contraseña debe tener al menos {min_length} caracteres"
    
    return True, ""


def formatear_saldo(cantidad, moneda="USD"):
    """
    Formatea un saldo monetario
    
    Args:
        cantidad (float): Cantidad a formatear
        moneda (str): Código de moneda
        
    Returns:
        str: Saldo formateado
    """
    return f"${cantidad:,.2f} {moneda}"


def guardar_sesion(usuario_data):
    """
    Guarda información de sesión del usuario
    
    Args:
        usuario_data (dict): Datos del usuario a guardar
    """
    try:
        with open(SESSION_FILE, 'w') as f:
            json.dump(usuario_data, f)
        return True
    except Exception as e:
        print(f"Error al guardar sesión: {e}")
        return False


def cargar_sesion():
    """
    Carga información de sesión guardada
    
    Returns:
        dict: Datos de sesión o None si no existe
    """
    try:
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error al cargar sesión: {e}")
    return None


def limpiar_sesion():
    """
    Elimina el archivo de sesión
    """
    try:
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)
        return True
    except Exception as e:
        print(f"Error al limpiar sesión: {e}")
        return False


def obtener_timestamp():
    """
    Obtiene timestamp actual formateado
    
    Returns:
        str: Timestamp en formato legible
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_evento(mensaje, tipo="INFO"):
    """
    Registra un evento en el log
    
    Args:
        mensaje (str): Mensaje a registrar
        tipo (str): Tipo de evento (INFO, ERROR, WARNING)
    """
    timestamp = obtener_timestamp()
    log_entry = f"[{timestamp}] [{tipo}] {mensaje}\n"
    
    try:
        from config import LOG_FILE
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error al escribir log: {e}")
