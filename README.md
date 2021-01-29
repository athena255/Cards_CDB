# Cards_CDB

This script generates nicely-formatted card descriptions for EDOPro. 

It downloads the latest card database from the ProjectIgnis/DeltaUtopia repository and modifies the card descriptions in the database. The generated folder can then be installed as a 'language' in EDOPro. 

## Build
```
python3 -m venv venv
pip install -r requirements.txt
python prettify_desc.py
```

## Install as a language
Copy the generated folder into your `ProjectIgnis/config/languages` folder
