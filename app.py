from flask import Flask
from api.routes import router

app = Flask(__name__)
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
