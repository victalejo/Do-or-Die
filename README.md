# Do or Die 🎯

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/victalejo/Do-or-Die)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

Una aplicación de escritorio desarrollada en Python para facilitar el acceso y gestión de cuentas de trading en IQ Option.

## 📋 Descripción

Do or Die es una interfaz gráfica de usuario (GUI) construida con PySimpleGUI que proporciona una experiencia simplificada para gestionar sesiones de trading en IQ Option. La aplicación permite a los usuarios autenticarse y acceder a sus cuentas de práctica (Demo) o cuentas reales.

## ✨ Características

- 🔐 **Sistema de autenticación avanzado** con validación de email y contraseñas
- 💼 **Gestión de cuentas** Demo y Real con cambio seguro
- 🎨 **Interfaz moderna** con tema Material Design 2
- 👤 **Personalización** de usuario con sesiones persistentes
- 📊 **Visualización de saldo** en tiempo real con múltiples monedas
- 📈 **Panel de trading** con operaciones CALL/PUT
- 📋 **Historial de operaciones** para seguimiento de trades
- 🔄 **Restauración automática** de sesiones previas
- 📝 **Sistema de logging** para auditoría y depuración
- ⚙️ **Arquitectura modular** con separación de responsabilidades

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

**Opción 1: Instalación automática**

```bash
python setup.py
```

**Opción 2: Instalación manual**

1. Clona el repositorio:

```bash
git clone https://github.com/victalejo/Do-or-Die.git
cd Do-or-Die
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Asegúrate de tener los recursos necesarios:
   - `Logo fondo transparente.png` - Logo de la aplicación
   - `do_or_die.ico` - Icono de la aplicación

## 💻 Uso

Ejecuta la aplicación con:

```bash
python main.py
```

### Flujo de uso

1. **Inicio de sesión**: Ingresa tus credenciales de IQ Option con validación de formato
2. **Selección de cuenta**: Elige entre cuenta Demo o Real con confirmación de seguridad
3. **Panel de trading**: Realiza operaciones, consulta saldo y gestiona tu cuenta
4. **Historial**: Revisa tus operaciones realizadas

Para más detalles, consulta la [Guía del Usuario](USER_GUIDE.md).

## 🛠️ Tecnologías utilizadas

- **Python 3.7+** - Lenguaje de programación
- **PySimpleGUI** - Framework para interfaz gráfica
- **JSON** - Almacenamiento de sesiones
- **Regex** - Validación de datos

## 🎯 Funcionalidades Principales

### Autenticación
- Validación de formato de email con expresiones regulares
- Validación de contraseñas con longitud mínima
- Persistencia de sesiones entre ejecuciones
- Opción de "Recordar sesión"

### Gestión de Cuentas
- Soporte para cuentas Demo y Real
- Cambio seguro entre tipos de cuenta
- Visualización de saldo en múltiples monedas (USD, EUR, GBP)
- Actualización de saldo en tiempo real

### Panel de Trading
- Selección de activos (EUR/USD, GBP/USD, USD/JPY, BTC/USD)
- Operaciones CALL (alcista) y PUT (bajista)
- Definición de montos de inversión
- Tabla de historial de operaciones

### Sistema de Logging
- Registro de todas las operaciones importantes
- Auditoría de sesiones (inicio/cierre)
- Registro de errores para depuración
- Archivo de log persistente (`app.log`)

## 📁 Estructura del proyecto

```text
Do-or-Die/
│
├── main.py                      # Archivo principal de la aplicación
├── config.py                    # Configuración y constantes
├── utils.py                     # Utilidades y funciones helper
├── session_manager.py           # Gestión de sesiones y autenticación
├── setup.py                     # Script de instalación automática
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos ignorados por Git
├── Logo fondo transparente.png  # Logo de la aplicación
├── do_or_die.ico               # Icono de la aplicación
├── README.md                    # Documentación principal
├── USER_GUIDE.md               # Guía detallada del usuario
├── LICENSE                      # Licencia MIT
└── CONTRIBUTING.md              # Guía de contribución
```

## 🏗️ Arquitectura del Sistema

El proyecto sigue una arquitectura modular con separación de responsabilidades:

- **main.py**: Punto de entrada y clase principal `DoOrDieApp`
- **config.py**: Centraliza todas las constantes y configuraciones
- **utils.py**: Funciones de utilidad (validación, formateo, logging)
- **session_manager.py**: Gestión del estado de sesión del usuario

### Flujo de la aplicación

1. Inicio → Verificación de sesión previa
2. Login → Validación de credenciales
3. Panel principal → Gestión de cuenta y trading
4. Operaciones → Registro y logging
5. Cierre → Limpieza de sesión

## ⚠️ Advertencias y consideraciones

- Esta aplicación es solo una interfaz de usuario y requiere credenciales válidas de IQ Option
- El trading conlleva riesgos financieros. Opera con responsabilidad
- Se recomienda usar primero la cuenta Demo antes de operar con dinero real
- Este proyecto es independiente y no está afiliado oficialmente con IQ Option

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles sobre nuestro código de conducta y el proceso para enviar pull requests.

## 📚 Documentación Adicional

- 🚀 [QUICKSTART.md](QUICKSTART.md) - Guía de inicio rápido
- 👤 [USER_GUIDE.md](USER_GUIDE.md) - Manual completo del usuario
- 💻 [EXAMPLES.md](EXAMPLES.md) - Ejemplos de código para desarrolladores
- 📝 [CHANGELOG.md](CHANGELOG.md) - Historial de cambios y versiones
- ✨ [MEJORAS_RESUMEN.md](MEJORAS_RESUMEN.md) - Resumen detallado de mejoras v2.0

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Victor Alejandro Cano Jaramillo** - [@victalejo](https://github.com/victalejo)

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en este repositorio.

## 🙏 Agradecimientos

- A la comunidad de PySimpleGUI por su excelente framework
- A todos los contribuidores que ayudan a mejorar este proyecto

---

⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub!
