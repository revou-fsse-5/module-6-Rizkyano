from flask import Flask
from routes.animal import animal_bp 
from routes.employee import employee_bp  

app = Flask(__name__)

app.register_blueprint(animal_bp)
app.register_blueprint(employee_bp)

def create_app():
    app = Flask(__name__)


    app.register_blueprint(animal_bp, url_prefix='/animals')
    app.register_blueprint(employee_bp, url_prefix='/employees')

    
    return app


@app.route('/')
def index():
    return "<h1>Welcome To The Zoo!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
