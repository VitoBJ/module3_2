def print_params(a=1, b='string', c=True):
   print(a,b,c)
print_params()
def print_params(a=5, b=9, c=6):
    print(a,b,c)
print_params()

print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, c=False)

   
values_list = [52, "Testing", 1987]
values_dict = {
    'a': 87,
    'b': "Covid",
    'c': False
}

print()
print_params(*values_list)

print()
print_params(**values_dict)


values_list_2 = [32, 'True']
print()
print_params(*values_list_2, 24)





