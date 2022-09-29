def order(sentence):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sentence = sentence.split(' ')
    for number in range(len(numbers)):
        for i in range(len(sentence)):
            if numbers[number] in sentence[i]:
                print(sentence[i])

def find_names():
    names = input()
    names_sp = names.split('/')
    names_like, names_comment = names_sp[0], names_sp[1]
    names_like = names_like.split(' ')
    names_comment = names_comment.split(' ')
    result = []
    for name in names_like:
        if name in names_comment:
            result.append(name)


    print(' '.join(result))

def boards(len_i_want, inaccuracy, all_lengths):
    result = []
    if inaccuracy < len_i_want:
        for i in range(len(all_lengths)):
            if (len_i_want - inaccuracy < all_lengths[i] < len_i_want + inaccuracy) or (all_lengths[i] == len_i_want):
                result.append(all_lengths[i])
    else:
        print("Недопустимая погрешность")
    diff_of_boards = len(all_lengths) - len(result)
    
    print(result)
    print(diff_of_boards)
    print(len(result))

def c_zadacha():
    O = 100000
    NH = 160
    P = 20000
    NT = 40
    salary_nums = list(map(int, input().split()))
    H = salary_nums[0]
    T = salary_nums[1]

    print(int(O * (H / NH) + P * (T / NT)))

def f_zadacha():
    salary_developer = None
    all_salary = 297
    salary_analitik = ((1 / 3) * salary_developer) + 18 # 78
    salary_tester = ((1 / 3) * salary_analitik) + 13 # 74
