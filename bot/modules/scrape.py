from telegram.ext import CommandHandler
from bot import AUTHORIZED_CHATS, dispatcher
from bot.helper.ext_utils.bot_utils import new_thread
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage
from bot.helper.ext_utils.parser import get_gp_link

@new_thread
def scrape_gp(update, context):
    try:
       query = update.message.text.split()[1]
    except:
       sendMessage('<b>✉️ Send a Gplinks Url Along With Comment! 👀</b>', context.bot, update)
       return
 
    if not query.startswith("https://gplinks") or query.startswith("gplinks"):
       sendMessage('<b>🔗 Sorry Dude, Please Give Me Gplinks Urls 🤒</b>', context.bot, update)
       return

    m = sendMessage('<b>🔄 Please Wait Scraping Your Gplinks.... 😎</b>', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("Something went wrong\nTry again later..", context.bot, update)
    else:
       sendMessage(f"<b>⚙️ Here is Your Link 👇</b>\n\n<code>/clone@MMCloneBot {link}</code>\n\n<b>📬 Ownerd By : #WhitE_DeviL09</b>", context.bot, update)


gplink_handler = CommandHandler("scrape", scrape_gp,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
