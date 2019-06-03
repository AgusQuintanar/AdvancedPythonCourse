###
### Works with tuples, lists, strings, files, iterators, and generators
###

### EXERCISES

#1) 
def unpackSeguenceOf5Items(object):
    a,b,c,d,e = object

    print("a:",a)
    print("b:",b)
    print("c:",c)
    print("d:",d)
    print("e:",e)

    print('------------------------------------------------------------------------------')


unpackSeguenceOf5Items('Hello')
unpackSeguenceOf5Items((1,2,3,4,5))
unpackSeguenceOf5Items(['dog',[1,2,3.4,3.1],True,'a',('apple', 'banana', 'orange')]) 