from django.core.mail import send_mail, mail_admins
from datetime import datetime
from django.utils import timezone
from dataclasses import dataclass
import threading


@dataclass
class Recommendation:
    assetstable: object
    coincotationtable: object

    def allclientes(self):
        return self.assetstable.objects.all()

    def lastcotations(self):
        coins = ['BTC', 'LINK', 'XRP', 'LTC', 'CHZ', 'ETH', 'DOGE', 'ADA']
        return {coin: self.coincotationtable.objects.filter(description=coin).last().price for coin in coins}

    def analisetimer(self, client):
        verificationtime = abs(client.emaildate - datetime.now(timezone.utc))
        hr = verificationtime.seconds // 3600
        minut = verificationtime.seconds // 60
        return hr, minut

    def emailbody(self, client, cotations_dict, status):
        hours, minutes = self.analisetimer(client)
        if hours != 0 or minutes >= client.timer:
            # implantar try aqui
            try:
                send_mail(
                    f'Recommendation to {status} the cripto {client.coin}',
                    f'Dear {client.user_id.username},\nAccording your alert "{client.nameconfig}", '
                    f'We recommend to {status} {client.coin} cripto:\nCurrent price: ${cotations_dict[client.coin]}'
                    f'\nAlert point: ${client.sell if status == "sell" else client.buy}',
                    'jrfirmino01@gmail.com',
                    [client.user_id.email],
                    fail_silently=False,
                )
                client.emaildate = datetime.now(timezone.utc)
                # client.emaildate = timezone.now()
                client.save()
            except:
                mail_admins(
                    'Email não enviado',
                    f'Email referente ao {client.user_id.username} com o alerta {client.nameconfig} '
                    f'não foi encaminhado.',
                    fail_silently=False,
                )

    def emailrecommendation(self):
        clientscripto = self.allclientes()
        current_cotations_dict = self.lastcotations()
        threadinstances = None
        threads = []
        for client in clientscripto:
            if client.sell <= current_cotations_dict[client.coin]:
                threadinstances = self.emailbody(client, current_cotations_dict, 'sell')
            elif client.buy >= current_cotations_dict[client.coin]:
                threadinstances = self.emailbody(client, current_cotations_dict, 'buy')
            threads.append(threading.Thread(target=threadinstances, args=()))

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
