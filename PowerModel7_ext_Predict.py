import numpy as np
import pandas as pd
import cpuinfo
import psutil
import csv
import pickle
import os.path
from os import cpu_count
from sklearn.preprocessing import PolynomialFeatures

my_number_of_cores = cpu_count()
poly_features = PolynomialFeatures(degree=3, include_bias=False)

my_cpu_info = cpuinfo.get_cpu_info()['brand_raw']
splited_cpu_info = my_cpu_info.split()
my_manufacturer_name = splited_cpu_info[0]
my_processor = splited_cpu_info[3]####check with Dr. Zong
my_number_of_threads = my_number_of_cores*2
my_processor_df_tree_new = {'instance': '\0', 'processor_manufacturer': my_manufacturer_name,	'number_of_cores': my_number_of_cores, 'frequency': 2.7}

df_new = pd.read_csv('230.csv')

df_new = df_new._append(my_processor_df_tree_new, ignore_index=True)#adding my_processor_data

df_new['processor_manufacturer'] = df_new['processor_manufacturer'].astype('category')
df_new['processor_manufacturer'] = df_new['processor_manufacturer'].cat.codes

df_new['processor'] = df_new['processor'].astype('category')
df_new['processor'] = df_new['processor'].cat.codes

df_new['instance'] = df_new['instance'].astype('category')
df_new['instance'] = df_new['instance'].cat.codes

print(df_new.iloc[19:36])
x_tree_new = df_new[['number_of_cores', 'frequency', 'processor_manufacturer', 'processor']]
my_processor_x_tree_new = x_tree_new.tail(1)
last_row_new = len(df_new) - 1

y_tree_new = df_new[['instance']]
y_tree_new = y_tree_new.drop(last_row_new)

if os.path.exists("DecisionTree_trained_model_new.pickle"):
    decisionTree = pickle.load(open("DecisionTree_trained_model_new.pickle", "rb"))
    my_input_instance_new = decisionTree.predict(my_processor_x_tree_new)

print(my_input_instance_new)
i_new, c_new = np.where(y_tree_new == my_input_instance_new)
take_one_value_new = i_new[1]
my_row_new = df_new.loc[take_one_value_new,]
print(my_row_new)
timestamp = 0
with open('res2.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['cpu-utilization', 'power(W)'])
    while(1):
        my_processor_input_new = my_row_new[['processor_manufacturer',	'processor',	'number_of_cores', 'frequency',	'load_percentile']]
        my_cpu_load = psutil.cpu_percent(1)##sampling interval
      
        my_processor_input_new['load_percentile'] = my_cpu_load
        my_processor_input_new = np.asarray(my_processor_input_new)
        my_processor_input_new = my_processor_input_new.reshape(1, -1)
        my_processor_input_poly_new = poly_features.fit_transform(my_processor_input_new)
        #

        if os.path.exists("trained_model.pickle"):
            model = pickle.load(open("trained_model.pickle", "rb"))
            my_power_new = model.predict(my_processor_input_poly_new)
            writer.writerow([my_cpu_load, my_power_new.item()])
            #print(my_processor_input_new)
            #print(my_power_new)
            timestamp = timestamp + 10
            output_file.flush()
        else:
            print("Model File Missing")