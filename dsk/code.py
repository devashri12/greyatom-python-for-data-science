# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("\nData:\n\n",data)
print("\nType of data:\n\n",type(data))

census=np.concatenate((new_record,data),axis=0)
print(census)

age=census[0:,0]
#print(age)

max_age=np.max(age)
print(max_age)

min_age=np.min(age)
print(min_age)

c=np.count_nonzero(age)
age_mean=(np.sum(age)/c)
print(age_mean)

age_std=np.std(age,axis=None)
print(age_std)

race_0=census[np.where(census[0:,2]==0)]
#print(race_0)
len_0= race_0.size
print(len_0)

race_1=census[np.where(census[0:,2]==1)]
#print(race_1)
len_1= race_1.size
print(len_1)

race_2=census[np.where(census[0:,2]==2)]
#print(race_2)
len_2= race_2.size
print(len_2)

race_3=census[np.where(census[0:,2]==3)]
#print(race_3)
len_3= race_3.size
print(len_3)

race_4=census[np.where(census[0:,2]==4)]
#print(race_4)
len_4= race_4.size
print(len_4)

l=np.array([len_0,len_1,len_2,len_3,len_4])
print(l)

m=np.min(l)

minority_race=np.where(l==m)
print(minority_race[0])

senior_citizens=census[np.where(census[0:,0]>60)]
#print(senior_citizens)
working_hours_sum=np.sum(senior_citizens[0:,6])
print(working_hours_sum)

senior_citizens_len=senior_citizens.size
print(senior_citizens_len)

avg_working_hours=(working_hours_sum/senior_citizens_len)
print(avg_working_hours)

high=census[np.where(census[0:,1]>10)]
low=census[np.where(census[0:,1]<=10)]



avg_pay_high=np.mean(high[0:,7],axis=None)
avg_pay_low=np.mean(low[0:,7],axis=None)

print(avg_pay_high)
print(avg_pay_low)











