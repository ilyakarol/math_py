# Simple text analys according to the the Cosine distance between sentences

import re
import numpy as np
import pandas as pd
import collections
from scipy.spatial import distance

data = open('sample.txt', 'r').read().lower()

def normalize_sentence(str):
    return np.array(filter(None, re.split('[^a-z]', str)))

sentenses = np.array(filter(None, data.split('.\n')))
count_by_sentence = pd.DataFrame \
                      .from_dict([collections.Counter(normalize_sentence(sentence)) for sentence in sentences]) \
                      .fillna(0)
count_by_sentence['distance'] = count_by_sentence.apply(lambda row: distance.cosine(count_by_sentence.iloc[0].tolist(), row.tolist()),
                                                        axis=1)
count_by_sentence.nsmallest(3, 'distance')
