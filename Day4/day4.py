def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        data = file.readlines()
    return data
target = 'XMAS'

def check_direction(data, pos, x_step, y_step, target):
    for i in range(len(target)):
        x = pos[0] + i * x_step
        y = pos[1] + i * y_step
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[0].strip()):
            return 0
        if data[x][y] != target[i]:
            return 0
    return 1

def check_pos(data, pos):
    result = 0
    result += check_direction(data, pos, 1, 0, target)
    result += check_direction(data, pos, 1, 1, target)
    result += check_direction(data, pos, 1, -1, target)
    result += check_direction(data, pos, -1, 0, target)
    result += check_direction(data, pos, -1, 1, target)
    result += check_direction(data, pos, -1, -1, target)
    result += check_direction(data, pos, 0, 1, target)
    result += check_direction(data, pos, 0, -1, target)
    return result

def check_pos_x(data, pos):
    if (pos[0] < 1 or pos[0] >= len(data) - 1):
        return 0
    x= pos[0]
    y = pos[1]
    if (data[x-1][y-1] == 'M') and (data[x-1][y+1] == 'M') and (data[x+1][y-1] == 'S') and (data[x+1][y+1] == 'S'):
        return 1
    if (data[x-1][y-1] == 'S') and (data[x-1][y+1] == 'S') and (data[x+1][y-1]  == 'M') and (data[x+1][y+1] == 'M'):
        return 1
    if (data[x-1][y-1]  == 'S') and (data[x-1][y+1]  == 'M') and (data[x+1][y-1]  == 'S') and (data[x+1][y+1] == 'M'):
        return 1
    if (data[x-1][y-1]  == 'M') and (data[x-1][y+1]  == 'S') and (data[x+1][y-1]  == 'M') and (data[x+1][y+1] == 'S'):
        return 1
    
    return 0
    




def find_pos(data, char, shape):
    y = 0
    result = 0
    for i in range(0, len(data)):
        r = 0
        y = 0
        while r != -1:
            r = data[i][y:].find(char)
            if r != -1:
                y += r
                pos = (i, y)
                if shape == 0:
                    result += check_pos(data, pos)
                else:
                    result += check_pos_x(data, pos)
                y+= 1
        
    return result

def main():
    filename = 'Day4/input.txt'
    data = read_data(filename)
    n = len(data)
    m = len(data[0].strip())
    result = find_pos(data, target[0], 0)
    print(f"Result: {result}")
    result = find_pos(data, 'A', 1)
    print(f"Result: {result}")
    print(f"Data loaded from {filename}")
    print(f"Data size: {n} rows, {m} columns")

if __name__ == "__main__":
    main()
    print("Day 4 script executed successfully.")