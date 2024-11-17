"""
docstring
"""

# from . import wz_model
from .wz_model import WzModel

# wz.db
wz_model_instance = WzModel("app/models/wz.db")
headers = wz_model_instance.get_headers_alternative()
data = wz_model_instance.get_all_data()
