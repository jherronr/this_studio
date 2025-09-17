# Chat Application with Llama 3, Ollama, and Gradio

Este proyecto es una aplicación de chat interactiva desarrollada como parte de la Tarea 4 del curso **SI7016 - NLP Aplicado** de la Universidad EAFIT. La aplicación permite a los usuarios conversar con el modelo de lenguaje grande (LLM) Llama 3 8B, servido localmente a través del framework Ollama y presentado con una interfaz de usuario creada con Gradio.

El sistema completo fue diseñado y desplegado en la plataforma cloud **Lightning.ai**.

<img width="1847" height="872" alt="Gradio" src="https://github.com/user-attachments/assets/170bfa53-c268-4dc9-866a-61cbfe237b45" />

## 🚀 Arquitectura de la Solución

La aplicación sigue una arquitectura modular simple:

  * **Plataforma de Cómputo:** Un Studio en **Lightning.ai** proveyendo el entorno de ejecución y los recursos de GPU.
  * **Backend (Servidor de Inferencia):** **Ollama** se encarga de cargar y servir el modelo LLM Llama 3 8B, exponiendo una API para la inferencia.
  * **Frontend (Interfaz de Usuario):** Un script de **Python** con la librería **Gradio** crea una interfaz de chat web amigable que se comunica con el backend de Ollama.

## ✨ Características

  * Interfaz de chat interactiva y fácil de usar.
  * Impulsado por el modelo open-source **Llama 3 8B**.
  * Backend de inferencia eficiente gracias a **Ollama**.
  * Desplegable en entornos locales o en la nube (optimizado para Lightning.ai).

## 🛠️ Pila Tecnológica (Tech Stack)

  * Lenguaje: **Python 3.x**
  * Servidor de Inferencia: **Ollama**
  * Framework de UI: **Gradio**
  * Plataforma de Hosting: **Lightning.ai**
  * Modelo LLM: **meta-llama/Llama-3-8b**

## ⚙️ Configuración e Instalación

Sigue estos pasos para ejecutar la aplicación en un entorno como Lightning.ai Studio.

### 1\. Prerrequisitos

  * Un entorno con Python 3.8 o superior.
  * Se recomienda una máquina con GPU para un rendimiento óptimo.
  * Git.

### 2\. Clonar el Repositorio

```bash
git clone https://github.com/jherronr/this_studio

```

### 3\. Instalar Dependencias

Instala las librerías de Python necesarias.

```bash
pip install -r requirements.txt
```

### 4\. Instalar y Configurar Ollama

Si Ollama no está instalado en el sistema, ejecute el siguiente comando:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 5\. Descargar el Modelo LLM

Una vez instalado Ollama, inicia el servidor en segundo plano y descarga el modelo Llama 3 8B.

```bash
# Inicia el servidor en segundo plano
ollama serve &

# Descarga el modelo (esto tomará varios minutos)
ollama pull llama3:8b
```

## ▶️ Cómo Ejecutar la Aplicación

Con el servidor de Ollama corriendo y el modelo descargado, ejecuta el script principal de la aplicación:

```bash
python app.py
```

La aplicación se iniciará y podrás acceder a ella a través de la URL que aparecerá en la terminal. Si estás en Lightning.ai, la plataforma te proporcionará una URL pública para acceder a la interfaz de chat.

-----
