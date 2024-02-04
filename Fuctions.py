
def my_fun():
    print("my name is Rihan")

my_fun()


def my_function_with_arg(name, id):
    print("hello is my name %s and my id %d" %(name, id))

my_function_with_arg("rohan" ,12)


# return

def my_fun(a, b):
    return a + b

print(my_fun(12, 5))



def list_return_fun():
    return ["str", "add"]

print(list_return_fun())


def new_str_save(myarr):
    for i in list_return_fun():
        myarr.append(i)
        return myarr



print(new_str_save([]))