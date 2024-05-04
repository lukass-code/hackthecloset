from flask import Blueprint, jsonify, request
from flask import current_app as app
import random
import pandas as pd
import os
from os.path import join, dirname, realpath

images_bp = Blueprint(
    'images_bp', __name__
)

def extract_features_url(url):
    url_cutted = url.split("/")
    print(url_cutted)
    if (url_cutted[7]=="S" or url_cutted[7]=="V"):
        season = "S"
    else:
        season = "W"
    feature_dict = {
        "section": url_cutted[9],
        "product_type": url_cutted[8],
        "season": season,#attention original 4
        "year": url_cutted[6],
        "enc_feature": 0000
    }
    return feature_dict

@images_bp.route("/get_images",methods=['GET'])
def get_images():
    number = int(request.args.get("number"))
    list_images = []
    basedir = join(dirname(realpath(__file__)))
    csv_path = basedir + "/raw_data.csv"
    df = pd.read_csv(csv_path)
    for i in range(0, number):
        random_index = int(random.random()*len(df))
        images_row = df.loc[random_index].dropna().to_list()
        
        list_images.append([images_row, extract_features_url(images_row[0])])
    #print(list_images)
    return jsonify(list_images), 201,

@images_bp.route("/get_image",methods=['GET'])
def get_image():
    basedir = join(dirname(realpath(__file__)))
    csv_path = basedir + "/raw_data.csv"
    df = pd.read_csv(csv_path)
    random_index = int(random.random()*len(df))
    images_row = df.loc[random_index].dropna().to_list()
    return jsonify([images_row, extract_features_url(images_row[0])]), 201,