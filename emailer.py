import smtplib
from email.message import EmailMessage
from importlib.resources import contents


def send_email(receiver):
    msg = EmailMessage()

    msg["Subject"] = 'Cellphones Relatory'
    msg['From'] = "emailsender080@gmail.com"
    msg['To'] = receiver
    password = "M1N3CR4FT"

    msg.set_content("Segue planilha com o relatório de todos os dados")
    archives = {"products.xlsx"}

    for archive in archives:
        with open(archive, 'rb') as arch:
            data = arch.read()
            archive_name = arch.name
        msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=archive_name)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.send_message(msg)

    print("\nEmail Enviado")
