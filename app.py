from flask import Flask, Response
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data.json")


def colorize_json(data):
    """Convert JSON data to colored HTML."""
    json_str = json.dumps(data, indent=2)
    html = f'<pre style="background-color: #f5f5f5; padding: 10px;"><code>{json_str}</code></pre>'
    return html


@app.route('/api')
def api():
    with open(JSON_PATH) as f:
        data = json.load(f)
    
    # Return colored HTML version
    colored = colorize_json(data)
    return Response(colored, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
