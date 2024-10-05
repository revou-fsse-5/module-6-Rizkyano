from flask import Flask
from routes.animal import animal_bp 
from routes.employee import employee_bp  

app = Flask(__name__)

# Register blueprints
app.register_blueprint(animal_bp)
app.register_blueprint(employee_bp)

@app.route('/')
def index():
    return "<h1>Welcome To The Zoo!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
