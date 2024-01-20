import json

def fileLoadRead(file_path, role, content):
    with open(file_path, "r") as r:
        data = json.load(r)
    with open(file_path, "w") as w:
        append_data = {"role": role, "content": content}
        data.append(append_data)
        json.dump(data, w)

while True:
    user_prompt = input("user : ")
    if user_prompt == "q":
        break
    else:
        ai_prompt = input("assistant : ")
        fileLoadRead("json_dataset//new.json", "user", user_prompt)
        fileLoadRead("json_dataset//new.json", "assistant", ai_prompt)