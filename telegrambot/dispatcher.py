import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from telegram.error import TelegramError

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ========================
# CONFIG
# ========================

ADMIN_LINK = "https://t.me/fabled20"
PARIPESA_LINK = "https://paripesa.bet/fabled20"

# ========================
# COUNTRY DATA
# ========================

COUNTRIES = {
    "algeria": ("🇩🇿 Algeria", "2,010 DZD"),
    "angola": ("🇦🇴 Angola", "13,800 AOA"),
    "botswana": ("🇧🇼 Botswana", "206 BWP"),
    "burundi": ("🇧🇮 Burundi", "44,260 BIF"),
    "cameroon": ("🇨🇲 Cameroon", "9,335 XAF"),
    "chad": ("🇹🇩 Chad", "9,335 XAF"),
    "gabon": ("🇬🇦 Gabon", "9,335 XAF"),
    "dr_congo": ("🇨🇩 DR Congo", "43,275 CDF"),
    "egypt": ("🇪🇬 Egypt", "757 EGP"),
    "ethiopia": ("🇪🇹 Ethiopia", "1,845 ETB"),
    "ghana": ("🇬🇭 Ghana", "227 GHS"),
    "kenya": ("🇰🇪 Kenya", "1,950 KES"),
    "madagascar": ("🇲🇬 Madagascar", "70,800 MGA"),
    "malawi": ("🇲🇼 Malawi", "26,050 MWK"),
    "mauritius": ("🇲🇺 Mauritius", "700 MUR"),
    "morocco": ("🇲🇦 Morocco", "151 MAD"),
    "mozambique": ("🇲🇿 Mozambique", "960 MZN"),
    "namibia": ("🇳🇦 Namibia", "275 NAD"),
    "nigeria": ("🇳🇬 Nigeria", "22,700 NGN"),
    "rwanda": ("🇷🇼 Rwanda", "20,850 RWF"),
    "south_africa": ("🇿🇦 South Africa", "275 ZAR"),
    "tanzania": ("🇹🇿 Tanzania", "39,375 TZS"),
    "tunisia": ("🇹🇳 Tunisia", "48 TND"),
    "uganda": ("🇺🇬 Uganda", "55,600 UGX"),
    "zambia": ("🇿🇲 Zambia", "415 ZMW"),
    "zimbabwe": ("🇿🇼 Zimbabwe", "5,430 ZWL"),

    "bangladesh": ("🇧🇩 Bangladesh", "1,800 BDT"),
    "cambodia": ("🇰🇭 Cambodia", "60,500 KHR"),
    "india": ("🇮🇳 India", "1,295 INR"),
    "indonesia": ("🇮🇩 Indonesia", "240,750 IDR"),
    "malaysia": ("🇲🇾 Malaysia", "66 MYR"),
    "nepal": ("🇳🇵 Nepal", "2,075 NPR"),
    "pakistan": ("🇵🇰 Pakistan", "4,180 PKR"),
    "philippines": ("🇵🇭 Philippines", "875 PHP"),
    "singapore": ("🇸🇬 Singapore", "20.25 SGD"),
    "sri_lanka": ("🇱🇰 Sri Lanka", "4,360 LKR"),
    "thailand": ("🇹🇭 Thailand", "515 THB"),
    "vietnam": ("🇻🇳 Vietnam", "382,000 VND"),
}

# ========================
# KEYBOARDS
# ========================

def start_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🎁 GET OVER 3.5", callback_data="get_over")]])

def country_keyboard():
    buttons, row = [], []
    for key, (name, _) in COUNTRIES.items():
        row.append(InlineKeyboardButton(name, callback_data=f"country_{key}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🌍 OTHER COUNTRIES", callback_data="country_other")])
    return InlineKeyboardMarkup(buttons)

def action_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 REGISTER HERE", url=PARIPESA_LINK)],
        [InlineKeyboardButton("📤 SEND SCREENSHOT", url=ADMIN_LINK)],
        [InlineKeyboardButton("🔙 BACK TO START", callback_data="back_start")]
    ])

# ========================
# HANDLERS
# ========================

# 1️⃣ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 Hey {username}!\n\n🎯 Ready to unlock FREE OVER 3.5 TICKETS?\n\nClick the button below to continue!",
        reply_markup=start_keyboard()
    )

# 2️⃣ GET OVER 3.5 button
async def get_over_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except TelegramError:
        pass  # ignore timeouts

    await query.message.reply_text(
        "Please select your country below 👇",
        reply_markup=country_keyboard()
    )

# 3️⃣ Country handler
async def country_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except TelegramError:
        pass  # ignore timeouts

    key = query.data.replace("country_", "")

    if key == "other":
        country = "OTHER COUNTRIES"
        rate = "$15"
    else:
        country, rate = COUNTRIES[key]

    message = (
        f"{country} USERS 🇺🇳\n\n"
        "🎯 FREE OVER 3.5 TICKETS\n\n"
        f"💱 Minimum Deposit: $15 ≈ {rate}\n\n"
        "📌 How to Join:\n"
        f"1️⃣ Register on [PARIPESA]({PARIPESA_LINK}) using the referral link below\n"
        f"2️⃣ Deposit a minimum of: {rate}\n\n"
        "3️⃣ Do NOT google the site\n"
        "4️⃣ Do NOT skip the referral link\n\n"
        f"📸 After deposit, send your screenshot to [Fabled20]({ADMIN_LINK}) for verification\n"
        "🔑 Promo Code: FABLED20"
    )

    await query.message.reply_text(message, reply_markup=action_keyboard(), parse_mode="Markdown")

# 4️⃣ Back handler
async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🔙 Back to start\n\nClick the button below to continue!",
        reply_markup=start_keyboard()
    )

async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except TelegramError:
        pass

    await query.message.reply_text(
        "🔙 Back to start\n\nClick the button below to continue!",
        reply_markup=start_keyboard()
    )

# ========================
# APP SETUP
# ========================

def setup_dispatcher():
    from django.conf import settings
    app = ApplicationBuilder()\
        .token(settings.BOT_TOKEN)\
        .connect_timeout(30)\
        .read_timeout(30)\
        .build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(get_over_handler, pattern="^get_over$"))
    app.add_handler(CallbackQueryHandler(back_handler, pattern="^back_start$"))
    app.add_handler(CallbackQueryHandler(country_handler, pattern="^country_"))

    return app