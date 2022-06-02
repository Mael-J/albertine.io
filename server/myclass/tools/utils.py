import pandas as pd
import numpy as np
import math

def list_to_sql(input_list, fct = ''):
    """transform a Python list to a SQL list"""
    #list ro DataFrame
    df_code = pd.DataFrame(input_list,columns =['code'],dtype = str)
    df_code = df_code.drop_duplicates()
    df_code['code'] = df_code['code'].apply(str)
    #escape '
    df_code['code'] = df_code['code'].str.replace("'","''",regex =False)
    
    return ','.join((fct + "('" + df_code['code'] + "')").tolist())


def max_min_tick(data,nb_tick):
    """max min and tick of chart """
    try:
        np_arr = np.array(data)

        max_d = math.ceil(np_arr.max())
        min_d = math.floor(np_arr.min())

        tick = max([(max_d-min_d)/nb_tick,1])
        

        return max_d, min_d, tick
    except:
        return 100, 0, 10
