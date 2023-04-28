import spacy
nlp = spacy.load("en_core_web_sm")

text = """
Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets.
"""

doc = nlp(text)
token_list = [token for token in doc]

print(token_list)

filtered_tokens = [token for token in doc if not token.is_stop]

print(filtered_tokens)

lemas = [
    f"token : {token} | lemma: {token.lemma_}"
    for token in filtered_tokens
]

print(lemas)

print(filtered_tokens[1].vector)