def create_full_name(f, m, l):
    fn = f + " " + m + " " + l
    return fn


def get_name_list(fn):
    name_list = fn.split(" ")
    return name_list


def get_first_name(fn):
    name_list = fn.split(" ")
    f = name_list[0]
    return f


def get_middle_name(fn):
    name_list = fn.split(" ")
    m = name_list[1]
    return m


def get_last_name(fn):
    name_list = fn.split(" ")
    l = name_list[2]
    return l


#### Module Test Program #####
#### Un-comment the following lines to test module code #####


first = "Vivian"
middle = "Elizabeth"
last = "Reed"

full_name = create_full_name(first, middle, last)
print(full_name)

nList = get_name_list(full_name)
print(nList)

first = get_first_name(full_name)
print(first)

middle = get_middle_name(full_name)
print(middle)

last = get_last_name(full_name)
print(last)
