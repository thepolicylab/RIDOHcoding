import csv
from os import remove
import pandas as pd

#Load in Katie dataframe and clean

df = pd.read_csv('Survey7Katie.csv')
    

df.fillna(0, inplace=True)
df.sort_values(by=['Respondent'], inplace=True)
df["why_not_booster_1"] = df["why_not_booster_1"].astype('float64')
df["why_not_booster_2"] = df["why_not_booster_2"].astype('float64')
df["why_not_booster_3"] = df["why_not_booster_3"].astype('float64')
df["why_scientists_reliable_unreliable_1"] = df["why_scientists_reliable_unreliable_1"].astype('float64')
df["why_scientists_reliable_unreliable_2"] = df["why_scientists_reliable_unreliable_2"].astype('float64')
df["why_scientists_reliable_unreliable_3"] = df["why_scientists_reliable_unreliable_3"].astype('float64')
df["why_isolation_change_1"] = df["why_isolation_change_1"].astype('float64')
df["why_isolation_change_2"] = df["why_isolation_change_2"].astype('float64')
df["why_isolation_change_3"] = df["why_isolation_change_3"].astype('float64')


#Load in Muskaan dataframe and clean

df2 = pd.read_csv('MuskaanSurvey7.csv')
    

df2.fillna(0, inplace=True)
df2.sort_values(by=['Respondent'], inplace= True)
df2["why_not_booster_1"] = df2["why_not_booster_1"].astype('float64')
df2["why_not_booster_2"] = df2["why_not_booster_2"].astype('float64')
df2["why_not_booster_3"] = df2["why_not_booster_3"].astype('float64')
df2["why_scientists_reliable_unreliable_1"] = df2["why_scientists_reliable_unreliable_1"].astype('float64')
df2["why_scientists_reliable_unreliable_2"] = df2["why_scientists_reliable_unreliable_2"].astype('float64')
df2["why_scientists_reliable_unreliable_3"] = df2["why_scientists_reliable_unreliable_3"].astype('float64')
df2["why_isolation_change_1"] = df2["why_isolation_change_1"].astype('float64')
df2["why_isolation_change_2"] = df2["why_isolation_change_2"].astype('float64')
df2["why_isolation_change_3"] = df2["why_isolation_change_3"].astype('float64')


#Q1 summary stats

#list of responses for q 1 (a list of lists)
Katie_q1 = []

Muskaan_q1 = []

#loop through Katie dataframe and populate Katie_sorted_ids and Katie_q1
for row in df.itertuples():
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        inner_list = []
        if (row[2] != "__NA__") and (row[3] != 0):
            inner_list.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            inner_list.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            inner_list.append(row[5])
        Katie_q1.append(inner_list)

#loop through Muskaan dataframe and populate Muskaan_sorted_ids and Muskaan_q1
for row in df2.itertuples():
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        inner_list = []
        if (row[2] != "__NA__") and (row[3] != 0):
            inner_list.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            inner_list.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            inner_list.append(row[5])
        Muskaan_q1.append(inner_list)


#Generates counts of a code value for katie code only
def summary_gen_katie(code: int):
    count = 0
    for i in Katie_q1:
        if code in i:
            count += 1
    return count

#dictionary for katie
Katie_count_dict = {}

#loops through all of katie q1 list
for id in range(0, len(Katie_q1)):
    values = Katie_q1[id]
    for value in values:
        if (value not in Katie_count_dict.keys()):
            Katie_count_dict[value] = summary_gen_katie(value)


#Generates frequency for muskaan
def summary_gen_muskaan(code: int):
    count = 0
    for i in Muskaan_q1:
        if code in i:
            count += 1
    return count

#dictionary for muskaan
Muskaan_count_dict = {}

#loops through all of muskaan q1 list
for id in range(0, len(Muskaan_q1)):
    values = Muskaan_q1[id]
    for value in values:
        if (value not in Muskaan_count_dict.keys()):
            Muskaan_count_dict[value] = summary_gen_muskaan(value)

# Q1
combined_dict_mremove = {}
combined_dict_kremove = {}


# stats with katie's values for overlap
for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_mremove[id] = values

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_mremove[id] = values

mremove_freq = {}

for id in combined_dict_mremove:
    values = combined_dict_mremove[id]
    for value in values:
        if (value not in mremove_freq.keys()):
            mremove_freq[value] = 1
        else:
            mremove_freq[value] += 1

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_kremove[id] = values

for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_kremove[id] = values

kremove_freq = {}

for id in combined_dict_kremove:
    values = combined_dict_kremove[id]
    for value in values:
        if (value not in kremove_freq.keys()):
            kremove_freq[value] = 1
        else:
            kremove_freq[value] += 1

