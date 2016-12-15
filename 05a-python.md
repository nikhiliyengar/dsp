# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both collections of elements. However, lists are mutable, while tuples are immutable.   
   Tupples will work as keys in dictionaries, because the keys of a dictionary need to be immutable, in order to be hashable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are both collections of itens. However, unlike lists, each item in a set must be unique and hashble, and sets do not have any order.  
   As their size increases, lists are faster to iterate through than sets, and sets are faster to check for a particular element.  
   In general, lists are suited for ordered, mutable collections, and sets for unique, unordered collections.  
   Examples : A) A set of student unique IDs:  setofids = SET ( [ 1001,1002,1003,1004] )  
              B) A record of daily temperatures for the month: temperatures = [65,70,65,68]  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 'Lambda' is used to create anonymous functions at runtime.  
   Example:  
    GOT_exit_tuples = [  
        ('Rob Stark', 'The Twins', 3),  
        ('Ned Stark', 'King's Landing', 1),  
        ('Rickon Stark', 'Winterfell', 6),  
]  
sorted(GOT_exit_tuples, key=lambda GOT_exit: GOT_exit[2])   # sort by season of departure of Game of Thrones character  
[ ('Ned Stark', 'King's Landing', 1),('Rob Stark', 'The Twins', 3),('Rickon Stark', 'Winterfell', 6),]  
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





