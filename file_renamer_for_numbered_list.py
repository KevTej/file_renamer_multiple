import os

file_list = os.listdir("C:\\Users\\KevTe\\OneDrive\\Desktop\\Programming\\BUTT")
listname = input("What will be the name of these files?\n")
num = 0
for i in file_list:
    metric_name = str(i)
    imperial_name = listname + " " + str(num) + ".txt"
    # I'm trying to replace the file name each time, using an f-string
    # imperial = open(f"C:\\Users\\KevTe\\OneDrive\\Desktop\\BUTT\\{file_name}.txt", "a+")
    os.rename(f"C:\\Users\\KevTe\\OneDrive\\Desktop\\Programming\\BUTT\\{metric_name}", f"C:\\Users\\KevTe\\OneDrive\\Desktop\\Programming\\BUTT\\{imperial_name}")
    num += 1
