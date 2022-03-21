import collections
from django.core.mail import send_mail, mail_admins
from datetime import datetime
from django.utils import timezone
from dataclasses import dataclass
import threading


@dataclass
class Recommendation:
    assetstable: object
    coincotationtable: object
    current_cotations_dict: dict = None

    def allclientes(self) -> collections.Iterable:
        return self.assetstable.objects.all()

    def lastcotations(self) -> dict:
        coins = ['BTC', 'LINK', 'XRP', 'LTC', 'CHZ', 'ETH', 'DOGE', 'ADA']
        return {coin: self.coincotationtable.objects.filter(description=coin).last().price for coin in coins}

    @staticmethod
    def analisetimer(client: object) -> tuple:
        verificationtime = abs(client.emaildate - datetime.now(timezone.utc))
        hr = verificationtime.seconds // 3600
        minut = verificationtime.seconds // 60
        return hr, minut

    def emailcontent(self, client: object, status: str) -> tuple:
        title = f'Recommendation to {status} the cripto {client.coin}'
        body = f'Dear {client.user_id.username},\nAccording your alert "{client.nameconfig}", ' \
               f'We recommend to {status} {client.coin} cripto:' \
               f'\nCurrent price: ${self.current_cotations_dict[client.coin]}' \
               f'\nAlert point: ${client.sell if status == "sell" else client.buy}'
        emailfrom = 'contato@firminostech.com'
        destination = [client.user_id.email]
        return title, body, emailfrom, destination

    def emailbody(self, client: object, status: str) -> None:
        hours, minutes = self.analisetimer(client)
        if hours != 0 or minutes >= client.timer - 1:
            try:
                title, msg, fromemail, listrecipient = self.emailcontent(client, status)
                send_mail(title, msg, fromemail, listrecipient, fail_silently=False,)
                client.emaildate = datetime.now(timezone.utc)
                client.save()
                print(f'Enviado: {datetime.now()}, {client.user_id.username} - {client.coin}')
            except Exception as e:
                mail_admins(
                    'Email não enviado',
                    f'Email referente ao {client.user_id.username} com o alerta "{client.nameconfig}" '
                    f'não foi encaminhado. Erro: {e}',
                    fail_silently=False,
                )

    def emailrecommendation(self) -> None:
        clientscripto = self.allclientes()
        self.current_cotations_dict = self.lastcotations()
        threads = []
        for client in clientscripto:
            if client.sell <= self.current_cotations_dict[client.coin]:
                threads.append(threading.Thread(target=self.emailbody, args=(client, 'sell')))
            elif client.buy >= self.current_cotations_dict[client.coin]:
                threads.append(threading.Thread(target=self.emailbody, args=(client, 'buy')))

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
