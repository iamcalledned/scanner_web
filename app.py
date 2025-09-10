from flask import Flask
from routes.routes_scanner import scanner_bp
from routes.routes_api_scanner import api_scanner_bp
import datetime

app = Flask(__name__)
app.register_blueprint(scanner_bp)
app.register_blueprint(api_scanner_bp)

# Register Jinja2 filter
@app.template_filter("datetimeformat")
def datetimeformat(value, format="%b %d, %I:%M %p"):
    if isinstance(value, (int, float)):
        value = datetime.datetime.fromtimestamp(value)
    elif isinstance(value, str):
        try:
            value = datetime.datetime.fromisoformat(value)
        except ValueError:
            return value
    return value.strftime(format)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
