import httpx
import asyncio
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
import openai

openai_api_key = "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"

openai_client = openai.OpenAI(api_key=openai_api_key)


async def fetch_response(prompt):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()  # Raise an exception if response status is not 2xx
        completion = response.json()
        if 'choices' not in completion or len(completion['choices']) == 0 or 'message' not in completion['choices'][0]:
            raise ValueError("Failed to generate response")
        return completion["choices"][0]["message"]["content"]


@Client.on_message(filters.command("gpt", [".", "/"]))
async def cmd_gpt(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if checkall[0] == False:
            return

        role = checkall[1]




    # try:
    #     user_id  = str(message.from_user.id)
    #     checkall = await check_all_thing(Client , message)
    #     if checkall[0] == False:
    #         return

    #     role  = checkall[1]
    #     getcc = await getmessage(message)






        if message.reply_to_message:
            prompt = message.reply_to_message.text
        else:
            try:
                prompt = message.text.split(" ", 1)[1]
            except IndexError:
                invalid_message = """<b>Invalid Promote ⚠️</b>\n\nMessage: Not Found Any Valid Promote From Your Input ."""
                await message.reply_text(invalid_message)
                return

        processing_message = await message.reply_text("⌛️ Answering...")

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = await fetch_response(prompt)
                break
            except httpx.ReadTimeout:

                await asyncio.sleep(2 ** attempt)
            except Exception as e:
                import traceback
                await error_log(traceback.format_exc())
                await processing_message.edit_text("⚠️ Failed to generate response. Please try again later.")
                return

        else:
            await processing_message.edit_text("⚠️ Timeout: The request took too long to process.")
            return

        await processing_message.edit_text(f"<b>{response}</b>")

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
