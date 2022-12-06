
input = [[1,'a',['cat',[1,"bünyamin"]],2],[[[3]],'dog'],4,5]
f = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            f.append(i)

flatten(input)
print(f)