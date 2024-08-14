from vanna.remote import VannaDefault
import pandas as pd
from llamadas import setup_vanna, create_connection

#-----------------------------------------------------
# Entrenamos el modelo de Vanna pasandole toda la BBDD
#-----------------------------------------------------
db_name="SAWDB"
db_server="LMRP"
db_user='sa'
db_password=''

vn = setup_vanna()
conn = create_connection(db_name, db_server, db_user)

sql = ""
sentencias = []

tables_query = """
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
ORDER BY TABLE_NAME, ORDINAL_POSITION
"""

tables_metadata = pd.read_sql(tables_query, conn)
i = ""
for index, row in tables_metadata.iterrows():
    if i !=  row['TABLE_NAME']:
        if sql != "":
            sql = sql + ")"
            sentencias.append(sql)

        sql = f"CREATE TABLE {row['TABLE_NAME']} ( {row['COLUMN_NAME']} {row['DATA_TYPE']}, "
        i = row['TABLE_NAME']
    else:
        sql = sql + f",{row['COLUMN_NAME']} {row['DATA_TYPE']}"

for i in sentencias:
    vn.train(ddl=i)
