import eso_calls
from datetime import datetime
import datastore

current_date = datetime.now().strftime("%Y-%m-%d")

url_params = {
    "resource_id": 'ddc4afde-d2bd-424d-891c-56ad49c13d1a',
    "filters": {'Company': 'HABITAT ENERGY LIMITED',
                'EFA Date': current_date},
    "limit": 3200
}

results = eso_calls.get_datastore_search(url_params)

print(f'{len(results)} total records returned.')

datastore.create_table()
datastore.load_table(results)


