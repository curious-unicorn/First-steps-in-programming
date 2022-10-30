architect_name = input()
number_of_projects = input()
preparation_time_per_project = 3

num_prepation_time_per_project = int(preparation_time_per_project)
num_number_of_projects = int(number_of_projects)

total_prepration_time = num_number_of_projects * preparation_time_per_project

print(f"The architect {architect_name} will need {total_prepration_time} hours to complete "
      f"{number_of_projects} project/s.")
