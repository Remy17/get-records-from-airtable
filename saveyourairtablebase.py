import json
import os
from airtable import Airtable
import config as cfg

if __name__ == "__main__":

    # get your airtable instance
    airtable = Airtable(cfg.baseKey, cfg.table_name, cfg.apiKey)

    # get record from a certain view
    records = airtable.get_all(view = cfg.view, maxRecords = 100)

    if not os.path.isdir('records') :
        os.mkdir("records", 0o755 )

    for record in records :

        # get fields from record
        fields = record['fields']

        # save them in a file
        with open('./records/record_' + record['id'] + '.json', 'w') as outfile:
            json.dump(fields, outfile)
