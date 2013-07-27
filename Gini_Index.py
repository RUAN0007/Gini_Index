import os
import fnmatch

def calculate_Gini_Index_from_list(salary):
    dots = convert_salary_list_into_dots(salary)
    integrate_result = integrate_dots_from_0_to_1(dots)
    return 1 - 2 * integrate_result

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

def strip_file_extension(file_name):
    file_name_list = file_name.split('.')
    return file_name_list[0]
    

salary_all_list = list()
result_file = open("result.txt",'w')
for file in os.listdir('./data'):
    if fnmatch.fnmatch(file, '*.txt'):
        file_name = strip_file_extension(file)
        salary_list = list()
        with open("data/"+file) as fl:
            for line in fl:
                salary_list.append(int(line))
        salary_all_list.extend(salary_list)               
        result = calculate_Gini_Index_from_list(salary_list)
        if(not result_file.write("{}: {}\n".format(file_name,round(result,3)))):
            print("File Overwriting Failed")

        final_result = calculate_Gini_Index_from_list(salary_all_list)     
result_file.write("\nAll: {}\n".format(round(final_result,3)))
result_file.close()
        
        
