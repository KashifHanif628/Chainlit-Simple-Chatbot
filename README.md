## 🚀 Simple Chatbot with Chainlit

![CHAINLIT CHAT LIFE CYCLE](https://github.com/user-attachments/assets/0dd7a863-a876-4e16-9c87-7332ed4b4701)


🔹 A lightweight and efficient chatbot built using Chainlit.

🔹 Just type a message, and the bot will respond dynamically!

## 📌 Features

✅ Minimalistic & Clean Code – Just a few lines to create a working chatbot.

✅ Async Support – Ensures non-blocking responses for better performance.

✅ Built on Chainlit – A powerful framework for interactive AI applications.

## 📂 Project Structure

📁 SimpleChatbot  

 ┣ 📄 chatbot.py  # Main chatbot script  
 
 ┣ 📄 README.md   # Documentation  
 
 ┗ 📄 requirements.txt  # Dependencies  
 
## ⚙️ Installation & Setup

1️⃣ Install UV

First, install UV (if not already installed):

curl -LsSf https://astral.sh/uv/install.sh | sh

For Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Verify installation:
uv --version

2️⃣ Create and Initialize the Project

uv init simple-chatbot

cd simple-chatbot

3️⃣ Install Chainlit (Dependency)
you can apply any 1 command

uv add chainlit
or
pip install chainlit

4️⃣ Activate UV Virtual Environment (Windows)

.venv\Scripts\activate

For Linux/macOS:

source .venv/bin/activate

2️⃣ Run the Chatbot

chainlit run chatbot.py

3️⃣ Start Chatting!

💬 Type a message, and the bot will respond instantly!

## 📝 Code Breakdown

Here’s a quick explanation of how the chatbot works:

import chainlit as cl

@cl.on_message  # Built-in decorator to handle incoming messages

async def main(message: cl.Message):  

    response = f"You said: {message.content}"  # Process user input
    
    await cl.Message(content=response).send()  # Send response to the user
    
🔹 @cl.on_message – Listens for user messages.

🔹 cl.Message – Represents a message object from Chainlit.

🔹 .send() – Sends the response back to the user.

## 🎯 Why Use This?

✅ Super Simple – Perfect for beginners.

✅ Lightweight – No extra dependencies required.

✅ Scalable – Extend it easily with AI models or APIs.

## 💡 Future Enhancements

🚀 Add AI-powered responses (e.g., OpenAI’s GPT)

🔗 Integrate with a database for persistent chat memory

🎨 Improve UI with a frontend interface

## 📜 License

📝 This project is open-source under the MIT License.
