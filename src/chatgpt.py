from openai import OpenAI
import sys
from load_credentials import load_secret
from logger import logger, log


API_KEY = load_secret('OPENAI_API_KEY')


def get_language_of_code_from_chatgpt(code_sample):
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
    openai_response = completion.choices[0].message.content.replace(' ','').split(',')
    identified_language = openai_response[0]
    log(logger.debug, 'Identified language', identified_language)
    return identified_language
