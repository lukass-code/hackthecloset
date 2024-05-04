from flask import Blueprint, jsonify, request
from flask import current_app as app
import random
import pandas as pd
import os
from os.path import join, dirname, realpath

images_bp = Blueprint(
    'images_bp', __name__
)

@images_bp.route("/get_images",methods=['GET'])
def get_images():
    number = int(request.args.get("number"))
    list_images = []
    basedir = join(dirname(realpath(__file__)))
    csv_path = basedir + "/raw_data.csv"
    df = pd.read_csv(csv_path)
    for i in range(0, number):
        random_index = int(random.random()*len(df))
        list_images.append(df.loc[random_index].dropna().to_list())
    print(list_images)
    return jsonify(list_images), 201,