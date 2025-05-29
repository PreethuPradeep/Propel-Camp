Loop

    A loop is a codeblock that returns a set of statements
    while a given condition is true.

    Loop is often used for performing a repeating task.

FOR Loop

    In Python, A container can be a range of numbers,
    a string of characters or a list of values.

    To access objects within a container,
    an iterative loop can be designed to retrieve items one at a time.

    For loop iterates over all elements in a container.

    For loop executes a block of code repeatedly
    until the conditions in the for statement
    in the for statement is no longer valid.

    A for loop can be used for iteration and counting.

Range()

    The  range() function is a common approach for counting in a for loop.

    A range() of function generates a sequence of integers between
    two numbers given the step size.

    the integer sequence is inclusive of the start and exclusive of end of function.

range(2,6)=[2,3,4,5]
range(start, stop, step) --> range(1,7,2)=[1,3,5]

While Loop
A while loop is a code construct thjat runs a set of statement known as aloop body whille a given condition known as loop condition is given as true

    At each iteration, once the loop statement is executed, the loop expression is evaluated again.

        If true, the loop body will execute atleast one more time.
        If false the loop execution will terminate
            and the next statement in the loop body will execute

Counting with a while loop

    While loop acn be used to count up or down.
    A counter variable can be used in a loop expression to determine the number of iteration executed.
    The change in the counter's value in each iteration is called the step size.
    Step size can be any positive or negative value.
        If the step size is positive number, the counter counts in ascending order
        If the step size is negative number, the counter counts in descending order.

    While loop repeatedly executes instructions inside the loop while a certain conditions remain valid.

Break Statement(Stop right before the true)

    A break Statement is used within a for or a while loop to allow the program execution to exit the loop once a given condition is triggered.
    A break statement can be used to improveruntime efficiency when further loop execution is not required.

Continue(Skip the true)

A continue staqtement allows for skipping the execution of the reminder of the loop without exiting the loop entirely.

A continuous statement can be used in a for or a while loop.
After the continuou statement's execution, the loop expression wil be evaluated again and the loop will continue from the loop's expression.

A continue statement facilitates the l;oop's control and readability.

Functions

If the same block of code is reused repeatedly, A function allows the programmer to run the code once, name the block,and use the code as many times as needed by calling the name.
Functions can read in values and return values perform tasks, including complex calculations.

A function is a named, reusable block of code that performs a task when called.
A function is defined using the def keyword.
The first line contains def followed by the function name, paranthesis and a colon.
A function must be defined before a function is called.

Benefits of Using Functions

A function promotes modularity by putting code statement related to a single task in a separate growth.
The body of a function can be executed repeatedly with multiple function calls so a function promotes reusability.

General Syntax

def FunctionName():
code that the function should do
return [expression]

Variable scope

Any variable declared inside a function is only accessable within the function. These are local variable

Any variable declared outside the function is known as global variable and is accessable anywhere in the program
