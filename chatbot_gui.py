import customtkinter as ctk
from chatbot import chatbot

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ana = chatbot("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", "json_dataset//chat.json")

root = ctk.CTk()
root.geometry("600x338")
root.title("Ana Chatbot - Aryan")

aiVar = ctk.StringVar()

def send():
    user_prompt = user_entry.get()
    ai_data = ana.chat(user_prompt)
    aiVar.set(ai_data)

ai_label = ctk.CTkLabel(root, text="AI output", textvariable=aiVar)
ai_label.pack()

user_entry = ctk.CTkEntry(root, placeholder_text="prompt")
user_entry.pack()

send_btn = ctk.CTkButton(root, text="Send", command=send)
send_btn.pack()

root.mainloop()