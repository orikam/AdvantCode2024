import re

list1 = []
list2 = []

    
def read_data():
    """
    Reads the input data from the file and populates list1 and list2 with integers.
    """
    with open("Day1/input.txt") as f:
        for line in f:
            ids = re.findall("\d+", line)
            list1.append(int(ids[0]))
            list2.append(int(ids[1]))

def calc_diff_score():
    """
    Calculates the difference score between two lists of integers.
    """
    return(sum(abs(list1[i] - list2[i]) for i in range(len(list1))))

def calc_similarity_score():
    """
    Calculates the similarity score between two lists of integers.
    The score is the sum of products of each unique element in list1
    with its count in list2.
    """
    s1 = set(list1)
    return(sum(list1[i] * list2.count(list1[i]) for i in range(len(list1))))

if __name__ == "__main__":
    read_data()
    list1.sort()
    list2.sort()
    print(f"Diff score: {calc_diff_score()}")
    print(f"similarity  score: {calc_similarity_score()}")

