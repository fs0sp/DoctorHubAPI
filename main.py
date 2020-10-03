from flask import Flask, jsonify
import doctors_list


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/docs')
def docs_display():
    return jsonify(doctors_list.doc_list)


@app.route('/top_doctors')
def top_docs_display():
    return jsonify(doctors_list.top_doctors)

if __name__ == "__main__":
    app.run(debug=True)