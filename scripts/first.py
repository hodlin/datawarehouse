import pandas as pd
from matplotlib import pyplot as plt
# from datetime_parser import date_parser, time_parser


# with open('../data/tra!!!.csv') as raw_data:
#     header = raw_data.readline().split(sep=',')
#     header = [string.replace('\"', '') for string in header][1:]
#     # header = ';'.join(header)
#     print(header)

# with open('../data/new_data.csv', 'w', newline='\n') as output:
#     output.write(header)

data = pd.read_csv('../data/transformed_dec.csv', sep=',')

print(data)

plt.figure(1)
plt.subplot(1, 2, 1)
plt.hist(data['Startzeit'], bins=24, range=(0, 24), color='green')
plt.title('Startzeit')
plt.xlabel('Time, h')
plt.ylabel('Number of observation')
x1, x2, y1, y2 = plt.axis()
plt.axis((0, 24, y1, y2))

plt.subplot(1, 2, 2)
plt.hist(data['Endzeit'], bins=24, range=(0, 24), color='red')
plt.title('Endzeit')
plt.xlabel('Time, h')
plt.ylabel('Number of observations')
x1, x2, y1, y2 = plt.axis()
plt.axis((0, 24, y1, y2))

plt.show()

# data.to_csv('data/normal_time.csv')
# print(data.shape)

