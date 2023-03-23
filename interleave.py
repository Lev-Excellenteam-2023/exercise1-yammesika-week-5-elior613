# def interleave(*arg):
#     new_list=[]
#     for item in zip(*arg):
#          new_list+=item
#     return new_list
# print(interleave('abc', [1, 2, 3], ('!', '@', '#')))

def interleave(*arg):
    for item in zip(*arg):
        for i in item:
            yield i
l=list(interleave('abc', [1, 2, 3], ('!', '@', '#')))    
print(l)