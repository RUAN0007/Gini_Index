def calculate_Gini_Index_from_list(salary):
    dots = convert_salary_list_into_dots(salary)
    integrate_result = integrate_dots_from_0_to_1(dots)
    return 2 - 2 * integrate_result

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

def integrate_dots_from_0_to_1(dots):
    count = len(dots)
    sum = 0
    dots.pop()
    for data in dots: #Pop the last item ,which is always 1
        sum += data * 2
    sum += 1
    return sum / count / 2
    

salary_list = list();
with open("data.txt") as file:
    for line in file:
        salary_list.append(int(line))
        
print (calculate_Gini_Index_from_list(salary_list))
        
