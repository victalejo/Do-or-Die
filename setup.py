"""
Script de instalación y configuración inicial para Do or Die
"""
import os
import sys


def verificar_python():
    """Verifica la versión de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Se requiere Python 3.7 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True


def instalar_dependencias():
    """Instala las dependencias del proyecto"""
    print("\n📦 Instalando dependencias...")
    try:
        import subprocess
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Dependencias instaladas correctamente")
            return True
        else:
            print(f"❌ Error al instalar dependencias:\n{result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def verificar_recursos():
    """Verifica que existan los archivos de recursos necesarios"""
    print("\n🖼️  Verificando recursos...")
    recursos = {
        'Logo fondo transparente.png': False,
        'do_or_die.ico': False
    }
    
    for archivo in recursos.keys():
        if os.path.exists(archivo):
            recursos[archivo] = True
            print(f"✓ {archivo} encontrado")
        else:
            print(f"⚠️  {archivo} no encontrado (opcional)")
    
    return True


def crear_archivos_iniciales():
    """Crea archivos necesarios si no existen"""
    print("\n📝 Creando archivos de configuración...")
    
    # Crear archivo .gitignore si no existe
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/

# Do or Die
.session
app.log
*.png
*.ico
"""
    
    if not os.path.exists('.gitignore'):
        with open('.gitignore', 'w') as f:
            f.write(gitignore_content)
        print("✓ .gitignore creado")
    else:
        print("✓ .gitignore ya existe")
    
    return True


def main():
    """Función principal de setup"""
    print("=" * 60)
    print("🎯 Do or Die - Script de Configuración")
    print("=" * 60)
    
    # Verificar Python
    if not verificar_python():
        sys.exit(1)
    
    # Instalar dependencias
    if not instalar_dependencias():
        print("\n⚠️  Advertencia: Algunas dependencias no se instalaron correctamente")
        respuesta = input("¿Desea continuar de todos modos? (s/n): ")
        if respuesta.lower() != 's':
            sys.exit(1)
    
    # Verificar recursos
    verificar_recursos()
    
    # Crear archivos iniciales
    crear_archivos_iniciales()
    
    print("\n" + "=" * 60)
    print("✨ ¡Configuración completada!")
    print("=" * 60)
    print("\nPara ejecutar la aplicación:")
    print("  python main.py")
    print("\nPara más información, consulta el README.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
