import inspect



class its_PHP():


   

    # i will create a function here to let a user output a php function with python code
    def php_function(self, name:str, params:str, action_type=str ):
        if(action_type == "print"):
            reason = "echo" + ""        
            the_function = f"<?php function {name}(${params}) {reason}  ?>"

        return the_function
    ## I will try another approach where the full function gets converted
    def php_full(self, my_func):
        source = inspect.getsource(my_func)
        lines = source.splitlines()
        new_array = []
        for i in lines:
            new_array.append(i)
        if"print" in new_array:
            new_array.remove("print")



        print(new_array)




tryout = its_PHP()
print(tryout.php_function("math_one", "x", "print"))

def first_try():
    x= "hello world"
    print(x)

tryout.php_full(first_try)



        