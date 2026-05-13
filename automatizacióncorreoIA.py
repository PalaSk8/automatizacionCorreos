import webbrowser
import urllib.parse
import pyautogui
from time import sleep

# 1. Configuración de datos
destinatarios = [
    "analista.ia@cemcomx.com",
    "eduardo.macedo@flecharoja.com.mx"
]
emails_concatenados = ",".join(destinatarios)

subject = "Reporte Automático"
body = "Hola,\n\nEste es un mensaje enviado automáticamente mediante Python y atajos de teclado.\n\nSaludos."

# 2. Codificación
subject_encoded = urllib.parse.quote(subject)
body_encoded = urllib.parse.quote(body)

# 3. Construcción de URL
url = f"https://mail.google.com/mail/?view=cm&fs=1&to={emails_concatenados}&su={subject_encoded}&body={body_encoded}"

# 4. Automatización
webbrowser.open(url)

# Esperamos a que el navegador abra y cargue la página
# Gmail es pesado, así que 6-8 segundos es más seguro
sleep(8) 

# PASO CLAVE: Asegurar el foco. 
# En lugar de una coordenada específica, damos un click genérico 
# en el centro de la pantalla para activar la ventana del navegador.
ancho, alto = pyautogui.size()
pyautogui.click(ancho / 2, alto / 2)

# Pequeña pausa tras el click para que el sistema reconozca el foco
sleep(1)

# ENVIAR: Usamos la combinación de teclas Ctrl + Enter
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

print(f"Correo enviado exitosamente a: {emails_concatenados}")