"""
docstring
"""

from flask import Blueprint

catalogue_bp = Blueprint('catalogue', __name__, template_folder='templates', static_folder='static')

from . import catalogue
