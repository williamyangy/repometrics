#!/usr/bin/env python3
import os
import json

def div_d(my_dict):
    sum_p = sum(my_dict.values())
    for i in my_dict:
        my_dict[i] = float(my_dict[i]/sum_p)
    return my_dict


working_folder = input("Enter your value: ")
overall_dict = dict()
summary_dict = dict()
summary_dict['make'] = summary_dict['js'] = summary_dict['python'] = summary_dict['C'] = summary_dict['C#'] \
    = summary_dict['Java'] = summary_dict['Golang'] = summary_dict['PHP'] = summary_dict['VB'] = summary_dict['Perl'] \
= summary_dict['HTML'] = summary_dict['css'] = summary_dict['others'] = 0


detail_dict = dict()
data = json.loads(json.dumps(overall_dict))


for file in os.listdir(working_folder):
        if os.path.splitext(file)[0] == 'Makefile':
            detail_dict[os.path.join(working_folder, file)] = 'make'
            summary_dict['make'] += 1

        elif file.endswith(".js"):
            detail_dict[os.path.join(working_folder, file)] = 'js'
            summary_dict['js'] += 1

        elif file.endswith(".py"):
            detail_dict[os.path.join(working_folder, file)] = 'python'
            summary_dict['python'] += 1

        elif file.endswith(".c"):
            detail_dict[os.path.join(working_folder, file)] = 'C'
            summary_dict['C'] += 1

        elif file.endswith(".cs"):
            detail_dict[os.path.join(working_folder, file)] = 'C#'
            summary_dict['C#'] += 1

        elif file.endswith(".java"):
            detail_dict[os.path.join(working_folder, file)] = 'Java'
            summary_dict['Java'] += 1

        elif file.endswith(".go"):
            detail_dict[os.path.join(working_folder, file)] = 'Golang'
            summary_dict['Golang'] += 1

        elif file.endswith(".php"):
            detail_dict[os.path.join(working_folder, file)] = 'PHP'
            summary_dict['PHP'] += 1

        elif file.endswith(".vb"):
            detail_dict[os.path.join(working_folder, file)] = 'VB'
            summary_dict['VB'] += 1

        elif file.endswith(".pl"):
            detail_dict[os.path.join(working_folder, file)] = 'Perl'
            summary_dict['Perl'] += 1

        elif file.endswith(".html"):
            detail_dict[os.path.join(working_folder, file)] = 'HTML'
            summary_dict['HTML'] += 1

        elif file.endswith(".css"):
            detail_dict[os.path.join(working_folder, file)] = 'css'
            summary_dict['css'] += 1

        else:
            detail_dict[os.path.join(working_folder, file)] = 'others'
            summary_dict['others'] += 1

summary_dict = div_d(summary_dict)


#print(detail_dict)
#print(summary_dict)


data['results'] = detail_dict
data['summary'] = summary_dict

#print(data)
output = json.dumps(data, ensure_ascii=False)
print(output)
