
from bot.config import Messages as tr
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import shutil
from os import execl
from time import sleep
from sys import executable
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, RPCError
from bot.config import Config
from bot import LOGGER


@Client.on_message(
     filters.private 
     & filters.incoming 
     & filters.command('log') 
     & filters.user(Config.AUTH_USERS), group=2
)

def _send_log(client, message):
  with open('log.txt', 'rb') as f:
    try:
      client.send_document(
        message.chat.id,
        document=f,
        file_name=f.name,
        reply_to_message_id=message.message_id
        )
      LOGGER.info(f'Log file sent to {message.from_user.id}')
    except FloodWait as e:
      sleep(e.x)
    except RPCError as e:
      message.reply_text(e, quote=True)

@Client.on_message(filters.private & filters.incoming & filters.command(['restart']) & filters.user(Config.SUDO_USERS), group=2)
def _restart(client, message):
  shutil.rmtree(Config.DOWNLOAD_DIRECTORY)
  LOGGER.info('Deleted Config.DOWNLOAD_DIRECTORY successfully.')
  message.reply_text('**♻️Restarted Successfully !**', quote=True)
  LOGGER.info(f'{message.from_user.id}: Restarting...')
  execl(executable, executable, "-m", "bot")


@Client.on_message(filters.private & filters.incoming & filters.command(['start']), group=2)
def _start(client, message):
    client.send_message(chat_id = message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("How To Use Me 🤔", f"help+1")
                ],
                [
                    InlineKeyboardButton("Update Channel", url="https://t.me/HxBots"),
                    InlineKeyboardButton("Support Group", url="https://t.me/HxSupport")
                ],
                [
                   InlineKeyboardButton("By Me A Coffee", url="https://pay2me.vercel.app/kkirodewal@okaxis")
                ]
            ]
        )
     )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']), group=2)
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(c, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    c.edit_message_text(chat_id = chat_id,    message_id = message_id,
        text = tr.HELP_MSG[msg],    reply_markup = InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '-->', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):

        button = [
            [InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")],
            [InlineKeyboardButton(text = '-->', callback_data = f"help+{pos+1}")]

        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")
                
            ]
        ]
    return button

@Client.on_message(filters.private & filters.incoming & filters.command(['update']), group=2)
def _update(client, message):
    client.send_message(chat_id = message.chat.id,
        text=tr.UPDATE_MSG.format(message.from_user.first_name),
        disable_web_page_preview=True
     )
