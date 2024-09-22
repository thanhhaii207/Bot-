import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from telegram.error import TimedOut

# Cấu hình logging

# Key VIP cho phép truy cập tool VIP
vip_key = "DTHVIP"  # Thay bằng key thực tế

# Danh sách người dùng đã nhập đúng key VIP
vip_users = set()

# Liên kết các file tool miễn phí và tool VIP
tools_free = {
    'okx_rancer': '',
    'blum': 'https://drive.google.com/file/d/1rbTQDjsnkyyCzD-FC4JsYEZfWQ5SCz1q/view?usp=drivesdk',
    'babydoge': 'https://drive.google.com/file/d/16SDWS0bUEBbF4M-HwVDRug_4Nd-m3Nyy/view?usp=drivesdk',
    'seed': 'https://drive.google.com/file/d/1d4cmdaX-8eRJ4VdOa7kySM4xv2mlhjH0/view?usp=drivesdk',
    'memefi': 'https://drive.google.com/file/d/1yF6rJ47VW9Ba8dmAEP-UbS98TQff9BR_/view?usp=drivesdk',
    'freedog': 'https://drive.google.com/file/d/1N32tnPc8UqCJGQe-EpccoSzDXpvK_zQk/view?usp=drivesdk',
    'tsubasa': 'https://drive.google.com/file/d/1suhT8kKtuzCUe19xJoBi1-ccBua6vfoW/view?usp=drivesdk',
    'yescoin': 'https://drive.google.com/file/d/1Ciydquv2IrOEJ7tS_BvpTxuZGd8AhsWU/view?usp=drivesdk',
    'matchquets': 'https://drive.google.com/file/d/1VtMxrMnW-szoNlWw47eMSjmxIaPz4542/view?usp=drivesdk',
    'agent301': 'https://drive.google.com/file/d/1NnjxFBsuOG26hwGGBDQSa7KsYusrlb1a/view?usp=drivesdk',
    'midas': 'https://drive.google.com/file/d/11l-2tvy3zZtSY6oWS8mqfJdC8UJjctaK/view?usp=drivesdk',
    'wukong': 'https://drive.google.com/file/d/10xEiLQZkFqnTyh-Vx12ZmbInjVlXSDE8/view?usp=drivesdk',
    'tomarket': 'https://drive.google.com/file/d/1qh0W3AJXufOZC2YewrvKsKR_YHVcBH2q/view?usp=drivesdk',
    'bypass': ' https://drive.google.com/file/d/1h4sxTlV0wpEWtjNtmwj_BlQOR1dQr9to/view?usp=drivesdk ',
    'videohuongdan':'https://youtube.com/@dthtoolairdrop?si=LlmZGArLO3A7GO3c',
    'setup_nodejs': '...',
    'setup_python': '...'
}

tools_vip = {
    'moobix': 'https://drive.google.com/file/d/1JIQwgkZckGt0QMCOSpq0d0wdlVPDugFE/view?usp=drivesdk',
    'xkucoin_ech': 'https://drive.google.com/file/d/1ZhF8BbrUVQ16BPlpYlms4WjFxjlfW6fx/view?usp=drivesdk'
}

