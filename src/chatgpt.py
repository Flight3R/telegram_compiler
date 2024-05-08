from openai import OpenAI
import re
import sys
from load_credentials import load_secret
from logger import logger, log


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
      Reply only with corrected code and send it as a code snippet, do not attach language name. \
      Do not attach anything else. \
      Code to refactor: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )

    openai_response = completion.choices[0].message.content
    matches = re.findall(r'```(.*?)```', openai_response, re.DOTALL)
    text_within_backticks = ''.join(matches)
    log(logger.debug, 'Refactored code openai response', openai_response)
    return text_within_backticks


def get_optimized_code_from_chatgpt(code_sample: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, optimize this code and make it more efficient. \
      Look for ways to improve performance of this code. \
      Reply only with corrected code and send it as a code snippet, do not attach language name. \
      Do not attach anything else. \
      Code to optimize: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )
    openai_response = completion.choices[0].message.content
    matches = re.findall(r'```(.*?)```', openai_response, re.DOTALL)
    text_within_backticks = ''.join(matches)
    log(logger.debug, 'Optimized code openai response', openai_response)
    return text_within_backticks


def get_fixed_code_from_chatgpt(code_sample: str, error: str) -> str:
    log(logger.debug, sys._getframe().f_code.co_name)
    '''
    OpenAI does not return code other than 200.
    '''
    client = OpenAI(api_key=API_KEY)

    message = f'Hello chat, there is an error in this code: {error}. \
      Please send me code with corrected error. \
      Reply only with corrected code and send it as a code snippet, do not attach language name. \
      Do not attach anything else. \
      Code to fix: {code_sample}'

    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[
        {'role': 'system', 'content': message},
      ]
    )

    openai_response = completion.choices[0].message.content
    matches = re.findall(r'```(.*?)```', openai_response, re.DOTALL)
    text_within_backticks = ''.join(matches)
    log(logger.debug, 'Fixed code openai response', openai_response)
    return text_within_backticks


if __name__ == '__main__':
  pass
  code_sample = '''
def fib(self, n: int) -> int:
      a,b,s = 0, 1, 0
      if n>1:
          for i in range(1,n):
              s = a+b
              a = b
              b = s
          return s
      elif n == 1:
          return 1
      else:
          return 0
  '''
  print(get_refactored_code_from_chatgpt(code_sample))
