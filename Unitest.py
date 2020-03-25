from  test_data_type import *

data='''    {"ad_network": "FOO",
    "date": "2019-06-05.",
    "app_name": "LINETV",
    "unit_id": "55665201314",
    "request": "100",
    "revenue": "0.00365325",
    "imp": "23"}
'''
column_dict= {"ad_network": str,
    "date": "date",
    "app_name": str,
    "unit_id": str,
    "request": int,
    "revenue": float,
    "imp": int}
data_type(data,column_dict)