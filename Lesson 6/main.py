sample_list=[1,2,1,3,2,4,3,5,4,5]
print(sample_list)
sample_set=set(sample_list)
print(sample_set)

if 6 in sample_set:
    print("yes")
else:
    print("no")

my_set=set([])
my_set.add(10)
my_set.add(15)
my_set.add(18)
my_set.add(14)
my_set.add(12)
print(my_set)
my_set.remove(15)
print(my_set)