
# load packages
import pandas as pd 

#==============================================================================================================================================================
# Load the data
d_customer = pd.read_excel('./data/tables.xlsx', sheet_name='d_customer')

line_sales = pd.read_excel('./data/tables.xlsx', sheet_name='line_sales')

product_table = pd.read_excel('./data/tables.xlsx', sheet_name='product_table')

# clean the column names for line_sales
line_sales.columns = [c.replace(" ", "_") for c in line_sales.columns]

#==============================================================================================================================================================
d_customer.head()
line_sales.head()
product_table.head()

#==============================================================================================================================================================
# 1. Write code to provide a list of clients that purchased the brand 'king' and have an email address
prod_info = pd.merge(line_sales, product_table, how='left', left_on='product_key', right_on='product_key')
total_tab = pd.merge(prod_info, d_customer, how='left', left_on='customer_id', right_on='customer_id')

total_tab = total_tab[total_tab.brand == 'king']
total_tab = total_tab[total_tab['email_address'].notnull()]

print(total_tab[['customer_id', 'email_address']])

#==============================================================================================================================================================
# 2. Write code to provide three lists
# A. One list of distinct clients that purchased from only the online channel and not the store channel
online_only = line_sales.loc[line_sales['purchase_channel'] == 'online', ['customer_id']]
online_only = online_only.customer_id.tolist()

new_table = line_sales[line_sales['customer_id'].isin(online_only)]
new_table = new_table.groupby(['customer_id']).nunique()
new_table = new_table[new_table['purchase_channel'] == 1]

for i in range(len(new_table)): 
    print("Customer ID: ", new_table.index[i])

# B. One list of distinct clients that purchase from only the store channel and not online
store_only = line_sales.loc[line_sales['purchase_channel'] == 'store', ['customer_id']]
store_only = store_only.customer_id.tolist()

new_table = line_sales[line_sales['customer_id'].isin(store_only)]
new_table = new_table.groupby(['customer_id']).nunique()
new_table = new_table[new_table['purchase_channel'] == 1]

for i in range(len(new_table)): 
    print("Customer ID: ", new_table.index[i])

# C. One list of distinct clients that purchased from both the online and store channel
store_only = line_sales.loc[line_sales['purchase_channel'] == 'store', ['customer_id']]
store_only = store_only.customer_id.tolist()

new_table = line_sales[line_sales['customer_id'].isin(store_only)]
new_table = new_table.groupby(['customer_id']).nunique()
new_table = new_table[new_table['purchase_channel'] == 2]

for i in range(len(new_table)): 
    print("Customer ID: ", new_table.index[i])

#==============================================================================================================================================================
# 3. Write code to provide the count of distinct clients, total orders, total sales, and average purchase by purchase channel
prod_info = pd.merge(line_sales, product_table, how='left', left_on='product_key', right_on='product_key')
total_tab = pd.merge(prod_info, d_customer, how='left', left_on='customer_id', right_on='customer_id')

total_tab.groupby('purchase_channel') \
    .agg({'customer_id': 'nunique', 'order_number': 'nunique', 'total_amt': 'sum', 'total_amt': 'mean'}).reset_index()


total_tab.groupby('purchase_channel') \
    .agg(
        customer_cnt=('customer_id', 'sum')
    )

#==============================================================================================================================================================
# 4. Write code to provide a list of distinct clients that have an email address, signed up for email after 01/01/2010, and purchased tops after 3/10/2010



#==============================================================================================================================================================
# 5. Write code to provide a list of each email address and each email addresses total sales
