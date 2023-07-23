import pandas as pd
from datetime import datetime
from pytz import timezone
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import os 
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ALLOWED_ID = "Your_TG_ID"

# Define different states for conversation
(PRODUCT, PRICE, HASH, BUYER, NOTE) = range(5)

# DataFrame to store the data
df = pd.DataFrame(columns=['ID', 'Product Name', 'Price', 'hash', 'Buyer Username/email', 'Note', 'Date Time'])

def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id

    # Only allowed user can type data
    if user_id != ALLOWED_ID:
        update.message.reply_text('Sorry, you do not have access to this bot.')
        return ConversationHandler.END

    update.message.reply_text('Please enter the product name:')
    return PRODUCT

def product(update: Update, context: CallbackContext) -> int:
    context.user_data['product'] = update.message.text
    update.message.reply_text('Please enter the price:')
    return PRICE

def price(update: Update, context: CallbackContext) -> int:
    context.user_data['price'] = update.message.text
    update.message.reply_text('Please enter the hash:')
    return HASH

def hash(update: Update, context: CallbackContext) -> int:
    context.user_data['hash'] = update.message.text
    update.message.reply_text('Please enter the buyer username/email:')
    return BUYER

def buyer(update: Update, context: CallbackContext) -> int:
    context.user_data['buyer'] = update.message.text
    update.message.reply_text('Please enter the note:')
    return NOTE

def note(update: Update, context: CallbackContext) -> int:
    context.user_data['note'] = update.message.text

    # Get current Indian time
    now = datetime.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    
    global df
    new_row = pd.Series({
    'ID': len(df) + 1,
    'Product Name': context.user_data['product'],
    'Price': context.user_data['price'],
    'hash': context.user_data['hash'],
    'Buyer Username/email': context.user_data['buyer'],
    'Note': context.user_data['note'],
    'Date Time': now
}, name='x')  # 'x' here is a placeholder index; it will be ignored

    df = pd.concat([df, pd.DataFrame(new_row).T], ignore_index=True)


    # Write data to Excel
    df.to_excel('data.xlsx', index=False)

    update.message.reply_text('Information saved.')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END

def main() -> None:

    updater = Updater(token=BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PRODUCT: [MessageHandler(Filters.text & ~Filters.command, product)],
            PRICE: [MessageHandler(Filters.text & ~Filters.command, price)],
            HASH: [MessageHandler(Filters.text & ~Filters.command, hash)],
            BUYER: [MessageHandler(Filters.text & ~Filters.command, buyer)],
            NOTE: [MessageHandler(Filters.text & ~Filters.command, note)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
