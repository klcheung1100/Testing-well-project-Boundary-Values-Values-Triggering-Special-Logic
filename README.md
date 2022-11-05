# pytest_project2
Testing boundary values and writing test for values triggering special behavior


<br>row_to_list() takes a row containing housing area and prices e.g. "2,041\t123,781\n" and returns the data as a list e.g. ["2,041", "123,781"]
<br>A row can be mapped to a 2-tuple (m, n), where m is the number of tab separators. n is 1 if the row has any missing values, and 0 otherwise.
<br> Example 1: "123\t456\n" ->  (1, 0).
<br> Example 2: "\t456\n" -> (1, 1).
<br> Example 3: "\t456\t\n" -> (2, 1).

<br>The function only returns a list for arguments mapping to (1, 0). All other tuples correspond to invalid rows, with either more than one tab or missing values. The function returns None in all these cases. (See the plot.svg)
<br>This mapping shows that the function has normal behavior at (1, 0), and special behavior everywhere else.
