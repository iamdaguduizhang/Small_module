# -*- coding:utf-8 -*-
# @Time    :2019-10-16 15:50
# @Author  :Dg

from threading import Thread
import time


def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True


def main():
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


def main2():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


def main3():
    start_time = time.time()
    t1 = Thread(target=my_counter)
    t2 = Thread(target=my_counter)
    t1.start()
    t2.start()
    t1.join()
    # t2.start()
    t2.join()
    end_time = time.time()
    print("totle_time: {}".format(end_time - start_time))


if __name__ == '__main__':
    main3()


# GIL  保证同一个进程内，同一时刻只能有一个线程在执行，为了保证数据的完整性和状态同步的问题。
# 多线程代码的话，解释器分时使用，使得不同的线程都能使用到解释器。切换频繁，给人并行的感觉，其实是并发，并且单核cpu'没有真正的并行。
# 即使是GIL也不能保证数据的安全，
# 在cpu计算密集型的时候。解释器会每隔100次或每隔一定时间15ms去释放GIL。唤起线程，线程获得执行权这里会浪费时间，所以多线程会比单线程更慢
# I/O阻塞的时候GIL会被释放.计算机密集的时候，解释器会每隔100次或每隔一定时间15ms去释放GIL。线程抢夺
# 所以，这里可以理解为IO密集型的python比计算密集型的程序更能利用多线程环境带来的便利。


# 举例 比如一个 ArrayList 类，在添加一个元素的时候，它可能会有两步来完成：1. 在 Items[Size] 的位置存放此元素；2. 增大 Size 的值。
#
# 在单线程运行的情况下，如果 Size = 0，添加一个元素后，此元素在位置 0，而且 Size=1；
# 而如果是在多线程情况下，比如有两个线程，线程 A 先将元素存放在位置 0。但是此时 CPU 调度线程A暂停，
# 线程 B 得到运行的机会。线程B也向此 ArrayList 添加元素，因为此时 Size 仍然等于 0 （
# 注意哦，我们假设的是添加一个元素是要两个步骤哦，而线程A仅仅完成了步骤1），
# 所以线程B也将元素存放在位置0。然后线程A和线程B都继续运行，都增加 Size 的值。
# 那好，现在我们来看看 ArrayList 的情况，元素实际上只有一个，存放在位置 0，而 Size 却等于 2。这就是“线程不安全”了。