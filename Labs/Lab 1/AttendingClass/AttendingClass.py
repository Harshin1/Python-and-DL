#list of students attending Python
python = ['A', 'B', 'C', 'D']
#list of students attending webApp
webApp = ['A', 'C', 'E']

new_list = []
#list of students attending Python but not webApp
for i in python:
    if i not in webApp:
        new_list.append(i)
print(new_list)