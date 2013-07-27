salary_list = list();
with open("data.txt") as file:
    for line in file:
        salary_list.append(int(line))
        
salary_list.sort()
print (salary_list)
        