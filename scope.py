# global scope
name = "Global"
number = 1 


def function_rafael():
    # Local scope
    name = "Local"

    def inner_function():
        # Internal scope
        name = "Internal"
        print(name)
        return name
        # Internal scope end
    
    
    inner_function()
    print(name)
    #print(locals())
    return name
    # Local scope end

function_rafael()

print(globals()['name'])



# global scope end