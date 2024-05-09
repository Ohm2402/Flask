from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_data', methods=['POST'])
def post_data():
    name = request.form.get('name')
    age = request.form.get('age')

    print(f"Name: {name}, Age: {age}")

    response = {
        "message": "Data received successfully",
        "name": name,"age": age
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=1998)
