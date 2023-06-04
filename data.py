from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("● sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ●", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="● ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ ●", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("● ʙᴏᴛs sᴛᴀᴛᴜs ●", url="https://t.me/Bots_Hub_ll")],
        [
            InlineKeyboardButton("● ʜᴏᴡ ᴛᴏ ᴜsᴇ ●", callback_data="help"),
            InlineKeyboardButton("● ᴀʙᴏᴜᴛ ●", callback_data="about")
        ],
        [InlineKeyboardButton("● ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛs ●", url="https://t.me/Bots_Hub_ll")],
    ]

    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ

ʙʏ @Daisy_Support_chat
    """

    HELP = """
● **ᴄᴏᴍᴍᴀɴᴅs** ●

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**● ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ ●** 

Telegram Bot to generate Pyrogram and Telethon string session by @Daisy_Support_chat

● ᴏᴡɴᴇʀ ●: [Click Here](https://t.me/II_Ronny_II)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

● ᴅᴇᴠᴇʟᴏᴘᴇʀ ● : @II_Ronny_II
    """
