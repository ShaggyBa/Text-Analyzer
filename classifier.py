import os
import zipfile


os.chdir(os.path.relpath("./Archieve/"))

file_name = 'data.zip'

with zipfile.ZipFile(file_name, "r") as archive:
    archive.extractall(path="./Archieve/")


def load_training_data(data_directory: str = "data/train", split: float = 0.8, limit: int = 0) -> tuple:
    reviews = []  #
    # for label in ["pos", "neg"]:  #
    #     labeled_directory = f"{data_directory}/{label}"  #
    #     for review in os.listdir(labeled_directory):  #
    #         if review.endswith(".txt"):  #
    #             with open(f"{labeled_directory}/{review}") as f:
    #                 text = f.read()  #
    #                 text = text.replace("<br />", "\n\n")  #
    #                 if text.strip():  #
    #                     spacy_label = {  #
    #                         "cats": {  #
    #                             "pos": "pos" == label,  #
    #                             "neg": "neg" == label  #
    #                         }  #
    #                     }  #
    #                     reviews.append((text, spacy_label))  #
    #

