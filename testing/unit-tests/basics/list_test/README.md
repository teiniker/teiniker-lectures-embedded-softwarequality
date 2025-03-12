# Example: List Test


A **list** is a **collection of items in a particular order**.
Square brackets `[]` indicate a list, and individual elements in the list are separated by commas.


## Setup Phase
We can factor out set-up code by implementing a method called `setUp()`,
which the testing framework will automatically call for every single
test we run.

```Python
    def setUp(self):
        self.list = ['homer', 'marge', 'bart']
```

## Test Cases
   
To **access an element in a list**, write the name of the list followed
by the index of the item enclosed in square brackets.
By asking for the item at index -1, Python always returns the last item in the list.
```Python
    def testListIndex(self):
        # exercise & verify
        self.assertEqual('marge', self.list[1])
        self.assertEqual('bart', self.list[-1])
```


The function `len()` returns the **length of a list**.
```Python
    def testListSize(self):
        # exercise
        actual = len(self.list)
        # verify
        expected = 3
        self.assertEqual(expected, actual)
```


To **change an element**, use the name of the list followed by the index of
the element you want to change, and then provide the new value you want
that item to have.
```Python
    def testListModifyElement(self):
        # exercise
        self.list[2] = 'lisa'
        # verify
        expected = ['homer', 'marge', 'lisa']
        self.assertEqual(expected, self.list)
```

The simplest way to **add a new element** to a list is to append the item
to the list.

```Python
    def testListAppend(self):
        # exercise
        self.list.append('lisa')
        # verify
        expected = ['homer', 'marge', 'bart', 'lisa']
        self.assertEqual(expected, self.list)
```

We can **add a new element at any position** in our list by using the
`insert()` method. We do this by specifying the index of the new element
and the value of the new item.

```Python
    def testListInsert(self):
        # exercise   
        self.list.insert(1,'lisa')
         # verify
        expected = ['homer', 'lisa', 'marge', 'bart']
        self.assertEqual(expected, self.list)
```

If we know the **position of the item we want to remove** from a list,
we can use the del statement.
```Python
    def testListDeleteElement(self):
        # exercise
        del self.list[1]
        # verify     
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)
```

The `pop()` method **removes the last item in a list**, but it lets us work
with that item after removing it.
```Python
    def testListPop(self):
        # exercise
        s = self.list.pop()
        # verify    
        expected = ['homer', 'marge']
        self.assertEqual(expected, self.list)
        self.assertEqual('bart', s)
```

We can actually use pop() to **remove an item in a list at any position**
by including the index of the item we want to remove in parentheses.
```Python
    def testListPopWithIndex(self):
        # exercise
        s = self.list.pop(1)
        # verify
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)
        self.assertEqual('marge', s)
```

If we only know the value of the item we want to remove, we can use
the `remove()` method, which deletes only the first occurrence of the value we
specify. If there is a possibility the value appears more than once in
the list, we will need to use a loop to determine if all occurrences of
the value have been removed.
```Python
    def testListRemove(self):
        # exercise
        self.list.remove('homer')
        # verify
        expected = ['marge', 'bart']
        self.assertEqual(expected, self.list)
```

The `sort()` method **changes the order of the list permanently**.
The `sorted()` function can also accept a reverse=True argument if we
want to display a list in reverse alphabetical order.
```Python
    def testListSort(self):
        # exercise
        self.list.sort()
        # verify
        expected = ['bart', 'homer', 'marge']
        self.assertEqual(expected, self.list)
```

To **reverse the original order** of a list, we can use the `reverse()` method.
```Python    
    def testListReverse(self):
        # exercise
        self.list.reverse()
        # verify
        expected = ['bart', 'marge', 'homer']
        self.assertEqual(expected, self.list)
```

To **make a slice**, we specify the index of the first and last elements
we want to work with.
```Python
    def testListSlice(self):
        # exercise    
        slice = self.list[1:2]  # [from:to)
        # exercise
        expected = ['marge']
        self.assertEqual(expected, slice)
```

When we wrap `list()` around a call to the `range()` function, the output
will be a **list of numbers**.
```Python
    def testListRange(self):
        # exercise
        numList = list(range(3,7))  # [from:to)
        # verify 
        expected = [3, 4, 5, 6]
        self.assertEqual(expected, numList)
```


## Special Assert Methods

* **assertListEqual(first, second, msg=None)**\
Tests that two lists or tuples are equal.
If not, an error message is constructed that shows only the differences
between the two. An error is also raised if either of the parameters
are of the wrong type.
These methods are used by default when comparing lists or tuples with
`assertEqual()`.
```Python
    def testListEqual(self):
        # Verify
        expected = ['homer', 'marge', 'bart']
        self.assertListEqual(expected, self.list)
```


* **assertCountEqual(first, second, msg=None)**\
First and second have the same elements in the same number, regardless of their order.
```Python
    def testCountEqual(self):
        # Verify
        expected = ['homer', 'marge', 'bart']
        self.assertCountEqual(expected, self.list)
```

    

*Egon Teiniker, 2020-2022, GPL v3.0*

 