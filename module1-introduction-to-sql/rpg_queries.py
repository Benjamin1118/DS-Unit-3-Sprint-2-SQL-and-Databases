import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

cur = conn.cursor()


# Question 1 - How many total Characters are there?
query = 'SELECT * FROM charactercreator_character;'
characters = len(cur.execute(query).fetchall())
print('Total characters: ', characters)

# Question 2 - How many of each specific subclass?

query = 'SELECT * FROM charactercreator_mage;'
characters = len(cur.execute(query).fetchall())
print('Total Mage: ', characters)

query = 'SELECT * FROM charactercreator_thief;'
characters = len(cur.execute(query).fetchall())
print('Total Thief: ', characters)

query = 'SELECT * FROM charactercreator_cleric;'
characters = len(cur.execute(query).fetchall())
print('Total Cleric: ', characters)

query = 'SELECT * FROM charactercreator_fighter;'
characters = len(cur.execute(query).fetchall())
print('Total Fighter: ', characters)

# Question 3 - How many total items?
query = 'SELECT * FROM armory_item'
total_items = len(cur.execute(query).fetchall())
print('Total Items: ', total_items)

# Question 4 - How many items are weapons? How many are not?
query = 'SELECT * FROM armory_weapon'
is_weapon = len(cur.execute(query).fetchall())
print('Are weapons', is_weapon)

query = 'SELECT * FROM armory_item'
is_not_weapon = (len(cur.execute(query).fetchall())) - is_weapon
print('Are not weapons: ', is_not_weapon)


#Question 5 - How many Items does each character have? (Return first 20 rows)
query = '''SELECT cc.character_id cid, 
    count(charactercreator_character_inventory.item_id) AS NumOfItems
    FROM charactercreator_character as cc
    LEFT JOIN charactercreator_character_inventory
    ON cid = charactercreator_character_inventory.character_id
    GROUP BY cid
    LIMIT 20;'''
items_per_char = cur.execute(query).fetchall()
print('total items per character: ', items_per_char)

#Question 6 = How many weapons does each character have. (Return first 20 rows)
query = """
        SELECT cc.character_id, COUNT(ci.item_id)
        FROM charactercreator_character as cc, 
        charactercreator_character_inventory as ci,
        armory_item as ai
        WHERE cc.character_id = ci.character_id 
        AND ci.item_id = ai.item_id
        AND ai.item_id IN (SELECT item_ptr_id FROM armory_weapon)
        GROUP BY cc.character_id LIMIT 20;
        """
weapons_per_char = cur.execute(query).fetchall()
print('Total weapons per character:', weapons_per_char)

#question 7 - On average how many items per character
query ='''
SELECT AVG( NumOfItems )
FROM(SELECT cc.character_id cid,
COUNT(charactercreator_character_inventory.item_id)
AS NumOfItems
FROM charactercreator_character as cc
LEFT JOIN charactercreator_character_inventory
on cid = 
charactercreator_character_inventory.character_id
GROUP BY cid)
'''
avg_items_per_char

#Question 8 - On average how many weapons per character