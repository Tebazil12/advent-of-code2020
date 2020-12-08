with open("input-day6", 'r') as f:
    num_yeses = 0
    current_answer = ''
    for i, line in enumerate(f):
        # print(i)
        if line == '\n':
            #stop and prcoess
            list_answer = list(current_answer)
            set_answer = set(list_answer)
            num_yeses = num_yeses + len(set_answer)

            # print(f"{list_answer} {set_answer} {len(set_answer)}")



            current_answer = ''
        else:
            current_answer = current_answer + line.strip()


print(f"Num valid = {num_yeses}")
