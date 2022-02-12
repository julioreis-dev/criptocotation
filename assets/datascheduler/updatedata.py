from apscheduler.schedulers.background import BackgroundScheduler
from assets.views.views import call_api
from assets.querys.querys import Recommendation
from assets.models.models_assets import Assetstable, Coincotationtable


def start():
    scheduler = BackgroundScheduler(job_defaults={'max_instances': 2}, timezone='America/Sao_Paulo')
    scheduler.add_job(call_api, 'interval', seconds=190)
    scheduler.start()

    recommendation = Recommendation(Assetstable, Coincotationtable)
    scheduler1 = BackgroundScheduler(job_defaults={'max_instances': 2}, timezone='America/Sao_Paulo')
    scheduler1.add_job(recommendation.emailrecommendation, 'interval', seconds=60)
    scheduler1.start()
