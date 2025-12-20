from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

PARIPESA_LINK = "https://paripesa.bet/fabled20"
ADMIN_LINK = "https://t.me/Fabled20"

# 1️⃣ START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.first_name

    keyboard = [
        [InlineKeyboardButton("🎁 GET OVER 3.5", callback_data="get_over")]
    ]

    if update.message:
        await update.message.reply_text(
            f"👋 Hey {username}!\n\n"
            "🎯 Ready to unlock FREE OVER 3.5 TICKETS?\n\n"
            "Click the button below to continue!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            f"👋 Hey {username}!\n\n"
            "🎯 Ready to unlock FREE OVER 3.5 TICKETS?\n\n"
            "Click the button below to continue!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# 2️⃣ COUNTRY SELECTION
async def choose_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🇪🇺 Europe", callback_data="europe")],
        [InlineKeyboardButton("🇺🇸 USA", callback_data="usa")],
        [InlineKeyboardButton("🇳🇬 Nigeria", callback_data="nigeria")],
        [InlineKeyboardButton("🇰🇪 Kenya", callback_data="kenya")],
        [InlineKeyboardButton("🇬🇧 UK", callback_data="uk")],
        [InlineKeyboardButton("🌍 Other Countries", callback_data="other")]
    ]

    await query.message.reply_text(
        "🌍 WHERE DO YOU COME FROM?\n\nSelect your region:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# 3️⃣ COUNTRY MESSAGE TEMPLATE
async def country_message(update: Update, country_name: str):
    query = update.callback_query
    await query.answer()

    text = (
        f"{country_name} WELCOME USERS! {country_name}\n\n"
        "You’re just one step away from joining our FREE OVER 3.5 TICKETS group 🎯\n\n"
        f"👤 Regional Admin: 👉 [fabled20]({ADMIN_LINK})\n"
        f"🔑 PROMO CODE: FABLED20\n\n"
        "📌 How to Join:\n"
        f"1️⃣ Register on [PARIPESA]({PARIPESA_LINK}) using the referral link\n"
        "2️⃣ Make a minimum deposit of $15\n"
        "3️⃣ ⚠️ IMPORTANT:\n"
        "    • Do NOT google the site\n"
        "    • Do NOT skip the referral link\n"
        f"4️⃣ After successful registration and deposit, send your screenshot to 👉 [fabled20]({ADMIN_LINK}) for verification\n\n"
        "📸 Final Step:\n"
        f"After completing registration and deposit, send your screenshot to 👉 [fabled20]({ADMIN_LINK}) for verification.\n\n"
        "⚠️ Note: You must use the referral link above to qualify for VIP access and FREE tickets."
    )

    keyboard = [
        [InlineKeyboardButton("🔗 REGISTER HERE", url=PARIPESA_LINK)],
        [InlineKeyboardButton("📤 SEND SCREENSHOT", url=ADMIN_LINK)],
        [InlineKeyboardButton("🔙 BACK TO START", callback_data="start")]
    ]

    await query.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
        disable_web_page_preview=False
    )

# 4️⃣ SPECIFIC COUNTRIES
async def europe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🇪🇺 EUROPEAN")

async def usa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🇺🇸 USA")

async def nigeria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🇳🇬 NIGERIAN")

async def kenya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🇰🇪 KENYAN")

async def uk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🇬🇧 UK")

async def other(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await country_message(update, "🌍 GLOBAL")
