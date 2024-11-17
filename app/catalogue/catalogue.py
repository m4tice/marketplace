"""
docstring
"""

from flask import render_template

from app.models import headers, data
from . import catalogue_bp

@catalogue_bp.route('/')
def catalogue():
    """
    node: /catalogue
    """
    return render_template('catalogue/catalogue.html', headers=headers, data=data)
