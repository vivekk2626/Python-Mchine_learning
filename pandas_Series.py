import pandas as pd
import numpy as np 

d='*'*20;



s=pd.Series(dtype='float');  # at the time of starting datatype is object bt it is now Float.
print(s); 
print(d);


print("\n Normal Series :")
data=np.array(['a','b','c','d']);
df=pd.Series(data)
print(df);
print("Only Specific Values Like this :df[]")
print(df[0]);
print(d);



print("\nSeries with Index :")
data=np.array(['a','b','c','d']);
series=pd.Series(data,index=[100,101,102,103])
print(series);
print("\nOnly Specific Values :")
print(series[101]);
print(d);




print("\nSeries Float Value :")
data={'a':1.1,'b':2.1,'c':3.1,'d':4.1};
series=pd.Series(data)
print(series);
print(d);





print("\nSeries With Index Another Syntax :")
data=pd.Series([1,2,3,4,5],index=['a','b','c','d','e']);
print(data);
print(data['c'])

