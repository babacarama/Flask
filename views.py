from django import views
from flask import Blueprint

views=Blueprint('views',__name__)
@views.route('/hello')
def hello():
    return "hello word"
