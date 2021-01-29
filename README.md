# Cards_CDB

This script generates nicely-formatted card descriptions for [ProjectIgnis/EDOPro](https://github.com/ProjectIgnis/EDOPro). 

It downloads the latest card database from the [ProjectIgnis/DeltaUtopia](https://github.com/ProjectIgnis/DeltaUtopia) repository and modifies the card descriptions in the database. The modified descriptions can then be installed as a language in EDOPro. 

## Build
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python prettify_desc.py
```

## Install as a language
1. Copy the `Cards_CDB` folder into your `ProjectIgnis/config/languages` folder
2. In EDOPro, change the language to `Cards_CDB`

<img src="https://user-images.githubusercontent.com/14916525/106236061-12b3e680-61ca-11eb-8615-a364e29355dc.PNG" width="50%" height="50%"/> <img src="https://user-images.githubusercontent.com/14916525/106236064-147daa00-61ca-11eb-87e6-90c24510de14.PNG" width="50%" height="50%"/>
