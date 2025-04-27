import sqlite3

con = sqlite3.connect('testleaf.db')
print("DB opened")
#
# con.execute('''CREATE TABLE leaf_db(NAME,USERNAME,EMAIL,PASSWORD)''')
# print("Table Created")

con.execute('''INSERT INTO 
leaf_db(NAME,USERNAME,EMAIL,PASSWORD) 
VALUES 
("Guru","Guru Prasad","gurursprasad@gmail.com","9940401362")''')
con.commit()
print("Values inserted and committed")

data = con.execute('''Select * from leaf_db''')
for i in data:
    print(i)
print("Read all data in a DB")

con.execute('''UPDATE leaf_db Set name = "Guru Prasad" where NAME = "Guru"''')
con.commit()
print("DB updated")

# con.execute('''DELETE FROM leaf_db WHERE name = "Guru Prasad"''')
# con.commit()
# print("Deleted")

con.close()
print("Database closed")
