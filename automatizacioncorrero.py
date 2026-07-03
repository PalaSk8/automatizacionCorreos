import pyautogui
import webbrowser
import pyperclip
from time import sleep

destinatario = "omar.padilla@flecharoja.com.mx"
asunto = "Tu tarjeta Flechamigo quiere viajar contigo"
cuerpo = "¡Hola, FLECHAMIGO!Esperamos que estés teniendo un excelente día. Te escribimos porque notamos que te falta un pequeño paso para completar tu registro. ¡Es más fácil de lo que crees!¿Qué sigue?Date una vuelta por nuestro módulo de atención(TOLUCA Y CDMX PONIENTE).  Menciona tu folio personalizado  FA00279 a nuestra ejecutiva de atención.Muestra tu identificación (INE) a nuestras ejecutivas de atención para corroborar tus datos. Completamos tu registro en tan solo unos minutos.  Si no sabes dónde nos encontramos o en qué horario atendemos, ¡escríbenos y te ayudamos!  ¡Te esperamos pronto! 'Acercándote cada vez más' Saludos,"

#establecer pausa entre comandos de pyautogui
pyautogui.PAUSE = 5



#abriur el navegador con la URL de Gmail para redactar un nuevo correo
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
sleep(5)  # Esperar a que Gmail se cargue completamente



# Hacer clic para asegurarse de que la ventana de Gmail esté activa
pyautogui.click(x=178, y=325)




# Copiar el destinatario al portapapeles y pegarlo en el campo "Para"
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')  # Pegar el destinatario
pyautogui.hotkey('tab')  # Mover al campo "Asunto"
# Copiar el asunto al portapapeles y pegarlo en el campo "Asunto"
pyperclip.copy(asunto)
pyautogui.hotkey('ctrl', 'v')  # Pegar el asunto
pyautogui.hotkey('tab')  # Mover al campo del cuerpo del mensaje
# Copiar el cuerpo del mensaje al portapapeles y pegarlo en el campo del cuerpo del mensaje
pyperclip.copy(cuerpo)
pyautogui.hotkey('ctrl', 'v')  # Pegar el cuerpo del mensaje





#click botón de enviar
# Coordenadas del botón de enviar (pueden variar según la resolución de pantalla y la interfaz de Gmail)
pyautogui.click(x=1013, y=1122)  # Ajusta estas coordenadas según tu pantalla
print("Gmail abierto con los datos precargados.")