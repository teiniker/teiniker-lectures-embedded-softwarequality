# Debugging

Software developers spend huge amounts of time for debugging. 
Estimates ranges up to half or more of their workdays.

Learning to debug well is essential to enjoying software development. 
As programmers, we know that bugs do not creep out of mother nature into our programs… 

**Bugs are inherent part of the programs we produce.**


## From Defects to Failures

* **The programmer creates a defect**\
  A defect is a piece of the code that can cause an infection. 
  The defect is technically created by the programmer.

* **The defect causes an infection**\
  After execution of the defect, the program state differs from what the programmer intended.

* **The infection propagates**\
  As the remaining program execution accesses the infected state, 
  it generates further infections tat can spread into later program states. 

* **The infection causes a failure**\
  A failure is an external observable error in the program behavior. 
  It is caused by an infection in the program state.

Not every defect results in an infection, and not every infection results in a failure, therefore: 

**Testing can only show the presents of defects, but never their absence.** (Dijkstra)

The issue of debugging is to **identify the infection chain, to find its root cause (the defect), and to remove the defect**.


## From Failures to Fixes

* **Track the problem**\
  The first step in debugging is to file a problem report such that the defect will not go by unnoticed.

* **Reproduce the failure**\
  Reproducing may require control over all possible input sources.

* **Automate and simplify the test case**\
  We have to think about how to automate the failure (in that we want to reproduce the failure automatically) 
  and how to simplify its input such that we obtain a minimum test case.

* **Find possible infection origins**\
  We have to observe what actually happens in a failing run. 
  Observation techniques include logging and interactive debuggers.

* **Correct the defect**\
  Finally, we have to correct the defect. 
  If the failure no longer occurs, we know that the defect caused the failure.

* **Learning from mistakes**\
  We can aggregate earlier problem reports and fixes to find out where 
  the most defects occur in the program.


## Debugging Techniques

The following techniques are commonly used to find bugs in applications:

* [Logging](https://github.com/teiniker/teiniker-lectures-softwaretesting/tree/master/debugging/logging)

* [Interactive Debugging](https://github.com/teiniker/teiniker-lectures-softwaretesting/tree/master/debugging/debugger)

* [Assertions](https://github.com/teiniker/teiniker-lectures-softwaretesting/tree/master/debugging/assertions)


## References
* Andreas Zeller. **Why Programs Fail - A Guide to Systematic Debugging**. dpunkt.verlag, 2009

*Egon Teiniker, 2020-2025, GPL v3.0*



