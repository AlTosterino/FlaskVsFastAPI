from flask_app.web_app.routes import news_router

from flask import Flask

app = Flask(__name__)
app.register_blueprint(news_router)

if __name__ == "__main__":
    app.run(debug=True)
