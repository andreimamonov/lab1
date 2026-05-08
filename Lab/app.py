from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def days_until_new_year():
    today = datetime.now()
    next_year = today.year + 1
    new_year = datetime(next_year, 1, 1)
    days_left = (new_year - today).days
    return jsonify({"days_before_new_year": days_left})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)