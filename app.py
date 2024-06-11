# Example: reuse your existing OpenAI setup
from openai import OpenAI
import streamlit as sl

# Crear titulo para Streamlit App
sl.title("Local ChatGPT con Memoria")
sl.caption("Chatea con un modelo Llama-3 hosteado localmente utilizando LM Studio")

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Inicializar historial del chat
if "messages" not in sl.session_state:
    sl.session_state.messages = []

# Mostrar historial del chat
for message in sl.session_state.messages:
    with sl.chat_message(message["role"]):
        sl.markdown(message["content"])

# Aceptar user input
if prompt := sl.chat_input("Hola, ¿cómo estás?"):
    # Agregar mensaje de usuario al historial y mostrarlo inmediatamente
    sl.session_state.messages.append({"role": "user", "content": prompt})
    with sl.chat_message("user"):
        sl.markdown(prompt)

    # Placeholder para la respuesta del asistente
    placeholder = sl.empty()

    # Ahora vamos a generar el response
    response = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=sl.session_state.messages,
        temperature=0.7
    )
    
    # Agregar response al historial
    assistant_message = response.choices[0].message.content
    sl.session_state.messages.append({"role": "assistant", "content": assistant_message})

    # Mostrar respuesta del asistente
    with placeholder.container():
        with sl.chat_message("assistant"):
            sl.markdown(assistant_message)
