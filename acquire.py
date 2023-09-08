from env import user, host, password
import pandas as pd
import numpy as np
import os
from env import user, host, password, create_url

from sklearn.model_selection import train_test_split

def get_zillow_data(db,
        user=user,
        password=password,
        host=host):
    '''
    This function acquires zillow.csv if it is available,
    otherwise, it makes the SQL connection and uses the query provided
    to read in the dataframe from SQL.
    If the csv is not present, it will write one.
    '''
    filename = "zillow.csv"

    if os.path.isfile(filename):

        return pd.read_csv(filename, index_col=0)
    else:
        # Create the url
        url = f"mysql+pymysql://{user}:{password}@{host}/{db}"
        sql_query = '''
            SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
            FROM properties_2017
            WHERE propertylandusetypeid = 261'''

        # Read the SQL query into a dataframe
        df = pd.read_sql(sql_query, url)

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df

def prep_zillow(df):
    '''
    This function takes in a dataframe and
    renames the columns and drops null values.
    Additionally, it changes datatypes for appropriate columns
    and renames fips to actual county names.
    Then returns a cleaned dataframe
    '''
    df = df.rename(columns = {'bedroomcnt':'bedrooms',
                     'bathroomcnt':'bathrooms',
                     'calculatedfinishedsquarefeet':'area',
                     'taxvaluedollarcnt':'taxvalue',
                     'fips':'county'})
    
    df = df.dropna()
    
    make_ints = ['bedrooms','area','taxvalue','yearbuilt']

    for col in make_ints:
        df[col] = df[col].astype(int)
        
    df.county = df.county.map({6037:'LA',6059:'Orange',6111:'Ventura'})
    
    df['county_encoded'] = df.county.map({'LA': 1, 'Orange': 2, 'Ventura': 3})

    return df

def train_val_test(df):
    train_val, test = train_test_split(df,
                                  random_state=1349,
                                  train_size=0.8)
    train, validate = train_test_split(train_val,
                                  random_state=1349,
                                  train_size=0.7)
    return train, validate, test

def get_model(db,
        user=user,
        password=password,
        host=host):
    '''
    This function acquires the average log error of the model in predictions_2017
    and turns it into a dataframe
    '''
    filename = "zillow_model.csv"

    if os.path.isfile(filename):

        return pd.read_csv(filename, index_col=0)
    else:
        # Create the url
        url = f"mysql+pymysql://{user}:{password}@{host}/{db}"
        sql_query = '''select avg(logerror) from predictions_2017;'''

        # Read the SQL query into a dataframe
        df = pd.read_sql(sql_query, url)

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df