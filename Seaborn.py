#Install numpy if not already installed.
#Add ! before pip to install in google colab or jupyter notebook

#pip install seaborn

import seaborn as sns
import pamdas as pd
dataset=pd.read_csv("snsdata.csv")

#Statistical Relationship 

#Scatter Plot

sns.replot(x="hours",y="marks",hue="age",data=dataset)
