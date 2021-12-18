"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.Article1_controller import Article1controller
from app.controllers.Article4_controller import Article4controller
from app.controllers.types_controller import typescontroller
from app.controllers.internet_controller import internetcontroller
from app.controllers.Arpanet_controller import Arpanetcontroller

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/types", methods=['GET'])
def types_get():
    return typescontroller.get()

@app.route("/internet", methods=['GET'])
def contributors_get():
    return internetcontroller.get()

@app.route("/Article1", methods=['GET'])
def Article1_get():
    return Article1controller.get()

@app.route("/Article4", methods=['GET'])
def Article4_get():
    return Article4controller.get()

@app.route("/Arpanet", methods=['GET'])
def inventors_get():
    return Arpanetcontroller.get()
