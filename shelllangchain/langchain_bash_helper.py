'''
Simple local script, that converts natural language to bash commands directly on commandline and copies it to clipboard.
'''
import json
import os
import sys

import pyperclip
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY','')


def get_bash_command(prompt : str) -> [str, str]:
    ''' returns the bash command and explanation for the commands parameters '''
    chat = ChatOpenAI()
    messages = [
        SystemMessage(content="""  You are an assistant and an expert on linux commands and bash. When asked in natural language, you
                        will provide the most fitting command and an explanation of the command workings in a structured way."""),
        HumanMessage(content="list all files in a current directory including their information"),
        AIMessage(content=json.dumps({"command": "ls -la",
                                      "explanation": "All files are listed using the inbuilt command \033[0;32mls\033[0m (is short for list).\n\t\033[0;32m-a\033[0m means all files\n\t\033[0;32m-l\033[0m means long format, \033[0;32m-l\033[0m means long format"})),
        HumanMessage(content=prompt)
    ]
    rsp = json.loads(chat(messages).content)
    return rsp['command'], rsp['explanation']


def main():
    ''' parses the arguments and executes the main logic '''
    if OPENAI_API_KEY == '':
        print("You need to have your OPENAI_API_KEY defined in your environment variables", file=sys.stderr)
        sys.exit(1)

    prompt = (" ").join(sys.argv[1:])
    if prompt.strip() == "":
        print("You need to provide the description of the command, otherwise, there is nothing to be helped with", file=sys.stderr)
        sys.exit(1)

    command, explanation = get_bash_command(prompt)
    pyperclip.copy(command)
    print(f"\033[0;32m{command}\033[0m\n\n{explanation}\n\n")


if __name__ == "__main__":
    main()