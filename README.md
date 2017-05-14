# Shici

## Overview

Shici is a scrapy-based crawler that can get all the dynasties, poets, poems, content and save them in the mongodb database and json files.

## Requirements

- Scrapy 1.3.3 
- Mongodb 3.4.3
- Python 3.6.1
- python-pymongo 3.4.0-2

## Usage

```bash
wget https://github.com/yuanjuntele/shici/archive/master.zip
unzip master.zip
cd shici-master/
rm home.json
scrapy crawl home -o home.json
```
