import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/TgCatUB/catuserbot ok && cd ok && pip3 install -r requirements.txt && python3 -m userbot")
