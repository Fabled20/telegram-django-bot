from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

PARIPESA_LINK = "https://paripesa.bet/fabled20"
ADMIN_LINK = "https://t.me/Fabled20"

# 1️⃣ Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.first_name

    keyboard = [
        [InlineKeyboardButton("🎁 GET OVER 3.5", callback_data="get_over")]
    ]

    await update.message.reply_text(
        f"👋 Hey {username}!\n\n"
        "🎯 Ready to unlock FREE OVER 3.5 TICKETS?\n\n"
        "Click the button below to continue!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# 2️⃣ Country selection
async def choose_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🇪🇺 Europe", callback_data="europe")],
        [InlineKeyboardButton("🇺🇸 USA", callback_data="usa")],
        [InlineKeyboardButton("🇨🇦 Canada", callback_data="canada")],
        [InlineKeyboardButton("🇦🇺 Australia", callback_data="australia")],
        [InlineKeyboardButton("🇹🇷 Turkey", callback_data="turkey")],
        [InlineKeyboardButton("🇮🇳 India", callback_data="india")],
        [InlineKeyboardButton("🇬🇧 UK", callback_data="uk")],
        [InlineKeyboardButton("🇳🇬 Nigeria", callback_data="nigeria")],
        [InlineKeyboardButton("🇰🇪 Kenya", callback_data="kenya")],
        [InlineKeyboardButton("🇬🇭 Ghana", callback_data="ghana")],
        [InlineKeyboardButton("🌍 Other Countries", callback_data="other")]
    ]

    await query.message.reply_text(
        "🌍 WHERE DO YOU COME FROM?\n\nSelect your region:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# 3️⃣ Country-specific messages
async def nigeria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(
        update,
        "🇳🇬 WELCOME, NIGERIAN USERS! 🇳🇬\n\n"
        "You’re just one step away from joining our FREE OVER 3.5 TICKETS group 🎯\n\n"
        f"👤 Regional Admin: 👉 [fabled20]({ADMIN_LINK})\n"
        f"🔑 PROMO CODE: FABLED20\n\n"
        "📌 How to Join:\n"
        "1️⃣ Register on PARIPESA using the referral link below\n"
        "2️⃣ Make a minimum deposit of $15\n"
        "3️⃣ ⚠️ IMPORTANT:\n"
        "    • Do NOT google the site\n"
        "    • Do NOT skip the referral link\n"
        "4️⃣ After successful registration and deposit, send your screenshot to\n"
        f"👉 [fabled20]({ADMIN_LINK}) for verification\n\n"
        "📸 Final Step:\n"
        "After completing your registration and deposit, send your screenshot to\n"
        f"👉 [fabled20]({ADMIN_LINK}) for verification.\n\n"
        "⚠️ Note: You must use the referral link provided above to qualify for VIP access and FREE tickets."
    )

async def usa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(
        update,
        "🇺🇸 WELCOME, USA USERS! 🇺🇸\n\n"
        "Follow the same steps to join FREE OVER 3.5 TICKETS group 🎯\n"
        f"👤 Admin: 👉 [fabled20]({ADMIN_LINK})\n"
        f"🔑 PROMO CODE: FABLED20\n"
        f"🔗 Register: {PARIPESA_LINK}\n"
        f"📤 Send screenshot: {ADMIN_LINK}"
    )

# Repeat for other countries (copy the template above for Canada, UK, India, etc.)
async def other(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🌍 WELCOME! Follow the instructions to join FREE OVER 3.5 TICKETS.")

# Utility function to send country message with buttons
async def country_message(update: Update, text: str):
    keyboard = [
        [InlineKeyboardButton("🔗 REGISTER HERE", url=PARIPESA_LINK)],
        [InlineKeyboardButton("📤 SEND SCREENSHOT", url=ADMIN_LINK)],
        [InlineKeyboardButton("🔙 BACK TO START", callback_data="start")]
    ]

    await update.callback_query.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
