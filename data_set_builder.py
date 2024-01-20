import os
import json

def createData(file_name, role, content):
    with open(file_name, "r") as r:
        data = json.load(r)
    with open(file_name, "w") as w:
        append_data = {"role": role, "content": content}
        data.append(append_data)
        json.dump(data, w)

if __name__ == "__main__":
    if not os.path.exists("json_dataset/"):
        os.mkdir("json_dataset/")
    print("1.Open file\n2.New file")
    uc = input(":- ")
    if uc == "1":
        file_name = input("Enter file name : ")
        if not file_name.endswith(".json"):
            file_name += ".json"
        if not os.path.exists(f"json_dataset//{file_name}"):
            print("File doesn't exists!!")
            exit()
        while True:
            user_prompt = input("user : ")
            if user_prompt == "q":
                break
            else:
                ai_prompt = input("assistant : ")
                createData(f"json_dataset/{file_name}", "user", user_prompt)
                createData(f"json_dataset/{file_name}", "assistant", ai_prompt)
    elif uc == "2":
        file_name = input("Enter file name : ")
        if not file_name.endswith(".json"):
            file_name += ".json"
        if os.path.exists(f"json_dataset//{file_name}"):
            print("File already exists!!")
            exit()
        else:
            with open(f"json_dataset//{file_name}", "w") as f:
                json.dump([], f)
        while True:
            user_prompt = input("user : ")
            if user_prompt == "q":
                break
            else:
                ai_prompt = input("assistant : ")
                createData(f"json_dataset/{file_name}", "user", user_prompt)
                createData(f"json_dataset/{file_name}", "assistant", ai_prompt)