# Example: reuse your existing OpenAI setup
from openai import OpenAI
import streamlit as sl

#Crear titulo para Streamlit App
sl.title("Local ChatGPT con Memoria")
sl.caption("Chatea con un modelo Llama-3 hosteado localmente utilizando LM Studio")

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Responde siempre con rimas."},
    {"role": "user", "content": "Presentate por favor."}
  ],
  temperature=0.7,
)

#Inicializar historial del chat

if "messages" not in sl.session_state:
    sl.session_state.messages = []


#Mostrar historial del chat
    
for message in sl.session_state.messages:
    with sl.chat_message(message["role"]):
        sl.markdown(message["content"])

#aceptar user input
        
if prompt := sl.chat_input("Hola como estas?"):
    sl.session_state.messages.append({"role":"system", "content":"Cuando el input empieza con /infouser, no seguir con el prompt y no responderle."})
    #agregar mensaje de usuario al historial
    sl.session_state.messages.append({"role":"user","content":prompt})
    #mostrar mensaje de usuario
    with sl.chat_message("user"):
        sl.markdown(prompt)
    #Ahora vamos a generar el response
    response = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=sl.session_state.messages,temperature=0.7
    )
    #Agrego response al historial
    sl.session_state.messages.append({"role":"assistant", "content":response.choices[0].message.content})
    #Muestro respuesta del asistente
    with sl.chat_message("assistant"):
        sl.markdown(response.choices[0].message.content)



