answer = 0

a = input()

save = []
save_str = ''

minus = 0

for i in a:
    if minus == 0:
        if i == '+':
            answer += int(save_str)
            save_str = ''

        elif i == '-':           
            answer += int(save_str)
            save_str = ''
            minus = 1

        else :
            save_str += i

    else : 
        if i == '+':
            answer -= int(save_str)
            save_str = ''

        elif i == '-':           
            answer -= int(save_str)
            save_str = ''

        else :
            save_str += i

if minus == 1 :
    answer -= int(save_str)

else :
    answer +=int(save_str)

print(answer)