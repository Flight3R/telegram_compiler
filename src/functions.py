from chatgpt import get_language_of_code_from_chatgpt, get_refactored_code_from_chatgpt
import subprocess
import os
import sys
from logger import logger, log
import logging

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)

CODE_STORAGE_PATH = 'storage/code_files'
CODE_STORAGE_PYTHON_PATH = os.path.join(CODE_STORAGE_PATH, 'python')
CODE_STORAGE_CPP_PATH = os.path.join(CODE_STORAGE_PATH, 'cpp')
STORAGE_COMPILED_FILES = 'storage/compiled_files'
CURRENT_CODE_FILE_NUMBER_PATH = os.path.join(CODE_STORAGE_PATH, 'current_code_file_number')


def get_current_code_file_number() -> int:
    log(logger.debug, sys._getframe().f_code.co_name)
    try:
        with open(CURRENT_CODE_FILE_NUMBER_PATH, 'r') as file:
            filename = file.read()
        return int(filename)
    except FileNotFoundError:
        with open(CURRENT_CODE_FILE_NUMBER_PATH, 'w') as file:
            file.write(str(1))
        return 1


def update_current_code_file_number(number: int):
    log(logger.debug, sys._getframe().f_code.co_name)
    log(logger.info, 'Updating current code file number', f'{number=}')
    with open(CURRENT_CODE_FILE_NUMBER_PATH, 'w') as file:
        file.write(str(number))


def save_code_to_file(path: os.path, code: str):
    log(logger.debug, sys._getframe().f_code.co_name)
    log(logger.info, 'Saving code to file', f'{path=}')
    with open(path, 'w') as file:
        file.write(code)


def compile_and_run_cpp(code: str) -> tuple[str, str, int]:
    log(logger.debug, sys._getframe().f_code.co_name)

    current_code_file_number = get_current_code_file_number()
    code_file_path = os.path.join(CODE_STORAGE_CPP_PATH, f'{current_code_file_number}.cpp')
    save_code_to_file(code_file_path, code)
    update_current_code_file_number(current_code_file_number+1)

    compiled_code_file = os.path.join(STORAGE_COMPILED_FILES, f'{current_code_file_number}.o')
    log(logger.info, 'Running cpp file', f'{code_file_path=}')
    compile_process = subprocess.Popen(['g++', code_file_path, '-o', compiled_code_file], stderr=subprocess.PIPE)
    _, compile_err = compile_process.communicate()

    if compile_process.returncode != 0:
        return None, compile_err.decode('utf-8'), compile_process.returncode
    run_process = subprocess.Popen([compiled_code_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_output, run_err = run_process.communicate()

    os.remove(compiled_code_file)

    return run_output.decode('utf-8'), run_err.decode('utf-8'), run_process.returncode


def run_python_code(code: str) -> tuple[str, str, int]:
    log(logger.debug, sys._getframe().f_code.co_name)
    current_code_file_number = get_current_code_file_number()
    code_file_path = os.path.join(CODE_STORAGE_PYTHON_PATH, f'{current_code_file_number}.py')
    save_code_to_file(code_file_path, code)
    update_current_code_file_number(current_code_file_number+1)

    try:
        log(logger.info, 'Running python file', f'{code_file_path=}')
        process = subprocess.Popen(['python3', code_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode('utf-8'), error.decode('utf-8'), process.returncode
    except Exception as e:
        return None, str(e), 1


def identify_and_run(code_sample: str) -> tuple[str, str, int]:
    identified_language = get_language_of_code_from_chatgpt(code_sample)
    if identified_language == 'python':
        output, error, status = run_python_code(code_sample)
    elif identified_language == 'cpp':
        output, error, status = compile_and_run_cpp(code_sample)
    else:
        output, error, status = None, f'language not supported: {identified_language}', None
    return output, error, status


if __name__ == '__main__':
#     code_sample = '''
# #include <iostream>
# using namespace std;
# int main(){
#     cout<<"Hello, World!"<< endl;
#     return 0;
# }
#     '''

#     print(get_refactored_code_from_chatgpt(code_sample))


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

#     code_sample = '''
# public class HelloWorld {
#     public static void main(String[] args) {
#         System.out.println("Hello, World!");
#     }
# }
# '''

    output, error, status = identify_and_run(code_sample)
    print(f'{output=}')
    print(f'{error=}')
    print(f'{status=}')