# Registro de Cambios - Do or Die

## [2.0.0] - Noviembre 2025

### 🎉 Versión Mayor - Rediseño Completo

Esta versión representa una reescritura completa del sistema con arquitectura modular y mejores prácticas de desarrollo.

---

## ✨ Nuevas Características

### Arquitectura Modular

- **config.py**: Sistema centralizado de configuración
  - Constantes globales
  - Configuración de fuentes y colores
  - Rutas de recursos
  - Mensajes de error estandarizados

- **utils.py**: Biblioteca de utilidades
  - Validación avanzada de emails con regex
  - Validación de contraseñas con requisitos mínimos
  - Formateo de montos monetarios
  - Sistema de logging a archivo
  - Gestión de timestamps

- **session_manager.py**: Gestor de sesiones robusto
  - Inicio/cierre de sesión
  - Persistencia de sesiones en JSON
  - Cambio seguro entre cuentas
  - Restauración automática de sesión

### Interfaz de Usuario Mejorada

#### Ventana de Login
- Labels descriptivos para campos
- Validación en tiempo real
- Checkbox "Recordar sesión"
- Mensajes de error específicos
- Botón "Salir" agregado
- Ventana redimensionable

#### Ventana Principal
- **Menú completo**:
  - Archivo: Cerrar Sesión, Salir
  - Cuenta: Cambiar a Demo/Real
  - Ayuda: Acerca de, Manual de Usuario

- **Panel de información de cuenta**:
  - Radio buttons mejorados para tipo de cuenta
  - Visualización de saldo con formato
  - Selector de moneda (USD, EUR, GBP)
  - Actualización dinámica

- **Panel de trading**:
  - Selector de activos (EUR/USD, GBP/USD, USD/JPY, BTC/USD)
  - Input de monto con validación
  - Botones CALL/PUT con símbolos visuales
  - Confirmación de operaciones

- **Tabla de historial**:
  - Columnas: Hora, Activo, Tipo, Monto, Resultado
  - Vista de últimas 5 operaciones
  - Formato tabular profesional

### Sistema de Validación

- **Email**: 
  - Validación de formato con expresiones regulares
  - Verificación de dominio
  - Mensajes de error específicos

- **Contraseña**:
  - Longitud mínima configurable (default: 6)
  - Validación de campo no vacío
  - Mensajes informativos

- **Montos**:
  - Validación numérica
  - Manejo de excepciones
  - Prevención de valores inválidos

### Gestión de Sesiones

- **Persistencia**:
  - Archivo `.session` en JSON
  - Almacena email y timestamp
  - Tipo de cuenta activa

- **Restauración**:
  - Detección automática al iniciar
  - Confirmación del usuario
  - Opción de nueva sesión

- **Seguridad**:
  - Limpieza al cerrar sesión
  - No almacena contraseñas
  - Confirmación para acciones críticas

### Sistema de Logging

- **Archivo**: `app.log`
- **Eventos registrados**:
  - Inicio/cierre de aplicación
  - Login/logout de usuarios
  - Cambios de cuenta
  - Operaciones de trading
  - Errores del sistema

- **Formato**:
  ```
  [YYYY-MM-DD HH:MM:SS] [TIPO] Mensaje
  ```

- **Tipos**: INFO, WARNING, ERROR

### Confirmaciones de Seguridad

- Advertencia al cambiar a cuenta Real
- Confirmación antes de cerrar sesión
- Popup informativos para operaciones
- Auto-cierre de mensajes exitosos

---

## 🔧 Mejoras Técnicas

### Código

- **POO**: Clase `DoOrDieApp` encapsula toda la lógica
- **Separación de responsabilidades**: Cada módulo tiene un propósito claro
- **DRY**: Eliminación de código duplicado
- **Imports organizados**: Estructura limpia de dependencias

### Manejo de Errores

- Try-catch para operaciones críticas
- Validación de entrada del usuario
- Mensajes de error descriptivos
- Logging de excepciones

