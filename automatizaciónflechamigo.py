import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Tus credenciales
mi_correo = "flechamigo@flecharoja.com.mx"
mi_password = "wfsqmjlttxspwzxa" # No es mi contraseña normal, sale de myaccount.google.com/apppasswords

# Leer Excel
df = pd.read_excel('control_datos_email.xlsx')
# Elimina las filas donde la columna 'Correo' esté vacía (los 'nan')
df = df.dropna(subset=['CORREO'])
nombre_imagen = "unnamed-10.png" # Asegúrate de que el nombre sea exacto

try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(mi_correo, mi_password)
    
    for index, fila in df.iterrows():
        destinatario = str(fila['CORREO']).strip()  # Eliminamos espacios en blanco al inicio y al final
        # Si por alguna razón el correo no tiene '@', se lo salta para no causar error
        if "@" not in destinatario:
            continue
        nombre = str(fila['NOMBRE COMPLETO'])
        folio = str(fila['FOLIO DE KIT'])
        
        # Si es uno solo, déjalo así: "tu_jefe@flecharoja.com.mx"
        # Si son varios, sepáralos por comas: "correo1@test.com, correo2@test.com"
        correos_ocultos = "omar.padilla@flecharoja.com.mx, jessica.perez@flecharoja.com.mx, efsoto@cemcomx.com, flechamigo@flecharoja.com.mx"
        #"omar.padilla@flecharoja.com.mx, jessica.perez@flecharoja.com.mx, efsoto@cemcomx.com, flechamigo@flecharoja.com.mx, eduardo.macedo@flecharoja.com.mx"
        # OJO: Usamos 'related' para que el correo entienda que lleva imágenes incrustadas
        msg = MIMEMultipart('related')
        msg['From'] = mi_correo
        msg['To'] = destinatario
        msg['Subject'] = f"Tu tarjeta Flechamigo quiere viajar contigo, {nombre}"
        
        
        # ⚠️ ¡OJO! QUITAMOS la línea que decía: msg['Bcc'] = correos_ocultos
        # Así el correo no lleva ningún rastro escrito de la copia oculta.
        # --- AQUÍ AGREGASTE LA LÍNEA PARA EL ENCABEZADO DE COPIA OCULTA ---
        #msg['Bcc'] = correos_ocultos
        
        # --- AHORA USAMOS HTML PARA EL DISEÑO ---
        cuerpo_html = f"""
        <html>
          <body style="font-family: Arial, sans-serif; color: #12724C;">
            <p>¡Hola, <strong>{nombre}</strong>!</p>
            <p>Todo gran recorrido comienza con un primer paso, y tú ya diste el tuyo al unirte a Flechamigo</p>
            <p>Tu folio de kit es: <strong>{folio}</strong></p>

            <p><strong>Comenzamos premiando tu confianza con un 5% de descuento, y gracias a la respuesta y entusiasmo de
            usuarios como tú, hoy ese beneficio ha crecido a un 10% de descuento en tus viajes.  Válido para dos
            viajes diarios a cualquier destino. Aplican Términos y Condiciones. Consultalos en:</p>
            <p><strong>https://flecharoja.com.mx/terminos_y_condiciones_2026.pdf</strong><br>
            <p>Queremos que formes parte de esta evolución y disfrutes de un programa pensado para reconocer tu preferencia, brindándote más beneficios y mejores experiencias en cada trayecto.</p>

            <br>¡No dejes pasar esta oportunidad! Tu registro está a un paso de completarse.<br>

            <br>Concluir tu registro es muy sencillo:<br>

            <br><strong>Visita nuestro módulo de atención.
            Menciona tu folio personalizado.
            Presenta tu identificación oficial (INE) para validar tus datos.
            En pocos minutos finalizamos tu registro y recibirás tu kit de bienvenida.</strong><br>

            <br>¿No sabes dónde se encuentra nuestro módulo o cuáles son nuestros horarios de atención?
            ¡Escríbenos y con gusto te ayudaremos!<br>

            <br><strong>Recuerda: tienes hasta el 31 de Agosto de 2026 para concluir tu registro y obtener tu kit de bienvenida.</strong><br>

            <br>Estamos listos para darte la bienvenida a la comunidad Flechamigo, donde cada viaje te acercará a más beneficios, experiencias y recompensas.<br>

            <br><strong>¡Completa tu registro y comienza a disfrutar de tu 10% de descuento hoy mismo!</strong><br>

            <br>"Acercándote cada vez más"<br>

            <br>Saludos cordiales,
            Equipo Flechamigo<br>
            
            
            <img src="cid:imagen_banner" alt="Banner Flechamigo" style="max-width: 100%; height: auto;">
            
            
            <p><strong>Si no sabes dónde nos encontramos o en qué horario atendemos, ¡escríbenos y te ayudamos!</strong></p>
            <p>¡Te esperamos pronto!<br>
            <em>'Acercándote cada vez más'</em><br>
            Saludos,</p>
          </body>
        </html>
        """
        
        # Pegamos el HTML al correo
        msg.attach(MIMEText(cuerpo_html, 'html'))
        
        
        # --- PREPARAMOS LA IMAGEN INCRUSTADA ---
        try:
            with open(nombre_imagen, 'rb') as archivo_img:
                imagen_adjunta = MIMEImage(archivo_img.read())
                # El 'Content-ID' debe coincidir con el 'cid:imagen_banner' que pusimos arriba en el HTML
                imagen_adjunta.add_header('Content-ID', '<imagen_banner>')
                imagen_adjunta.add_header('Content-Disposition', 'inline') # Le decimos que vaya incrustada
                msg.attach(imagen_adjunta)
        except FileNotFoundError:
            print(f"¡Ojo! No se encontró la imagen '{nombre_imagen}'.")
            
        # --- EL TRUCO PARA EL ENVÍO ---
        # Creamos una lista de todos los destinatarios reales (El cliente del Excel + los ocultos)
        # Usamos .split(',') por si pusiste más de un correo oculto separados por comas
        todos_los_destinatarios = [destinatario] + [c.strip() for c in correos_ocultos.split(',')]
        
        # Enviar
        servidor.sendmail(mi_correo, todos_los_destinatarios, msg.as_string())
        print(f"Enviado a: {destinatario}) (con copia oculta en secreto)")
        
    servidor.quit()
    print("¡Proceso finalizado con éxito!")

except Exception as e:
    print(f"Hubo un error al conectar o enviar: {e}")