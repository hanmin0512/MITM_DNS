#define error
def func1(n1,n2):
    def func2(v1,v2):
        return v1+v2
    return func2(n1,n2)

print(func1(100,200))
print(func2(200,300))