#Q2 summary stats

#list of responses for q 1 (a list of lists)
Katie_q2 = []

Muskaan_q2 = []

#loop through Katie dataframe and populate Katie_sorted_ids and Katie_q1
for row in df.itertuples():
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[7] != 0):
            inner_list.append(row[7])
        if (row[8] != 0):
            inner_list.append(row[8])
        if (row[9] != 0):
            inner_list.append(row[9])
        Katie_q2.append(inner_list)

#loop through Muskaan dataframe and populate Muskaan_sorted_ids and Muskaan_q1
for row in df2.itertuples():
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[7] != 0):
            inner_list.append(row[7])
        if (row[8] != 0):
            inner_list.append(row[8])
        if (row[9] != 0):
            inner_list.append(row[9])
        Muskaan_q2.append(inner_list)

def summary_gen_katie_2(code: int):
    count = 0
    for i in Katie_q2:
        if code in i:
            count += 1
    return count

def summary_gen_muskaan_2(code: int):
    count = 0
    for i in Muskaan_q2:
        if code in i:
            count += 1
    return count

Katie_count_dict_2 = {}
Muskaan_count_dict_2 = {}

#loops through all of katie q1 list
for id in range(0, len(Katie_q2)):
    values = Katie_q2[id]
    for value in values:
        if (value not in Katie_count_dict_2.keys()):
            Katie_count_dict_2[value] = summary_gen_katie_2(value)

#loops through all of muskaan q1 list
for id in range(0, len(Muskaan_q2)):
    values = Muskaan_q2[id]
    for value in values:
        if (value not in Muskaan_count_dict_2.keys()):
            Muskaan_count_dict_2[value] = summary_gen_muskaan_2(value)

# Q1
combined_dict_mremove_2 = {}
combined_dict_kremove_2 = {}

# stats with katie's values for overlap
for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        if (row[7] != 0):
            values.append(row[7])
        if (row[8] != 0):
            values.append(row[8])
        if (row[9] != 0):
            values.append(row[9])
        combined_dict_mremove_2[id] = values

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        if (row[7] != 0):
            values.append(row[7])
        if (row[8] != 0):
            values.append(row[8])
        if (row[9] != 0):
            values.append(row[9])
        combined_dict_mremove_2[id] = values

mremove_freq_2 = {}

for id in combined_dict_mremove_2:
    values = combined_dict_mremove_2[id]
    for value in values:
        if (value not in mremove_freq_2.keys()):
            mremove_freq_2[value] = 1
        else:
            mremove_freq_2[value] += 1

print("Combined summary q2 Muskaan overlap removed")
print(mremove_freq_2)

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        if (row[7] != 0):
            values.append(row[7])
        if (row[8] != 0):
            values.append(row[8])
        if (row[9] != 0):
            values.append(row[9])
        combined_dict_kremove_2[id] = values

for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        if (row[7] != 0):
            values.append(row[7])
        if (row[8] != 0):
            values.append(row[8])
        if (row[9] != 0):
            values.append(row[9])
        combined_dict_kremove_2[id] = values

kremove_freq_2 = {}

for id in combined_dict_kremove_2:
    values = combined_dict_kremove_2[id]
    for value in values:
        if (value not in kremove_freq_2.keys()):
            kremove_freq_2[value] = 1
        else:
            kremove_freq_2[value] += 1

#Q3 (NOTE: This is for all codes not just the overlapping ones)

def summary_gen_katie_3(code: int):
    count = 0
    for i in Katie_q3:
        if code in i:
            count += 1
    return count

def summary_gen_muskaan_3(code: int):
    count = 0
    for i in Muskaan_q3:
        if code in i:
            count += 1
    return count

Katie_q3 = []

Muskaan_q3 = []

for row in df.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Katie_q3.append(inner_list)

for row in df2.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Muskaan_q3.append(inner_list)

Katie_count_dict_3 = {}
Muskaan_count_dict_3 = {}

#loops through all of katie q1 list
for id in range(0, len(Katie_q3)):
    values = Katie_q3[id]
    for value in values:
        if (value not in Katie_count_dict_3.keys()):
            Katie_count_dict_3[value] = summary_gen_katie_3(value)

#loops through all of muskaan q1 list
for id in range(0, len(Muskaan_q3)):
    values = Muskaan_q3[id]
    for value in values:
        if (value not in Muskaan_count_dict_3.keys()):
            Muskaan_count_dict_3[value] = summary_gen_muskaan_3(value)

combined_dict_mremove_3 = {}
combined_dict_kremove_3 = {}

