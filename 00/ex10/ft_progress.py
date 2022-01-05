import sys
import time

start_time = time.time()


def ft_progress(aList):
    count = len(aList)

    def show(j):
        x = int(20 * j / count)
        print("ETA: {:.2f}s [{:3d}%][{}>{}] {}/{} | {} {:.2f}".format(
            ((count - j)*(time.time() - start_time)/j),
            int(j / count * 100),
            '='*x, ' '*(20 - x),
            j,
            count,
            "elapsed time",
            (time.time() - start_time)),
            end='\r')

    show(1)
    for i, item in enumerate(aList):
        yield item
        show(i+1)
    print()


if __name__ == "__main__":
    print("example 1:")
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
    start_time = time.time()
    print("\nexample 2:")
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)
