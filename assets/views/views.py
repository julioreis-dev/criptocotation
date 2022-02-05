# from django.shortcuts import render
# import multiprocessing as mp
# from gevent.pool import Pool
from django.views.generic import TemplateView
from assets.models.models_assets import Coincotationtable
import requests
import threading


def return_price(keyvaluetuplas):
    addressapi = f'https://api.coinpaprika.com/v1/price-converter?base_currency_id={keyvaluetuplas[1]}' \
                 f'&quote_currency_id=usd-us-dollars&amount=1'
    response = requests.get(addressapi).json()
    price_coin = round(response["price"], 2)
    coin = Coincotationtable(description=keyvaluetuplas[0], price=price_coin)
    coin.save()
    print(f'Executado {keyvaluetuplas[0]}')


def call_api():
    """Função que consome a API que fornece as cotações atuais das criptocoins."""
    coins = {'BTC': 'btc-bitcoin', 'LINK': 'link-chainlink', 'XRP': 'xrp-xrp', 'LTC': 'ltc-litecoin',
             'CHZ': 'chz-chiliz', 'ETH': 'eth-ethereum', 'DOGE': 'doge-dogecoin', 'ADA': 'ada-cardano'}
    threadslist = [threading.Thread(target=return_price, args=((coin, coins[coin]),)) for coin in coins]
    [thread.start() for thread in threadslist]
    [thread.join() for thread in threadslist]


class IndexTemplateView(TemplateView):
    template_name = 'home/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['info'] = salutation()
    #     return context


# def return_price(keyvaluetuplas):
#     addressapi = f'https://api.coinpaprika.com/v1/price-converter?base_currency_id={keyvaluetuplas[1]}' \
#                  f'&quote_currency_id=usd-us-dollars&amount=1'
#     response = requests.get(addressapi).json()
#     price_coin = round(response["price"], 2)
#     return Coincotationtable(description=keyvaluetuplas[0], price=price_coin)
#
#
# def call_api2():
#     """Função que consome a API que fornece as cotações atuais das criptocoins."""
#
#     coins = {'BTC': 'btc-bitcoin', 'LINK': 'link-chainlink', 'XRP': 'xrp-xrp', 'LTC': 'ltc-litecoin',
#              'CHZ': 'chz-chiliz', 'ETH': 'eth-ethereum', 'DOGE': 'doge-dogecoin', 'ADA': 'ada-cardano'}
#     pool = Pool(8)
#     coinameslist = [(coin, coins[coin]) for coin in coins]
#     coinsinstances = pool.map(return_price, coinameslist)
#     Coincotationtable.objects.bulk_create(coinsinstances)
#     print('Executado')
#
#
# def call_api1():
#     coins = {'BTC': 'btc-bitcoin', 'LINK': 'link-chainlink', 'XRP': 'xrp-xrp', 'LTC': 'ltc-litecoin',
#              'CHZ': 'chz-chiliz', 'ETH': 'eth-ethereum', 'DOGE': 'doge-dogecoin', 'ADA': 'ada-cardano'}
#     coinameslist = [(coin, coins[coin]) for coin in coins]
#     x = []
#     for cointuple in coinameslist:
#         x.append(return_price(cointuple))
#     Coincotationtable.objects.bulk_create(x)
#     print('Executado!!!')
