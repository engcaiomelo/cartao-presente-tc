import os
import psycopg2
import pandas as pd



db = psycopg2.connect(
    host = "ec2-54-235-192-146.compute-1.amazonaws.com",
    database = "datt05cqvmsqah",
    user = "trqhsigntgkcrq",
    password = "31a7209a91c1bc6905eae1ffa6b21ba9c8f1ef3f1ad7b1e8735b257d046b3e72",

)
df = pd.read_sql_query('Select * from CartaoPresente', db)
print(df)