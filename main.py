import os
import random
import spacy

def train_model(
    training_data: list,
    test_data: list,
    iterations: int = 20
) -> None:
    # Строим конвейер
    nlp = spacy.load("en_core_web_sm")
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.create_pipe(
            "textcat", config={"architecture": "simple_cnn"}
        )
        nlp.add_pipe(textcat, last=True)