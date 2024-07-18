#sep 구분자 매개변수 기억 안 나니?
x = 15
print(x,"의 데이터 타입은 " ,type(x) ,"입니다.",sep="")

x2=3.141592
print(x2,"의 데이터 타입은 " ,type(x2) ,"입니다.",sep="")


fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", [1, 2, 3]]
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed List:", mixed_list)

mixed_list[2:3]

numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", [1, 2, 3]]
for _ in range(len(mixed_list)):
    numbers.append(10)
    
def min_max(numbers):
    return min(numbers), max(numbers)
result = min_max([1, 2, 3, 4, 5])
result = min_max((1, 2, 3, 4, 5))
print("Minimum and maximum:", result)

person = {
'name': 'John',
'age': 30,
'city': 'New York'
}
print("Person:", person)

person.get('name')
person['name'] = "yonggyu"
print("Person:", person)

fruits = {'apple', 'tomato', 'melon'}

empty_set = set()
empty_set

empty_set.add("apple")
empty_set.union(fruits)

empty_set.remove("apple")
empty_set

empty_set.add("apple")
empty_set

empty_set.pop()
empty_set

other_fruits = {'berry', 'cherry'}
union_fruits = fruits.union(other_fruits)
intersection_fruits = fruits.intersection(other_fruits)
print("Union of fruits:", union_fruits)
print("Intersection of fruits:", intersection_fruits)

p = True
q = False
print(p, type(p))
print(q, type(q))
print(p + p)

num = 123
str_num = str(num)
print("문자열:", str_num, type(str_num))

num_again = float(str_num)
print("숫자형:", num_again, type(num_again))

set_example = {'a', 'b', 'c'}

dict_from_set = {key: True for key in set_example}

dict_from_set = {key: 'a' for key in set_example}

print("Dictionary from set:", dict_from_set)

#-----------------------------

import seaborn as sns
import pandas as pd
import numpy as npy
import matplotlib.pyplot as plt
import math
import sklearn.metrics

print("1")

var = ["a","b","c","d"]
var

sns.countplot(x = var)
plt.show()
var = ["a", "b", "a", "a", "c", "b", "c", "a", "d", "d"]
data = pd.Series(var)


sns.countplot(x=data)

df_titanic = sns.load_dataset("titanic")
df_titanic

sns.countplot(data = df_titanic, x = 'class')

sns.countplot(data = df_titanic, y = 'class',hue = "alive")
plt.show()
plt.clf()


#축이 왜 이 모양? abcd 어디서 나왔지 (clf 안하면 전에거 섞임)



