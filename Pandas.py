
!pip install pandas
import pandas
pandas.__version__

import pandas as pd
a=[7,9,4]
dataset=pd.Series(a)
print(dataset)

import pandas as pd
a=[7,9,4]
dataset=pd.Series(a,index=["No.1","No.2","No.3"])
print(dataset)
     
data={"Name":["Apple","Guava","Grapes"],"Color":["Red","Green","Violet"]}
dataset=pd.DataFrame(data)
print(dataset)

dataset1=pd.read_csv("dataset.csv")
print(dataset1.head())

dataset1=pd.read_csv("dataset.txt")
print(dataset1.head())

dataset1=pd.read_excel("datasetexcel.xlsx")
print(dataset1.head())

print(dataset1.shape)
print(dataset1.describe())

print(dataset1.columns)
print(dataset1[["Name","Speed"]])
print(dataset1["Name"][0:6])


print(dataset1.iloc[0])
print(dataset1.iloc[0:5])
print(dataset1.iloc[0,1])  #like matrix [0,1]

for index,row in dataset1.iterrows():
  print(index,row["Name"])

print(dataset1.loc[dataset1["Name"]=="Pikachu"])
print(dataset1.loc[dataset1["Speed"]>90])

dataset1["Power"]=dataset1["HP"]+dataset1["Attack"]
print(dataset1.head())

dataset1.sort_values(["Speed"],ascending=True)

dataset1=dataset1.drop(columns=["Power"])
print(dataset1.head())
     
dataset1.to_excel("newdataset.xlsx")

dataset1.isnull().any()

dataset1=dataset1[dataset1["Type 2"].notna()]
print(dataset1.isnull().any())
dataset1

meandata=dataset1["Speed"].fillna(dataset1["Speed"].mean())
print(meandata)

print(dataset1.head())
Generation=set(dataset1["Generation"])
dataset1["Generation"]=dataset1["Generation"].map({1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six"}).astype(str)
print(dataset1.head())
     
