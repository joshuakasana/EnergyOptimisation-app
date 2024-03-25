from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


from optimise import routes

# if __name__ == '__main__':
#     app.run(debug=False)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# def create_app():
#     app = Flask(__name__)
    
#     app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#     db.init_app(app)
#     from optimise import routes
#     return app

# if __name__ == '__main__':
#     app.run(debug=False)