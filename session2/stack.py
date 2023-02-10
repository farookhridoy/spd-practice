# push
# pop
# MAXSIZE 10
# TOP = -1

def make_stack():
    global MAXSIZE
    MAXSIZE = 5
    st = []
    return st

# empty


def is_empty(st):
    len(st) == 0

# push


def push(st, value):
    if (len(st) <= MAXSIZE):
        st.append(value)
    else:
        print('Stack is full')

# pop


def pop(st):
    if is_empty(st):
        return "it's already empty"
    else:

        return st.pop()


st = make_stack()
push(st, 'S')
push(st, 'T')
push(st, 'A')
push(st, 'C')


print(st)
push(st, 'O')
print(pop(st))
