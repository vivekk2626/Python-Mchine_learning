import pandas as pd 
import xlsxwriter;


data=[{'Name': 'PPA','Duration': 4,'Fees ':9000},{'Name':'LB','Duration':3,'Fees ':6000}];

df=pd.DataFrame(data);
print(df);

writer=pd.ExcelWriter('vivek.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name='Sheet2');

writer.save();
print("\nSuccessfully Write it into Excel sheet :")