from app.controllers.controller import ControllerBase
from flask import render_template


class Arpanetcontroller(ControllerBase):
    @staticmethod
    def get():
        return render_template("Arpanet.html")
