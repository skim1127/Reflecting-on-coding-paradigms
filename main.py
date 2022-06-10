### FUNCTIONAL PROMPT ###

# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def array_sorter(array):
    sorted_array = []
    for element in array:
        for num in element:
            sorted_array.append(num)
    sorted_array.sort()
    print(sorted_array)

example_array = [[2, 5, 1], [7, 14, 3], [23, 6, 21]]
array_sorter(example_array)
print(example_array)

# QUESTIONS #
'''
1.  How does this solution ensure data immutability?

    This solution ensures data immutability by making sure to not change any external values,
    or the input value. Instead, the returned value can simply be printed or assigned to a new
    varaible.

2.  Is this soution a pure function? Why or why not?

    Yes, The function does not change the input value or any external values. Given the same
    input, the function will always return the same output.

3.  Is this solution a higher order function? Why or why not?

    No, this is not a higher order function because it does not accept a function as an input,
    and does not return a function as the output.
    
4.  Would it have been easier to solve this problem using a different program style?

    No, a functional programming approach seems to be very efficient in keeping the code concise
    for this problem.

5.  Why in particular is functional programing a helpful paradigm when solving this problem?

    This problem doesn't require complex state management or many different moving parts, which
    would be better for object oriented programming.

'''

### OBJECT ORIENTED PROMPT ###

# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.
'''
1.  First, he'll need a general Podracer class defined with max_speed, 
    condition (perfect, trashed, repaired) and price attributes.

2.  Define a repair() method that will update the condition of the podracer to "repaired".

3.  Define a new class, AnakinsPod that inherits the Podracer class, but also contains 
    a special method called boost that will multiply max_speed by 2.

4.  Define another class that inherits Podracer and call this one SebulbasPod. 
    This class should have a special method called flame_jet that will update the 
    condition of another podracer to "trashed".
'''

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"
    
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price) 

    def boost(self):
        self.max_speed = self.max_speed * 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = "trashed"

example_pod = Podracer(100, "perfect", "$999,999")
example_pod.repair()
print(example_pod.condition)

new_pod = AnakinsPod(2, "perfect", "$1,999,999")
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(24, "perfect", "$599,999")
third_pod.flame_jet()
print(third_pod.condition)
# QUESTIONS
'''
1.  How does this solution demonstrate the four pillars of OOP? 
    (It may not demonstrate all of them, describe only those that apply)

    - Encapsulation
        The code itself is very readable, and one can easily figure out the functionality of the
        written methods.
    - Abstraction
        By having much of the code inside the class object, it hides unneccessary information 
        if the code were to be uploaded onto a web application.
    - Inheritance
        The two classes, AnakinsPod and SebulbasPod both inherit properties from the Podracer
        class, making the code efficient and reusable.
    - Polymorphism
        AnakinsPod and SebulbasPod classes both have a unique method, making the code much 
        more flexible and adding depth to the use of inheritance.

2.  Would it have been easier to implement a solution to this problem using 
    a different coding style? Why or why not?
    
    No, the OOP approach made a lot of the code reusable, and easy to read.

3.  How in particular did Object Oriented Programming assist in the solving of this problem?

    OOP is the best method to solving this problem, because there are many states to keep track
    of (many moving parts) such as max_speed, condition, and price.

'''

### REFLECTION
'''
1.  Is one of these coding paradigms "better" than the other? Why or why not?

    No, programmers must first analyze the problem, then decide which approach would be 
    the most efficient in solving the problem. Functional programing is not always the better
    approach to solving a problem and OOP, and vice versa.

2.  Given the opportunity to work predominantly using either of these coding paradigms, 
    which seems more appealing? Why?

    OOP seems more appealing because of the code being easier to read, and being able to 
    give life-like attributes to a given object. It also seems to be able to solve more complex
    problems, and would probably be used in big projects.

3.  Now being more familiar with these coding paradigms, what tasks/features/pieces of 
    logic would be best handled using functional programming? Object Oriented Programming?

    When keeping data immutability in mind, functional programming would be the best approach, 
    as well as taking care of simple tasks such as going through an iterable and returning a 
    different version of it.
    When it comes to keeping track of multiple object attributes and moving parts, OOP would be
    the best approach, making it easy to keep the code readable and reusable.

4.  Personally, which of these styles takes more work to understand? What should be done 
    in order to deepen understanding related to this paradigm?

    Personally, OOP takes more work to understand, as I haven't used OOP in practice. 
    It seems like there are so many different possible ways to solve a problem using OOP that
    it may be hard to decide on exactly what to do.
'''