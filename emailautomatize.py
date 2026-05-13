import pyautogui
import webbrowser
import urllib.parse
from time import sleep

email = [
    "analista.ia@cemcomx.com",
    "eduardo.macedo@flecharoja.com.mx"
    ]

emailConcatenados = ",".join(email)
subject = "prueba"
body = "Hola, este es un correo de prueba enviado desde Python utilizando el módulo webbrowser. ¡Espero que funcione correctamente!"

# Codificar los parámetros para que sean seguros en una URL
subject_encoded = urllib.parse.quote(subject)
body_encoded = urllib.parse.quote(body)

# La URL correcta para Gmail Web es 'https://mail.google.com/mail/?view=cm&fs=1'
# Parámetros: 
# to -> Destinatario
# su -> Asunto (Subject)
# body -> Cuerpo del mensaje
url = f"https://mail.google.com/mail/?view=cm&fs=1&to={emailConcatenados}&su={subject_encoded}&body={body_encoded}"

# Abrir el navegador
webbrowser.open(url)
sleep_time = 5  # Tiempo para esperar a que Gmail se cargue completamente
pyautogui.sleep(5)  # Esperar a que Gmail se cargue completamente

pyautogui.click(x=245, y=1072)# Hacer clic para asegurarse de que la ventana de Gmail esté activa

#click botón de enviar


print("Gmail abierto con los datos precargados.")