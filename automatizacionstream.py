import webbrowser
import pyautogui
from time import sleep



# 3. Construcción de URL
url = f"https://lirio-v03.streamlit.app/"

# 4. Automatización
webbrowser.open(url)

# Esperamos a que el navegador abra y cargue la página
# Gmail es pesado, así que 6-8 segundos es más seguro
sleep(8) 

# PASO CLAVE: Asegurar el foco. 
# En lugar de una coordenada específica, damos un click genérico 
# en el centro de la pantalla para activar la ventana del navegador.
ancho, alto = pyautogui.size()
pyautogui.click(x=425, y=256)

# Pequeña pausa tras el click para que el sistema reconozca el foco
sleep(1)

# ENVIAR: Usamos la combinación de teclas Ctrl + Enter
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

print(f"ejecutar limpieza")