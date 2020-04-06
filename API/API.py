from flask import Flask,request
from flask_restful import Resource,Api
from SeoulCampus import seoulCampus
from SejongCampus import sejongCampus
app = Flask(__name__)
api = Api(app)

@app.route("/seoul")
def returnSeoul():
    return seoulCampus()
@app.route("/sejong")
def returnSejong():
    return sejongCampus()


if __name__=='__main__':
    app.run(debug=True)