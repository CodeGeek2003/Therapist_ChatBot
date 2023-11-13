import tkinter as tk
import openai

# Set up your OpenAI API key
api_key = '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'
openai.api_key = api_key  # Set the API key

# Create a function to get a chatbot response
def get_chatbot_response(input_text):
    prompt = f"You: {input_text}\nNADA (Therapist, 23 years old, works as a therapist):"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

# Create a function to clear the chat window
def clear_chat():
    chat_history.delete('1.0', tk.END)

# Create the GUI
def send_message():
    user_input = entry.get()
    chatbot_response = get_chatbot_response(user_input)
    chat_history.insert(tk.END, f"You: {user_input}\n\n Nada: {chatbot_response}\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot GUI")

chat_history = tk.Text(root)
chat_history.pack()

entry = tk.Entry(root)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack()

root.mainloop()
