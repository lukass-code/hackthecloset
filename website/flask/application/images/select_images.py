from flask import Blueprint, jsonify, request, session, flash
import random
import pandas as pd
import json
import os
from os.path import join, dirname, realpath
import json
import math

basedir = join(dirname(realpath(__file__)))
csv_path = basedir + "/images_men.csv"
df = pd.read_csv(csv_path)
with open(basedir + "/color.json", "r") as infile:
   color = json.load(infile)
global rank_list
rank_list = [[i, 0] for i in range(0, len(df))]
random.shuffle(rank_list)



def extract_features_url(url, index):
    global color
    url_cutted = url.split("/")
    #print(url_cutted)
    if (url_cutted[7]=="S" or url_cutted[7]=="V"):
        season = "S"
    else:
        season = "W"
    #print(index)
    #print(len(color))
    feature_dict = {
        "index": index,
        "section": url_cutted[9],
        "product_type": url_cutted[8],
        "season": season,#attention original 4
        "year": url_cutted[6],
        "enc_feature": 0000,
        "color": color[index]
    }
    return feature_dict

def select_image():
        #print(rank_list)
        global rank_list
        random_index = int(random.random()*len(df))
 
        rank_index = rank_list.pop()
        print(f"Rank {rank_index[1]}")

        images_row = df.loc[rank_index[0]].dropna().to_list()
        return images_row, rank_index[0]

def rgb_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

#Update ranklist : [index, score], storted at the end to get first item as next
def update_rank(json_choices):
    global rank_list

    for item in rank_list:
        images_row = df.loc[item[0]].dropna().to_list()
        feature_dict = extract_features_url(images_row[0], item[0])
        
        #color similarity:
        try:
            #print(color[json_choices["index"]][0])
            #print(len(color))
            difference = rgb_distance(color[feature_dict["index"]][1], color[json_choices["index"]][1])
            item[1] = item[1] + (200-difference)/442*30
            #print(difference/442*0)
        except:
            pass
            #print("Fail")
        if feature_dict["year"] == json_choices["year"]:
            item[1] = item[1] + 2
        else:
            item[1] = item[1] - 2
        if feature_dict["product_type"] == json_choices["product_type"]:
            item[1] = item[1] + 10
        else:
            item[1] = item[1] - 10
        if feature_dict["season"] == json_choices["season"]:
            item[1] = item[1] + 20
        else:
            item[1] = item[1] - 20

    rank_list = sorted(rank_list, key=lambda x: x[1])
    print(rank_list[-3:])
    #json_object = json.dumps(rank_list, indent=4)
    #with open("rank.json", "w") as outfile:
    #    outfile.write(json_object)

def create_reset_rank():
    print("RESET RANK")
    global rank_list
    rank_list = [[i, 0] for i in range(0, len(df))]
    #print(rank_list)
    random.shuffle(rank_list)
    #json_object = json.dumps(rank_list, indent=4)
    #with open("rank.json", "w") as outfile:
    #    outfile.write(json_object)
