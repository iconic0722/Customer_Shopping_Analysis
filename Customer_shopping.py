# import pandas as pd
# import numpy as np

# df = pd.read_csv(r"C:\Users\verma\Downloads\customer_shopping_behavior_large.csv")
# print(df.head(10))

# print(df.info())
# print(df.describe())

# # Checking Null Value
# print(df.isnull().sum())
# # If we have missing value we use this method ex. we have missing of review rating
# # df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))

# df.columns = df.columns.str.lower()
# df.columns = df.columns.str.replace(" ","_")
# print(df)

# # Create a column age_group
# labels = ['Young Adult', 'Adult', 'Middle Age', 'Senior']
# df["age_group"] = pd.qcut(df["age"],q=4,labels=labels)

# print(df[["age","age_group"]].head(10))

# # Create column purchase_frequency_days
# frequency_mapping = {
#     "Fortnightly" :14,
#     "Weekly" : 7,
#     "Monthly" : 30,
#     "Quarterly" : 90,
#     "Bi-Weekly" : 14,
#     "Annually": 365,
#     "Every Three Months" : 90
# }

# df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)
# print(df.columns)

# print(df[['discount_applied', 'promo_code_used']].head(10))


# from sqlalchemy import create_engine, text

# engine = create_engine("mysql+pymysql://root:Bhavek22%40@localhost:3306/shopping_db")

# try:
#     with engine.connect() as conn:
#         conn.execute(text("SELECT 1"))
#     print("Connection successful!")
# except Exception as e:
#     print(f"Connection failed: {e}")

# import pandas as pd
# import numpy as np
# from sqlalchemy import create_engine, text

# df = pd.read_csv(r"C:\Users\verma\Downloads\customer_shopping_behavior_large.csv")

# # Clean column names
# df.columns = df.columns.str.lower().str.replace(" ", "_")

# # Age group
# labels = ['Young Adult', 'Adult', 'Middle Age', 'Senior']
# df["age_group"] = pd.qcut(df["age"], q=4, labels=labels)
# df["age_group"] = df["age_group"].astype(str)  # convert categorical for MySQL

# # Purchase frequency days
# frequency_mapping = {
#     "Fortnightly": 14, "Weekly": 7, "Monthly": 30,
#     "Quarterly": 90, "Bi-Weekly": 14, "Annually": 365,
#     "Every Three Months": 90
# }
# df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

# # Export to MySQL
# engine = create_engine("mysql+pymysql://root:Bhavek22%40@localhost:3306/shopping_db")

# df.to_sql(
#     name="customer_shopping",
#     con=engine,
#     if_exists="replace",
#     index=False
# )

# print(f"✓ {len(df)} rows exported to MySQL table 'customer_shopping'")
# print(f"✓ {len(df.columns)} columns: {list(df.columns)}")

import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://root:Bhavek22%40@localhost:3306/shopping_db")

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# Load Data
df = pd.read_csv(r"C:\Users\verma\Downloads\customer_shopping_behavior_large.csv")

print(df.head(10))
print(df.info())
print(df.describe())

# Check Null Values 
print(df.isnull().sum())
# If we have missing value we use this method ex. we have missing of review rating
# df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))

# Clean Column Names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
print(df)

# Create age_group Column
labels = ['Young Adult', 'Adult', 'Middle Age', 'Senior']
df["age_group"] = pd.qcut(df["age"], q=4, labels=labels)
df["age_group"] = df["age_group"].astype(str)  # required for MySQL

print(df[["age", "age_group"]].head(10))

# Create purchase_frequency_days Column
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every Three Months": 90
}

df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)
print(df.columns)

print(df[['discount_applied', 'promo_code_used']].head(10))


df.to_sql(
    name="customer_shopping",
    con=engine,
    if_exists="replace",
    index=False
)

print(f"✓ {len(df)} rows exported to MySQL table 'customer_shopping'")
print(f"✓ {len(df.columns)} columns: {list(df.columns)}")