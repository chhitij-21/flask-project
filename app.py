from flask import Flask, Response
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data.json")

def colorize_json(data):
    """Convert JSON to colored HTML for browser display"""
    if isinstance(data, dict):
        html = "<pre style='font-family:monospace;background:#1e1e1e;color:#d4d4d4;padding:20px;'>"
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                html += f"<span style='color:#ce9178'>{json.dumps(key)}:</span> {json.dumps(value, indent=2)}\n"
            else:
                html += f"<span style='color:#ce9178'>{key}:</span> <span style='color:#569cd6'>{json.dumps(value)}</span>\n"
        return html + "</pre>"
    return json.dumps(data)

@app.route('/api')
def api():
    with open(JSON_PATH) as f:
        data = json.load(f)
    
    # Return colored HTML version
    colored = colorize_json(data)
    return Response(colored, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
