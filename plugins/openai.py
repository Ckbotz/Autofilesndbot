import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

class TelegramBot:
    def __init__(self, token, api_key):
        self.token = BOT_TOKEN 
        self.api_key = "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"
        self.bot = None
        self.engine_id = 'GPT-3.5'  # Replace with your GPT-3.5 engine ID

    def initialize_openai(self):
        openai.api_key = self.api_key

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a chatbot. How can I help you?")

    def handle_message(self, update, context):
        message = update.message.text
        response = self.get_response(message)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def get_response(self, message):
        response = openai.Completion.create(
            engine=self.engine_id,
            prompt=message,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=15
        )
        return response.choices[0].text.strip()

    def run(self):
        self.initialize_openai()
        self.bot = telegram.Bot(token=self.token)
        updater = Updater(bot=self.bot, use_context=True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', self.start)
        message_handler = MessageHandler(Filters.text & ~Filters.command, self.handle_message)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(message_handler)
        updater.start_polling()
        updater.idle()

# Replace 'your_bot_token' with the token obtained from BotFather
# Replace 'your_api_key' with your OpenAI API key
bot = TelegramBot(token='your_bot_token', api_key='your_api_key')
bot.run()
