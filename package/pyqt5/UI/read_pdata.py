import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygal

t_data = pd.read_csv(r'C:\Users\TianJian\Desktop\python\UI\cpk.csv',header = 0)


print("======t_data======")
print(t_data)


print("=====t_data.keys()=======")
print(t_data.keys())
print(t_data.keys().values.item(1))


print("======t_data.values[1][0]=========")
print(t_data.values[1][0])

print("======t_data.info()=========")
print(t_data.info())

print("===============")
print(t_data['Special Build Description'])

# print(t_data['Special Build Description'])
special_build_arr = t_data['Special Build Description'].array
print("========SSSSSSSSSSSSSSSSSSSSSS=======")
print(set(special_build_arr))
print(list(set(special_build_arr)))


print(t_data['Station ID'])
station_id_arr = t_data['Station ID'].array
print("===============")
print(set(station_id_arr))
print(list(set(station_id_arr)))

print(t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).mean())
print(t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).value_counts())

print("=======get_group(J230-P4B_FBU-QS2)========")
print(t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).get_group("J230-P4B_FBU-QS2"))
squares=t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).get_group("J230-P4B_FBU-QS2")
#t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).value_counts().unstack().plot(kind='bar', figsize=(20, 4))
#data.groupby('race')['flee'].value_counts().unstack().plot(kind='bar', figsize=(20, 4))

#plt.plot(squares)
#plt.show()

print("=== t_data[Sensorgroup CoreLoad Test Starfire Core: IC0R post]===")
print(t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].values)
#t_data["Sensorgroup CoreLoad Test Starfire Core: IC0R post"].groupby(t_data["Special Build Description"]).hist(bins= 50,figsize=(8,8))

items = list(set(special_build_arr))
stations = list(set(station_id_arr))

#t_data_mean = t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby(t_data["Special Build Description"]).mean().agg([np.mean, np.median, np.std])
#t_data_std = t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby(t_data["Special Build Description"]).std()


t_data_mean=t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby(t_data["Special Build Description"]).agg([np.mean, np.median, np.std])
print(t_data_mean)

#for i in t_data_mean.index:
#	print(i)

path = "/Users/willzhang/Desktop/py/pdata/cpk.csv"
t_data_mean.to_csv(path)

# with open(path, "w") as file_object:
# 	for i in t_data_mean:
# 		print(i)
# 		file_object.write(i)
#



def get_group_mean_data(t_data):
	
	
	pass


def function1():
	for item in items:
		for station in stations:
			if str(item) == "nan":
				pass
				print("nan"+str(item))
			else:
				if str(station) == "nan":
					pass
				else:
					print(item)
					#temp = t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby(t_data['Special Build Description']).get_group(item)
					try:
						temp = t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby([t_data["Special Build Description"],t_data["Station ID"]]).get_group((item,station))
					except KeyError:
						pass
					else:
						print(temp)
						temp.hist(bins=10, figsize=(4, 4))
						
						item_count = len(temp)
						
						
						
						plt.xlabel('')
						plt.ylabel('')
						
						plt.title(item+" "+ station+" "+str(item_count))
						#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
						#plt.xlim(40, 160)
						#plt.ylim(0, 0.03)
						plt.grid(True)
						
						plt.savefig("/tmp/1/"+item+" "+ station+" "+str(item_count)+".png", bbox_inches='tight')
						#plt.show()
						plt.close()
						temp=""
				
			
def funtion1():
	for item in items:
		if str(item) == "nan":
			pass
			print("nan" + str(item))
		else:
			print(item)
			temp = t_data["Sensorgroup CoreLoad Test Starfire Core: PCPT post"].groupby(
				t_data["Special Build Description"]).get_group(item)
			temp.hist(bins=50, figsize=(8, 8))
			
			item_count = len(temp)
			
			plt.xlabel('')
			plt.ylabel('')
			
			plt.title(item + " " + str(item_count))
			# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
			# plt.xlim(40, 160)
			# plt.ylim(0, 0.03)
			plt.grid(True)
			
			plt.savefig("/tmp/1/" + item + ".png", bbox_inches='tight')
			plt.close()
			temp = ""