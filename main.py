## Аналог .split() который разбивает string на масив
def separete_string_to_int(s):
    s1 =s
    arr = []
    s2 = ''
    for i in range(0, len(s1)):
        if s1[i].isdigit() == True:
            s2 = s2+s1[i]
        else:
            if s2 != '':
                arr.append(s2)
            s2 = ''
            arr.append(s1[i])
    if s[len(s)-1].isdigit() == True:
        pass
    return arr
## Присвоение приоритетов элементам масива в зависимости от знаков и скобок
def comand_priority(arr):
    prior = 1
    new_arr = []
    for i in range(0,len(arr)):
        if arr[i]== '(':
            prior += 2
            new_arr.append(0)
        elif arr[i] == ')':
            prior -= 2;
            new_arr.append(0)
        if arr[i].isdigit() == True:
            new_arr.append(0)
        elif arr[i]== '+' or arr[i]=='-':
            new_arr.append(prior)
        elif arr[i] == '*' or arr[i] == '/':
            new_arr.append(prior+1)
    return new_arr
## Функция выполняющая одну операцию с наибольшим приоритетом
def do_math(arr, priot_arr):
    max_priot = 0
    max_index = 0
    left_max_index = 0
    righ_max_index = 0
    s = ''
    for i in range(0, len(arr)):
        if priot_arr[i]>max_priot:
            max_priot = priot_arr[i]
            max_index = i
            for j in range(i+1, len(arr)):
                if arr[j].isdigit() == True:
                    righ_max_index = j
                    break
            for k in range(i-1, 0,-1):
                if arr[k].isdigit() == True:
                    left_max_index = k
                    break
    if max_priot <= 0:
        print('error')
        return 'error'
    if arr[max_index] == '/' and arr[righ_max_index] == '0':
        s = 'False'
        print('error')
        return 'error'
    n_s = arr[left_max_index]+arr[max_index]+arr[righ_max_index]
    arr[left_max_index] = str(eval(n_s))
    arr.pop(righ_max_index)
    arr.pop(max_index)
    return arr
## Общая функция
def all_math(s):
    s = '(' + s + ')'
    all_arr = []
    all_arr = separete_string_to_int(s)
    pr_arr = comand_priority(all_arr)
    setter = 0
    for i in range(0, len(pr_arr)):
        if pr_arr[i] != 0:
            setter += 1
    s1 = ''
    for i in range(0, setter):
        all_arr = do_math(all_arr, pr_arr)
        if all_arr[0] == 'error':
            return 'error'
        pr_arr = comand_priority(all_arr)
        for k in range(0, len(all_arr)):
            s1 = s1 + all_arr[k]
        s1 = ''
    for u in range(0, len(all_arr)):
        if all_arr[u].isdigit() == True:
            return all_arr[u]

s = '(111+2+3+((45)*(9)-9)+27*2))*2'
s_v2 = '(111+2+3+((45)*(9)-9)+27*2))/(1-1)'
print(all_math(s))
print(all_math(s_v2))

