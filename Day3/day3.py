import re

if __name__ == "__main__":
    with open("Day3/input.txt") as f:
        data = f.read()
    
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    res = 0
    for m in muls:
        res += int(m[0]) * int(m[1])
    print(f"Part 1: {res}")
    
    #first don't
    stop = len
    re_res = re.search(r"don\'t", data)
    if re_res:
        stop = re_res.end()
    res = 0
    temp_data = data[:stop]
    while len(temp_data) > 0:
        muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", temp_data)
        for m in muls:
            res += int(m[0]) * int(m[1])
        #find the next do
        re_res = re.search(r"do", data[stop+5:])
        if re_res is None:
            break
        start = re_res.end()
        if start > 0:
            start += stop
            stop = len(data)
            re_res = re.search(r"don\'t", data[start:])
            if re_res:
                stop = re_res.end() + start
            temp_data = data[start:stop]

    print(res)
    
    
