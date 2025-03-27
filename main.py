import random
import time
import tabulate

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        #print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        #print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
        
def qsort(a, pivot_fn):
    ## TO DO
    if len(a) <= 1:
        return a
    else:
        pivot_index= pivot_fn(a)
        pivot_val = a[pivot_index]
        rest = a[:pivot_index] + a[pivot_index+1:]
        left = [x for x in rest if x < pivot_val]
        right = [x for x in rest if x >= pivot_val]
        return qsort(left, pivot_fn) + [pivot_val] + qsort(right, pivot_fn)
        
def first_pivot(a):
    return 0
def qsort_first_pivot(a):
    return qsort(a, first_pivot)
def random_pivot(a):
    return random.randint(0, len(a)-1)
def qsort_random_pivot(a):
    return qsort(a, random_pivot)
    
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes= [100,500,60,200,5,2]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: qsort(a, lambda a: 0)
    qsort_random_pivot = lambda a: qsort(a, lambda a: random.randint(0, len(a)-1))
    tim_sort = sorted
    selection_sort = ssort
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(selection_sort, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'selection sort', 'tim sort'], #add tims sort
                            floatfmt=".3f",
                            tablefmt="github"))

def run_print(): #cant call it test_ throw an error
    print_results(compare_sort())

random.seed()
run_print()
