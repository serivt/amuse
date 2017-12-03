import binascii
import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def enviar_correo(plantilla, mails, asunto, info={}, mail='noreply@amuse.co'):
    plaintext = get_template('%s.txt' % plantilla)
    htmly = get_template('%s.html' % plantilla)
    text_content = plaintext.render(info)
    html_content = htmly.render(info)
    msg = EmailMultiAlternatives(asunto, text_content, mail, mails)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def generar_hash(longitud=None):
    """
    Retorna un cadena de caratecteres aleatoria de la longitud especificada. Si
    no se especifica la longitud sera de 16
    """
    longitud = 8 if longitud is None else longitud / 2
    return binascii.hexlify(os.urandom(int(longitud))).decode('utf-8')
