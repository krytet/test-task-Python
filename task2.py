

def calculate(m: int, n: int, p: list[int]):
    result = 0
    day = 1
    level = 1
    while day <= m:
        if level == n:
            result += p[level-1]
            level = 1
            day += 1
        elif sum(p[:level]) > sum(p[level:]) and (m - day >= day + 1):
            result += p[level-1]
            level = 1
            day += 2
        else:
            result += p[level-1]
            level += 1
            day += 1
    return result


def main():
    print(calculate(3, 3, [10, 4, 8]))


if __name__ == "__main__":
    main()
