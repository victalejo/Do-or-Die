"""
Módulo de gestión de sesiones y autenticación
Maneja la lógica de login y estado del usuario
"""
from utils import validar_email, guardar_sesion, cargar_sesion, limpiar_sesion, log_evento


class SessionManager:
    """Gestor de sesiones de usuario"""
    
    def __init__(self):
        self.usuario_actual = None
        self.cuenta_activa = None
        self.saldo = 0
        self.moneda = "USD"
        self.sesion_iniciada = False
        
    def iniciar_sesion(self, email, password):
        """
        Inicia sesión de usuario
        
        Args:
            email (str): Correo electrónico
            password (str): Contraseña
            
        Returns:
            tuple: (bool, str) - (éxito, mensaje)
        """
        # Validar email
        if not validar_email(email):
            log_evento(f"Intento de login fallido: email inválido - {email}", "WARNING")
            return False, "El formato del correo electrónico no es válido"
        
        # Aquí se integraría con la API real de IQ Option
        # Por ahora, simulamos una autenticación exitosa
        
        self.usuario_actual = email
        self.sesion_iniciada = True
        
        # Guardar sesión
        sesion_data = {
            "email": email,
            "timestamp": self._obtener_timestamp(),
            "cuenta_tipo": "Demo"
        }
        
        guardar_sesion(sesion_data)
        log_evento(f"Sesión iniciada: {email}", "INFO")
        
        return True, "Inicio de sesión exitoso"
    
    def cerrar_sesion(self):
        """Cierra la sesión actual"""
        if self.usuario_actual:
            log_evento(f"Sesión cerrada: {self.usuario_actual}", "INFO")
        
        self.usuario_actual = None
        self.cuenta_activa = None
        self.sesion_iniciada = False
        limpiar_sesion()
    
    def cambiar_cuenta(self, tipo_cuenta):
        """
        Cambia el tipo de cuenta activa
        
        Args:
            tipo_cuenta (str): "Demo" o "Real"
        """
        if tipo_cuenta in ["Demo", "Real"]:
            self.cuenta_activa = tipo_cuenta
            # Actualizar saldo según tipo de cuenta
            if tipo_cuenta == "Demo":
                self.saldo = 10000
                self.moneda = "USD"
            log_evento(f"Cambio a cuenta {tipo_cuenta}", "INFO")
    
    def obtener_saldo(self):
        """
        Obtiene el saldo actual formateado
        
        Returns:
            str: Saldo formateado
        """
        from utils import formatear_saldo
        return formatear_saldo(self.saldo, self.moneda)
    
    def restaurar_sesion(self):
        """
        Intenta restaurar una sesión guardada
        
        Returns:
            bool: True si se restauró la sesión
        """
        sesion = cargar_sesion()
        if sesion and "email" in sesion:
            self.usuario_actual = sesion["email"]
            self.sesion_iniciada = True
            log_evento(f"Sesión restaurada: {sesion['email']}", "INFO")
            return True
        return False
    
    def _obtener_timestamp(self):
        """Obtiene timestamp actual"""
        from utils import obtener_timestamp
        return obtener_timestamp()
