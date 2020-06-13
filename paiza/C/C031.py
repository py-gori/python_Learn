# input
input_line = int(input())

list_keys = []
list_values = []
for i in range(input_line):
    keys, values = input().split()
    values = int(values)

    list_keys.append(keys)
    list_values.append(values)
dict_city = dict(zip(list_keys, list_values))

u_city, u_time = input().split()

# output
h = int(u_time[0:2])
m = int(u_time[3:5])

for keys in dict_city.keys():
    if not u_city == keys:
        time_lag = dict_city[keys] - dict_city[u_city]

        if h + time_lag > 24:
            city_h = (h + time_lag) - 24
        elif h + time_lag < 0:
            city_h = (h + time_lag) + 24
        else:
            city_h = h + time_lag
        city_time = str(city_h).rjust(2, "0") + ":" + str(m).rjust(2, "0")
        print(city_time)
    else:
        print(u_time)