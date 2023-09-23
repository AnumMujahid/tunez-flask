from gradio_client import Client
from flask import Flask, request, send_file, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return { "message" : "Hello World"}

@app.route('/generate_music', methods=['POST'])
def generate_music():
    data = json.loads(request.data)
    client = Client("https://facebook-musicgen.hf.space/")
    result = client.predict(
				data["text"],
				"",
				fn_index=0
    )
    return send_file(result, as_attachment=True)

# if __name__ == '__main__':
#     app.run()
