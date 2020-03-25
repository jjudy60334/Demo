import pandas as pd
import json
from ast import literal_eval
import time
def data_type(data,column_dict):
    data_json=eval(data)
    # df=pd.DataFrame.from_dict([data_json])
    for c in column_dict:
        if column_dict[c] in [int,float]:
            # print (data_json[c])
            # print (c,isinstance(5, int))
            try :
               column_dict[c](data_json[c])
                   
            except ValueError:
                print(c,"Incorrect Format")
            
        if column_dict[c] in ["date"]:
            try:
                time.strptime(data_json[c], "%Y-%m-%d")
                
            except ValueError:
                print(c,"Incorrect Format")


