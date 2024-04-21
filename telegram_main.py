TOKEN = 'TOKEN'

import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, ConversationHandler, \
    CallbackContext

STATE_KEY = "state"
GET_CODE = 1
RESULTS = []
CODE_SNIPETS = []

async def compile_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Paste code that you want to compile!')
    context.user_data[STATE_KEY] = GET_CODE

async def code_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = context.user_data.get(STATE_KEY)
    if state == GET_CODE:
        user_text = update.message.text
        CODE_SNIPETS.append(user_text)

        print(user_text)

        context.user_data[STATE_KEY] = None

        """COMPILATION OF USER_TEXT"""
        output = "Hello World"
        result = "ERROR" # OK lub ERROR

        RESULTS.append(result)

        await update.message.reply_text(f"Output:\n{output}")
        await update.message.reply_text(f"Result:\n{result}")

    if RESULTS[-1] == "OK":
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")

async def refactor_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """CHAT GPT REFACTOR AND COMPILE CODE_SNIPETS[-1]"""
    code = 'print("Hello World")'
    output = "Hello World"
    result = "OK"

    RESULTS.append(result)
    CODE_SNIPETS.append(code)

    await update.message.reply_text("AFTER REFACTOR")
    await update.message.reply_text(f"Code:\n{code}")
    await update.message.reply_text(f"Output:\n{output}")
    await update.message.reply_text(f"Result:\n{result}")

    if RESULTS[-1] == "OK":
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")

async def optimize_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """CHAT GPT OPTIMIZE AND COMPILECODE_SNIPETS[-1]"""
    code = 'print("Hello World")'
    output = "Hello World"
    result = "OK"

    RESULTS.append(result)
    CODE_SNIPETS.append(code)

    await update.message.reply_text("AFTER OPTIMIZATION")
    await update.message.reply_text(f"Code:\n{code}")
    await update.message.reply_text(f"Output:\n{output}")
    await update.message.reply_text(f"Result:\n{result}")

    if RESULTS[-1] == "OK":
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")

async def fix_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if RESULTS[-1] == "ERROR":
        """CHAT GPT FIX AND COMPILECODE_SNIPETS[-1]"""
        code = 'print("Hello World")'
        output = "Hello World"
        result = "OK"

        RESULTS.append(result)
        CODE_SNIPETS.append(code)

        await update.message.reply_text("AFTER FIX")
        await update.message.reply_text(f"Code:\n{code}")
        await update.message.reply_text(f"Output:\n{output}")
        await update.message.reply_text(f"Result:\n{result}")
        
        if RESULTS[-1] == "OK":
            await update.message.reply_text("Your code compiled successfully,"
                                            " you can /refactor or /optimize")
        else:
            await update.message.reply_text("Something went wrong. You can /fix")

        await update.message.reply_text("To clear session data click /clear")

    else:
        await update.message.reply_text("Everything is ok. Lets /compile new code"
                                        " or /refactor or /optimize last code.")

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global GET_CODE, RESULTS, CODE_SNIPETS
    
    GET_CODE = 1
    RESULTS = []
    CODE_SNIPETS = []

    await update.message.reply_text("Data was successfully erased")
    await update.message.reply_text("You can /compile new code!")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm CodeCheetah, your agile ally in code optimization. "
                                    "Ready to boost the performance and efficiency of your code? "
                                    "Just send me a code snippet /compile, and I'll take care of the rest!")

if __name__ == '__main__':
    handlers = [
        CommandHandler('start', start_command),
        CommandHandler('compile', compile_command),
        CommandHandler('refactor', refactor_command),
        CommandHandler('optimize', optimize_command),
        CommandHandler('fix', fix_command),
        CommandHandler('clear', clear_command),
        MessageHandler(filters=filters.TEXT, callback=code_input)
    ]

    app = Application.builder().token(TOKEN).build()

    for handler in handlers:
        app.add_handler(handler)

    app.run_polling(poll_interval=1)
