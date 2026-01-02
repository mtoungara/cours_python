# Git commande

git init 

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/mtoungara/ansible.git

git push -u origin main

# Update your git remote url

git remote set-url origin git@github.com:mtoungara/cours_python.git

# Now you can push without a password

git push -u origin main

## Python and Pandas for data engineering 

- Objectives 

    - Write functions   
    - Call function 
    - Assign parameter values by order 

- function syntax
def my_func():
    print('hello world')
my_func()

- pass statement 

def do_nothing():
    pass

return statement 
do_nothing() == None

def ret_two():
    return 2
ret_two()

- Parameters
def add_one(num):
    return num + 1
add_one(2)

add_one(5)

parameters by order and by name 

def my_func(first, second, third):
    print(first)
    print(seconde)
    print(third)

my_func(1,3,4)

my_func(third=1, first=4, second=22)

my_func(2, third=4, second=3)

- Setting default values 

def say_hello(name="Linux"):
    print("hello " + name)

- function syntax
def my_func():
    print('hello')

my_func()

- Pass statement 
    def do_nothing():
        pass 

return statement 
do_nothing() == None

def ret_two():
    return 2

    ret_two()

parameters

def add_one(num):
    return num + 1

add_one(2)

add_one(5)

parameters by order and by name 

def my_func(first, second, third):
print(first)
print(second)
print(third)

my_func(1,3,4)

my_func(third1, first=4, second=22)

my_func(2, thirs=4, second=3)

Setting default values

def say_hello(name"Linux"):
    print("Hello " + name)
say_hello()

## Exercices

    - Timing Decorator

    # Function decorator that times execution 

    from time import time 

    def timer(funct):
        # Nested wrapper function 
        def wrapper():
            start = time()
            func()
            end = time()
            print(f"Duration: {end-star}")
        return wrapper

@timer
def sum_num():
result = 0
for x in range(2000000):
    result +=x
sum_num()

## Listes et tubles en Python

- lists
    - hold items of any data type
    - mixed data types
    - mutable 
        - adding 
        - removing 
        - reordering

- Tuples 
    - hold items of any data type
    - mixed data types
    - immutable
        - set during creation

## Creation 
tuple()

list()

tup = (1,2)

some_list = [1,2,3]

some_tuple = (1)

name = "transformer"
letters = list(name)
letters

composers = ('valid', 'test')

composers.append('linux')
composers

composers.insert(0,"cloud")
composers

composers.pop(0)

vips.extend(composers)
vips

list = [()] = 4 

lists[-1].append(4)
lists
lists = [[] for _ in range(4)]
lists (-1).append(4)
lists

## Ordering 

name = "linux"
letters = list(name)
letters

letters.sort()
letters
letters.revers()
letters


## Chaines de Caractères

- Create strings
- Change capitalization 
- Interrogation methods 
- F-strings

## Strings

'here is a string' 

"here is a string" == 'Here is a string'

'Here "is" a string 

a_very_large_phrase = === Wikipedia is hosted by the wikimedia fondation, a non-profit organization that also hosts a range of other projets. 

print(a_very_large_phrase)

print("Ludwing\tBeethoven")

windows_path = "c:\tam\Projects\now"
print(windows_path)

bill = "William Byrd"
bill

bill.capitalize()

bill.lower()

bill.upper()

## Interrogation 

leo = 'leonin'

leo.index(e)

leo.index('r')

leo.startswith('L')

leo.endswith('in')
'abc123'.isalpha()
'abc123'.isnum()
lowercase.islower()
'lowercase'.isupper()

one = '1'
one.isnumeric()

f"Example {1}"

## Insert variable into replacement field 

strings_count = 5
frets_count = 24
f"Noam Pikelny's banjo has {strings_count} strings and {frets_count} frets"

## Insert experession into replacement field 

a = 12 
b = 32

f"{a} times {b} equals {a+b}"

players = ["Tony Trischka", "Bill Evans", "Alan Munder"]
f"Performances will be help by {players[]}, {players[0]}, and {players[2]}"

Paddind a number 

lucky_num = 13

f"To pad the number {lucky_name} to 5 places:{lucky_num:54}"

## Setting padding value at runtime 

luckey_num = 13
padding = 5 
f"To pad the number {lucky_num} to {padding} places:{lucky_name:{padding}d}"

## Commas
balance = 1232980098
print(f"Your balance is {balance:,}")

## Manipulate strings

    - Removing whitespace
ship = " Python sous Linux "
ship 

