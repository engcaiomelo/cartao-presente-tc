import os
import psycopg2
import pandas as pd
import numpy as np
import psycopg2.extras as extras
from io import StringIO




db = psycopg2.connect(
    host = "ec2-54-235-192-146.compute-1.amazonaws.com",
    database = "datt05cqvmsqah",
    user = "trqhsigntgkcrq",
    password = "31a7209a91c1bc6905eae1ffa6b21ba9c8f1ef3f1ad7b1e8735b257d046b3e72",

)



df = pd.read_sql_query('Select * from CartaoPresente', db)
#df.to_sql('CartaoPresente', db, index=False, if_exists='replace')
execute_many(db, df, 'cartaopresente')

print(df)

