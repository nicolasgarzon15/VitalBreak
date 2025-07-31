# VitalBreak

Aplicación Flask para gestión de rutinas de ejercicios.

## 🚀 Características

- Sistema de autenticación de usuarios
- Gestión de ejercicios por dificultad y grupo muscular
- Seguimiento de progreso de rutinas
- Dashboard de supervisión con estadísticas

## 🛠️ Tecnologías

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Base de datos**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **CI/CD**: GitHub Actions

## 📋 Requisitos

- Python 3.11+
- PostgreSQL
- Git

## 🔧 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd VitalBreak
```

### 2. Crear entorno virtual
```bash
python -m venv env
# Windows PowerShell
.\env\Scripts\Activate.ps1
# Windows CMD
.\env\Scripts\activate.bat
# Linux/macOS
source env/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

### 5. Ejecutar la aplicación
```bash
python src/app.py
```

## 🚀 CI/CD con GitHub Actions

### Configuración inicial

1. **Subir el código a GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <tu-repositorio-github>
git push -u origin main
```

2. **Configurar Secrets en GitHub**:
   - Ve a Settings > Secrets and variables > Actions
   - Añade los siguientes secrets:
     - `DATABASE_URL`: URL de tu base de datos de producción
     - `SECRET_KEY`: Clave secreta para Flask

### Pipeline CI/CD

El pipeline incluye:

#### ✅ **Continuous Integration (CI)**
- **Linting**: Análisis de código con flake8
- **Security Scan**: Escaneo de vulnerabilidades con bandit
- **Testing**: Pruebas automatizadas con pytest
- **Database Testing**: PostgreSQL en containers

#### 🚀 **Continuous Deployment (CD)**
- **Auto-deploy**: Deployment automático en push a `main`
- **Environment Variables**: Configuración segura
- **Health Checks**: Verificación post-deployment

### Activación automática

El pipeline se ejecuta en:
- Push a las ramas `main` y `develop`
- Pull requests hacia `main`

### Personalizar Deployment

Para configurar tu deployment específico, edita la sección `deploy` en `.github/workflows/ci-cd.yml`:

```yaml
- name: Deploy to production
  run: |
    # Aquí configura tu deployment específico:
    # Heroku: git push heroku main
    # AWS: aws deploy...
    # DigitalOcean: doctl apps create-deployment...
```

## 🐳 Docker

### Construir imagen
```bash
docker build -t vitalbreak .
```

### Ejecutar container
```bash
docker run -p 5000:5000 --env-file .env vitalbreak
```

## 📁 Estructura del Proyecto

```
VitalBreak/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD
├── src/
│   ├── app.py                 # Aplicación principal
│   ├── config.py              # Configuración
│   ├── models/                # Modelos de datos
│   ├── static/                # Archivos estáticos
│   └── templates/             # Templates HTML
├── requirements.txt           # Dependencias Python
├── Dockerfile                 # Configuración Docker
├── .env.example              # Variables de entorno ejemplo
└── README.md                 # Documentación
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. 