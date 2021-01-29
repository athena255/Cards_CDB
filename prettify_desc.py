# prettify_desc.py

# Downloads the cards database (cards.cdb) from ProjectIgnis
# Modifies the downloaded cards.cdb to make the card descriptions readable:
#   Inserts a blank line (2 newlines) after each sentence
#   Inserts a newline followed by an indent after a semicolon, colon, or an independent clause
# Creates the modified cards.cdb in the current directory

import os, re, sqlite3, requests

OUTPUT_DIR = 'Cards_CDB'

CARDS_CDB_URL = 'https://github.com/ProjectIgnis/DeltaUtopia/raw/master/cards.cdb'

# Pattern that matches a new sentence
pat_newsent = re.compile(r'(\w{2,}\S?\. )(\S?[A-Z])')
# Pattern that matches a semi-colon or colon
pat_semi = re.compile(r'(\S[;:] )(\S)')
# Pattern that matches ', ' + and/then
pat_linking = re.compile(r'(\w+ \w+, )(then|and)')

BLANK_LINE = r'\1\r\n\r\n\2'
NEWLINE_INDENT = r'\1\r\n    \2'

# Download the database
r = requests.get(CARDS_CDB_URL)
try:
    os.makedirs(OUTPUT_DIR)
except FileExistsError:
    pass

with open(f'{OUTPUT_DIR}/cards.cdb', 'wb') as f:
    f.write(r.content)

# Connect to the database
conn = sqlite3.connect(f'{OUTPUT_DIR}/cards.cdb')
c = conn.cursor()

# Retrieve all the descriptions of the cards
c.execute("SELECT id, desc FROM texts;")
texts = c.fetchall()

for i, desc in texts:
    new_desc = pat_newsent.sub(BLANK_LINE, desc)
    new_desc = pat_semi.sub(NEWLINE_INDENT, new_desc)
    new_desc = pat_linking.sub(NEWLINE_INDENT, new_desc)

    # Update the card entry
    c.execute("UPDATE texts SET desc =? WHERE id =?", (new_desc, i))

# Write the changes to the database
conn.commit()
conn.close()
