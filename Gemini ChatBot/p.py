import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

# Set up Gemini API
genai.configure(api_key="AIzaSyBnZKePAqOp5td0sZolL7kr55GryfxRqaw")

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to process user input and get response
def send_message():
    user_input = entry_box.get()
    if user_input.lower() == "exit":
        root.quit()  # Closes the application
    elif user_input.strip():
        chat_area.insert(tk.END, " " * 50 + " " + user_input + "\n", "user")  # Right-align user
        entry_box.delete(0, tk.END)  # Clear entry box
        entry_box.config(fg="black") # Reset text color
        try:
            response = model.generate_content(user_input)
            chat_area.insert(tk.END, " " + response.text + " " * 50 + "\n", "bot")  # Left-align bot
        except Exception as e:
            chat_area.insert(tk.END, " Error in response " + " " * 50 + "\n", "bot")

        chat_area.yview(tk.END)  # Auto-scroll to the latest message

def on_entry_click(event):
    if entry_box.get() == "Type your message here...":
        entry_box.delete(0, tk.END)
        entry_box.config(fg="black")  # Change text color to black

def on_focus_out(event):
    if not entry_box.get():
        entry_box.insert(0, "Type your message here...")
        entry_box.config(fg="grey")  # Change text color to grey

# Create the GUI window
root = tk.Tk()
root.title("Gemini Chatbot")
root.geometry("600x600")

# Chat area (ScrolledText)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="blue", justify=tk.RIGHT)  # Right-align user
chat_area.tag_config("bot", foreground="green", justify=tk.LEFT)  # Left-align bot

# Entry box
entry_box = tk.Entry(root, font=("Arial", 14), fg="grey")
entry_box.insert(0, "Type your message here...")
entry_box.pack(padx=10, pady=5, fill=tk.X)
entry_box.bind("<Return>", lambda event: send_message())  # Send on Enter key
entry_box.bind("<FocusIn>", on_entry_click)
entry_box.bind("<FocusOut>", on_focus_out)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Run the GUI
root.mainloop()