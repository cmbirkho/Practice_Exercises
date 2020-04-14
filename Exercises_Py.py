
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

# All three of these questions (A, B, C) are similar. Let's define a function to help us answer them
# so we can avoid re-typing the same code over and over again
def three_lists(sales_data, channel_list, channel_cnt):
    """
    Function that returns a list of customer ids
    channel_list requires a list object so we raise an error if it is not a list
    """
    if isinstance(channel_list, list):
        channel_data = sales_data.loc[sales_data['purchase_channel'].isin(channel_list), ['customer_id']]
        l = channel_data.customer_id.tolist()
        channel_data = sales_data[sales_data['customer_id'].isin(l)]
        channel_data = channel_data.groupby(['customer_id']).nunique()
        channel_data = channel_data[channel_data['purchase_channel'] == channel_cnt]
        cust_id_list = []
        for cust_id in range(len(channel_data)):
            cust_id_list.append(channel_data.index[cust_id])
        return cust_id_list
    else:
        raise TypeError("Expected channel_list to be a list")

# A. One list of distinct clients that purchased from only the online channel and not the store channel
three_lists(line_sales, ['online'], 1)

# B. One list of distinct clients that purchase from only the store channel and not online
three_lists(line_sales, ['store'], 1)

# C. One list of distinct clients that purchased from both the online and store channel
three_lists(line_sales, ['store', 'online'], 2)

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
