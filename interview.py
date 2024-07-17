

def numbers_sum_up_to_target(l: list, target: int):
    i, j = 0, len(l) - 1
    while i < j:
        if l[i] + l[j] > target:
            j -= 1
        elif l[i] + l[j] < target:
            i += 1
        else:
            return True
    return False


print(numbers_sum_up_to_target([1, 2, 3, 4, 4], 8))

#  -------------DATA STRUCTURES--------------------------

"""
1. What are the characteristics of a list
- Ordered
- Each element in the list is a reference (or pointer) to the actual data stored elsewhere in memory. This allows lists to store elements of different data types.
- The list is backed by a contiguous block of memory, which makes element access by index fast (constant time, O(1)) because the memory location of each element can be directly calculated.
- Mutable
- Heterogeneous

Side questions:
- What if we wanted to use a more memory efficient structure than a list (we can use an array)
- Is it a good idea to use a list as a queue (first in first out)?
-------------------------------------------------------------------------------------------------------------
2. What are the characteristics of a set
- Unordered Collection (you cannot access elements by index)
- Unique Elements
- Efficient Membership Testing

---------------------------------------------------------------------------------------------------------------------
3. How are you going to benefit by substituting a list for a set when searching for elements
- sets use hashmaps and provide very fast lookups, whereas looking for elements within a list
requires you to traverse the whole list

---------------------------------------------------------------------------------------------------------

4. What is the main feature of a tuple
5. What can you use as a key in a dictionary
6. Pandas DataFrame strengths
7. Why are data frames so fast for certain operations
8. What is a key difference between a python list and a numpy array
9. Can we create an API with Flask
10. What is the purpose of APIs
"""


# ------------DATA MODELING------------------------------

"""
1. How would we model a database that is meant for reading - we would try to set up indexes and aim to denormalize tables to avoid joins

2. Let's say we have this table.

sales_records
+---------+------------+--------------+-------------------+-----------+--------------+-----------------+-----------+----------+------------+
| OrderID | CustomerID | CustomerName | CustomerEmail     | ProductID | ProductName  | ProductCategory | OrderDate | Quantity | TotalPrice |
+---------+------------+--------------+-------------------+-----------+--------------+-----------------+-----------+----------+------------+
| 1       | 101        | Alice        | alice@example.com | 201       | Laptop       | Electronics     | 2024-07-01| 1        | 1000       |
| 2       | 102        | Bob          | bob@example.com   | 202       | Phone        | Electronics     | 2024-07-02| 2        | 1500       |
| 3       | 101        | Alice        | alice@example.com | 203       | Desk Chair   | Furniture       | 2024-07-03| 1        | 200        |
| 4       | 103        | Charlie      | charlie@example.com| 202       | Phone        | Electronics     | 2024-07-04| 1        | 750        |
+---------+------------+--------------+-------------------+-----------+--------------+-----------------+-----------+----------+------------+

What can we do to make it more suitable for writing?

Answer: we can normalize it by splitting it into a few tables:

customers
+------------+--------------+-------------------+
| CustomerID | CustomerName | CustomerEmail     |
+------------+--------------+-------------------+
| 101        | Alice        | alice@example.com |
| 102        | Bob          | bob@example.com   |
| 103        | Charlie      | charlie@example.com|
+------------+--------------+-------------------+

products
+-----------+--------------+-----------------+
| ProductID | ProductName  | ProductCategory |
+-----------+--------------+-----------------+
| 201       | Laptop       | Electronics     |
| 202       | Phone        | Electronics     |
| 203       | Desk Chair   | Furniture       |
+-----------+--------------+-----------------+

orders
+---------+------------+-----------+
| OrderID | CustomerID | OrderDate |
+---------+------------+-----------+
| 1       | 101        | 2024-07-01|
| 2       | 102        | 2024-07-02|
| 3       | 101        | 2024-07-03|
| 4       | 103        | 2024-07-04|
+---------+------------+-----------+

order_details
+---------+-----------+----------+------------+
| OrderID | ProductID | Quantity | TotalPrice |
+---------+-----------+----------+------------+
| 1       | 201       | 1        | 1000       |
| 2       | 202       | 2        | 1500       |
| 3       | 203       | 1        | 200        |
| 4       | 202       | 1        | 750        |
+---------+-----------+----------+------------+


---------------------------------------------------------------------------------------------------------------------
Here's the reason for keeping the orders and order_details as separate tables:
if we combined them into this one table:

orders_combined
+---------+------------+-----------+-----------+----------+------------+
| OrderID | CustomerID | OrderDate | ProductID | Quantity | TotalPrice |
+---------+------------+-----------+-----------+----------+------------+
| 1       | 101        | 2024-07-01| 201       | 1        | 1000       |
| 1       | 101        | 2024-07-01| 204       | 2        | 600        |
| 2       | 102        | 2024-07-02| 202       | 2        | 1500       |
| 3       | 101        | 2024-07-03| 203       | 1        | 200        |
| 4       | 103        | 2024-07-04| 202       | 1        | 750        |
+---------+------------+-----------+-----------+----------+------------+

we could have the issue where we have multiple orders with the same order id if one customer orders multiple products
---------------------------------------------------------------------------------------------------------------------
"""

# ----------CI/CD, Terraform--------------------------------------------------------

"""
1. What is the concept of infrastructure as code and why is it useful for developer teams?

Answer: We use infrastructure as code so we can have a repository that keeps the state of the whole infrastructure 
and everyone in the team can know about changes that have occurred.
"""

