from flask import Flask, request, jsonify
from tasks import create_keys, insert_keys
from config import Config
from database import db
from models import Key

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/generate-keys', methods=['POST'])
def generate_keys_endpoint():
    start = int(request.json['start'])
    end = int(request.json['end'])
    keys = create_keys(start, end)
    insert_keys(keys)
    return jsonify({"message": "Keys generated and inserted successfully."}

if __name__ == '__main__':
    app.run()
