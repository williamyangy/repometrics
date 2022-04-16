import os
import json


overall_dict = dict()
summary_dict = dict()
summary_dict['make'] = summary_dict['js'] = summary_dict['python'] = summary_dict['C'] = summary_dict['C#'] \
    = summary_dict['Java'] = summary_dict['Golang'] = summary_dict['PHP'] = summary_dict['VB'] = summary_dict['Perl'] \
= summary_dict['HTML'] = summary_dict['css'] = summary_dict['others'] = 0


detail_dict = dict()
data = json.loads(json.dumps(overall_dict))
file_count = sum(len(files) for _, _, files in os.walk(r'./'))
for file in os.listdir("./"):
    if os.path.splitext(file)[0] == 'Makefile':
        detail_dict[os.path.join("./", file)] = 'make'
        summary_dict['make'] += 1/file_count
    elif file.endswith(".js"):
        detail_dict[os.path.join("./", file)] = 'js'
        summary_dict['js'] += 1 / file_count
    elif file.endswith(".py"):
        detail_dict[os.path.join("./", file)] = 'python'
        summary_dict['python'] += 1 / file_count
    elif file.endswith(".c"):
        detail_dict[os.path.join("./", file)] = 'C'
        summary_dict['C'] += 1 / file_count
    elif file.endswith(".cs"):
        detail_dict[os.path.join("./", file)] = 'C#'
        summary_dict['C#'] += 1 / file_count
    elif file.endswith(".java"):
        detail_dict[os.path.join("./", file)] = 'Java'
        summary_dict['Java'] += 1 / file_count
    elif file.endswith(".go"):
        detail_dict[os.path.join("./", file)] = 'Golang'
        summary_dict['Golang'] += 1 / file_count
    elif file.endswith(".php"):
        detail_dict[os.path.join("./", file)] = 'PHP'
        summary_dict['PHP'] += 1 / file_count
    elif file.endswith(".vb"):
        detail_dict[os.path.join("./", file)] = 'VB'
        summary_dict['VB'] += 1 / file_count
    elif file.endswith(".pl"):
        detail_dict[os.path.join("./", file)] = 'Perl'
        summary_dict['Perl'] += 1 / file_count
    elif file.endswith(".html"):
        detail_dict[os.path.join("./", file)] = 'HTML'
        summary_dict['HTML'] += 1 / file_count
    elif file.endswith(".css"):
        detail_dict[os.path.join("./", file)] = 'css'
        summary_dict['css'] += 1 / file_count
    else:
        detail_dict[os.path.join("./", file)] = 'others'
        summary_dict['others'] += 1 / file_count


#print(detail_dict)
#print(summary_dict)


data['results'] = detail_dict
data['summary'] = summary_dict

#print(data)
output = json.dumps(data, ensure_ascii=False)
print(output)
