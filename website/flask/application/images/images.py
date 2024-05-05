from flask import Blueprint, jsonify, request, session, flash
from flask import current_app as app
import random
import pandas as pd
import json
import os
from os.path import join, dirname, realpath
from . import select_images as si

images_bp = Blueprint(
    'images_bp', __name__
)



@images_bp.route("/get_images",methods=['GET'])
def get_images():
    number = int(request.args.get("number"))
    list_images = []
    si.create_reset_rank()
    for i in range(0, number):
        random_index = int(random.random()*len(si.df))
        images_row = si.df.loc[random_index].dropna().to_list()
        
        list_images.append([images_row, si.extract_features_url(images_row[0], random_index)])
    #print(list_images)
    return jsonify(list_images), 201,

@images_bp.route("/get_image",methods=['GET'])
def get_image():
    #with open("rank.json", "r") as infile:
    #    rank_list = json.load(infile)
    images_row, index = si.select_image()
    return jsonify([images_row, si.extract_features_url(images_row[0], index)]), 201,

@images_bp.route("/set_choice",methods=['GET'])
def set_choice_data():
    json_choice = json.loads(request.args.get("choice"))
    si.update_rank(json_choice)
    if session.get('choices'):
        session["choices"].append(json_choice)
    else:
        session["choices"] = [json_choice]
    print(session["choices"])
    return jsonify("Success"), 201


@images_bp.route("/reset_choice",methods=['GET'])
def reset_choice_data():
    if session.get('choices'):
        session.pop("choices")
    si.create_reset_rank()
    print("Reset")
    return jsonify("Success"), 201
