import pandas as pd;

print("********************************************* ");
print(" Demonstration Of DataFrame :");
print("********************************************* ");
df=pd.DataFrame();
print(df);



print("\n********************************************* ");
print(" Demonstration Of Series with list :");
print("********************************************* ");
data=[1,2,3,4,5,6,7]
df=pd.DataFrame(data);
print(df)




print("\n********************************************* ");
print(" Demonstration Of DataFrame with list of list :");
print("********************************************* ");
data1=[['ppa',4],['LB',2],['Python',3],['Angular',4],['Django',6],['C',4]];
df=pd.DataFrame(data1,columns=['Name :','Duration :']);
print(df);



print("\n********************************************* ");
print(" Demonstration Of DataFrame with List of Set :");
print("********************************************* ");
data1=[{'Name':'Vivek','Duration:':4,'Fees :':4000},{'Name':'Poti','Duration:':4,'Fees :':4000},{'Name':'Aai','Duration:':4,'Fees :':4000}]
df=pd.DataFrame(data1);
print(df);
print("********************************************* ");




print("\n********************************************* ");
print(" Demonstration Of DataFrame with List of Set :");
print("********************************************* ");
data1=[{'Name':'Vivek','Duration:':4,'Fees :':4000},{'Name':'Poti','Duration:':4,'Fees :':4000},{'Name':'Aai','Duration:':4,'Fees :':4000}]
df=pd.DataFrame(data1);
print(df);
print("********************************************* ");




print("\n********************************************* ");
print(" Demonstration Of DataFrame with List of Set :");
print("********************************************* ");
data1={'one':pd.Series([1,2,3],index=['a','b','c'])}
df=pd.DataFrame(data1);
print(df['one']);
