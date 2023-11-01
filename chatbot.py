import openai
import json

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
            self.response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.final_user_data,
                temperature=0.5,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            self.ai_data = self.response["choices"][0]["message"]["content"]
            fileLoadRead(self.file_path, "assistant", self.ai_data)
            return self.ai_data
        except Exception as e:
            print(e)

if __name__ == "__main__":
    Ana = chatbot("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", "json_dataset//new.json")

    print("Chatroom - AnaAI")
    while True:
        user_prompt = input("You : ")
        if user_prompt == "q":
            break
        else:
            ai_prompt = Ana.chat(user_prompt)
            print(f"AI : {ai_prompt}")

