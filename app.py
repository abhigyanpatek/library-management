from flask import Flask
from routes.books import books_bp
from routes.members import members_bp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!~</p>"

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(members_bp, url_prefix='/members')

if __name__ == '__main__':
    app.run(debug=True)
