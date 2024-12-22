import json
from .func import *
from pyrogram import Client, filters

# Define a modern UI message for no permission
NO_PERMISSION_MESSAGE = """<b>
You don't have permission to use this command.
Contact the bot owner @FNxELECTRA!
</b>"""

# Define a success message header
REDEEM_GENERATED_HEADER = """<b>Redeem Generated ✅</b>\n"""

# Define a command to generate redeem codes
@Client.on_message(filters.command("gc", [".", "/"]))
async def generate_redeem_codes(client, message):
    try:
        user_id = str(message.from_user.id)
        with open("FILES/config.json", "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
        
        owner_ids = config.get("OWNER_ID", [])

        if user_id not in owner_ids:
            await message.reply_text(NO_PERMISSION_MESSAGE, message.id)
            return

        try:
            amount = int(message.text.split(" ")[1])
        except (IndexError, ValueError):
            amount = 10

        response_text = REDEEM_GENERATED_HEADER

        for _ in range(amount):
            redeem_code = f"GRAND-{gcgenfunc()}{gcgenfunc()}{gcgenfunc()}-PAA"
            await insert_pm(redeem_code)
            response_text += f"➔ <code>{redeem_code}</code>\n"

        response_text += """<b>\nYou can redeem this code using this command: /redeem FN-XXXX-CHECKER</b>"""
        
        await message.reply_text(response_text, message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())

