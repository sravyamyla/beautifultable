from app.controllers.controller import ControllerBase
from flask import render_template

class inventorscontroller(ControllerBase):
    @staticmethod
    def get():
        return render_template('inventors.html')
