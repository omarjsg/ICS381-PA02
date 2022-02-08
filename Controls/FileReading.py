import numpy as np
import csv


def read(path):
    data = open(path, 'rt')
    reader = csv.reader(data, delimiter=',', quoting=csv.QUOTE_NONE)
    lister = list(reader)
    data = np.array(lister, dtype=float)
    return data
