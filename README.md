# intelligentzone-backend
Backend para redirección segura a WhatsApp Business
# 🧠 Intelligent Zone Backend

Sistema backend para la gestión de asistentes conversacionales, automatización de flujos y ocultamiento seguro del número de WhatsApp Business. Desarrollado con enfoque en escalabilidad, branding digital y experiencia del cliente.

Características principales

-  Ocultamiento dinámico del número de WhatsApp Business
-  Integración modular con frontend React y widgets Elfsight
- API RESTful con Django y Django REST Framework
-  CI/CD con Docker, Kubernetes y Azure AD
-  Panel administrativo para gestión de flujos y métricas conversacionales

##  Tecnologías utilizadas

| Tecnología        | Propósito                                  |
|------------------|---------------------------------------------|
| Django + DRF     | Backend y API REST                          |
| PostgreSQL       | Base de datos relacional                    |
| Docker + K8s     | Contenedores y orquestación                 |
| Azure AD         | Autenticación empresarial                   |
| Elfsight         | Widgets conversacionales embebidos         |
| GitHub Actions   | Automatización de despliegues               |

##  Instalación local

```bash
git clone https://github.com/fabiimagenweb/intelligentzone-backend.git
cd intelligentzone-backend
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
