"""
Do or Die - Sistema de Trading para IQ Option
Aplicación mejorada con arquitectura modular y mejores prácticas
"""
import PySimpleGUI as sg
import os
from config import *
from utils import validar_email, validar_password, formatear_saldo, log_evento
from session_manager import SessionManager


class DoOrDieApp:
    """Clase principal de la aplicación"""
    
    def __init__(self):
        self.session_manager = SessionManager()
        sg.theme(THEME)
        log_evento("Aplicación iniciada", "INFO")
        
    def mostrar_login(self):
        """
        Muestra la ventana de inicio de sesión
        
        Returns:
            bool: True si el login fue exitoso
        """
        # Layout mejorado con labels
        layout = [
            [sg.Image(LOGO_PATH if os.path.exists(LOGO_PATH) else None)],
            [sg.Text('Bienvenido a Do or Die', justification="center", 
                    size=(30, 1), font=FONT_TITLE)],
            [sg.Text('Inicio de Sesión', justification="center", 
                    size=(30, 1), font=FONT_SUBTITLE, pad=(0, 10))],
            [sg.Text('Correo electrónico:', size=(15, 1), font=FONT_TEXT)],
            [sg.Input(key="correo", size=(40, 1), font=FONT_INPUT)],
            [sg.Text('Contraseña:', size=(15, 1), font=FONT_TEXT, pad=(0, (10, 0)))],
            [sg.Input(key="contrasena", size=(40, 1), password_char="•", font=FONT_INPUT)],
            [sg.Checkbox('Recordar sesión', key='recordar', font=FONT_TEXT, pad=(0, 10))],
            [sg.Button("Iniciar Sesión", button_color=COLOR_SUCCESS, 
                      key="iniciar_sesion", font=FONT_BUTTON, size=(15, 1)),
             sg.Button("Salir", button_color=COLOR_ERROR, 
                      key="salir", font=FONT_BUTTON, size=(15, 1))]
        ]
        
        icon_path = ICON_PATH if os.path.exists(ICON_PATH) else None
        window = sg.Window('Do or Die - Login', layout, 
                          element_justification="c", icon=icon_path, 
                          finalize=True, resizable=True)
        
        login_exitoso = False
        
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "salir"):
                log_evento("Usuario canceló el login", "INFO")
                break
                
            if event == "iniciar_sesion":
                correo = values["correo"].strip()
                contrasena = values["contrasena"].strip()
                
                # Validaciones mejoradas
                if not correo and not contrasena:
                    sg.popup_error(MSG_ERROR_EMPTY_FIELDS, 
                                  title="Error", font=FONT_TEXT)
                    continue
                    
                if not correo:
                    sg.popup_error(MSG_ERROR_EMPTY_EMAIL, 
                                  title="Error", font=FONT_TEXT)
                    continue
                    
                if not validar_email(correo):
                    sg.popup_error(MSG_ERROR_INVALID_EMAIL, 
                                  title="Error", font=FONT_TEXT)
                    continue
                
                # Validar contraseña
                valida, mensaje = validar_password(contrasena)
                if not valida:
                    sg.popup_error(mensaje, title="Error", font=FONT_TEXT)
                    continue
                
                # Intentar iniciar sesión
                exito, mensaje = self.session_manager.iniciar_sesion(correo, contrasena)
                
                if exito:
                    sg.popup_auto_close(MSG_SUCCESS_LOGIN, 
                                       title="Éxito", 
                                       font=FONT_TEXT,
                                       background_color=COLOR_SUCCESS,
                                       auto_close_duration=2)
                    login_exitoso = True
                    break
                else:
                    sg.popup_error(mensaje, title="Error de autenticación", 
                                  font=FONT_TEXT)
        
        window.close()
        return login_exitoso
    
    def mostrar_principal(self):
        """Muestra la ventana principal de la aplicación"""
        
        # Establecer cuenta por defecto
        self.session_manager.cambiar_cuenta("Demo")
        
        # Layout mejorado
        menu_def = [
            ['Archivo', ['Cerrar Sesión', 'Salir']],
            ['Cuenta', ['Cambiar a Demo', 'Cambiar a Real']],
            ['Ayuda', ['Acerca de', 'Manual de Usuario']]
        ]
        
        layout = [
            [sg.Menu(menu_def)],
            [sg.Image(LOGO_PATH if os.path.exists(LOGO_PATH) else None)],
            [sg.Text(f'Bienvenido {self.session_manager.usuario_actual}', 
                    justification="center", size=(50, 1), font=FONT_HEADING)],
            [sg.HorizontalSeparator()],
            
            # Panel de información de cuenta
            [sg.Frame('Información de Cuenta', [
                [sg.Text('Tipo de Cuenta:', size=(15, 1), font=FONT_TEXT),
                 sg.Radio('Demo', group_id="cuenta", key="demo", 
                         font=FONT_TEXT, default=True, enable_events=True),
                 sg.Radio('Real', group_id="cuenta", key="real", 
                         font=FONT_TEXT, enable_events=True)],
                [sg.Text('Saldo Actual:', size=(15, 1), font=FONT_TEXT),
                 sg.Text(self.session_manager.obtener_saldo(), 
                        key="saldo_texto", font=FONT_TEXT, 
                        text_color=COLOR_SUCCESS, size=(20, 1))],
                [sg.Text('Moneda:', size=(15, 1), font=FONT_TEXT),
                 sg.Combo(['USD', 'EUR', 'GBP'], default_value='USD', 
                         key='moneda', font=FONT_TEXT, readonly=True, 
                         size=(18, 1))]
            ], font=FONT_TEXT, pad=(10, 10))],
            
            [sg.HorizontalSeparator()],
            
            # Panel de operaciones
            [sg.Frame('Panel de Trading', [
                [sg.Text('Activo:', size=(10, 1), font=FONT_TEXT),
                 sg.Combo(['EUR/USD', 'GBP/USD', 'USD/JPY', 'BTC/USD'], 
                         default_value='EUR/USD', key='activo', 
                         font=FONT_TEXT, size=(15, 1))],
                [sg.Text('Monto:', size=(10, 1), font=FONT_TEXT),
                 sg.Input('100', key='monto', size=(10, 1), font=FONT_INPUT),
                 sg.Text('USD', font=FONT_TEXT)],
                [sg.Text('Dirección:', size=(10, 1), font=FONT_TEXT),
                 sg.Button('CALL ▲', button_color=('white', 'green'), 
                          key='call', font=FONT_BUTTON, size=(10, 1)),
                 sg.Button('PUT ▼', button_color=('white', 'red'), 
                          key='put', font=FONT_BUTTON, size=(10, 1))],
            ], font=FONT_TEXT, pad=(10, 10))],
            
            [sg.HorizontalSeparator()],
            
            # Historial de operaciones
            [sg.Frame('Historial de Operaciones', [
                [sg.Table(values=[], headings=['Hora', 'Activo', 'Tipo', 'Monto', 'Resultado'],
                         auto_size_columns=True, justification='center',
                         key='tabla_historial', font=FONT_TEXT,
                         num_rows=5)]
            ], font=FONT_TEXT, pad=(10, 10))],
            
            [sg.Button("Actualizar Saldo", button_color=COLOR_INFO, 
                      key="actualizar", font=FONT_BUTTON),
             sg.Button("Cerrar Sesión", button_color=COLOR_WARNING, 
                      key="cerrar_sesion", font=FONT_BUTTON),
             sg.Button("Salir", button_color=COLOR_ERROR, 
                      key="salir", font=FONT_BUTTON)]
        ]
        
        icon_path = ICON_PATH if os.path.exists(ICON_PATH) else None
        window = sg.Window('Do or Die - Panel Principal', layout, 
                          element_justification="c", icon=icon_path,
                          finalize=True, resizable=True)
        
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "salir", "Salir"):
                log_evento("Aplicación cerrada", "INFO")
                break
                
            if event in ("cerrar_sesion", "Cerrar Sesión"):
                if sg.popup_yes_no("¿Desea cerrar sesión?", 
                                  title="Confirmar", font=FONT_TEXT) == "Yes":
                    self.session_manager.cerrar_sesion()
                    log_evento("Sesión cerrada por el usuario", "INFO")
                    break
            
            # Cambio de tipo de cuenta
            if event in ("demo", "Cambiar a Demo"):
                self.session_manager.cambiar_cuenta("Demo")
                window["saldo_texto"].update(self.session_manager.obtener_saldo())
                window["demo"].update(True)
                
            if event in ("real", "Cambiar a Real"):
                respuesta = sg.popup_yes_no(
                    "¿Está seguro de cambiar a cuenta REAL?\n"
                    "Operará con dinero real.",
                    title="Advertencia", font=FONT_TEXT
                )
                if respuesta == "Yes":
                    self.session_manager.cambiar_cuenta("Real")
                    window["saldo_texto"].update(self.session_manager.obtener_saldo())
                    window["real"].update(True)
                else:
                    window["demo"].update(True)
            
            # Operaciones de trading
            if event in ("call", "put"):
                try:
                    monto = float(values["monto"])
                    activo = values["activo"]
                    tipo = "CALL" if event == "call" else "PUT"
                    
                    mensaje = f"Operación {tipo} registrada:\n"
                    mensaje += f"Activo: {activo}\n"
                    mensaje += f"Monto: ${monto:.2f}"
                    
                    sg.popup_auto_close(mensaje, title="Operación Ejecutada",
                                       font=FONT_TEXT, auto_close_duration=2)
                    
                    log_evento(f"Operación {tipo}: {activo} - ${monto}", "INFO")
                except ValueError:
                    sg.popup_error("Ingrese un monto válido", 
                                  title="Error", font=FONT_TEXT)
            
            if event == "actualizar":
                window["saldo_texto"].update(self.session_manager.obtener_saldo())
                sg.popup_auto_close("Saldo actualizado", 
                                   auto_close_duration=1, font=FONT_TEXT)
            
            # Acerca de
            if event == "Acerca de":
                sg.popup("Do or Die v2.0\n\n"
                        "Sistema de Trading para IQ Option\n"
                        "Desarrollado por Victor Alejandro Cano Jaramillo\n\n"
                        "© 2025 Todos los derechos reservados",
                        title="Acerca de", font=FONT_TEXT)
        
        window.close()
    
    def ejecutar(self):
        """Ejecuta la aplicación completa"""
        try:
            # Intentar restaurar sesión previa
            if self.session_manager.restaurar_sesion():
                respuesta = sg.popup_yes_no(
                    f"¿Desea continuar con la sesión de {self.session_manager.usuario_actual}?",
                    title="Sesión anterior detectada", font=FONT_TEXT
                )
                if respuesta != "Yes":
                    self.session_manager.cerrar_sesion()
                    if not self.mostrar_login():
                        return
                # Si acepta restaurar, continúa al panel principal
            else:
                # No hay sesión previa, mostrar login
                if not self.mostrar_login():
                    return
            
            # Mostrar ventana principal
            self.mostrar_principal()
            
        except Exception as e:
            log_evento(f"Error crítico: {str(e)}", "ERROR")
            sg.popup_error(f"Error crítico en la aplicación:\n{str(e)}", 
                          title="Error", font=FONT_TEXT)
        finally:
            log_evento("Aplicación finalizada", "INFO")


if __name__ == '__main__':
    app = DoOrDieApp()
    app.ejecutar()
