import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/TgCatUB/catuserbot && cd catuserbot && pip3 install -r requirements.txt && cp ../config.py config.py && python3 -m userbot &")
