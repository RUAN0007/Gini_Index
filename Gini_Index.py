def sum_list(ls):
    sum = 0
    for element in ls:
        sum += element
    return sum


def convert_salary_list_into_dots(salary_list):
    salary_list.sort()
    dots = list();
    salary_sum = sum_list(salary_list)
    sum = 0
    for salary in salary_list:
        sum += salary
        dots.append(sum /salary_sum)
    return dots;


salary_list = list();
with open("data.txt") as file:
    for line in file:
        salary_list.append(int(line))
        
print (convert_salary_list_into_dots(salary_list))
        
