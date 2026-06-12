import os
import smtplib
from email.mime.text import MIMEText


def enviar_correo(destinatario, asunto, cuerpo):
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")

    if not gmail_user or not gmail_password:
        print("Error: Define GMAIL_USER y GMAIL_PASSWORD en tus variables de entorno")
        return

    msg = MIMEText(cuerpo, _charset="utf-8")
    msg["From"] = gmail_user
    msg["To"] = destinatario
    msg["Subject"] = asunto

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, [destinatario], msg.as_string())
        print("Correo enviado exitosamente")
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación: usa una contraseña de aplicación de Gmail")
    except Exception as ex:
        print("Error al enviar correo:", ex)


if __name__ == "__main__":
    destino = input("Destinatario: ").strip()
    asunto = input("Asunto: ").strip()
    cuerpo = input("Mensaje: ").strip()
    enviar_correo(destino, asunto, cuerpo)
