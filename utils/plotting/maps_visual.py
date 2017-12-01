import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import mplleaflet
import seaborn as sns

import datetime
import prettyplotlib as ppl
from scipy import stats
import statsmodels.api as sm

import pysal as ps


def sampling_data_points(dataset, col_cat="Category", category='LARCENY_THEFT', col_time='year',
                         num_1=2016, num_2=2017, num_sample=1000):

    frame_1 = dataset[(dataset[col_cat] == category) & (
        dataset[col_time] == num_1)].reset_index()
    frame_2 = dataset[(dataset[col_cat] == category) & (
        dataset[col_time] == num_2)].reset_index()
    if frame_1.shape[0] >= num_sample and frame_2.shape[0] >= num_sample:
        frame_1 = frame_1.sample(num_sample)
        frame_2 = frame_2.sample(num_sample)
    else:
        pass
    print ('incidents display for year ' + str(num_1) + ":"+
           str(frame_1.shape[0]), 'of ' + str(num_sample)) 
    print ('incidents display for year ' + str(num_2) + ":" +
           str(frame_2.shape[0]), 'of ' + str(num_sample))
    return frame_1, frame_2

