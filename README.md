# Challenge 1

If you solved the task about Neumann's Random Generator you are already aware that not all methods of generating pseudo-random sequences are good. Particularly, Neumann's method is not suitable for anything except programming exercises.

Here is the other method which is more widespread (it is implemented in most of programming languages and libraries) and still simple enough: let us start with some initial number and generate each new member Xnext of a sequence by the current Xcur using the following rule:

## Formula
Xnext = (A * Xcur + C) % M

So we need three constants to define such a sequence (and an initial number). Not all combinations of constants are good (you may read details at Random Numbers), however, here are many good variants which allow to produce sequences with period of M, i.e. significantly long.

In this task we are going to build this algorithm to tell the value of n-th member of a sequence.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow, each in separate line.
Test-case consists of five values: A, C, M, X0, N where first three are the same as in formula, while X0 is the initial member of a sequence and N is the number of a member which we want to calculate.
Answer should contain N-th member's value for each test-case, separated by spaces.

input data:
2
3 7 12 1 2
2 3 15 8 10

answer:
1 11

# Challene 2: Dijkstra in the Network

Note: to start work on this task you need to solve Graph Generator to generate input data.

Dijkstra's algorithms solves very popular task - it allows to find the sortest paths from the given node of a graph to all other nodes.

Of course this can find applications in logistics etc., but far more common usage is in communication networks.

For example, think of Zig-Bee network, consisting of N modules. These small devices are capable of determining the shortest route to destination extremely fast, notwithstanding that the network geometry can change over time - some modules can go offline, some other could be installed on vehicles etc. So most routers in almost every network technology utilize this method or some derivative (like A*).

In this task you are to implement Dijkstra's algorithm - the details you can find in the corresponding Wikipedia article.

The simplest form (without min-priority queue) would be sufficient.

The graph is described the same way as in Graph Generator problem - by specifying the number of vertices and the seed for randomizer.

For example, if we use the same graph with 10 nodes and initialize random generator with the same seed 0 and will run the Dijkstra's algorithm starting from node 1, we'll get the following paths to each of destinations:

dest.          path            length
  1            1                  0
  2            1-2                1
  3            1-2-3              2
  4            1-2-4              2
  5            1-2-4-5            5
  6            1-2-4-6            9
  7            1-2-4-8-7          4
  8            1-2-4-8            3
  9            1-2-4-6-9         16
  10           1-10               3

The tree of these paths is marked with green lines in the picture above.

Input data will contain three numbers N - the number of nodes, X0 - seed for random generator and S the index of starting vertex (from where we are to search for paths to others).
Answer should contain the route length to each vertex in the graph.

<strong>Example:</strong>
input data:
10 0 1

answer:
0 1 2 2 5 9 4 3 16 3


# Challenge 3: Depth First Search

Algorithm Implementation
Nice thing is that we need only slight modification of BFS to convert it to DFS:

we should use a Stack instead of the Queue for storing vertices;
we do not check whether node was seen when storing neighbors in the stack - instead we perform this checking when retrieving the node from it.
You probably know that the Stack is similar to Queue, but the elements are retrieved in the reversed order, which is often called LIFO, i.e. Last in, First out. If we add elements to the end of array and retrieve it from the end also, then it is just the implementation of the stack.

So here is the detailed steps of the algorithm:

We add the initial node to stack.
Remove the next element from the stack and call it current.
If the current node was seen then skip it (going to step 6).
Otherwise mark the current node as seen.
Get all neighbors of the current node and add all them to stack.
Repeat from the step 2 until the stack becomes empty.

## Problem Statement
Again you should produce the array representing the spanning tree built by the algorithm. There are different ways to extend the algorithm to allow it remember where you came from to which nodes.

To avoid ambiguosity please take care that neighbors should be tried in order of increasing their ids (like in BFS problem).

Input data will contain the amount of nodes N and the amount of edges M.
Then M lines will follow each containing ids of two nodes connected by an edge. Node ids are integers between 0 and N-1.
Answer should contain the array of values: a[i] should contain the index of the node from which i-th one was visited by the algorithm. It should have -1 for the initial node, i.e. a[0]=-1.

Example:

input data:
7 10
0 1
2 0
0 3
1 4
4 3
2 3
5 2
6 3
4 6
6 5

answer:
-1 0 3 4 1 2 5

Another example:
input data
4 4
0 1
1 2
3 1
2 0

answer
-1 0 1 1
