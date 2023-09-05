[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11681059&assignment_repo_type=AssignmentRepo)
# CMPS 2200  Recitation 01

**Name (Team Member 1):** Jack Zemke, completed independently

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 
  
  - For both `linear_search` and `binary_search` the worst case value for `key` is a value that is not contained within the input list. This is because it would require the search algorithms to evaluate every single item in the list before finally determining it is not contained within the list.

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 
  
    - The best case input value for `linear search` is the smallest value in the input list. This is because `linear search` iterates through the list from the beginning, which is where the smallest value is. If the key is the smallest value in the list, it will be the first value to be evaluated and will therefore terminate in the best case time.

    - The best case input value for `binary search` is the middle value in the list. This is because the algorithm splits the list down the middle and compares the pivot value to the key. If the middle (pivot) value is equal to the key, the algorithm will terminate on the very first evaluation resulting in the best case time. 

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:



    |            n |   linear |   binary |
    |--------------|----------|----------|
    |       10.000 |    0.001 |    0.002 |
    |      100.000 |    0.003 |    0.015 |
    |     1000.000 |    0.022 |    0.012 |
    |    10000.000 |    0.233 |    0.092 |
    |   100000.000 |    2.342 |    0.846 |
    |  1000000.000 |   21.321 |    9.703 |
    | 10000000.000 |  224.120 |   95.807 |

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

    - Yes, these theoretical running times do match my empirical results. The math tells us that binary search should be faster for larger arrays, and as $n \rightarrow \infty$ the difference in speeds should grow greater. My empirical results followed this trend. 
    There was a slight deviation, where $n\le 100$, but this is to be expected. For relatively small lists, linear search is faster because it does not require the splitting of the list, which can be time/memory intensive.

**TODO: your answer goes here**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? 
  
    We must first sort the list, taking $\Theta(n^2)$ time, and then search it using linear search $k$ times taking $O(nk)$ time. The time complexity is the sum of these steps, $\Theta(n^2)+O(nk)$. $n^2$ is the dominant term in this expression, because as $n\rightarrow\infty$, $O(nk)$ grows at a linear rate while $\Theta(n^2)$ grows exponentially.

  + For binary search? 
  
    We must first sort the list, taking $\Theta(n^2)$ time, and then search it using binary search $k$ times, taking $O(k * log_2(n))$ time. The time complexity is the sum of these steps, $\Theta(n^2)+O(k* log_2(n))$. Again $n^2$ is the dominant term in this expression, because as $n\rightarrow\infty$, $O(k*log_2(n))$ grows at a logarithmic rate while $\Theta(n^2)$ grows exponentially.

  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? 
  
    For this problem we will compare the time complexity of sort+binary_search with the time complexity of unsorted linear search. The time complexity of sort+binary_search is $\Theta(n^2)+O(k* log_2(n))$, and the time complexity of unsorted linear search is $O(nk)$. We are looking for a value of $k$ such that $O(nk) > (n^2)+O(k* log_2(n))$. The arithmetic is as follows:
  
      $nk> n^2 + k*log(n)$
      
      We will consider cases where n is very large, leading us to only consider terms that scale as n becomes very large. Thus our inequality becomes $nk> n^2$. 

      Dividing both sides by $n$, we obtain the inequality of $k>n$. 

      Thus, when dealing with lists with less elements $n$ than the number of searches $k$ you expect to do, it is more effecient to first sort the list and then execute the binary search $k$ times. When dealing with lists with more elements $n$ than the number of searches $k$ you expect to do, it is more effecient perform $k$ searches on an unsorted list using linear_search. 
  