# stats with katie's values for overlap
for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        if (row[11] != 0):
            values.append(row[11])
        if (row[12] != 0):
            values.append(row[12])
        if (row[13] != 0):
            values.append(row[13])
        combined_dict_mremove_3[id] = values

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        if (row[11] != 0):
            values.append(row[11])
        if (row[12] != 0):
            values.append(row[12])
        if (row[13] != 0):
            values.append(row[13])
        combined_dict_mremove_3[id] = values

mremove_freq_3 = {}

for id in combined_dict_mremove_3:
    values = combined_dict_mremove_3[id]
    for value in values:
        if (value not in mremove_freq_3.keys()):
            mremove_freq_3[value] = 1
        else:
            mremove_freq_3[value] += 1

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        if (row[11] != 0):
            values.append(row[11])
        if (row[12] != 0):
            values.append(row[12])
        if (row[13] != 0):
            values.append(row[13])
        combined_dict_kremove_3[id] = values

for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        if (row[11] != 0):
            values.append(row[11])
        if (row[12] != 0):
            values.append(row[12])
        if (row[13] != 0):
            values.append(row[13])
        combined_dict_kremove_3[id] = values

kremove_freq_3 = {}

for id in combined_dict_kremove_3:
    values = combined_dict_kremove_3[id]
    for value in values:
        if (value not in kremove_freq_3.keys()):
            kremove_freq_3[value] = 1
        else:
            kremove_freq_3[value] += 1

print("Combined summary q1 Muskaan overlap removed")
print(mremove_freq)

with open('combined_q1_mremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in mremove_freq.items():
       writer.writerow([key, value])

print("Combined summary q1 Katie overlap removed")
print(kremove_freq)

with open('combined_q1_kremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in kremove_freq.items():
       writer.writerow([key, value])

print("q1 freq for Katie")
print(Katie_count_dict)

with open('q1_katie.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Katie_count_dict.items():
       writer.writerow([key, value])

print("q1 freq for Muskaan")
print(Muskaan_count_dict)

with open('q1_muskaan.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Muskaan_count_dict.items():
       writer.writerow([key, value])

print("Combined summary q2 Muskaan overlap removed")
print(mremove_freq_2)

with open('combined_q2_mremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in mremove_freq_2.items():
       writer.writerow([key, value])

print("Combined summary q2 Katie overlap removed")
print(kremove_freq_2)

with open('combined_q2_kremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in kremove_freq_2.items():
       writer.writerow([key, value])

print("q2 freq for Katie")
print(Katie_count_dict_2)

with open('q2_katie.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Katie_count_dict_2.items():
       writer.writerow([key, value])

print("q2 freq for Muskaan")
print(Muskaan_count_dict_2)

with open('q2_muskaan.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Muskaan_count_dict_2.items():
       writer.writerow([key, value])

print("Combined summary q3 Muskaan overlap removed")
print(mremove_freq_3)

with open('combined_q3_mremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in mremove_freq_3.items():
       writer.writerow([key, value])

print("Combined summary q3 Katie overlap removed")
print(kremove_freq_3)

with open('combined_q3_kremove.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in kremove_freq_3.items():
       writer.writerow([key, value])

print("q3 freq for Katie")
print(Katie_count_dict_3)

with open('q3_katie.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Katie_count_dict_3.items():
       writer.writerow([key, value])

print("q3 freq for Muskaan")
print(Muskaan_count_dict_3)

with open('q3_muskaan.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Muskaan_count_dict_3.items():
       writer.writerow([key, value])

print("size of set q1 - Muskaan")
print(len(Muskaan_q1))
print("size of set q2 and 3 - Muskaan")
print(len(Muskaan_q2))
print(len(Muskaan_q3))


print("size of set q1 - Katie")
print(len(Katie_q1))
print("size of set q2 and 3 - Katie")
print(len(Katie_q2))
print(len(Katie_q3))

print("COMBINED size q1")
print(len(combined_dict_mremove))
print(len(combined_dict_kremove))
print("COMBINED size q2")
print(len(combined_dict_mremove_2))
print(len(combined_dict_kremove_2))
print("COMBINED size q3")
print(len(combined_dict_mremove_3))
print(len(combined_dict_kremove_3))


#Testing

test_list_1 = [[1], [1], [2, 1], [3]]
test_list_2 = [[2], [2], [1], [3, 2]]

#freq for code 1 in test list 1 should be .75; in both should be .5

# print("test 1 freq code 1")
# print(summary_gen(1, True, False, test_list_1, test_list_2))

# print("test 1 + 2 freq code 1")
# print(summary_gen(1, True, True, test_list_1, test_list_2))
