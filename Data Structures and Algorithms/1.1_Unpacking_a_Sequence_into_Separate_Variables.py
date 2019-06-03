##Problem
You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

##Solution
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. 
The only requirement is that the number of variables and structure match the sequence. For example:

##Examples 

####1)
```
>>> p = (4, 5) 
>>> x, y = p 

>>> x
4

>>> y 
5
```
####2)
```
>>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ] 
>>> name, shares, price, date = data

>>> name
'ACME'

>>> date 
(2012, 12, 21)
```


####3)
```
>>> name, shares, price, (year, mon, day) = data 

>>> name
'ACME'

>>> year 2012
>>> mon 12
>>> day 21
```

####4)
If there is a mismatch in the number of elements, you’ll get an error. For example:
```
>>> p = (4, 5)
>>> x, y, z = p

Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack
>>>
```



