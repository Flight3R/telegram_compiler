from openai import OpenAI
import re
import sys
from load_credentials import load_secret
import logging
from logger import logger, log


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)

API_KEY = load_secret('OPENAI_API_KEY')


def get_language_of_code_from_chatgpt(code_sample: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, please identify for me some code. \
      If it is written in Python please respond only with "python". \
      if it is written in C++ please respond only with "cpp". \
      If it is any other language please respond only with language name. \
      Code sample: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )
    openai_response = completion.choices[0].message.content
    log(logger.debug, 'Identified language', openai_response)
    return openai_response


def get_refactored_code_from_chatgpt(code_sample: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, refacor this code and make it better looking. \
      Check also for proper variable names and best coding practices. \
      Reply only with corrected code and send it as a code snippet. \
      Do not attach anything else. \
      Code to refactor: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )

    openai_response = completion.choices[0].message.content
    code_response = '\n'.join(openai_response.removeprefix('```').removesuffix('```').splitlines()[1:])
    log(logger.debug, 'Openai response', code_response)
    return code_response


def get_optimized_code_from_chatgpt(code_sample: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, optimize this code and make it more efficient. \
      Look for ways to improve performance of this code. \
      Reply only with corrected code and send it as a code snippet. \
      Do not attach anything else. \
      Code to optimize: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )
    openai_response = completion.choices[0].message.content
    code_response = '\n'.join(openai_response.removeprefix('```').removesuffix('```').splitlines()[1:])
    log(logger.debug, 'Openai response', code_response)
    return code_response


def get_fixed_code_from_chatgpt(code_sample: str, error: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, there is an error in this code: {error}. \
      Please send me code with corrected error. \
      Reply only with corrected code and send it as a code snippet. \
      Do not attach anything else. \
      Code to fix: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )

    openai_response = completion.choices[0].message.content
    code_response = '\n'.join(openai_response.removeprefix('```').removesuffix('```').splitlines()[1:])
    log(logger.debug, 'Openai response', code_response)
    return code_response


if __name__ == '__main__':
  pass
  code_sample = '''
def fibonacci(self, n: int) -> int:
    first_num, second_num, result = 0, 1, 0
    if n > 1:
        for i in range(1, n):
            result = first_num + second_num
            first_num = second_num
            second_num = result
        return result
    elif n == 1:
        return 1
    else:
        return 0
  '''
  print(get_optimized_code_from_chatgpt(code_sample))
