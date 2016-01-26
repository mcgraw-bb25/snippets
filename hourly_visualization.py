
# coding: utf-8

# Begin by loading data through making requests to CouchDB view URI.
# Load data into native Python objects temperature_data and count_data.

# In[1]:

# loading data
import json
import urllib as requestlib

# building frames
import pandas as pd
from pandas import DataFrame, Series

# plotting
import numpy as np
import matplotlib.pyplot as matplt

# get_ipython().magic(u'matplotlib inline')
try:
    import IPython
    shell = IPython.get_ipython()
    shell.enable_matplotlib(gui='qt')
except:
    pass

# In[2]:

hourly_temp_view = "http://127.0.0.1:5984/temperature_data/_design/temperature_data/_view/temp_by_hour?group_level=1"
hourly_count_view = "http://127.0.0.1:5984/temperature_data/_design/temperature_data/_view/count_by_hour?group_level=1"

# temperature_request = requestlib.urlopen(hourly_temp_view)
# temperature_response = temperature_request.read()
# temperature_data = json.loads(temperature_response.decode())
# temperature_data = temperature_data["rows"]

# count_request = requestlib.urlopen(hourly_count_view)
# count_response = count_request.read()
# count_data = json.loads(count_response.decode())
# count_data = count_data["rows"]

def load_data(uri):
    request = requestlib.urlopen(uri)
    response = request.read()
    data = json.loads(response.decode())
    data = data["rows"]
    return data

temperature_data = load_data(hourly_temp_view)
count_data = load_data(hourly_count_view)


# In[3]:

temperature_frame = DataFrame(temperature_data)
temperature_frame.columns = ["date", "temperature_sum"]

count_frame = DataFrame(count_data)
count_frame.columns = ["date", "count"]

full_data = pd.merge(temperature_frame, count_frame, on="date")


# In[4]:

def average(sum, count):
    if count != 0:
        return sum / count * 1.0
    else:
        return 0

full_data["average_temperature"] = map(average, full_data["temperature_sum"], full_data["count"])


# In[5]:

def plot_data():
    ''' method to plot line graph of temperature by hour'''
    items = len(full_data) + 1
    
    x_data = np.arange(1, items)
    
    y_data = [avg_temp for avg_temp in full_data["average_temperature"] ]
    
    x_labels = [date for date in full_data["date"]]
    x_samples = [ '' ] * items
    for i in range( 0, items, items/15 ):
        x_samples[i] = x_labels[i]
    
    matplt.plot(x_data, y_data)
    matplt.xticks( np.arange(700), x_samples, rotation=65 )
    matplt.show()

plot_data().savefig("temp_graph.png")