ship.strip()

ship.lstrip()

ship.rstrip()

## Spitting and Joining

words_string = "Here, Are, Some, Words"
words_string 

## Split on comma 

words = words_string.split(',')
words

## Joining
':'.join(words)

## Split on newline 
multiline = "Sometimes we are given\na multiline document\nas a single string"
multiline

multiline.splitlines()


## Range Objects

## Strings
name = 'username'
name
name.endswitch('in')
'username'.isupper()
"Hello " + "my name is name "
name = 'username'
name.endswith('in')
f'Hello {name}'

## Creating Object Range

range(2,10)
list(range(1, 10))
import sys
r = range(10000000)
sys.getsizeof(r)
l = list(range(10000000))
list(range(0,10,2))
list(range(10, 0, -2))
sys.getsizeof(l)
list(range(0,10,2))
list(range(10,0, -2))
start = 0
for count in range(5):
    start +=count
    print{start}
    
##
# Create a set 
set1 = {"value1", "value2", "value3"}

# Add new element
set1.add("value4")
print(set1)

# Set union 
set2 = set1 & set2
print(set4)

# Set difference
set5 = set1 - set2
print(set5)

## Creating Dictonaries

key_1 = "user_name"
key_1.__hash__()
dict(name="userm_name", service="cloud infrastructure")
{'name':'prenom', 'service':cloud infrastructure}
{'name':'prenom', 'service':cloud infrastructure}
{'name':'prenom', 'service':cloud infrastructure}
{'name':'prenom', 'service':cloud infrastructure} == {'service':cloud infrastructure, 'systeme': 'Linux'}

## Sets and Set Operations

- Sets

set("aaabbbcc")

s = set('aaabbbccc')

s.add('d')

s.pop()

s.remove('b')

## Set Operations

## Disjoint 
Two sets are disjoint if they have no items in common

s1.disjoint(s2)
## Subset 
s1 = set(range(10))

s2 = set(range(2,6))
s2.ssubset(s1)

s2 = set("Herman")

s1.union(s2)

s2.issubset(s1)

## Intersection 
s1 = set(range(5))
s2 = set(range(2,9))
s1.intersection(s2)
## Superset
- All items of second set are found in the first 
s1.issuperset(s2)
## Union 

s1 = set(range(10))

## Difference 
items from first set that are not in second

s1.difference(s2)

## List Comprehensions 

output = []

for x in range (10):
    output.append(x==2)

output 

output = [x==2 for x in range (10)]
output 

## Map

import randos

scores = []

for i in range(5):
    scores.append(random.randint(1,10))

scores

[random.randin(i, 10) for in range (5)]

## Filter

caps = []

for letter in "Henry Honey":
    if letter.isupper():
        caps.append(letter)

caps

[letter for letter in "Henry Honey" if letter.isupper()]

## Nest

list_of_lists = [('a','b','c'),('d','e','f'),('g','h','i')]
flat = []

for sub_list in list_of_lists:
    for item in sub_list:
    flat.append(item)

flat

[item for sublist in list_of_lists for item in sublist]

## Generator Expressions
large_num = 99999999
l_squares = [x==2 for x in range(large_num)]

import sys
sysgetsizeof(l_squares)

g_squares = (x==2 for x in range (large_num))
sys.getsizeof(g_squares)

g_squares

next(g_squares)

for x in g_squares:
print(x)
if x > 12:
break 

evens = (x for in range(0, 100, 2))
div_three = (y for y in events if y == 0)
netx(div_tree)

for x in g_squares:
    print(x)
    if x > 12:
        break

Chaining Generator Expressions 
evens = (x for x in range(0, 100, 2))
div_three = (y for y in events if y/3 == 0)
next(div_three)

[x for x in div_three]

## Generator functions
def return_num():
    for x in range(5):
    yield x
gen_num = return_num()

netx(gen_num)

def counter(x):

    while True:
        yield x
        x += 1
    
    count = counter(12)

    next(count)

    def fib():
        for cur in (0,1):
            last = cur 
            yield cur
        while True:
            yield cur 
            last, cur = cur, last + cur 

f = fib()

next(f)

## Comprehensions and Generators in Python

## Creating DataFrames 

import pandas as pd 

## From dictionary 

data = { "Name" [ 'script', 'linux', 'python'],
            "heure": [ 1, 2, 3 ],
            "lecture": [ livre, linux, programming ]
            }
