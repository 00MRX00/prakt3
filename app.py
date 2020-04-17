from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://i.gifer.com/2GU.gif",
    "https://i.gifer.com/6os.gif",
    "https://i.gifer.com/3QeI.gif",
    "https://i.gifer.com/4j.gif",
    "https://i.gifer.com/41W0.gif",
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")