import re

import emailer
from webscrapper import WebScrapping

regex_email = "[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"

while True:
    receiver = input(str("Informe o email que deseja receber o relatório: "))
    is_email = re.findall(regex_email, receiver)
    if not is_email:
        print("Email Inválido\n Exemplo: [teste@exemplo.com]")
    else:
        break

obj = WebScrapping()
obj.Init()
emailer.send_email(receiver)
