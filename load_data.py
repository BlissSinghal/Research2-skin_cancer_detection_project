from pathlib import Path
from typing import List
import os
from os import listdir

def load_data():
    folder = Path("train.csv")
    lines = (folder).read_text().splitlines()
    training_labels = dict(parse_labels(lines[1:len(lines)]))
    #test_set = dict(parse_labels(lines[10001: 20001]))
    return training_labels

def parse_labels(lines:List[str]):
    for line in lines:
        id, patient, gender, age, body_part, diagnosis, benign_malignant, label = line.split(",")
        #id, label = line.split(",")
        yield id, int(label)

