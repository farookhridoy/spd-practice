# enqueue
# dequeue
# initial a empty queue


def make_queue():
    qe = []
    global MAXSIZE
    MAXSIZE = 5
    # global f
    # f = -1
    # global r
    # r = 1
    return qe

# empty


def is_empty(qe):
    return len(qe) == 0

# enqueue


def enqueue(qe, item):
    if (len(qe) <= MAXSIZE):
        qe.append(item)
    else:
        print('Queue is full')
        # f += 1
        # r += 1

# dequeue


def dequeue(qe):
    if (is_empty(qe)):
        return "It's empty"
    else:
        # f -= 1
        # r -= 1
        return qe.pop(0)


# def f_element(qe):
#     if (is_empty(qe)):
#         return f + "&" + r


qe = make_queue()

enqueue(qe, 'O')
enqueue(qe, 'M')
enqueue(qe, 'A')
enqueue(qe, 'R')
enqueue(qe, 'F')
enqueue(qe, 'A')
print(qe)
enqueue(qe, 'R')

print(dequeue(qe))
print(dequeue(qe))
print(dequeue(qe))
print(dequeue(qe))
print(qe)
# print(f_element(qe))
