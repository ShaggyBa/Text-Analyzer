import os
# import tarfile

os.chdir(os.path.relpath("./Archieve/"))

file_name = 'Lenovo_отзыв№1.txt'

# with tarfile.open(file_name, "r:rtf") as tar:
#     tar.extractall()
#     tar.close()


file = open(file_name, mode="r", encoding="UTF-8")
print(file.read())

file.close()

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

