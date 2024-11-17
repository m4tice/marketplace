"""
home.py
"""
from flask import render_template

from . import home_bp

@home_bp.route('/')
def home():
    """
    node: /home
    """
    return render_template('home/home.html')