# Lệnh /start để chào mừng người dùng và hiển thị danh sách tool
async def start(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.first_name
    message = f"Chào mừng {user_name} đến với bot!\nDưới đây là danh sách các tool :\n\n"

    # Thêm các tool miễn phí vào danh sách
    message += "🎁 **Tool Miễn Phí**:\n"
    for tool_name in tools_free.keys():
        message += f"/{tool_name} - Tải {tool_name.capitalize()} tại đây\n"

    # Kiểm tra nếu người dùng đã nhập đúng key VIP
    if str(update.message.from_user.id) in vip_users:
        message += "\n🔒 **Tool VIP**:\n"
        for tool_name in tools_vip.keys():
            message += f"/{tool_name} - Tải {tool_name.capitalize()} tại đây\n"
    else:
        message += "\n🔒 **Tool VIP**:\n Bạn cần nhập key VIP để truy cập tool này.\nLink lay Key : htpps://...\nNhap /enter_key (key đã lấy) "

    await update.message.reply_text(message)

# Lệnh nhập key VIP
async def enter_key(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if context.args:
        key = context.args[0]
        if key == vip_key:
            vip_users.add(user_id)
            with open("keybotvip.txt", "a") as file:
                file.write(f"{user_id}\n")
            await update.message.reply_text("Bạn đã được cấp quyền truy cập VIP thành công! Vui lòng dùng lệnh /start để xem danh sách tool VIP.")
        else:
            await update.message.reply_text("Key không hợp lệ. Vui lòng thử lại.")
    else:
        await update.message.reply_text("Vui lòng nhập key VIP sau lệnh /enter_key.")

# Các lệnh gửi link tool miễn phí
async def okx_rancer(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool OKX Rancer tại đây: {tools_free['okx_rancer']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def setup_python(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"setup python\n\nLệnh 1\n\ntermux-setup-storage && apt update && apt upgrade && pkg install php && pkg install python && pkg install git && pkg install wget && pip install --upgrade pip &&pip install requests && pip install pycurl \n\nLệnh 2\n\npip install requests\n\nLệnh 3\n\npip install bs4\n\ncách out tool : CTR + C {tools_free['setup_python']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def setup_nodejs(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"lệnh 1. pkg update\nlệnh 2. pkg install nodejs\nlệnh 3. termux-setup-storage {tools_free['setup_nodejs']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")


async def blum(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Blum tại đây: {tools_free['blum']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def wukong(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Wukong tại đây: {tools_free['wukong']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def tomarket(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Tomarket tại đây: {tools_free['tomarket']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def agent301(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Agent301 tại đây: {tools_free['agent301']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def freedog(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Freedog tại đây: {tools_free['freedog']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def midas(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Midas tại đây: {tools_free['midas']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def seed(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Seed tại đây: {tools_free['seed']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def memefi(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Memefi tại đây: {tools_free['memefi']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def bypass(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải bypass tại đây: {tools_free['bypass']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")
        
async def videohuongdan(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"LINK KÊNH HD : {tools_free['videohuongdan']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def babydoge(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Babydoge tại đây: {tools_free['babydoge']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def tsubasa(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Tsubasa tại đây: {tools_free['tsubasa']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")
async def yescoin(update: Update, context: CallbackContext) -> None:
    try:
        await update.message.reply_text(f"Bạn có thể tải Tool yescoin tại đây: {tools_free['yescoin']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")


# Lệnh gửi link tool VIP (chỉ cho người dùng VIP)
async def moobix(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if user_id not in vip_users:
        await update.message.reply_text("Bạn không có quyền truy cập Tool VIP. Vui lòng nhập key VIP.")
        return

    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Moobix (VIP) tại đây: {tools_vip['moobix']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

async def xkucoin_ech(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if user_id not in vip_users:
        await update.message.reply_text("Bạn không có quyền truy cập Tool VIP. Vui lòng nhập key VIP.")
        return

    try:
        await update.message.reply_text(f"Bạn có thể tải Tool Xkucoin Ech (VIP) tại đây: {tools_vip['xkucoin_ech']}")
    except TimedOut:
        await update.message.reply_text("Yêu cầu bị timeout. Vui lòng thử lại.")

# Khởi tạo bot
app = ApplicationBuilder().token("7508981785:AAGOpoH_qcSgBD5l14YeR0mzUfkwgRTPktA")\
    .read_timeout(20)\
    .write_timeout(20)\
    .build()

# Thêm lệnh /start để chào mừng và hiển thị danh sách tool
app.add_handler(CommandHandler('start', start))

# Thêm lệnh nhập key VIP
app.add_handler(CommandHandler('enter_key', enter_key))

# Thêm các lệnh gửi link tool tương ứng
app.add_handler(CommandHandler
('yescoin',yescoin))
app.add_handler(CommandHandler('okx_rancer', okx_rancer))
app.add_handler(CommandHandler('blum', blum))
app.add_handler(CommandHandler('babydoge', babydoge))
app.add_handler(CommandHandler('memefi', memefi))
app.add_handler(CommandHandler('agent301', agent301))
app.add_handler(CommandHandler('tsubasa', tsubasa))
app.add_handler(CommandHandler('wukong', wukong))
app.add_handler(CommandHandler('seed', seed))
app.add_handler(CommandHandler('midas', midas))
app.add_handler(CommandHandler('bypass', bypass))
app.add_handler(CommandHandler('videohuongdan', videohuongdan))
app.add_handler(CommandHandler
('setup_python', setup_python))
app.add_handler(CommandHandler
('setup_nodejs', setup_nodejs))
app.add_handler(CommandHandler('freedog', freedog))
app.add_handler(CommandHandler('tomarket', tomarket))
app.add_handler(CommandHandler('xkucoin_ech', xkucoin_ech))
app.add_handler(CommandHandler('moobix', moobix))  # Tool VIP

# Chạy bot
app.run_polling()