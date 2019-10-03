import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle

df = pd.read_csv('tmppj4rb047.csv')

harassment = df[df.OFFENSE_CODE_GROUP.str.contains("Harassment")]
criminal_harassment= df[df.OFFENSE_CODE_GROUP.str.contains("Criminal Harassment")]
simple_assault = df[df.OFFENSE_CODE_GROUP.str.contains("Simple Assault")]
aggravated_assault = df[df.OFFENSE_CODE_GROUP.str.contains("Aggravated Assault")]

all_crimes = harassment
all_crimes.append(criminal_harassment)
all_crimes.append(simple_assault)
all_crimes.append(aggravated_assault)

all_crimes = all_crimes.drop(['OFFENSE_CODE', 'OFFENSE_DESCRIPTION', 'DISTRICT', 'REPORTING_AREA', 'SHOOTING', 'OCCURRED_ON_DATE', 'YEAR', 'MONTH', 'UCR_PART', 'STREET', 'Location'], axis=1)

all_crimes = all_crimes.dropna()

all_crimes = all_crimes[all_crimes.Long < -10]
all_crimes = all_crimes[all_crimes.Lat > 10]

print("All crimes: " + str(all_crimes.size))
print(all_crimes)

#all_crimes.plot(kind='scatter', x='Long', y='Lat', color='red')
#plt.show()

crime_locations = all_crimes.drop(['INCIDENT_NUMBER', 'OFFENSE_CODE_GROUP', 'DAY_OF_WEEK'], axis=1)

print("crime locations")
print(crime_locations)

#all_crimes = all_crimes[]

crime_locations_at_0 = crime_locations[crime_locations.HOUR == 0]

#crime_locations_at_0 = crime_locations_at_0.drop(['INCIDENT_NUMBER', 'OFFENSE_CODE_GROUP', 'DAY_OF_WEEK', 'HOUR'], axis=1).to_numpy()

crime_locations_at_0 = crime_locations_at_0.drop(['HOUR'], axis=1).to_numpy()

print("crime locations at 0")
print(crime_locations_at_0)

#for location in crime_locations:
#    crime_locations_time.append(location[])


#B= np.split(A, np.where(A[:, 0]== 0.)[0][1:])

#print(crime_locations)

bandwidth = estimate_bandwidth(crime_locations_at_0, quantile=0.02, n_samples=500)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(crime_locations_at_0)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    #plt.plot(crime_locations_at_0[my_members, 0], crime_locations_at_0[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], col + 'x')#, markerfacecolor=col, markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()