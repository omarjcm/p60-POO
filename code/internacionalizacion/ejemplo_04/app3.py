import datetime
import dateutil.parser

format = '%Y-%m-%dT%H:%M:%S%z'
date_to_parse = '2021-07-21T20:40:21-06:00'
dt = dateutil.parser.parse(date_to_parse)
print(dt)

