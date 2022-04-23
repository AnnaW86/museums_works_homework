from flask import Flask, render_template

from controllers.museums_controller import museums_blueprint
from controllers.works_controller import works_blueprint

app = Flask(__name__)

app.register_blueprint(museums_blueprint)
app.register_blueprint(works_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
