import time
import pyautogui
# Esperar 5 segundos para que el usuario pueda colocar el cursor en la posición deseada
print("Coloca el cursor en la posición deseada en los próximos 5 segundos...")
time.sleep(5)
# Obtener las coordenadas actuales del cursor
print("Coordenadas del cursor:", pyautogui.position())