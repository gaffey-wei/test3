from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def my_api():
    if request.method == 'POST':
        data = request.json
        print('hello world')
        return jsonify({"message": "Data received", "data": data})
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
