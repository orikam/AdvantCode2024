def read_data():
    """
    Reads the input data from the file and returns a list of reports.
    Each report is a list of strings representing the values in the report.
    """
    res = []
    with open("Day2/input.txt") as f:
        for line in f:
            line = line[:-1]
            report = line.split(" ")
            res.append(report)
    return res

def check_report(report):
    """
    Checks if the report is valid.
    A report is valid if the values are in a non-decreasing order,
    with each value differing from the next by 1, 2, or 3.
    Returns a tuple (is_valid, error_index) where is_valid is a boolean
    indicating if the report is valid, and error_index is the index of the
    first error found (or -1 if no errors).
    """
    error_cnt = 0
    s = 1
    if int(report[0]) < int(report[1]):
        s = -1
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if abs(diff) < 1 or abs(diff) > 3 or (s * diff < 0):
            error_cnt += 1
            return (False, i)
    if error_cnt == 0:
        return (True, -1)

def check_report_dump(report):
    """
    Checks if the report is valid by trying all permutations of the report.
    Returns a tuple (is_valid, error_index) where is_valid is a boolean
    indicating if the report is valid, and error_index is the index of the
    first error found (or -1 if no errors).
    """
    res = check_report(report)
    if res[0]:
        return res
    else:
        for i in range(len(report)):
            value = report.pop(i)
            res = check_report(report)
            report.insert(i, value)
            if res[0]:
                return res
    return (False, -1)

if __name__ == "__main__":
    count = 0
    count2 = 0
    data = read_data()
    for report in data:
        if check_report(report)[0]:
            count += 1
 
        if check_report_dump(report)[0]:
            count2 += 1

    print(f"{count}, {count2}")
        
