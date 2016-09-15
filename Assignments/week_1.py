import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("./Exam_Scores.csv")
scatter1=data[['reading score','math score']]
df1=pd.DataFrame(data,columns=['gender','parental level of education','math score'])
df2=pd.DataFrame(data,columns=['lunch','reading score','writing score'])
dataframe1=pd.DataFrame(data,columns=['test preparation course','math score','reading score','writing score'])
dataframe2=pd.DataFrame(data,columns=['lunch','math score','reading score','writing score'])
dataframe3=pd.DataFrame(data,columns=['gender','math score','reading score','writing score'])
dataframe4=pd.DataFrame(data,columns=['race/ethnicity','math score','reading score','writing score'])
dataframe5=pd.DataFrame(data,columns=['parental level of education','math score','reading score','writing score'])
maindf=pd.merge(df1,df2,how='inner',left_index=True,right_index=True)
matrix=maindf.corr(method='pearson',min_periods=1)
#print matrix
maindf.plot.scatter(x='math score', y='reading score')
dfone=dataframe1.groupby(['test preparation course']).mean()
dfone.plot.bar()
dftwo=dataframe2.groupby(['lunch']).mean()
#print dftwo
dftwo.plot.bar()
df3=dataframe3.groupby(['gender']).mean()
#print df3
df3.plot.bar()
df4=dataframe4.groupby(['race/ethnicity']).mean()
#print df4
df4.plot.bar()
df5=dataframe5.groupby(['parental level of education']).mean()
#print df5
plt.scatter(scatter1['reading score'],scatter1['math score'])
plt.show()
print "Answer:1=>From the graph, the test preparation course is slightly effective when the results are compared"
print "Answer:2=>The major factors that contribute to test outcomes are  lunch, race/ethnicity, parental level of education and test preparation course as per the plotted graphs"
print "Answer:3=>The best way to improve scores is providing standard lunch or good test preparation course as per the plotted graphs"

