from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(data)

    return jsonify({"message": "Item stored successfully"})

if __name__ == '__main__':
    app.run(debug=True)