import json
import os, sys
from airtable import Airtable

if __name__ == "__main__":

    _baseKey = "appXXXXX"
    _table_name = "YYYYY"
    _apiKey = "apiZZZZZ"
    _view = "Grid view"

    # get your airtable instance
    #airtable = Airtable( basekey = _baseKey, table_name = _table_name, api_key = _apiKey)
    airtable = Airtable('appS4HDhbgxbzOXco', 'Quiz', api_key = 'keyTv9YoTufkmEn6e')

    # get record from a certain view
    records = airtable.get_all(view = _view, maxRecords = 100)

    if not os.path.isdir('records') :
        os.mkdir( "records", 0o755 )

    for record in records :

        # get fields from record
        fields = record['fields']

        with open('./records/record_' + record['id'] + '.json', 'w') as outfile:
            json.dump(fields, outfile)

        #airtable.update(record['id'], {'URL Typeform' : data['_links']['display']})