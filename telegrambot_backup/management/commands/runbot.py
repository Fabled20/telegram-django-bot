from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import ApplicationBuilder
from telegrambot.dispatcher import setup_dispatcher

class Command(BaseCommand):
    help = "Run the Telegram bot"

    def handle(self, *args, **options):
        # Build the bot application using the token from settings
        app = ApplicationBuilder().token(settings.BOT_TOKEN).build()

        # Setup all handlers from dispatcher
        app = setup_dispatcher()

        # Start the bot in polling mode
        print("Bot is running...")
        app.run_polling()
