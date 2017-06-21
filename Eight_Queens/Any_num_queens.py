#Any Queens puzzle
def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy


def col_clashes(bs, c):
    """
        Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(the_board):
    """
        Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
        If it has clashes, return True.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def interchange_list(j, k, list):
    temp = list[j]
    list[j] = list[k]
    list[k] = temp

# list = [1, 2, 3]
# interchange_list(1, 2, list)
# print(list)


def generating_next_permutation_in_lexicographic_order(result):
    per_list = result[:]
    n = len(per_list) - 1
    j = n - 1
    while per_list[j] > per_list[j + 1]:
        j = j - 1
        if j < 0:
            return [0]
    k = n
    while per_list[j] > per_list[k]:
        k = k - 1
    interchange_list(j, k, per_list)
    r = n
    s = j + 1
    while r > s:
        interchange_list(r, s, per_list)
        r = r - 1
        s = s + 1
    return per_list


def main(num):
    per_list = list(range(0, num))
    num_found = 0
    result = []
    while per_list != [0]:
        if not has_clashes(per_list):
            #print(per_list)
            #print(has_clashes(per_list))
            # print(has_clashes([0, 4, 7, 5, 2, 6, 1, 3]))
            result.append(per_list)
            #print(result[0])
            num_found += 1
        per_list = generating_next_permutation_in_lexicographic_order(per_list)
        
    #print(num_found)
    #print(result)
    return result

#main(8)


def mirror_in_y_axis(solution):
    result = solution[:]
    length = len(solution)
    for i in range(0, length):
        result[length - 1 - i] = solution[i]
    return result

def mirror_in_x_axis(solution):
    result = solution[:]
    length = len(result)
    for i in range(0, length):
        result[i] = length - 1 - result[i]
    return result

def rotate_90_anti_clockwise_degrees(solution):
    result = solution[:]
    n = len(solution) - 1
    for (i, j) in enumerate(solution):
        result[j] = n - i
    return result


def rotate_n_anti_clockwise_degrees(solution, n):
    n = n // 90
    result = solution[:]
    length = len(solution) - 1
    for k in range(n):
        result1 = result[:]
        for (i, j) in enumerate(result):
            result1[j] = length - i
        result = result1
    return result


def mirror_x_and_y(solution):
    result = []
    result1 = mirror_in_x_axis(solution)
    result.append(result1)
    result1 = mirror_in_y_axis(solution)
    if result1 not in result:
        result.append(result1)
    return result


def generate_family_symmetries_solution(solution):
    result1 = []
    result1.append(solution)
    result1.extend(mirror_x_and_y(solution))

    for k in [90, 180, 270]:
        solution1 = rotate_n_anti_clockwise_degrees(solution, k)
        result1.append(solution1)
        result1.extend(mirror_x_and_y(solution1))
    result = []
    for i in result1:
        if i not in result:
            result.append(i)
    return result


def solutions_from_unique_families(num):
    result = main(num)
    for i in result:
        solution = generate_family_symmetries_solution(i)
        for j in range(1, len(solution)):
            if solution[j] in result:
                result.remove(solution[j])
    return result

result = solutions_from_unique_families(8)
print(len(result))
print(result)







