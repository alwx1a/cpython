import alexia
from tkinter import alexia

# --- Función que genera respuestas del chatbot ---
def responder(pregunta):
    pregunta = pregunta.lower()

    if "hola" in pregunta:
        return "¡Hola! 😊 ¿Cómo estás?"
    elif "cómo estás" in pregunta:
        return "Estoy muy bien, gracias por preguntar 😄"
    elif "tu nombre" in pregunta:
        return "Soy un chatbot creado con Python y Tkinter 🤖"
    elif "adiós" in pregunta or "bye" in pregunta:
        return "¡Adiós! 👋 ¡Que tengas un gran día!"
    elif "gracias" in pregunta:
        return "¡De nada! 😁"
    else:
        return "No estoy seguro de cómo responder a eso 🤔"

# --- Función para enviar mensaje ---
def enviar():
    mensaje_usuario = entrada_texto.get().strip()
    if mensaje_usuario == "":
        return

    # Mostrar mensaje del usuario
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"Tú: {mensaje_usuario}\n", "usuario")

    # Obtener respuesta del bot
    respuesta = responder(mensaje_usuario)
    chat.insert(tk.END, f"Bot: {respuesta}\n\n", "bot")

    # Limpiar entrada y hacer scroll al final
    entrada_texto.delete(0, tk.END)
    chat.yview(tk.END)
    chat.config(state=tk.DISABLED)

# --- Crear ventana principal ---
ventana = tk.Tk()
ventana.title("Chatbot en Tkinter 🤖")
ventana.geometry("420x500")
ventana.resizable(False, False)
ventana.config(bg="#E8E8E8")

# --- Área del chat ---
chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=20, font=("Arial", 10))
chat.pack(padx=10, pady=10)
chat.tag_config("usuario", foreground="#1E90FF", font=("Arial", 10, "bold"))
chat.tag_config("bot", foreground="#008000", font=("Arial", 10))
chat.insert(tk.END, "Bot: ¡Hola! Soy tu asistente virtual. Escribe algo para empezar.\n\n", "bot")
chat.config(state=tk.DISABLED)

# --- Campo de entrada ---
entrada_texto = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_texto.pack(padx=10, pady=5)

# --- Botón de enviar ---
boton_enviar = tk.Button(
    ventana,
    text="Enviar",
    command=enviar,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=10
)
boton_enviar.pack(pady=5)

# --- Permitir enviar con Enter ---
ventana.bind("<Return>", lambda event: enviar())

# --- Ejecutar interfaz ---
ventana.mainloop()
