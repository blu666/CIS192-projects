""" CIS 192 Python Programming 
    Do not distribute. Collaboration is NOT permitted.
"""

def all_factors(num):
    """ Return the set of factors of n (including 1 and n).
    You may assume n is a positive integer. Do this in one line for full credit.

    Example:
    >>> all_factors(24)
    {1, 2, 3, 4, 6, 8, 12, 24}
    >>> all_factors(5)
    {1, 5}
    """
    return set([i for i in range(1,num+1) if num % i == 0])

def get_student_avg(gradebook_dict, student):
    """ Given a dictionary where each key-value pair is of the form: (student_name, [scores]),
    return the average score of the given student. If the given student does not exist, return -1

    Example:
    >>> get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "Sally")
    90.0
    >>> get_student_avg({"Sally":[80, 90, 100], "Harry": [75, 80, 85]}, "John")
    -1
    """
    if (student not in gradebook_dict):
        return -1
    else:
        student_grades = gradebook_dict.get(student)
        return sum(student_grades)/len(student_grades)



def every_other(seq):
    """ Returns a new sequence containing every other element of the input sequence, starting with
    the first. If the input sequence is empty, a new empty sequence of the same type should be
    returned.

    Example: every_other("abcde")
    "ace"
    """
    return seq[::2]

def all_but_last(seq):
    """ Returns a new sequence containing all but the last element of the input sequence.
    If the input sequence is empty, a new empty sequence of the same type should be returned.

    Example:
    >>> all_but_last("abcde")
    "abcd"
    """
    return seq[:-1]

def substrings(seq):
    """ Returns a set of all the substrings of s.
    Recall we can compute a substring using s[i:j] where 0 <= i, j < len(s).

    Example:
    >>> substrings("abc")
    "a", "ab", "abc", "b", "bc", "c"
    """
    substrings_set = set()
    for i in range(len(seq)):
        for j in range(i+1, len(seq)+1):
            substrings_set.add(seq[i:j])
    return substrings_set

def many_any(lst, k):
    """ Returns True if at least k elements of lst are True;
    otherwise False. Do this in one line for full credit.
    Hint: use a list comprehension.

    Example:
    >>> many_any([True, True, False, True], 3)
    True
    >>> many_any([True, True, False, False], 3)
    False
    """
    return lst.count(True) >= k

def alphabet_construct(seq, alphabet):
    """ Returns True if string s can be constructed from the set of length-1 strings
    alphabet and False otherwise.

    Example:
    >>> alphabet_construct("hello", {"a", "b", "h", "e", "l", "o"})
    True
    >>> alphabet_construct("hello", {"a", "b", "h", "e", "o"})
    False
    """
    for ch in seq:
        if ch in alphabet:
            continue
        else:
            return False
    return True

def common_chars(seq, k):
    """ Returns the set of characters that appear more than k times in
    the input string, along with their number of occurrences.

    Example:
    >>> common_chars("cat in a hat", 2)
    {("a", 3)}
    """
    chars_list = [ch for ch in seq]
    chars_set = set(chars_list)
    result_set = set()
    for i in chars_set:
        if chars_list.count(i) > k:
            result_set.add((i,chars_list.count(i)))
    return result_set


def dict_to_tuple_list(my_dict):
    """ Given a dictionary where each k-v pair is of the form (x, [y]), convert the dictionary
    into a list of tuples.

    Example:
    >>> dict_to_tuple_list({'x': [1, 2, 3], 'y':[4, 5, 6]})
    [(x, 1), (x, 2), (x, 3), (y, 4), (y, 5), (y, 6)]
    """
    result = list()
    for key in my_dict:
        for value in my_dict.get(key):
            result.append((key, value))
    return result

"You're done! Wahoo!"
