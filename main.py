from flask import Flask
from views import views #name of varble


app = Flask(__name__)
app.register_blueprint(views)

if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=8080)












