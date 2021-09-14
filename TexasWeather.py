#********************** TexasWeather.py  *********************
#
# Name: Vladislava Sicicorez
#
# Course: CSCI 1470
#
# Assignment: #9
#
# Algorithm:
#
#open the original file to read the information
#open new file to write
#write a header in the new file
#get the city name, avegarge temperatue and record temperature from original file
#write it to new file
#close original file
#close new file
#**********************************************************
temps = open ("C:\\Users\\vladi\\OneDrive\\Documents\\College\\Python\\Temp.txt",'r')
temps_upd = open ("C:\\Users\\vladi\\OneDrive\\Documents\\College\\Python\\Temp_upd.txt",'w')
table_format = '{:<20}{:^10}{:^10}{:^10}'
temps_upd.write(table_format.format("City","Avg.Temp","Record","Difference"))
temps_upd.write("\n")
for line in temps:
    l = line.split()
    avg = l[1]
    record_high = l[2]
    difference = float(record_high)-float(avg)
    difference = "{:.2f}".format(difference)
    print(table_format.format(l[0],avg,record_high,difference))
    temps_upd.write (table_format.format(l[0],avg,record_high,difference))
    temps_upd.write("\n")
temps.close()
temps_upd.close()

