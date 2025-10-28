import pandas as pd

Data ={
    "name":["John","Jane","Doe"],
    "age":[28,34,29],
    "city":["New York","Los Angeles","Chicago"]
    
}

df = pd.DataFrame(Data)
print(df)