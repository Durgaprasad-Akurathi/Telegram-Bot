from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '5894043541:AAGiL8GqvYuwH1-S0rArS62dMMhK2Y0Dc5k'
BOT_USERNAME: Final = '@GeneralStoreMarketingBot'


#------------------------------------------------------------------COMMANDS-----------------------------------------------------------------------------#

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Greetings of day! Its pleasure to have you in ADP General Store  Bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please tell me how can I help you!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I will make your work easier')


#------------------------------------------------------------------RESPONSE-----------------------------------------------------------------------------#

if __name__ == '__main__':

    app=Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('start', custom_command))


