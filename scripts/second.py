import re
from datetime_parser import to_decimal_time, to_date, to_timedelta, to_seconds, to_datetime

HEADER = ('Jobname', 'Startdatetime', 'Enddatetime', 'Starttime', 'Endtime', 'Jobduration (s)')

with open('../data/short.csv', 'r') as input:
    input.readline()
    with open('../data/transformed_dec_duration.csv', 'w') as output:
        output.write(','.join(HEADER)+'\n')
        for line in input:
            # line = line[:-1]
            line = line.replace('\"', '')
            line = line.split(sep=',')
            del line[0]
            line[1] = to_datetime(line[1], line[3])
            line[2] = to_datetime(line[2], line[4])
            line[3] = to_decimal_time(line[3])
            line[4] = to_decimal_time(line[4])
            line[5] = (line[2] - line[1]).seconds
            output.write(','.join(map(str, line))+'\n')
            # break
