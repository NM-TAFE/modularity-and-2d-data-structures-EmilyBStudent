## Short Answer (Knowledge Questions)

### 1. Briefly explain: what is modular programming

Modular programming is an approach to software development in which code is broken up into self-contained, reusable
pieces (modules), each with a specific, single purpose. This allows each module to be tested and maintained
independently, and allows easy code reuse between projects. To facilitate this, each module should avoid relying on
knowledge of other modules in a project, and should only access and change its own data.

### 2. How can you import only a specific function or class from a module in Python? What is the syntax for this?

```python
from module_name import SpecificClass
```

This will import SpecificClass under the name "SpecificClass", without needing to specify the module name in your code.
The statement "import module_name" by itself will import everything from the module, and you would access items from the
module using dot notation, e.g. you would refer to SpecificClass as "module_name.SpecificClass". 

### 3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.

Python's parameter-passing mechanism is more similar to pass-by-reference. When calling a function or method, the
arguments are passed as copies of references to the objects' locations in memory. (Remember, everything in Python is
an object.) However, this behaves a little differently depending on whether the object pointed to by the reference is
mutable or not.

If an argument is a reference to an immutable object, any change to the argument within the function/method will replace
the reference with a new reference to a different object, elsewhere in memory. The original object will not be changed
(because it can't be changed). When the function returns, any change to the argument will be lost.

However, if the argument is a reference to a mutable object such as a list, then it is possible for the function/method
to change the object. Code such as "my_list_parameter.append(item)" will follow the reference in my_list_parameter to
where the list is stored in memory and append "item" to the original list. This change to the list will persist even
after the function returns, since it is a change to the original object and not a change to the reference stored in the
parameter.

### 4. Given the following Python code, what will be the output and why?

    ```python
    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)
    ```

The output of this code will be "['original', 'new']". The process is as follows:
1. A list containing one item, the string "original", is created in memory. A reference to this list is stored in the
variable "items".
2. modify_list is called, passing in the reference to the "items" list. "list_" is created as a second reference to this
list object. Now "items" and "list_" both point to the same object (the list) stored in memory.
3. 'list_.append("new")' first looks up the reference in 'list_' and finds the object it points to. It then calls
'append("new")' on that object, updating the list where it is stored in memory.
4. A new list containing the strings "completely" and "new" is created. A reference to this list is stored in the
parameter "list_". This overwrites the previous reference stored in "list_" with a different reference to the newly
created list. Now "items" and "list_" contain different references to two different objects in memory.
5. "modify_list" returns, and Python cleans up its data. The parameter "list_" and its reference to the second list
object are deleted. Python's automatic garbage collection will notice that the list object created in step 4 no longer
has any references to it left, and will also delete the object from memory.
6. The reference in "items" is looked up and the object is printed. This is the original list object from step 1 with
the modification made in step 3.

In short, the line of code 'list_.append("new")' follows the reference in 'list_' to update the object in memory, while
'list_ = ["completely", "new"]' replaces the reference entirely with a reference to a different object, without changing
the original object in its memory location or the reference stored in the "items" variable. 

### 5. In Python even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.

Since variables and parameters in Python are just references to objects stored in memory, it is possible for multiple
references in different scopes to point to the same object in memory. If the object is mutable, changes made to the
object using any of these references will be visible when accessing it from any other reference that points to it.

Parameters of functions and methods are always passed as references to objects, and not copies of the objects. This
means that when passing a reference to a mutable object into a function or method, changes to that object made within
the function/method will persist after the function/method returns. This is because the parameter that is deleted when
the function/method returns is only a(nother) reference to the object, not a copy of the object. 

### 6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?

Two benefits of modular coding are that it allows easy reuse of code between projects and parts of a project, and that
it allows a module to be maintained and tested (particularly unit-tested) independently.

Medium-sized and larger projects will often have reason to use similar code in multiple parts of the project. For
instance, there may be multiple parts of an app that need to query client and job data from the database and work with
it. By creating modules for Client and Job classes, this code can be abstracted. It avoids writing similar code multiple
times (which in turn avoids code getting out of sync and reduces the opportunity for bugs to creep in). It keeps all
project code dealing with client and job data simple and consistent.

As a project becomes larger, it becomes harder for each person working on the project to familiarise themselves with and
understand all the code within the project. Having the majority of code in self-contained modules allows a developer to
focus more easily on specific aspects of the codebase. It is easier to understand and maintain one self-contained module
with a single, specific purpose than code that does a large number of things and jumps around between multiple files. As
long as the module's API does not change and it continues to pass its unit tests, changes within the module should have
minimal effect on the code that relies on it.
