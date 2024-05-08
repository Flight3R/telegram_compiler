import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, ConversationHandler, \
    CallbackContext
from functions import identify_and_run
from chatgpt import get_refactored_code_from_chatgpt, get_optimized_code_from_chatgpt, get_fixed_code_from_chatgpt
from load_credentials import load_secret


TELEGRAM_TOKEN = load_secret('TELEGRAM_API_KEY')
STATE_KEY = "state"
GET_CODE = 1
STATUSES = []
CODE_SNIPETS = []
ERRORS = []


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

        compiler_output, compiler_error, compiler_status = identify_and_run(user_text)
        STATUSES.append(compiler_status)
        if compiler_status == 0:
            result = "SUCCESS"
            output = compiler_output if compiler_output != '' else '<None>'
        else:
            result = "ERROR"
            output = compiler_error
            ERRORS.append(compiler_error)

        await update.message.reply_text(f"Result:\n{result}")
        await update.message.reply_text("Output:\n")
        await update.message.reply_markdown(f"``` {output} ```")

    if STATUSES[-1] == 0:
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")


async def refactor_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """CHAT GPT REFACTOR AND COMPILE CODE_SNIPETS[-1]"""
    code_to_refactor = CODE_SNIPETS[-1]
    refactored_code = get_refactored_code_from_chatgpt(code_to_refactor)

    compiler_output, compiler_error, compiler_status = identify_and_run(refactored_code)
    STATUSES.append(compiler_status)
    if compiler_status == 0:
        result = "SUCCESS"
        output = compiler_output if compiler_output != '' else '<None>'
    else:
        result = "ERROR"
        output = compiler_error
        ERRORS.append(compiler_error)

    STATUSES.append(compiler_status)
    CODE_SNIPETS.append(refactored_code)

    await update.message.reply_text("AFTER REFACTOR")
    await update.message.reply_text("Code:\n")
    await update.message.reply_markdown(f"``` {refactored_code} ```")
    await update.message.reply_text(f"Result:\n{result}")
    await update.message.reply_text("Output:\n")
    await update.message.reply_markdown(f"``` {output} ```")

    if STATUSES[-1] == 0:
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")


async def optimize_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """CHAT GPT OPTIMIZE AND COMPILE CODE_SNIPETS[-1]"""
    code_to_optimize = CODE_SNIPETS[-1]
    optimized_code = get_optimized_code_from_chatgpt(code_to_optimize)

    compiler_output, compiler_error, compiler_status = identify_and_run(optimized_code)
    STATUSES.append(compiler_status)
    if compiler_status == 0:
        result = "SUCCESS"
        output = compiler_output if compiler_output != '' else '<None>'
    else:
        result = "ERROR"
        output = compiler_error
        ERRORS.append(compiler_error)

    STATUSES.append(compiler_status)
    CODE_SNIPETS.append(optimized_code)

    await update.message.reply_text("AFTER OPTIMIZATION")
    await update.message.reply_text("Code:\n")
    await update.message.reply_markdown(f"``` {optimized_code} ```")
    await update.message.reply_text(f"Result:\n{result}")
    await update.message.reply_text("Output:\n")
    await update.message.reply_markdown(f"``` {output} ```")

    if STATUSES[-1] == 0:
        await update.message.reply_text("Your code compiled successfully,"
                                        " you can /refactor or /optimize")
    else:
        await update.message.reply_text("Something went wrong. You can /fix")

    await update.message.reply_text("To clear session data click /clear")


async def fix_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if STATUSES[-1] == 1:
        """CHAT GPT FIX AND COMPILECODE_SNIPETS[-1]"""
        code_to_fix = CODE_SNIPETS[-1]
        error_to_fix = ERRORS[-1]

        fixed_code = get_fixed_code_from_chatgpt(code_to_fix, error_to_fix)
        compiler_output, compiler_error, compiler_status = identify_and_run(fixed_code)
        STATUSES.append(compiler_status)
        if compiler_status == 0:
            result = "SUCCESS"
            output = compiler_output if compiler_output != '' else '<None>'
        else:
            result = "ERROR"
            output = compiler_error
            ERRORS.append(compiler_error)

        STATUSES.append(compiler_status)
        CODE_SNIPETS.append(fixed_code)

        await update.message.reply_text("AFTER FIX")
        await update.message.reply_text("Code:\n")
        await update.message.reply_markdown(f"``` {fixed_code} ```")
        await update.message.reply_text(f"Result:\n{result}")
        await update.message.reply_text("Output:\n")
        await update.message.reply_markdown(f"``` {output} ```")


        if STATUSES[-1] == 0:
            await update.message.reply_text("Your code compiled successfully,"
                                            " you can /refactor or /optimize")
        else:
            await update.message.reply_text("Something went wrong. You can /fix")

        await update.message.reply_text("To clear session data click /clear")

    else:
        await update.message.reply_text("Everything is ok. Lets /compile new code"
                                        " or /refactor or /optimize last code.")


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global GET_CODE, STATUSES, CODE_SNIPETS

    GET_CODE = 1
    STATUSES = []
    CODE_SNIPETS = []
    ERRORS = []

    await update.message.reply_text("Data was successfully erased")
    await update.message.reply_text("You can /compile new code!")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm CodeCheetah, your agile ally in code optimization. "
                                    "Ready to boost the performance and efficiency of your code? "
                                    "Just send me a code snippet /compile, and I'll take care of the rest!")

if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    handlers = [
        CommandHandler('start', start_command),
        CommandHandler('compile', compile_command),
        CommandHandler('refactor', refactor_command),
        CommandHandler('optimize', optimize_command),
        CommandHandler('fix', fix_command),
        CommandHandler('clear', clear_command),
        MessageHandler(filters=filters.TEXT, callback=code_input)
    ]

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    for handler in handlers:
        app.add_handler(handler)

    app.run_polling(poll_interval=1)
