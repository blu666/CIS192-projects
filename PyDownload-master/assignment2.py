""" CIS 192 Python Programming
    Do not distribute. Collaboration is NOT permitted.
"""

# Pro tip: think long and hard about testing your code.
# In this assignment, we aren't giving you example function calls.

def my_sort(lst):
    ''' Return a sorted copy of a list. Do not modify the original list. Do
    not use Python's built in sorted method or [].sort(). You may use
    any sorting algorithm of your choice.
    '''
    copy = lst.copy()
    if (len(copy) - 1) < 0:
        return copy
    else:
        p_index = int(len(copy) / 2)
        loc = partition(copy, 0, len(copy) - 1, p_index)
        result = my_sort(copy[0: loc])
        result.append(copy[loc])
        result.extend(my_sort(copy[loc+1:]))
        return result

def partition(lst, lo, hi, pIndex):
    pivot = lst[pIndex]
    lst[pIndex], lst[hi] = lst[hi], lst[pIndex]
    left = lo
    right = hi - 1
    while left <= right:
        if lst[left] <= pivot:
            left += 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
    lst[left], lst[hi] = lst[hi], lst[left]
    return left

def sort_dict(d):
    ''' Sort a dictionary by value. The function should return
    (not print) a list of key, value tuples, in the form (key, value).
    '''
    temp_d = {d.get(k): k for k in d.keys()}
    sorted_val = sorted(temp_d.keys())
    return [(temp_d.get(v), v) for v in sorted_val]

def prefixes(seq):
    ''' Create a generator that yields all the prefixes of a 
    given sequence. Extra credit will be rewarded for doing this 
    in a single line.
    '''
    return (seq[:i] for i in range(len(seq)+1))

def suffixes(seq):
    ''' Create a generator that yields all the suffixes of a 
    given sequence. Extra credit will be rewarded for doing this 
    in a single line.
    '''
    return (seq[i:] for i in range(len(seq)+1))

def slices(seq):
    ''' Create a generator that yields all the slices of a 
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    def gen():
        yield seq[0:0]
        for i in range(len(seq)):
            for j in range(i+1, len(seq)+1):
                yield seq[i:j]

    return gen()

def extract_and_apply(l, p, f):
    '''
    Implement the function below in a single line:
        def extract_and_apply(l, p, f):
            result = []
            for x in l:
                if p(x):
                    result.append(f(x))
            return result
    where l is a list, p is a predicate (boolean) and f is a function.
    '''
    return [f(x) for x in l if p(x)]

def my_reduce(function, l, initializer=None):
    '''Apply function of two arguments cumulatively to the items of list l, from left to right,
    so as to reduce l to a single value. This is equivalent to the 'fold' function from CIS 120.
    If the optional initializer is present, it is placed before the items of l in the calculation, 
    and serves as a default when the sequence is empty. 
    If initializer is not given and sequence contains only one item,
    the first item is returned. You may assume that if no initializer is given, the sequence will not
    be empty.
    '''
    if len(l) == 0:
        return initializer
    elif len(l) == 1 and initializer == None:
        return l[0]
    else:
        temp = function(initializer, l[0])
        for i in range(1, len(l)):
            temp = function(temp, l[i])
        return temp

class BSTree(object):
    ''' Implement a binary search tree.
    See here: http://en.wikipedia.org/wiki/Binary_search_tree
    or https://www.seas.upenn.edu/~cis120/current/notes/120notes.pdf
    The examples in the test file illustrate the desired behavior.
    Each method you need to implement has its own docstring
    with further instruction. You'll want to move most of the
    implementation details to the Node class below.
    '''

    def __init__(self):
        self.root = None

    def __str__(self):
        ''' Return a representation of the tree as (left, elem, right)
        where elem is the element stored in the root, and left and right
        are the left and right subtrees (which print out similarly).
        Empty trees should be represented by underscores. Do not include spaces.
        '''
        if self.root is None:
            return "(_,_,_)"
        else:
            return str(self.root)

    def __len__(self):
        ''' Returns the number of nodes in the tree.'''
        return len(self.root)

    def __contains__(self, element):
        ''' Finds whether a given element is in the tree.
        Returns True if the element is found, else returns False.
        '''
        return self.root.contains(element)

    def insert(self, element):
        ''' Insert a given value into the tree.
        Our implementation will allow duplicate nodes. The left subtree
        should contain all elements <= to the current element, and the
        right subtree will contain all elements > the current element.
        '''
        if self.root is None:
            self.root = Node(element)
        else:
            self.root.insert(element)

    def elements(self):
        ''' Return a list of the elements visited in an inorder traversal:
        http://en.wikipedia.org/wiki/Tree_traversal
        Note that this should be the sorted order if you've inserted all
        elements using your previously defined insert function.
        '''
        if self.root is None:
            return []
        else:
            return self.root.elements()


class Node(object):
    ''' A Node of the BSTree.
    Important data attributes: value (or element), left and right.
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        if self.left is None:
            if self.right is None:
                return "(_," + str(self.val) + ",_)"
            else:
                return "(_," + str(self.val) + "," + str(self.right) + ")"
        else:
            if self.right is None:
                return "(" + str(self.left) + "," + str(self.val) + ",_)"
            else:
                return "(" + str(self.left) + "," + str(self.val) + "," + str(self.right) + ")"

    def __len__(self):
        if self.left is None:
            if self.right is None:
                return 1
            else:
                return 1 + len(self.right)
        else:
            if self.right is None:
                return 1 + len(self.left)
            else:
                return 1 + len(self.left) + len(self.right)

    def contains(self, element):
        if self.val == element:
            return True
        if self.left is None:
            if self.right is None:
                return False
            else:
                return self.right.contains(element)
        else:
            if self.right is None:
                return self.left.contains(element)
            else:
                return self.left.contains(element) or self.right.contains(element)

    def insert(self, element):
        if self.val == element:
            new_node = Node(element)
            new_node.left = self.left
            self.left = new_node
        elif self.val > element:
            if self.left is None:
                self.left = Node(element)
            else:
                self.left.insert(element)
        else:
            if self.right is None:
                self.right = Node(element)
            else:
                self.right.insert(element)

    def elements(self):
        if self.left is None:
            if self.right is None:
                return [self.val]
            else:
                return [self.val] + self.right.elements()
        else:
            if self.right is None:
                return self.left.elements() + [self.val]
            else:
                return self.left.elements() + [self.val] + self.right.elements()
