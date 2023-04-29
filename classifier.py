import os
# import zipfile
import random

os.chdir(os.path.relpath("./Archieve/"))

# file_name = 'data.zip'

# with zipfile.ZipFile(file_name, "r") as archive:
#     archive.extractall(path="./data/train")


def load_training_data(data_directory: str = "./data/train", split: float = 0.8, limit: int = 0) -> tuple:
    reviews = []  #
    for label in ["pol", "neg"]:  #
        labeled_directory = f"{data_directory}/{label}"  #
        for review in os.listdir(labeled_directory):  #
            if review.endswith(".txt"):  #
                with open(f"{labeled_directory}/{review}", encoding = "UTF-8") as f:
                    text = f.read()  #
                    if text.strip():  #
                        spacy_label = {  #
                            "cats": {  #
                                "pol": "pol" == label,  #
                                "neg": "neg" == label  #
                            }  #
                        }  #
                        reviews.append((text, spacy_label))  #

    random.shuffle ( reviews )  #

    if limit :  #
        reviews = reviews [ :limit ]  #
    split = int ( len ( reviews ) * split )  #

    return reviews [ :split ] , reviews [ split : ]  #


print(load_training_data(split = 0.8, limit = 0)[0][0])