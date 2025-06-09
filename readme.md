# Configuración Inicial del Entorno Python

Antes de interactuar con cualquier API de LLM, es fundamental preparar el entorno de desarrollo en Python.

## Requisitos del Sistema

Se necesita tener Python 3.7 o superior instalado en el sistema.

## Entornos Virtuales (venv)

Es una práctica recomendada y esencial utilizar entornos virtuales. Estos permiten aislar las dependencias de cada proyecto, evitando conflictos entre diferentes versiones de librerías.

### Crear un entorno virtual

Abrir la terminal o el símbolo del sistema y ejecutar:

```bash
python3 -m venv llm-env
```

## Activar el entorno virtual
En Linux/macOS: source llm-env/bin/activate
En Windows: llm-env\Scripts\activate
Una vez activado, el nombre del entorno (ej. (llm-env)) aparecerá al inicio de la línea de comandos.

## Instalación de Librerías
Con el entorno virtual activado, se instalan las librerías necesarias.

Para los ejemplos de OpenAI, se utiliza: pip install openai
Si se desea experimentar con Google Gemini o Anthropic Claude, se instalarían:
pip install -q -U google-genai
pip install anthropic
## Obtención de API Keys
Obtener sus propias claves de API de los respectivos proveedores (OpenAI, Google AI Studio, Anthropic Console). Estos procesos suelen implicar el registro en la plataforma y la generación de una clave personal.

Es crucial recordar que estas claves son credenciales sensibles y deben manejarse con la máxima seguridad, preferiblemente cargándolas desde variables de entorno.