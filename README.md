# Habitat Energy Backend Challenge

Habitat Energy submit their batteries into a frequency service called dynamic
containment each day. The service operates as an auction where you submit your price
and you find out if you are accepted or not.

This application reads the auction result (via [the API](https://data.nationalgrideso.com/api-guidance)) and saves Habitat's current day's result to a local database.

## Run it
```shell
pip install -r requirements.txt
python main.py
```

## What's Happening

_[main.py](main.py)_ is the entry point of the application. It will call retrieve the API's data using the functions in the _[eso_calls](eso_calls.py)_ module, and save it to a sqlite3 database with the _[datastore](datastore.py)_ module.

## Next Steps

Steps I'd take to increase the robustness of the application:

* Write unit tests
* Implement Exception Handling
