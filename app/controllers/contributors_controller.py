from app.controllers.controller import ControllerBase
from flask import render_template

class contributorscontroller(ControllerBase):
    @staticmethod
    def get():
        return render_template('contributors.html')
