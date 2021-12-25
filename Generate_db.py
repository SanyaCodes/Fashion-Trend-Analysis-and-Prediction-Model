import random
import sqlite3
import csv

att_list = ['id','above-the-hip (length)',
'hip (length)',
'micro (length)',
'mini (length)',
'above-the-knee (length)',
'knee (length)',
'below the knee (length)',
'midi',
'maxi (length)',
'floor (length)',
'single breasted',
'double breasted',
'lace up',
'wrapping',
'zip-up',
'fly (opening)',
'buckled (opening)',
'toggled (opening)',
'no opening',
'asymmetrical',
'symmetrical',
'peplum',
'circle',
'flare',
'fit and flare',
'trumpet',
'mermaid',
'balloon',
'bell',
'bell bottom',
'bootcut',
'peg',
'pencil',
'straight',
'a-line',
'tent',
'baggy',
'wide leg',
'high low',
'curved (fit)',
'tight (fit)',
'regular (fit)',
'loose (fit)',
'oversized',
'burnout',
'distressed',
'washed',
'embossed',
'frayed',
'printed',
'ruched',
'quilted',
'pleat',
'gathering',
'smocking',
'tiered',
'cutout',
'slit',
'perforated',
'lining',
'no special manufacturing technique',
'plain (pattern)',
'abstract',
'cartoon',
'letters, numbers',
'camouflage',
'check',
'dot',
'fair isle',
'floral',
'geometric',
'paisley',
'stripe',
'houndstooth (pattern)',
'herringbone (pattern)',
'chevron',
'argyle',
'leopard',
'snakeskin (pattern)',
'cheetah',
'peacock',
'zebra',
'giraffe',
'toile de jouy',
'plant',
'empire waistline',
'dropped waistline',
'high waist',
'normal waist',
'low waist',
'basque (wasitline)',
'no waistline']


#Setting up data
ids = []
with open('db_csv/img_id.csv', newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		ids.append(row[0])

atts = []
with open('db_csv/attributes.csv', newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		atts.append(row)
		# print(', '.join(row))
# print(atts)

no_of_ids = len(ids)

for i in range(no_of_ids):
	id = ids[i][0:8] + " " + ".jpg"
	print(id)
	atts[i].insert(0, ids[i])

print(atts)

#Database connection
conn = sqlite3.connect('/Users/prashantvaidya/Desktop/Myntra_web/myntra.db')
print("Database opened successfully")

def Create_table(table):
	conn.execute(f"CREATE TABLE IF NOT EXISTS {table}(id TEXT)")
	print("Table Created")

def add_column(table, column):
	try:
		conn.execute(f"ALTER TABLE {table} ADD {column} VARCHAR(100)")
		print("Column Added")
	except:
		print("Column Exists")

def insert(table, value):
	# try:
	conn.execute(f"INSERT INTO {table}(id) VALUES('{value}')")
	print("Value inserted")
	# except:
	# 	print("Value not inserted")

def update_column(table, column, value):
	try:
		conn.execute(f"UPDATE {table} SET {column} = {value}")
		print("Column updated")
	except:
		print("Column not updated")



#Attribute Table
def clean_up(att):
	att = att.replace(" ","_")
	att = att.replace(")","")
	att = att.replace("(","")
	att = att.replace("-","_")
	return att

Create_table('attributes')

for att in att_list:
	add_column('attributes', clean_up(att))

for apparel in atts:
	#check for id insert
	flag = False
	for att in apparel:
		if not flag:
			insert('attributes', att)
			flag = True
		else:
			update_column('attributes', clean_up(att), 1)

conn.commit()
print("Attribute database created successfully")
conn.close()

"""
	COLORS
"""
conn = sqlite3.connect('/Users/prashantvaidya/Desktop/Myntra_web/myntra.db')
print("Database opened successfully")
#Setting up data for colors
color_list = ['aqua', 'black', 'blue', 'fuchsia', 'green', 'gray', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow', 'brown', 'pink', 'plum']

colors = []
with open('db_csv/colors.csv', newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		colors.append(row)

no_of_ids = len(ids)

print(len(colors), len(ids))

for i in range(no_of_ids):
	colors[i].insert(0, ids[i])
print(colors)

Create_table('colors')

for color in color_list:
	add_column("colors", color)


for apparel in colors:
	#check for id insert
	flag = False
	for color in apparel:
		if (color == '1'):
			break;
		if not flag:
			insert('colors', color)
			flag = True
		else:
			update_column('colors', color, 1)


conn.commit()
print("Colors database created successfully")
conn.close()



