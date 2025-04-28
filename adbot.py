import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "7854708883:AAFq2zJoDvDsSibYjqvfoBLKERj6RScfgEI"
CHANNEL_LINK = "https://t.me/anderdogskrttt"
FILE_PATH = r"C:\Users\makso\Desktop\DRUMKITADS2025\!AD$ STASH2025.zip"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Да", callback_data='confirm1')],
        [InlineKeyboardButton("Перейти на канал", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Ты готов получить драмкит? Сначала подпишись на канал.", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'confirm1':
        keyboard = [
            [InlineKeyboardButton("Да", callback_data='confirm2')],
            [InlineKeyboardButton("Нет", callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Ты точно подписался? Проверь ещё раз.", reply_markup=reply_markup)

    elif query.data == 'confirm2':
        keyboard = [
            [InlineKeyboardButton("Да", callback_data='confirm3')],
            [InlineKeyboardButton("Нет", callback_data='cancel')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Подписка оформлена? Готов получить драмкит?", reply_markup=reply_markup)

    elif query.data == 'confirm3':
        if os.path.exists(FILE_PATH):
            await query.edit_message_text("Отлично! Вот твой драмкит.")
            await context.bot.send_document(chat_id=query.message.chat.id, document=open(FILE_PATH, 'rb'))
        else:
            await query.edit_message_text("Файл не найден. Обратитесь к администратору.")

    elif query.data == 'cancel':
        await query.edit_message_text("Жду тебя. Как будешь готов — напиши снова!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == '__main__':
    main()
