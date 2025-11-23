# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a Do or Die! Este documento proporciona las directrices para contribuir al proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Proceso de desarrollo](#proceso-de-desarrollo)
- [Estándares de código](#estándares-de-código)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Reporte de bugs](#reporte-de-bugs)
- [Sugerencias de mejoras](#sugerencias-de-mejoras)

## 📜 Código de Conducta

Este proyecto y todos los participantes están regidos por un código de conducta. Al participar, se espera que respetes este código. Por favor, reporta comportamientos inaceptables abriendo un issue.

### Nuestros estándares

- Usar un lenguaje acogedor e inclusivo
- Respetar diferentes puntos de vista y experiencias
- Aceptar críticas constructivas con gracia
- Enfocarse en lo que es mejor para la comunidad
- Mostrar empatía hacia otros miembros de la comunidad

## 🚀 ¿Cómo puedo contribuir?

### Reportar Bugs

Los bugs se rastrean como issues de GitHub. Antes de crear un nuevo issue:

1. **Verifica** si el bug ya ha sido reportado
2. **Incluye** detalles específicos sobre tu configuración y cómo reproducir el problema
3. **Proporciona** información del sistema (OS, versión de Python, etc.)

### Sugerir Mejoras

Las sugerencias de mejoras también se rastrean como issues. Al crear una sugerencia:

1. **Usa un título claro y descriptivo**
2. **Proporciona una descripción detallada** de la mejora propuesta
3. **Explica por qué** esta mejora sería útil
4. **Incluye ejemplos** si es posible

### Tu Primera Contribución de Código

¿No estás seguro por dónde empezar? Busca issues etiquetados como:

- `good first issue` - Issues apropiados para principiantes
- `help wanted` - Issues que necesitan atención

## 🔧 Proceso de Desarrollo

1. **Fork** el repositorio
2. **Crea** una rama desde `main`:
   ```bash
   git checkout -b feature/mi-nueva-funcionalidad
   ```
   o
   ```bash
   git checkout -b fix/correccion-de-bug
   ```

3. **Realiza** tus cambios siguiendo los estándares de código
4. **Prueba** tus cambios exhaustivamente
5. **Commit** tus cambios con mensajes descriptivos:
   ```bash
   git commit -m "feat: agrega nueva funcionalidad X"
   ```
6. **Push** a tu fork:
   ```bash
   git push origin feature/mi-nueva-funcionalidad
   ```
7. **Abre** un Pull Request

## 💻 Estándares de Código

### Python

Seguimos las convenciones de estilo PEP 8:

- **Indentación**: 4 espacios (no tabs)
- **Longitud de línea**: Máximo 79 caracteres
- **Nombres de variables**: snake_case
- **Nombres de clases**: PascalCase
- **Nombres de constantes**: UPPER_CASE

### Ejemplo de código bien formateado:

```python
def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra.
    
    Args:
        precio (float): Precio unitario del producto
        cantidad (int): Cantidad de productos
        
    Returns:
        float: Total de la compra
    """
    return precio * cantidad
```

### Documentación

- Todas las funciones públicas deben tener docstrings
- Usa comentarios para explicar lógica compleja
- Actualiza el README.md si añades nuevas características

### Testing

- Prueba todas las funcionalidades nuevas
- Asegúrate de que el código existente sigue funcionando
- Incluye casos de prueba para bugs corregidos

## 🔄 Proceso de Pull Request

1. **Actualiza** el README.md con detalles de cambios si es necesario
2. **Asegúrate** de que tu código sigue los estándares establecidos
3. **Prueba** que todo funciona correctamente
4. **Describe** claramente los cambios en el PR:
   - ¿Qué problema resuelve?
   - ¿Cómo se probó?
   - ¿Qué tipo de cambio es? (bugfix, feature, etc.)

### Plantilla de Pull Request

```markdown
## Descripción
[Descripción breve de los cambios]

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Cambio que rompe compatibilidad
- [ ] Documentación

## ¿Cómo se ha probado?
[Describe las pruebas realizadas]

## Checklist
- [ ] Mi código sigue los estándares del proyecto
- [ ] He realizado auto-revisión de mi código
- [ ] He comentado mi código en áreas difíciles de entender
- [ ] He actualizado la documentación correspondiente
- [ ] Mis cambios no generan nuevas advertencias
- [ ] He probado que mi solución funciona correctamente
```

## 🐛 Reporte de Bugs

Al reportar un bug, incluye:

- **Título descriptivo**
- **Pasos para reproducir** el problema
- **Comportamiento esperado** vs **comportamiento actual**
- **Capturas de pantalla** si aplica
- **Información del sistema**:
  - OS: [ej. Windows 10]
  - Python version: [ej. 3.9.0]
  - PySimpleGUI version: [ej. 4.60.0]
- **Logs o mensajes de error**

### Plantilla de Bug Report

```markdown
**Descripción del bug**
[Descripción clara del problema]

**Pasos para reproducir**
1. Ir a '...'
2. Hacer click en '...'
3. Ver error

**Comportamiento esperado**
[Lo que debería suceder]

**Capturas de pantalla**
[Si aplica]

**Información del sistema:**
 - OS: [ej. Windows 10]
 - Python: [ej. 3.9.0]
 - PySimpleGUI: [ej. 4.60.0]

**Contexto adicional**
[Información adicional relevante]
```

## 💡 Sugerencias de Mejoras

Para sugerir mejoras:

1. **Verifica** que la sugerencia no exista ya
2. **Describe** la mejora propuesta en detalle
3. **Explica** el beneficio para los usuarios
4. **Proporciona ejemplos** de uso si es posible

## 🏷️ Convenciones de Commits

Usamos commits semánticos:

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formateo, punto y coma faltantes, etc.
- `refactor:` Refactorización de código
- `test:` Añadir tests
- `chore:` Mantenimiento

Ejemplo:
```bash
git commit -m "feat: añade soporte para múltiples idiomas"
git commit -m "fix: corrige error en validación de login"
git commit -m "docs: actualiza guía de instalación"
```

## ❓ Preguntas

Si tienes preguntas sobre cómo contribuir, no dudes en:

- Abrir un issue con la etiqueta `question`
- Contactar al mantenedor del proyecto

---

¡Gracias por contribuir a Do or Die! 🎉
