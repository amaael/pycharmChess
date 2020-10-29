# This is a sample Python script.
import numpy as np

S = 12
N = S * S


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def valid(x_dest, y_dest):
    return 0 <= x_dest < S and 0 <= y_dest < S


A = [(-2,-1),
     (-2, 1),
     ( 2,-1),
     ( 2, 1),
     (-1,-2),
     (-1, 1),
     ( 1,-2),
     ( 1, 2)]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def set_path(table, x_i, y_i, x_f, y_f):
    cnt = 0
    x = x_f
    y = y_f
    reverse_path = [(x, y)]
    while x != x_i or y != y_i:
        cnt += 1
        x, y = table[x, y, 0:2]
        if cnt >= N:
            break
        reverse_path.append((x, y))
    return reverse_path


def find_path(x_i, y_i, x_f, y_f):
    visited = np.zeros((S, S), dtype=int)
    visited[x_i, y_i] = 1
    history = []
    previous = [(x_i, y_i)]
    history.append(previous)
    table = np.zeros((S, S, 3), dtype=int)

    # print(A)
    dist = 0
    done = x_i == x_f and y_i == y_f
    l1 = 0
    while not done:
        l1 += 1
        if l1 > N:
            print("ERROR: {}".format(l1))
            print(previous)
            print(history)
            exit(1)
        after = []
        dist += 1
        for point in previous:
            for action in A:
                x = point[0] + action[0]
                y = point[1] + action[1]
                if valid(x, y) and visited[x, y] == 0:
                    after.append((x, y))
                    table[x, y, 0] = point[0]
                    table[x, y, 1] = point[1]
                    table[x, y, 2] = dist
                    visited[x, y] = 1
                    done = x == x_f and y == y_f
                    if done:
                        break
            if done:
                break
        previous = after
        history.append(previous)

    return history, table


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    s1 = s2 = s3 = s4 = 1
    # s1 = 2
    # s2 = 2
    # s3 = 3
    # s4 = 3
    for xi in range(0, S, s1):
        for yi in range(0, S, s4):
            for xf in range(0, S, s2):
                for yf in range(0, S, s3):
                    h, t = find_path(xi, yi, xf, yf)

                    print("(", xi, yi, ")", "->", "(", xf, yf, ") dist", t[xf, yf, 2], "path:", end=" ")
                    path = set_path(t, xi, yi, xf, yf)
                    # print(type(path))
                    # exit(1)
                    for p in reversed(path[1:]):
                        print(p, "-> ", end="")
                    print(path[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
