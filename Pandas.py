
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

