
# load packages
import pandas as pd 

#==============================================================================================================================================================
# Load the data
d_customer = pd.read_excel('./data/tables.xlsx', sheet_name='d_customer')

line_sales = pd.read_excel('./data/tables.xlsx', sheet_name='line_sales')

product_table = pd.read_excel('./data/tables.xlsx', sheet_name='product_table')

# clean up the column names for line_sales. Replacing spaces with underscores
line_sales.columns = [c.replace(" ", "_") for c in line_sales.columns]

#==============================================================================================================================================================
# Check the structure of the data
d_customer.head()
d_customer.dtypes

line_sales.head()
line_sales.dtypes

product_table.head()
product_table.dtypes

#==============================================================================================================================================================
# 1. Write code to provide a list of clients that purchased the brand 'king' and have an email address

# lets define a function to join our three data sets together
def joined_data(sales_data, product_data, customer_data):
    '''
    Joins are three data sets together
    '''
    prod_info = pd.merge(sales_data, product_data, how='left', left_on='product_key', right_on='product_key')
    return pd.merge(prod_info, customer_data, how='left', left_on='customer_id', right_on='customer_id')

total_tab = joined_data(sales_data=line_sales, product_data=product_table, customer_data=d_customer)

total_tab = total_tab[total_tab.brand == 'king'] # filter to brand 'king'
total_tab = total_tab[total_tab['email_address'].notnull()] # filter to non NULL values in `email_address`

print(total_tab[['customer_id', 'email_address']]) # print the list

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
        # create a list of customer_id who have a purchase in the designated channel
        channel_data = sales_data.loc[sales_data['purchase_channel'].isin(channel_list), ['customer_id']]
        l = channel_data.customer_id.tolist()
        # filter the data based on our list `l`
        channel_data = sales_data[sales_data['customer_id'].isin(l)]
        # group by customer_id and use nunique to get a unique cnt 
        channel_data = channel_data.groupby(['customer_id']).nunique()
        # filter the data based on the unique cnt in column purchase_channel and the designated channel_cnt
        channel_data = channel_data[channel_data['purchase_channel'] == channel_cnt]
        # set up an empty list to store our output from the for loop
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
total_tab = joined_data(sales_data=line_sales, product_data=product_table, customer_data=d_customer)

(total_tab.groupby('purchase_channel').
    agg({'customer_id': 'nunique', 'order_number':'nunique', 'total_amt': ['sum', 'mean']})
)


#==============================================================================================================================================================
# 4. Write code to provide a list of distinct clients that have an email address, signed up for email after 01/01/2010, and purchased tops after 3/10/2010
total_tab = joined_data(sales_data=line_sales, product_data=product_table, customer_data=d_customer)

import datetime as dt
total_tab.set_index('signup_date') # set my index as the `signup_date` for easy filtering

dt_filter = dt.datetime(2010, 1, 1)
total_tab[:dt_filter]




#==============================================================================================================================================================
# 5. Write code to provide a list of each email address and each email addresses total sales
