from flask import Flask, request
import Service

app = Flask(__name__)


@app.route("/recognize-by-words", methods=['POST'])
def recognize_words():
    print(request.files)
    image = request.files.get('photo')
    words = Service.recognize_words_by_photo(image)
    return words


app.run(port=5000)
