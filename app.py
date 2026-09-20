from flask import Flask
import threading
import asyncio
import main  # তোমার existing main.py

app = Flask(__name__)

@app.route("/")
def home():
    return "EH MUNNA BOT is running on Render!"

def run_bot():
    asyncio.run(main.StarTinG())

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
