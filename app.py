from flask import Flask, render_template
from controllers.member_controller import members_blueprint
app = Flask(__name__)

# app.register_blueprint(bookings_blueprint)
# app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html', current_page = 'Home')

if __name__ == '__main__':
    app.run(debug=True)

