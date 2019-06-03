## Problem
You need to unpack N elements from an iterable, but the iterable may be longer than N elements,
causing a “too many values to unpack” exception.

## Solution
Python “star expressions” can be used to address this problem. 

For example, suppose you run a course and decide at the end of the semester that you’re going to drop the first and last
homework grades, and only average the rest of them. If there are only four assignments, maybe you simply unpack all four, 
but what if there are 24? A star expression makes it easy:

## Examples 

1)  def drop_first_last(grades): 
        first, *middle, last = grades 
        return avg(middle)

2)  As another use case, suppose you have user records that consist of a name and email address, followed by an arbitrary number
of phone numbers. You could unpack the records like this:

>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212') 
>>> name, email, *phone_numbers = user_record
>>> name
'Dave'
>>> email
'dave@example.com'
>>> phone_numbers ['773-555-1212', '847-555-1212'] >>>

3)
records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
]

def do_foo(x, y): 
    print('foo', x, y)

def do_bar(s): 
    print('bar', s)

for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)

4)
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false' 
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname 'nobody'
>>> homedir '/var/empty'
>>> sh '/usr/bin/false' >>>

5)
Sometimes you might want to unpack values and throw them away. You can’t just specify a bare * when unpacking, but you
could use a common throwaway variable name, such as _ or ign (ignored). 

For example:
>>> record = ('ACME', 50, 123.45, (12, 18, 2012)) >>> name, *_, (*_, year) = record
>>> name
'ACME'
>>> year 2012
>>>
There is a certain similarity between star unpacking and list-processing features of var‐ ious functional languages. For example, if you have a list, you can easily split it into head and tail components like this:
>>> items = [1, 10, 7, 4, 5, 9] >>> head, *tail = items
>>> head
1
>>> tail
[10, 7, 4, 5, 9] >>>
One could imagine writing functions that perform such splitting in order to carry out some kind of clever recursive algorithm. For example:
>>> def sum(items):
... head, *tail = items
... return head + sum(tail) if tail else head ...
>>> sum(items)
36
>>>
