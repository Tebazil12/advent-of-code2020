with open("input-day6", 'r') as f:
    num_yeses = 0
    person_answers = []
    for i, line in enumerate(f):
        # print(i)
        if line == '\n':
            #stop and prcoess
            print()
            print(person_answers)

            # print(f"{list_answer} {set_answer} {len(set_answer)}")

            overlap = set.intersection(*person_answers)
            print(overlap)
            num_yeses = num_yeses + len(overlap)


            person_answers = []

        else:
            person_answers.append( set(list(line.strip())))


print(f"Num valid = {num_yeses}")
