"""def longestBalanced(s: str):
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2

    my_dict = {}
    for value in set(s):
        my_dict[value] = 0
    for char in s:
        my_dict[char]+=1

    letter, highest = max(my_dict.items(), key=lambda x: x[1])
    second_letter, sec_highest = max(
        (x for x in my_dict.items() if x[1] <= highest and x[0] != letter),
        key=lambda x: x[1],
        default=(None, 0),
    )
    print(highest, sec_highest)
    
    if highest == sec_highest:
        count = 0
        for value in my_dict.values():
            if value == highest:
                count += 1
        final = count * highest
        return final
    elif highest > sec_highest:
        count = 0
        run_count = 0
        for key, value in my_dict.items():
            print(key)
            if value >= sec_highest:
                count += 1
                run_count += 1
                if run_count == 2 and sec_highest > 1:
                    break
        final = count * sec_highest
        return final"""

def longestBalanced(s: str):
    for i, char1 in enumerate(s):
        for j, char2 in enumerate(s):
            pass

if __name__ == "__main__":
    print(longestBalanced("mmlo"))