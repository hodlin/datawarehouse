import re
from datetime_parser import to_decimal_time, to_date, to_timedelta

with open('../data/short.csv', 'r') as input:
    line = input.readline()
    with open('../data/transformed_dec.csv', 'w') as output:
        line = line[3:]
        line = line.replace('\"', '')
        output.write(line)
        for line in input:
            # line = line[:-1]
            line = line.replace('\"', '')
            line = line.split(sep=',')
            del line[0]
            line[1] = to_date(line[1])
            line[2] = to_date(line[2])
            line[3] = to_decimal_time(line[3])
            line[4] = to_decimal_time(line[4])
            line[5] = line[5]
            output.write(','.join(map(str, line)))

