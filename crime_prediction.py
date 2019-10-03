import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle

df = pd.read_csv('tmppj4rb047.csv')

harassment = df[df.OFFENSE_CODE_GROUP.str.contains("Harassment")]
criminal_harassment = df[df.OFFENSE_CODE_GROUP.str.contains("Criminal Harassment")]
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

crime_locations = all_crimes.drop(['INCIDENT_NUMBER', 'OFFENSE_CODE_GROUP', 'DAY_OF_WEEK'], axis=1)

print("crime locations")
print(crime_locations)

crime_locations_at_0 = crime_locations[crime_locations.HOUR == 0].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_1 = crime_locations[crime_locations.HOUR == 1].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_2 = crime_locations[crime_locations.HOUR == 2].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_3 = crime_locations[crime_locations.HOUR == 3].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_4 = crime_locations[crime_locations.HOUR == 4].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_5 = crime_locations[crime_locations.HOUR == 5].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_6 = crime_locations[crime_locations.HOUR == 6].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_7 = crime_locations[crime_locations.HOUR == 7].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_8 = crime_locations[crime_locations.HOUR == 8].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_9 = crime_locations[crime_locations.HOUR == 9].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_10 = crime_locations[crime_locations.HOUR == 10].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_11 = crime_locations[crime_locations.HOUR == 11].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_12 = crime_locations[crime_locations.HOUR == 12].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_13 = crime_locations[crime_locations.HOUR == 13].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_14 = crime_locations[crime_locations.HOUR == 14].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_15 = crime_locations[crime_locations.HOUR == 15].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_16 = crime_locations[crime_locations.HOUR == 16].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_17 = crime_locations[crime_locations.HOUR == 17].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_18 = crime_locations[crime_locations.HOUR == 18].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_19 = crime_locations[crime_locations.HOUR == 19].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_20 = crime_locations[crime_locations.HOUR == 20].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_21 = crime_locations[crime_locations.HOUR == 21].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_22 = crime_locations[crime_locations.HOUR == 22].drop(['HOUR'], axis=1).to_numpy()
crime_locations_at_23 = crime_locations[crime_locations.HOUR == 23].drop(['HOUR'], axis=1).to_numpy()

def create_cluster_center_files(crime_locations_at, hour):
    bandwidth = 0.007

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(crime_locations_at)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    filename = "cluster_centers_h" + hour + ".txt"
    f = open(filename, "w+")
    f.write(str(cluster_centers))
    f.close()

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)

    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(crime_locations_at[my_members, 0], crime_locations_at[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], col + 'x')
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


create_cluster_center_files(crime_locations_at_0, "0")
create_cluster_center_files(crime_locations_at_1, "1")
create_cluster_center_files(crime_locations_at_2, "2")
create_cluster_center_files(crime_locations_at_3, "3")
create_cluster_center_files(crime_locations_at_4, "4")
create_cluster_center_files(crime_locations_at_5, "5")
create_cluster_center_files(crime_locations_at_6, "6")
create_cluster_center_files(crime_locations_at_7, "7")
create_cluster_center_files(crime_locations_at_8, "8")
create_cluster_center_files(crime_locations_at_9, "9")
create_cluster_center_files(crime_locations_at_10, "10")
create_cluster_center_files(crime_locations_at_11, "11")
create_cluster_center_files(crime_locations_at_12, "12")
create_cluster_center_files(crime_locations_at_13, "13")
create_cluster_center_files(crime_locations_at_14, "14")
create_cluster_center_files(crime_locations_at_15, "15")
create_cluster_center_files(crime_locations_at_16, "16")
create_cluster_center_files(crime_locations_at_17, "17")
create_cluster_center_files(crime_locations_at_18, "18")
create_cluster_center_files(crime_locations_at_19, "19")
create_cluster_center_files(crime_locations_at_20, "20")
create_cluster_center_files(crime_locations_at_21, "21")
create_cluster_center_files(crime_locations_at_22, "22")
create_cluster_center_files(crime_locations_at_23, "23")
