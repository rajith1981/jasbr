import pandas as pd

# dataframe Name and Age columns
x = 20
y =30
z =40
A = ["xxx","bbb","ccc"]
B = [x, y, z]

df = pd.DataFrame({'Name': A , 'Age': B})


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo2.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
# Set the column width and format.
worksheet.set_column(1, 3, 25)
# Close the Pandas Excel writer and output the Excel file.
writer.save()



# In[ ]:




