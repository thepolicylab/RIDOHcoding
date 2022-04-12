from sklearn.metrics import cohen_kappa_score
from scipy.stats import chi2_contingency
import csv
import pandas as pd
import numpy as np

####Q1

#list of the sorted respondent ids
Katie_sorted_ids = []

Muskaan_sorted_ids = []

#dictionary that maps id to q1 code responses
Katie_q1 = {}

Muskaan_q1 = {}

#Load in Katie dataframe and clean

df = pd.read_csv('Survey7Katie.csv')

df.fillna(0, inplace=True)
df = df.astype({"Respondent" : int}, errors="raise")
df.set_index("Respondent")
df.sort_values(by=['Respondent'], inplace=True)
# df["why_not_booster_1"] = df["why_not_booster_1"].astype('float64')
# df["why_not_booster_2"] = df["why_not_booster_2"].astype('float64')
# df["why_not_booster_3"] = df["why_not_booster_3"].astype('float64')
# df["why_scientists_reliable_unreliable_1"] = df["why_scientists_reliable_unreliable_1"].astype('float64')
# df["why_scientists_reliable_unreliable_2"] = df["why_scientists_reliable_unreliable_2"].astype('float64')
# df["why_scientists_reliable_unreliable_3"] = df["why_scientists_reliable_unreliable_3"].astype('float64')
# df["why_isolation_change_1"] = df["why_isolation_change_1"].astype('float64')
# df["why_isolation_change_2"] = df["why_isolation_change_2"].astype('float64')
# df["why_isolation_change_3"] = df["why_isolation_change_3"].astype('float64')
#df.to_csv("~/Desktop/policylab/RIDOHCODING/katiedf.csv")
#print("katie exported")

#Load in Muskaan dataframe and clean

df2 = pd.read_csv('MuskaanSurvey7.csv')

df2.fillna(0, inplace=True)
df2 = df2.astype({"Respondent" : int}, errors="raise")
df2.set_index("Respondent")
df2.sort_values(by=['Respondent'], inplace= True)
# df2[""]
# df2["why_not_booster_1"] = df2["why_not_booster_1"].astype('float64')
# df2["why_not_booster_2"] = df2["why_not_booster_2"].astype('float64')
# df2["why_not_booster_3"] = df2["why_not_booster_3"].astype('float64')
# df2["why_scientists_reliable_unreliable_1"] = df2["why_scientists_reliable_unreliable_1"].astype('float64')
# df2["why_scientists_reliable_unreliable_2"] = df2["why_scientists_reliable_unreliable_2"].astype('float64')
# df2["why_scientists_reliable_unreliable_3"] = df2["why_sciesntists_reliable_unreliable_3"].astype('float64')
# df2["why_isolation_change_1"] = df2["why_isolation_change_1"].astype('float64')
# df2["why_isolation_change_2"] = df2["why_isolation_change_2"].astype('float64')
# df2["why_isolation_change_3"] = df2["why_isolation_change_3"].astype('float64')
#df2.to_csv("~/Desktop/policylab/RIDOHCODING/muskaandf.csv")
#print("muskaan exported")


#combined = df.merge(df2,"inner","Respondent",copy=False,suffixes=('_katie', '_muskaan'))
#combined.to_csv("~/Desktop/policylab/RIDOHCODING/joined.csv")


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
        Katie_q1[row[1]] = inner_list
        Katie_sorted_ids.append(row[1])


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
        Muskaan_q1[row[1]] = inner_list
        Muskaan_sorted_ids.append(row[1])

#Sort ids in sorted id list
Katie_sorted_ids.sort()
Muskaan_sorted_ids.sort()


#function that checks if Katie and Muskaan share at least one code for a respondent
def is_in_list(num):
        KatieList = Katie_q1.get(num)
        KatieList.sort()
        MuskaanList = Muskaan_q1.get(num)
        MuskaanList.sort()
        #If both inner lists are the same length
        if len(KatieList) == len(MuskaanList):
            for i in range(0, len(KatieList)):
                if KatieList[i] in MuskaanList:
                    return "yes"
        elif len(KatieList) > len(MuskaanList):
            for i in range(0, len(MuskaanList)):
                if MuskaanList[i] in KatieList:
                    return "yes"
        else:
            for i in range(0, len(KatieList)):
                if KatieList[i] in MuskaanList:
                    return "yes"
        return "no"

#final lists 
final_list = []  
for i in range(0, len(Katie_sorted_ids)):
    if Katie_sorted_ids[i] in Muskaan_sorted_ids:
        inputVal = is_in_list(Katie_sorted_ids[i])
        if inputVal == "no":
            #If value is "no" append False to Muskaan and True to Katie so there is a difference
            final_list.append(False)
        else:
            #Append True to both Muskaan and Katie
            final_list.append(True)

print("proportion of overlap q1")
proportion1 = np.mean(final_list)
print(proportion1)
print(f"std dev q1 {np.std(final_list)}")
print(pd.Series(final_list).describe())


#Q1 cohen's kappa RI
# print("Length of overlap")
# print(len(KatieYN_q1))
# print("")

# yes_count_q1 = 0

# for i in KatieYN_q1:
#     if i == "yes":
#         yes_count_q1 += 1


# print("yes proportion question 1")
# print(yes_count_q1/len(KatieYN_q1))
# print("")

# obs = np.array([KatieYN_q1, MuskaanYN_q1])
# q1IR = chi2_contingency(obs)
# print("chi2 for q1")
# print(q1IR)

#Q2
Katie_sorted_ids_2 = []

Muskaan_sorted_ids_2 = []

Katie_q2 = {}

Muskaan_q2 = {}

