
from sistemas import CAMINHO_RESULTADO_JSON
import os
import pathlib
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Caminho arquivo HTML
#CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
def enviar_email_resultado():
    remetente = 'marcelotoller@datacempro.com.br'
    destinatario = 'marcelo.toller@yahoo.com.br'

    # Configurações SMTP
    smtp_server = 'email.datacempro.com.br'
    smtp_port = 587
    smtp_username = 'marcelotoller@datacempro.com.br'
    smtp_password = 'kj6378'

    # Mensagem de texto
    # with open(CAMINHO_RESULTADO_JSON, 'r') as arquivo:
    #     texto_arquivo = arquivo.read()
        
    # Transformar nossa mensagem em MIMEMultipart
    mime_multipart = MIMEMultipart()
    mime_multipart['from'] = remetente
    mime_multipart['to'] = destinatario
    mime_multipart['subject'] = 'resultado dos sistemas'


    #body = 'Conteúdo do e-mail'
    mime_multipart.attach(MIMEText('corpo do e-mail', 'plain'))

    # Anexo - Arquivo JSON    
    with open(CAMINHO_RESULTADO_JSON, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype='json')
        attachment.add_header('Content-Disposition', 'attachment', filename='resultado.json')
        mime_multipart.attach(attachment)    

    #corpo_email = MIMEText(texto_arquivo, 'json', 'utf-8')
    #mime_multipart.attach(corpo_email)

    # Envia o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        #server.ehlo()
        #server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multipart)
        print('E-mail enviado com  sucesso!')

#enviar_email_resultado()        