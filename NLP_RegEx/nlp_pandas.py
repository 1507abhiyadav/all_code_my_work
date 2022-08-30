
from traceback import print_tb
from unicodedata import name
import pandas as pd
from sqlalchemy import false
dct= {
    "name":['abhi','rilwan','alex','uma','loki'],
    "age":[22,23,24,25,21],
    "mark":[91,92,93,94,95],
    "city":["up","mang","che","che","che"]
}
# print(dct)
df= pd.DataFrame(dct)
# print(df)  ###  df print as taburl  in form. when i used dataframe.
## if I want to access of row than use index.if I want to access of column than use column name. ------->
# df.to_csv('data.csv')
df.to_csv('data2.csv')
# df.to_csv('data1.csv',index=False)
# print(df.head(2))  ####  print data from start
# print(df.tail(2))  #### print data from end
# print(df.describe()) ### print data information about numarical data like--> count,mean.std,min,,,etc.
studentDetail = pd.read_csv('data1.csv')  ### read data as from csv file.
# print(studentDetail)
studentDetail.index = ['i','ii','iii','iv','v']  ### change the index 
# print(studentDetail)
# print(studentDetail.T)  #### tronspose  change row <--> column.  -------------->

## series --> one Dimensional and it stored the data column 
# ## DataFrame ---> tow dimensional and row and column.  


####    when we used to_numpy  then create a array   -------------->
# print(studentDetail.to_numpy())  


####  sort     -------------------------->

### axis =0 (row)   ## axis =1 (column) 
# st =studentDetail.set_index(index =0,ascending = false)
# print(st)
################  useing loc function  ---------------------------->
studentDetail.loc['iv','name'] = 'nitya'  ########  replaced value 
# print(studentDetail) 
st= studentDetail.loc[['i','iv'],['name','city']]
# print(st)
## output --->     name city
#####              i    abhi   up
#####             iv  nitya  che

st= studentDetail.loc[['i','iv'],:]  ####  print all column -------.>
# print(st)
st= studentDetail.loc[:,['name','city']]  ##### print all row ------>
# print(st)

###########  using iloc ------>
st = studentDetail.iloc[0,3]  
# print(st) 
st= studentDetail.drop('age',axis=1)
# print(st)
