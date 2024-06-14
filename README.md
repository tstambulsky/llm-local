# Local ChatGPT con Memoria

Esta aplicación utiliza Streamlit para crear una interfaz web interactiva que permite chatear con un modelo de lenguaje Llama 3 alojado localmente. 

## Descripción

La aplicación permite a los usuarios interactuar con un modelo de lenguaje Llama 3, manteniendo un historial de chat y respondiendo de acuerdo a las instrucciones dadas. Este proyecto demuestra cómo integrar modelos de lenguaje avanzados en aplicaciones web fáciles de usar.

## Requisitos

- Python 3.8+
- Streamlit
- OpenAI

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/local-chatgpt-con-memoria.git
    cd local-chatgpt-con-memoria
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Asegúrate de tener un servidor local de Llama 3 corriendo en `http://localhost:1234`.

## Uso

1. Inicia la aplicación de Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Abre tu navegador y ve a `http://localhost:8501` para interactuar con la aplicación.
