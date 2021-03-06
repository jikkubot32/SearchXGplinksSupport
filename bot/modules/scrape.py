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
       sendMessage('<b>âï¸ Send a Gplinks Url Along With Comment! ð</b>', context.bot, update)
       return
 
    if not query.startswith("https://gplinks") or query.startswith("gplinks"):
       sendMessage('<b>ð Sorry Dude, Please Give Me Gplinks Urls ð¤</b>', context.bot, update)
       return

    m = sendMessage('<b>ð Please Wait Scraping Your Gplinks.... ð</b>', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("Something went wrong\nTry again later..", context.bot, update)
    else:
       sendMessage(f"<b><i>ð Yá´á´Ê LÉªÉ´á´ Sá´Êá´á´á´á´ ð</i></b>\n\n<b>ð¤ Yá´á´Ê LÉªÉ´á´ :</b> <code>/clone@MMCloneBot {link}</code>\n\n<b>ð¬ Oá´¡É´á´Êá´ BÊ : #WhitE_DeviL09</b>", context.bot, update)


gplink_handler = CommandHandler("scrape", scrape_gp,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
