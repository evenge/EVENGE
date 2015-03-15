import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("**** Enviar email con Gmail ****")
user = input("Cuenta de gmail: ")
password = getpass.getpass("Password: ")

#Para las cabeceras del email
remitente = input("From, ejemplo: administrador <admin@gmail.com>: ")
destinatario = input("To, ejemplo: amigo <amigo@mail.com>: ")
asunto = input("Subject, Asunto del mensaje: ")
mensaje = input("Mensaje HTML: ")

#Host y puerto SMTP de Gmail
gmail = smtplib.SMTP('smtp.gmail.com', 587)

#protocolo de cifrado de datos utilizado por gmail
gmail.starttls()

#Credenciales
gmail.login(user, password)

#muestra la depuración de la operacion de envío 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html') #Content-type:text/html
header.attach(mensaje)

#Enviar email
gmail.sendmail(remitente, destinatario, header.as_string())

#Cerrar la conexión SMTP
gmail.quit()