### Rendimiento

- Carga condicional de recursos
- Validación eficiente
- Gestión de memoria mejorada

---

## 📝 Documentación

### Archivos Nuevos

1. **USER_GUIDE.md**: Guía completa del usuario
   - Inicio rápido
   - Tutoriales paso a paso
   - Solución de problemas
   - Tips y trucos

2. **setup.py**: Script de instalación
   - Verificación de Python
   - Instalación automática de dependencias
   - Verificación de recursos
   - Creación de archivos de configuración

3. **requirements.txt**: Dependencias
   - PySimpleGUI>=4.60.0
   - Fácil instalación con pip

4. **.gitignore**: Exclusiones de Git
   - Archivos Python compilados
   - Sesiones y logs
   - Archivos del IDE
   - Archivos del sistema operativo

5. **CHANGELOG.md**: Este archivo
   - Registro detallado de cambios
   - Versionado semántico

### Documentación Mejorada

- **README.md actualizado**:
  - Características expandidas
  - Arquitectura del sistema
  - Instrucciones detalladas
  - Estructura del proyecto

- **CONTRIBUTING.md**: 
  - Mantiene guías originales
  - Referencia a nueva estructura

---

## 🔄 Migración desde v1.0

### Cambios No Compatibles

- La estructura del código cambió completamente
- Se requiere instalación de dependencias
- Configuración centralizada

### Pasos de Migración

1. Respalda tu versión actual
2. Clona la nueva versión
3. Ejecuta `python setup.py`
4. Inicia con `python main.py`

### Datos

- No hay migración de datos necesaria
- Las credenciales no se almacenan
- Cada sesión es independiente

---

## 🐛 Correcciones de Bugs

- **Login**: Validaciones robustas previenen inputs inválidos
- **Sesión**: Manejo correcto de archivos de sesión
- **Recursos**: Manejo de archivos faltantes sin crashes
- **Errores**: Try-catch previene cierres inesperados

---

## 🎨 Mejoras de UI/UX

- **Diseño consistente**: Fuentes y colores centralizados
- **Navegación clara**: Menús y botones intuitivos
- **Feedback inmediato**: Confirmaciones y mensajes
- **Responsividad**: Ventanas redimensionables
- **Accesibilidad**: Labels descriptivos

---

## 📊 Comparativa de Versiones

| Característica | v1.0 | v2.0 |
|----------------|------|------|
| Archivos Python | 1 | 4 |
| Líneas de código | ~60 | ~600+ |
| Validaciones | Básicas | Avanzadas |
| Logging | No | Sí |
| Sesiones | No | Persistentes |
| Documentación | Básica | Completa |
| Testing | No | Preparado |
| Arquitectura | Monolítica | Modular |
| Menús | No | Sí |
| Historial | No | Sí |

---

## 🚀 Próximas Características (Roadmap)

### v2.1.0 (Planeado)
- [ ] Integración real con API de IQ Option
- [ ] Gráficos de saldo histórico
- [ ] Notificaciones de sistema
- [ ] Configuración de alertas

### v2.2.0 (Futuro)
- [ ] Trading automático
- [ ] Análisis técnico básico
- [ ] Estrategias predefinidas
- [ ] Backtesting

### v3.0.0 (Visión)
- [ ] Machine Learning para predicciones
- [ ] Dashboard web
- [ ] Multi-usuario
- [ ] API REST

---

## 🙏 Agradecimientos

- Comunidad de PySimpleGUI por su excelente framework
- Usuarios beta testers (si aplica)
- Contribuidores del proyecto

---

## 📞 Soporte

Para reportar bugs o sugerir características:
- GitHub Issues: [https://github.com/victalejo/Do-or-Die/issues]
- Email: (si está disponible)

---

**Nota**: Esta es una versión mayor con cambios significativos. Se recomienda revisar toda la documentación antes de usar en producción.
