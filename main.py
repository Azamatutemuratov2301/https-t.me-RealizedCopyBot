from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

BOT_TOKEN = "8158588417:AAEVoM7CdKJztk_eJHrHvipbUkRXYfHKowA"

# /start komandasi
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"Assalomu alaykum, {user.first_name}!\n\n"
        "Bu Realized_Profit trading botidir.\n"
        "Siz bu yerda quyidagi xizmatlardan foydalanishingiz mumkin:\n"
        "- Signal olish\n"
        "- Avtomatik copy trading\n"
        "- VIP bo‘lim\n"
        "- Statistika va hisobotlar\n"
        "- Obuna tizimi\n\n"
        "Bot yaratuvchisi: Azamat Utemuratov"
    )
    await update.message.reply_text(text)

# Asosiy ishga tushirish qismi
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    print("Bot ishga tushdi...")
    app.run_polling()
