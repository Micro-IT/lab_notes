# df_usa_cleanlap = previous saved final dataframe

import pandas as pd
import numpy as np

import collections

scipy.stats import linregress
from scipy.stats import pearsonr

import random
import sys
import array
import matplotlib.pyplot as plt

from pprint import pprint

#--------------------------------- Import cleaned-up and pickeled dataframe

# import cleaned up data
df_ireland_mening = pd.read_pickle('clean_ireland_us.pkl')
df_usa_mening = pd.read_pickle('clean_usa_ir.pkl')

#value counts of all loci in dataframe and store into a dictionary of dictionaries
value_counts_usa = {c: df_usa_mening[c].value_counts(normalize=True, dropna=True).to_dict() for c in df_usa_mening}
value_counts_czech = {c: df_czech_mening[c].value_counts(normalize=True, dropna=True).to_dict() for c in df_czech_mening}
value_counts_usa

#--------------------------------- flatten nested dictionaries to obtain unique allele keys
def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + str(k) if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flat_usa = flatten(value_counts_usa)
flat_czech = flatten(value_counts_czech)

#--------------------------------- combine flattened dictionaries for one dictionary with only allele keys that both exist
finalfdict = {key:(flat_usa[key], flat_czech[key]) for key in flat_usa.keys() & flat_czech}
pprint(finalfdict)

#--------------------------------- drop loci based on conditions for final dictionary

#delete items with values <0.05
for key, value in dict(finalfdict).items():
    if value[0] < 0.05 or value[1] < 0.05 :
        del finalfdict[key]

#--------------------------------- calculate correlations
#arrange data into numpy arrray
data = {"x":[], "y":[], "label":[]}
for label, coord in finalfdict.items():
    data["x"].append(coord[0])
    data["y"].append(coord[1])
    data["label"].append(label)

#calculate correlation

linregress(data["x"], data["y"])
pearsonr(data["x"],  data["y"])
