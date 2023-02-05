from telegram.ext import *

print('starting')

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi, I'm a bot to calculate your total cost.")

# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'I\'m good!'

    return 'I don\'t understand'

# def handle_message(update, context):
#     # Get basic info of the incoming message
#     message_type = update.message.chat.type
#     text = str(update.message.text).lower()
#     response = ''
#
#     # Print a log for debugging
#     print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')
#
#     # React to group messages only if users mention the bot directly
#     if message_type == 'group':
#         # Replace with your bot username
#         if '@bot19292bot' in text:
#             new_text = text.replace('@bot19292bot', '').strip()
#             response = handle_response(new_text)
#     else:
#         response = handle_response(text)
#
#     # Reply normal if the message is in private
#     update.message.reply_text(response)
def calculate(update, context):
    no = update.message.text.split()[1]
    mt = float(update.message.text.split()[2])
    adv = int(update.message.text.split()[3])
    diesel = int(update.message.text.split()[4])

    tot = mt * 1600
    response = f"{no}\n{mt} * 1600 = {tot}\nAdvance: {adv}\nDiesel: {diesel}\nBal: {tot-adv-diesel}"
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

    tot = mt * 1575
    response = f"{no}\n{mt} * 1575 = {tot}\nAdvance: {adv}\nDiesel: {diesel}\nBal: {tot-adv-diesel}"
    context.bot.send_message(chat_id=update.message.chat_id, text=response)
def error(update, context):
    print(f'Update {update} caused error {context.error}')

token = '6042497392:AAEAAjU-hVvmsbCrhY-mnNm1IJU0RGvx9ns'

if __name__ == '__main__':
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler("calculate", calculate))

    # Messages
    # dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()