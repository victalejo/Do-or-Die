# Guía del Usuario - Do or Die v2.0

## 📖 Introducción

Bienvenido a Do or Die v2.0, un sistema mejorado de trading para IQ Option con arquitectura modular y características avanzadas.

## 🚀 Inicio Rápido

### Primera ejecución

1. Ejecuta el script de setup:
```bash
python setup.py
```

2. Inicia la aplicación:
```bash
python main.py
```

## 🔐 Sistema de Autenticación

### Inicio de Sesión

La aplicación incluye validaciones avanzadas:

- **Email**: Debe ser un correo electrónico válido (ej: usuario@dominio.com)
- **Contraseña**: Mínimo 6 caracteres

### Recordar Sesión

Puedes marcar "Recordar sesión" para que la aplicación restaure automáticamente tu sesión en el próximo inicio.

## 💼 Gestión de Cuentas

### Cuenta Demo

- **Propósito**: Practicar sin riesgo real
- **Saldo inicial**: $10,000 USD
- **Ideal para**: Principiantes y pruebas de estrategias

### Cuenta Real

- **Propósito**: Trading con dinero real
- **Advertencia**: La aplicación mostrará una confirmación antes de cambiar
- **Recomendación**: Practica primero en Demo

### Cambio de Cuenta

1. Selecciona el tipo de cuenta usando los radio buttons
2. Para cuenta Real, confirma en el diálogo de advertencia
3. El saldo se actualizará automáticamente

## 📈 Panel de Trading

### Selección de Activos

Activos disponibles:
- EUR/USD (Euro / Dólar Estadounidense)
- GBP/USD (Libra Esterlina / Dólar)
- USD/JPY (Dólar / Yen Japonés)
- BTC/USD (Bitcoin / Dólar)

### Tipos de Operación

**CALL (▲)**
- Opción alcista
- Se usa cuando predices que el precio subirá
- Botón verde

**PUT (▼)**
- Opción bajista
- Se usa cuando predices que el precio bajará
- Botón rojo

### Realizar una Operación

1. Selecciona el activo en el combo box
2. Ingresa el monto a invertir
3. Presiona CALL o PUT según tu predicción
4. Verás una confirmación de la operación

## 📊 Historial

La tabla de historial muestra:
- Hora de la operación
- Activo negociado
- Tipo (CALL/PUT)
- Monto invertido
- Resultado (cuando esté implementado)

## ⚙️ Configuración

### Monedas Disponibles

- USD (Dólar Estadounidense)
- EUR (Euro)
- GBP (Libra Esterlina)

Puedes cambiar la moneda de visualización desde el combo box "Moneda".

## 📝 Logs del Sistema

La aplicación registra automáticamente:

- Inicios y cierres de sesión
- Cambios de cuenta
- Operaciones realizadas
- Errores del sistema

Los logs se guardan en `app.log` para auditoría y depuración.

## 🔄 Sesiones

### Archivo de Sesión

La aplicación guarda información de sesión en `.session`:
- Email del usuario
- Timestamp de login
- Tipo de cuenta activa

### Restauración Automática

Al iniciar la aplicación:
1. Se verifica si existe una sesión previa
2. Se pregunta si deseas continuar con esa sesión
3. Puedes aceptar o iniciar sesión nuevamente

### Cerrar Sesión

Opciones para cerrar sesión:
1. Botón "Cerrar Sesión" en el panel principal
2. Menú: Archivo → Cerrar Sesión

Al cerrar sesión se limpia el archivo `.session`.

## 🛡️ Seguridad

### Buenas Prácticas

1. **No compartas tus credenciales**: La aplicación no almacena contraseñas
2. **Usa contraseñas fuertes**: Mínimo 6 caracteres, idealmente más
3. **Revisa los logs**: Verifica actividad sospechosa en `app.log`
4. **Cuenta Demo primero**: Practica antes de usar dinero real

### Validaciones

- Email: Formato válido requerido
- Contraseña: Longitud mínima verificada
- Montos: Solo números válidos aceptados

## 🐛 Solución de Problemas

### La aplicación no inicia

```bash
# Verifica la versión de Python
python --version

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error al cargar recursos

Si faltan `Logo fondo transparente.png` o `do_or_die.ico`:
- La aplicación funcionará sin ellos
- Son opcionales para la funcionalidad

### Sesión no se restaura

1. Verifica que `.session` existe en el directorio
2. Revisa `app.log` para errores
3. Intenta eliminar `.session` manualmente

### Errores de importación

```bash
# Asegúrate de tener PySimpleGUI instalado
pip install PySimpleGUI
```

## 📞 Soporte

Si encuentras problemas:

1. Revisa `app.log` para detalles del error
2. Consulta la sección de Issues en GitHub
3. Crea un nuevo issue con:
   - Descripción del problema
   - Pasos para reproducir
   - Contenido relevante de `app.log`

## 🎓 Tips y Trucos

### Atajos útiles

- **ESC**: Cerrar diálogos
- **Enter**: Confirmar en diálogos

### Mejores Prácticas

1. Siempre prueba en Demo primero
2. Revisa tu historial regularmente
3. No inviertas más de lo que puedes permitirte perder
4. Actualiza el saldo frecuentemente

### Optimización

- Cierra sesión cuando no uses la app
- Revisa y limpia `app.log` periódicamente
- Mantén las dependencias actualizadas

## 📚 Recursos Adicionales

- [README.md](README.md) - Documentación general
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guía de contribución
- [LICENSE](LICENSE) - Información de licencia

## 🔄 Actualizaciones

Para actualizar a la última versión:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

---

**Versión**: 2.0  
**Última actualización**: Noviembre 2025  
**Autor**: Victor Alejandro Cano Jaramillo
