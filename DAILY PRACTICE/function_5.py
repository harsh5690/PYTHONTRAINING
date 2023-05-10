"""
*args and "kwargs"

args = arguments ( tuple as a parameter )
kwargs : key with arguments (dictionary as a parameter)


"""

def args_example(*a):
    print(a)

args_example(12,2,3,158,8198,198,78)

# dictionary as a parameter
def mydict_example(**kwargs):
    for k,v in kwargs.items():
        
        print(f"{k}={v}")

mydict_example(name="python",cetagory="programming")