# version 0.0.2

from colorama import init

import openai
import json

import config

init(autoreset=True)
YELLOW = "\x1b[1;33;40m"
RED = "\x1b[1;31;40m"
LIGHT_GREEN = "\033[1;32;40m"


def fileLoadRead(file_path, role, content):
    with open(file_path, "r") as r:
        data = json.load(r)
    with open(file_path, "w") as w:
        append_data = {"role": role, "content": content}
        data.append(append_data)
        json.dump(data, w)


def fileRead(file_path):
    with open(file_path, "r") as rr:
        data = json.load(rr)
    return data


class chatbot:
    def __init__(self, openai_api_key, json_file_path):
        openai.api_key = openai_api_key
        self.file_path = json_file_path

    def chat(self, user_prompt):
        try:
            fileLoadRead(self.file_path, "user", user_prompt)
            self.final_user_data = fileRead(self.file_path)
            self.response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.final_user_data,
                temperature=1,
                max_tokens=128,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            self.ai_data = self.response.choices[0].message.content
            fileLoadRead(self.file_path, "assistant", self.ai_data)
            return self.ai_data
        except Exception as e:
            print(e)


if __name__ == "__main__":
    Ana = chatbot(config.OPENAI_API_KEY, "json_dataset//chat.json")

    print("Chatroom - AnaAI")
    while True:
        user_prompt = input(f"{LIGHT_GREEN}You : ")
        if user_prompt == "q":
            break
        else:
            ai_prompt = Ana.chat(user_prompt)
            print(f"{YELLOW}AI : {ai_prompt}")
