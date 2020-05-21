import psycopg2
import pandas as pd

#First
try:
	conn = psycopg2.connect(
	database = 'auction',
	user = 'postgres',
	host = 'localhost'
	)
	answer1 = "Database opened successfully"
except Exception as e:
	raise e

# print(answer1)

cur = conn.cursor()

#Second
def read_data_to_dataframe(table):
	return pd.read_sql_query(r'SELECT * FROM {}'.format(table), conn)

answer2 = read_data_to_dataframe('item_information')
# print(answer2.head())

#Third
def query_sql(column, table):
	query = r'SELECT {} FROM {}'.format(column, table)
	cur.execute(query)
	rows = cur.fetchall()
	print(column)
	for row in rows:
		print(row[0])

# answer3 = query_sql('start_price', 'item_information')

#Fourth
def query_dataframe(df, column):
	return df[column]

answer4 = query_dataframe(answer2, 'start_price')
# print(answer4)

#Fifth
def analysis(df):
	print(df.info())
	print(df.describe())

analysis(answer2)

# Sixth

# Insert data
def insert_data(table, name, bday, city, number):
	cur.execute('''INSERT INTO {}(fullName, bday, address, telephoneNumber)
	 VALUES({}, {}, {}, {});'''.format(
	 	table, name, bday, city, number))
conn.commit()

