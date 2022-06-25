dnastring = input('DNA String:')
substring = input('Substring:')
res = [i for i in range(len(dnastring)) if dnastring.startswith(substring, i)]
new_list = [x+1 for x in res]
print(new_list)