pd.DataFrame(data)
pd.dataFrame(data, columns=['livre', 'livre', 'livre'])

## From List of lists 
data = 

## from File 
file _path = '.../data/USCG.Search.rescue.Stats.cvs'
pd.read_cvs(file_path)

data = { "code_name" [ 'v1', 'v2', 'v3'],
        "nombre": [1, 2, 3]
}
pd.dataFrame(data)

## Investigating Data in Data in a Pandas Dataframe

import pandas as pd 
file_path = '../data/USCG.Search.Rescue.stats.cvs'
df = pd.read_csv(file_path)

## Heads/Tails 
df.head(3)
df.tail(2)

## DataFrame head method 

## DataFrame desciptive statistics

df.describe()
df.min()
df.std()


## Selecting Columns 
df.columns 
df['Cases']
df[['Cases', 'Sorties']]
df.sorties

## Selecting Columns and Rows
df.iloc[3:29, 3:6]
df.iloc[3:29]
df.head()
df.loc[1965:1974, ['Cases' 'Sorties']]

## 
import pandas as pd 

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Comparison operators 
print(df[df['A'] == 2]) # Simple filter

# Boolean operators 
filter = (df['A'] > 1) & (df['B'] == 6)
print(df[filter]) # Complex filter 

# Filters with loc accessor 
filter = df['A'] > 1
print(df.loc[filter])

# isin() method
values = [2, 5]
filter = df['A'].isin(values)
printer(df[filter])

## Manipulating DataFrames

import pandas as pd 
data = {'first' ['M', 'O', 'T'],
        'last': ['R', 'M', 'N'],
        'U':    ['1', '2', '3']}
clients = pd.DataFrame(data)
clients

## Renaming 

clients.rename(columns={'first':'First Name'})
clients.rename(index={0:'a', 1:'b', 2:'c'})
clients
clients.reset_index(implace=True)

## Dropping 
clients.drop(columns='first')
clients.drop(index=0)

## Set Type 
clients.age
clients.age.astype(int)

## Updating Pandas DataFrame Data

- Add rows 
- Update to specific value 
- Update using math operations
- Update using replace method

## Updating DataFrame Data

import pandas as pd
data = {'first': ['A', 'B', 'C'],
        'last':  ['D', 'E', 'F'],
        'e':     ['1', '2', '3'],
        'g_count': [4, 5, 6]}
h = pd.dataFrame(data)
h

## Adding rows
new_data = {'first':['i', 'j'],
            'k':['l', 'm'],
            'n':[7, 8],
            'o_count':[9, 10]}
new_p = pd.DataFrame(new_data)
new_p
p.append(new_p)

## Setting specific value 
q.loc[1, 'first'] = 'R'
q
q.loc[0:1, 'g_count'] = -1
q

## Math Operations
s.g_count + 1

## Replace 
t.replace()

## Applying functions in a pandas dataframe 

- Objectives 
    - accross rows 
    - across colums
    - Applying your own function 
    - Single column

## DataFrame Apply

import pandas as pd 
data =  { 'linux': range(0,1,2),
           'unix': range(3,4,5)
        }
df = pd.DataFrame(data)
df

## Apply

df.apply(sum)
df
df.apply(sum, axis=1)



## Define column function

def b(d):
    if sum(c) > 2:
    return "Greater than 2"
return "Not greater than 2"

## Define row function 

## Expanding results

## Creating NumPy Arrays in Python 

- differences between arrays and arrays and DataFrames 
- create arrays
- Setting array dimensions
- When to use arrays vs Dataframes

    - Nimpy : 
        - Designed for scientific computing 
        - Ndarray object 
        - Highly optimized computational tools
        - Ecosystem of scientific and mathematical libraries 
    - ndarray 
        - size set at creation 
        - single data type 
        - not limited to two dimensions
        - can be reshaped 

    np.arange{10}

    np.arange[3, 12, 4]
    array ([3, 7, 11])
    ## Dimensions and Shape 
    oned = np.arange(21)
    oned
    oned.shape
    oned.ndim
    oned.size
    list_o_lists = [(1,2,3), (4,5,6), (7,8,9)]
    twod = np.array(list_o_lists)
    twod
    twod.ndim
    twod.shape
    oned = np.arange(12)
    oned
    twod = oned.reshape(3,4)
    twod.ndim
    twod.reshape[2,2,3]



    ## Setting data type 
    darray = np.arange(100)
    darray

    darray.dtype
    dtype('int64')
    darray.nbytes
    darray[12] = 'a'
    darray[12] = 0.4
    darray[12]

    ## Broadcasting

    A1 = np.array([1,2,3],
                  [4,5,6],
                  [7,8,9])
    A1.shape

    A2 = np.array([[1,1,1],
                  [1,1,1],
                  [1,1,1]])
    A1 + A2

    A1 + 3

    A3.shape

    A1 + A3
    
    A4 = np.arange(10).reshape(2,1,5)

    A4 = np.arange(10).reshape(2,1,5)
    A4

    A5 = np.arange(14).reshape(2,7,1)
    A5

    A6 = A4 + A5
    A6.shape
    
    ## Matrix Operations

    M1 = np.arange(9).reshape(3,3)
    M1

    M2 = np.arange(2, 11).reshape(3,3)
    M2
    M1.transpose()
    M1.diagonal()
    M1 @ M2

    
        - DataFrame
            - Two dimensional data
            - Multiple data types
            - Data analysis 
            - Data visualization 
        
        - ndarray
            - Multi dimensional data
            - Single data type 
            - Complex numerical calculations

