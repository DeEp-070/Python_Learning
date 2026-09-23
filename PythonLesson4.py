#List comprehension
prices = [100, 200, 300,5,7,3,6]
res = [n*n for n in prices]
print(res)

prev_res = [n*100 for n in prices]
print(prev_res)

res_even = [n if n%2==0 else "odd number" for n in prices]
print(res_even)

#Dictionary and set comprehension

#dictionary
dict_res = {n:n*n for n in prices}
print(dict_res)

#set
set_unique_res = {len(str(n)) for n in prices}
print(set_unique_res)
print("Sum of the prices: ",sum(n*n for n in prices))

#enumerate
dict_enum = {}
for i,j in enumerate(prices):
    dict_enum.update({i:j})
print(dict_enum)

#zip (combines iterables)
dict_zip = {}
names = ["Ajay", "ram", "Sam"]
scores = [85, 92, 78]
for name , score in zip(names,scores):
    dict_zip.update({name:score})
print(dict_zip)

# sorted() return a new list
# sort() change the existing list

#reversed() does not return a list