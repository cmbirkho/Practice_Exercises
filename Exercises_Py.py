
# load packages
import pandas as pd 

#==============================================================================================================================================================
# Load the data
d_customer = pd.read_excel('./data/tables.xlsx', sheet_name='d_customer')

line_sales = pd.read_excel('./data/tables.xlsx', sheet_name='line_sales')

product_table = pd.read_excel('./data/tables.xlsx', sheet_name='product_table')

#==============================================================================================================================================================
# 1. Write code to provide a list of clients that purchased the brand 'king' and have an email address
newTable = pd.merge(line_sales, product_table, how='left', left_on='product_key', right_on='product_key')
newTable = pd.merge(newTable, d_customer, how='left', left_on='customer_id', right_on='customer_id')

newTable = newTable[newTable.brand == 'king']
newTable = newTable[newTable['email_address'].notnull()]

print(newTable[['customer_id', 'email_address']])

#==============================================================================================================================================================
# 2. Write code to provide three lists
# A. One list of distinct clients that purchased from only the online channel and not the store channel



# B. One list of distinct clients that purchase from only the store channel and not online



# C. One list of distinct clients that purchased from both the online and store channel




#==============================================================================================================================================================
# 3. Write code to provide the count of distinct clients, total orders, total sales, and average purchase by purchase channel



#==============================================================================================================================================================
# 4. Write code to provide a list of distinct clients that have an email address, signed up for email after 01/01/2010, and purchased tops after 3/10/2010



#==============================================================================================================================================================
# 5. Write code to provide a list of each email address and each email addresses total sales