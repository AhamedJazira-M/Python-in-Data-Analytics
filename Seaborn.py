#Install numpy if not already installed.
#Add ! before pip to install in google colab or jupyter notebook

#pip install seaborn

import seaborn as sns
import pamdas as pd
dataset=pd.read_csv("snsdata.csv")

#Statistical Relationship 

#Scatter Plot
sns.replot(x="hours",y="marks",hue="age",data=dataset)

#Line Plot
sns.replot(x="hours",y="marks",hue="age",data=dataset,kind="line",style="internet")
#mutiple --> col="internet"

#Data Distribution 

#Histogram
sns.displot(dataset, x="age", binwidth=0.5,hue="internet",multiple="stack")
#bins ---> Groups the bars or columns in the chart as given.
sns.displot(dataset, x="marks",col="internet")

#Bivariate Distribution 
sns.displot(dataset, x="age", y="marks",hue="internet")

#kernel Density Estimation KDE
kind="kde"

#Pair Plot
sns.pairplot(dataset)

#Categorical Data

#Scatter Plot
sns.catplot(x,y,data,hue)
sns.catplot(x,y,kind=box,data,hue)

#Regression
sns.replot(x,y,data)
sns.lmplot(x,y,data,hue,markers=['o','x'],palette='Set1')
