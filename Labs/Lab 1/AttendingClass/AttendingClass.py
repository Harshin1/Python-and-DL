python = ['A', 'B', 'C', 'D']
webApp = ['A', 'C', 'E']

new_list = []
for i in python:
    if i not in webApp:
        new_list.append(i)
print(new_list)