# prettify_desc.py

# Require: DeltaUtopia repo must be cloned in this directory
# Modifies the downloaded every .cdb to make the card descriptions readable:
#   Inserts a blank line (2 newlines) after each sentence
#   Inserts a newline followed by an indent after a semicolon, colon, or an independent clause

import os, re, sqlite3

UTOPIA_URL = 'https://github.com/ProjectIgnis/DeltaUtopia.git'
UTOPIA_DIR = 'DeltaUtopia'
# Pattern that matches a new sentence
pat_newsent = re.compile(r'(\w{2,}\S?\.\S? ?)(\S+ \S+ \S+)')
# Pattern that matches a semi-colon or colon
pat_semi = re.compile(r'( \S+ \S+[;:]\s?)(\S+ \S+ )')
# Pattern that matches ', ' + and/then
pat_linking = re.compile(r'(\w+ \S+,\s?)((?:then|and|also|or) \S+ \S+ \S+ \S+)')

BLANK_LINE = r'\1\r\n\r\n\2'
NEWLINE_INDENT = r'\1\r\n    \2'

def modify_desc(cdb_path):
    # Connect to the database
    conn = sqlite3.connect(cdb_path)
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

def main():
    os.system(f"rm -rf {UTOPIA_DIR}")
    os.system(f"git clone {UTOPIA_URL} {UTOPIA_DIR}")
    for entry in os.scandir(UTOPIA_DIR):
        if entry.path.endswith(".cdb") and entry.is_file():
            print(f"[+] Modifying {entry.path}")
            modify_desc(entry.path)
        else:
            print(f"[-] Removing {entry.path}")
            os.system(f"rm -rf {entry.path}")

main()