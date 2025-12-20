import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Update
from telegram.ext import Dispatcher
from django.conf import settings
from .dispatcher import setup_dispatcher

bot = Bot(token=settings.BOT_TOKEN)

@csrf_exempt
def webhook(request):
    update = Update.de_json(json.loads(request.body), bot)

    dispatcher = Dispatcher(bot, None, workers=0)
    setup_dispatcher(dispatcher)

    dispatcher.process_update(update)
    return HttpResponse("OK")