q2 = 6
q2_why_1 = 7
q2_why_2 = 8
q2_why_3 = 9

for row in df.itertuples():
   if (row[q2_why_1] != 0 or row[q2_why_2] != 0 or row[q2_why_3] != 0):
        inner_list = []
        if (row[q2] != "") and (row[q2_why_1] != 0):
            inner_list.append(row[q2_why_1])
        if (row[q2] != "") and (row[q2_why_2] != 0):
            inner_list.append(row[q2_why_2])
        if (row[q2] != "") and (row[q2_why_3] != 0):
            inner_list.append(row[q2_why_3])
        Katie_q2[row[1]] = inner_list
        Katie_sorted_ids_2.append(row[1])

for row in df2.itertuples():
    if (row[q2_why_1] != 0 or row[q2_why_2] != 0 or row[q2_why_3] != 0):
        inner_list = []
        if (row[q2] != "") and (row[q2_why_1] != 0):
            inner_list.append(row[q2_why_1])
        if (row[q2] != "") and (row[q2_why_2] != 0):
            inner_list.append(row[q2_why_2])
        if (row[q2] != "") and (row[q2_why_3] != 0):
            inner_list.append(row[q2_why_3])
        Muskaan_q2[row[1]] = inner_list
        Muskaan_sorted_ids_2.append(row[1])



Katie_sorted_ids_2.sort()
Muskaan_sorted_ids_2.sort()

Katie_final_ids = []
Muskaan_final_ids = []

#keep only overlapping sorted ids
for i in range(0, len(Muskaan_sorted_ids_2)):
    if Muskaan_sorted_ids_2[i] in Katie_sorted_ids_2:
        Muskaan_final_ids.append(Muskaan_sorted_ids_2[i])

for i in range(0, len(Katie_sorted_ids_2)):
    if Katie_sorted_ids_2[i] in Muskaan_sorted_ids_2:
        Katie_final_ids.append(Katie_sorted_ids_2[i])



def is_in_list(num):
    KatieList = Katie_q2.get(num)
    KatieList.sort()
    MuskaanList = Muskaan_q2.get(num)
    MuskaanList.sort()
        #If both inner lists are the same length
    if len(KatieList) == len(MuskaanList):
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    elif len(KatieList) > len(MuskaanList):
        for i in range(0, len(MuskaanList)):
            if MuskaanList[i] in KatieList:
                return "yes"
    else:
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    return "no"
    

final_list_2 = []
for i in range(0, len(Muskaan_final_ids)):
        inputVal = is_in_list(Katie_final_ids[i])
        if inputVal == "no":
            final_list_2.append(False)
        else:
            final_list_2.append(True)




#Q2 overlap
print("")
print("Proportion of overlap")
proportion2 = np.mean(final_list_2)
print(proportion2)
print(f"std dev q2 {np.std(final_list_2)}")
print(pd.Series(final_list_2).describe())
print("")

# yes_count_q2 = 0

# for i in KatieYN_q2:
#     if i == "yes":
#         yes_count_q2 += 1


# print("yes proportion question 2")
# print(yes_count_q2/len(KatieYN_q2))


# q2IR = cohen_kappa_score(KatieYN_q2, MuskaanYN_q2)
# print("kappa for q2")
# print(q2IR)


#Q3

Katie_sorted_ids_3 = []

Muskaan_sorted_ids_3 = []

Katie_q3 = {}

Muskaan_q3 = {}

for row in df.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Katie_q3[row[1]] = inner_list
        Katie_sorted_ids_3.append(row[1])

for row in df2.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Muskaan_q3[row[1]] = inner_list
        Muskaan_sorted_ids_3.append(row[1])

MuskaanYN_q3 = []
KatieYN_q3 = []
Katie_sorted_ids_3.sort()
Muskaan_sorted_ids_3.sort()

Katie_final_ids_3 = []
Muskaan_final_ids_3 = []

#keep only overlapping sorted ids
for i in range(0, len(Muskaan_sorted_ids_3)):
    if Muskaan_sorted_ids_3[i] in Katie_sorted_ids_3:
        Muskaan_final_ids_3.append(Muskaan_sorted_ids_3[i])

for i in range(0, len(Katie_sorted_ids_3)):
    if Katie_sorted_ids_3[i] in Muskaan_sorted_ids_3:
        Katie_final_ids_3.append(Katie_sorted_ids_3[i])
def is_in_list(num):
    KatieList = Katie_q3.get(num)
    KatieList.sort()
    MuskaanList = Muskaan_q3.get(num)
    MuskaanList.sort()
        #If both inner lists are the same length
    if len(KatieList) == len(MuskaanList):
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    elif len(KatieList) > len(MuskaanList):
        for i in range(0, len(MuskaanList)):
            if MuskaanList[i] in KatieList:
                return "yes"
    else:
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    return "no"
    

final_list_3 = []
for i in range(0, len(Muskaan_final_ids_3)):
        inputVal = is_in_list(Katie_final_ids_3[i])
        if inputVal == "no":
            final_list_3.append(False)
        else:
            final_list_3.append(True)




#Q3 proportion
print("Proportion of overlap q 3")
proportion3 = np.mean(final_list_3)
print(proportion3)
print(f"std dev q3 {np.std(final_list_3)}")
print(pd.Series(final_list_3).describe())



'''Recall that Muskaan and I labeled each response with a set of categories. We decided to operationalize “agreement” as 
“do these sets share a category in common.” Thus, we decided to report inter rater 
reliability as the proportion of  of responses with overlapping categories. 
Using a measure such as chi-squared or cohen's kappa was difficult because we only had 
20-100 shared responses but 20+ code options for a response.
'''



