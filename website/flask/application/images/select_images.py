from flask import Blueprint, jsonify, request, session, flash
import random
import pandas as pd
import json
import os
from os.path import join, dirname, realpath


def select_image():
    basedir = join(dirname(realpath(__file__)))
    csv_path = basedir + "/raw_data.csv"
    df = pd.read_csv(csv_path)
    random_index = int(random.random()*len(df))
    images_row = df.loc[random_index].dropna().to_list()
    return images_row