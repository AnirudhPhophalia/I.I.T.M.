'''Fibonacci

Fibonacci is a young resident of the Italian city of Pisa. He spends a lot of time visiting the Leaning Tower of Pisa, one of the iconic buildings in the city, that is situated close to his home. During all his visits to the tower, he plays a strange game while climbing the marble steps of the tower.
The Game

Fibonacci likes to climb the steps either one at a time, two at a time or three at a time. This adds variety to the otherwise monotonous task of climbing. He wants to find the total number of ways in which he can climb 
n
n steps, assuming that the order of his individual steps matters. Your task is to help Fibonacci compute this number.

For example, if he wishes to climb three steps, the case of n=3, he could do it in four different ways:
(1,1,1): do it in three moves, one step at a time(1,2): do it in two moves, first take a single step, then a double step(2,1): do it in two moves, first take a double step, then a single step(3): do it in just one move, directly leaping to the third stepTo take another example, if n=5, then some of the sequences could be:(1,3,1),(1,1,3),(3,1,1),(2,1,1,1),(1,2,1,1),(2,1,2)Each sequence is one of the ways of climbing five steps. The point to note here is that each element of a sequence can only be 11, 22 or 33.

'''
def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if n == 0:
        return 1  # One way to remain at the starting position (no steps)
    if n < 0:
        return 0  # No way to climb a negative number of steps

    # Recursive case: Sum of ways to climb by taking 1, 2, or 3 steps
    return steps(n - 1) + steps(n - 2) + steps(n - 3)