import json


def get_stored_favorite_num(filename):
    """get favorite number from json file"""

    try:
        with open(filename) as f_obj:
            