## Spark and Pyspark DataFrames in Python

- Objectives 
    - Distributed solutions for Big Data
    - Lazy evaluation
    - Considerations when choosing Spark

    - Pandas
        . Designef to run on single machine 
        . Performance bound by machines memory
        . Chunking 
        . Upper limit Gigabytes (1? 5? 100?)

## Big Data 
    . Hadoop 
    . Spark : Node 1, Node 1, Node 1 ... Node 1
    . Distributed

## Spark

    . Distributed DataFrames on JVM 
    . Written in Scala
    . PySpark Library 
    . Data sources include Hadoop HDFS, S3, and Streaming 
    . Lazy Evaluation 

Eager (Pandas)
    - Operation --> Calculate result
    - Operation --> Calculate result 
    - Operation --> Calculate result 

Lazy (Spark)

    - Operation 
    - Operation 
    - Operation ---> Calculate result 

## Consideration 

    . Built for big data transformations 
    . Optimized integration plan strategy 
    . Debugging challenges 

## Creating Dask DataFrames in Python 

- Objectives 
    - Create a Dask DataFrame 
    - Use Dask lazy evaluation 
    - Visualize Dask task graph 

## Dask 

- Python native 
- Distributed operations
- Pandas DataFrames 
- NumPy arrays 
- Arbitrary Python code 

    - Dask 

    import pandas as pd 
    import random

    leng = 100000000
    data = { 'a': (random.randint(0,100) for _ in range(leng)),
            'b': (random.randin(2, 200) for _ in range(leng))}

    df = pd.Dataframe(data)
    df.head()

    df.std()

import dask.dataframe as dd
ddf = dd.from_pandas(df, npartitions=3)

ddf

## Dask DataFrame Structure 

ddf.std().compute()
result = ddf.a.sum() - ddf.b.sum()
result 

result.compute()

result.dask
result.visualize()

## Choosing a framework 

Pandas or NumPy vs PySpark or Dask 
            Size of data

Pandas          vs          NumPy 

            Nature of data 

PySpark         vs          Dask 

            Nature of entreprise 

    import polars as pl

    # Create DataFrame 
    data = [{"fruit": "apple", "count":10, "price": 0.50},
            {"fruit": "banana", "count": 20, "price": 0.25}]
    df = pl.from_dicts(data)

    # Expressions to select, filter, aggregate
    sel = df.select(["fruit", "count"]) # Select columns 
    filt = sel.filter(pl.col("fruit") == "apple") # filter rows 
    agg = filt.groupby("fruit").agg(pl.col("count").sum()) # Aggregat 
    print(agg)

## Code 

# Join DataFrames 
joined = df.join(df2, on=["kiwi"])

# Visualize
joined.plot.scatter(x="count", y="price")

## Introduction to Python development environments

## Introduction au mode normal vim

- vim modes 
- moving 
- text editor 
- text editor 
- keyboard only 
- customization through settings and plugins 

## Modes

- normal 
- insert 
- visual 
- command line 

## Switching to normal mode

            - Normal

- Visual    - Insert    - Command Line 

## Basic Navigation 

- h - move left 
- j - move down 
- k - move up 
- l - move right 
- w - word
- b - word beginning
- e - word end 
- gg - top of file 
- G - bottom of file 
- y - copy hightlighted text 
- yw - copy word 
- yy - copy line 
- p - past 
- x - delete character 
- dd - delete line 

    
