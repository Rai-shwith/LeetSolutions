import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({"quantity":0},inplace=True) #  fill missing values in 'quantity' column with 0 inplace = True  means that the changes are made directly to the original DataFrame
    return products

