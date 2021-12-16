from app.controllers.controller import ControllerBase
from flask import render_template

class Article4controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article4.html')
