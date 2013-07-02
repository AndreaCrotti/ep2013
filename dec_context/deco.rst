=================================
 Decorators and Context managers
=================================

.. general motivation: Showing two important constructs in Python that
.. even if they are just syntactic sugar they help a lot writing
.. better and less code.

Twitter: @andreacrotti

.. image:: img/wazoku.png
   :height: 70

https://github.com/AndreaCrotti/ep2013

Background
==========

.. Before I show what a decorator is in Python, it should be clear to
.. everyone that in Python a function is a first class object, with
   type function.

.. Once a function func is defined the name 'func' will be bound in
.. the current namespace to a object, which type is function.

.. We can inspect the function and see for example its arguments,
.. or even see the compiled code with func.func_code.co_code.

.. SHOW: go in Ipython and show how to inspect functions and classes
.. for example showing inside the arguments passed in.

- every function is a *first class object* of type **function**

::

    def func(arg1, arg2):
        var1 = 10
    
::
    
    >>> type(func)
    >>> function


- every class is a *first class object* of type **type**

::
   
   class X(object):
       pass

::

   >>> type(X)
   >>> type


Decorator
=========
.. TODO: use inline urls if possible

In python a **decorator** is a callable that takes a function (or a
class) as argument, and returns a function (or a class) with an
altered behaviour.

The @ decorator syntax for functions has been introduced in Python 2.4, and for classes in Python 2.6 (see decorator-history_).

.. TODO: remove the definition, and just show a nice example first


Shocking example
================

.. And here we see a very simple first example of where a decorator
.. might be useful.

.. literalinclude:: code/deco.py
   :pyobject: fib

::

    @memoize
    def fib_memoized(n):
        if n <= 1:
            return 1
        return fib_memoized(n - 1) + fib_memoized(n - 2)


+-----+---------+--------------+---------+
|  n  | fib     | fib_memoized | speedup |
+-----+---------+--------------+---------+
|   5 | 2.66 μs | 1.16 μs      | 2x      |
+-----+---------+--------------+---------+
|  20 | 3780 μs | 1.21 μs      |3000x    |
+-----+---------+--------------+---------+


Hello decorator
===============

.. TODO: should I explain why (*args, **kwargs) is the generic way to
   call any function?

.. this is not what is supposed to do, should be in the right order

.. literalinclude:: code/deco.py
   :pyobject: decorator


::

    @decorator
    def my_function(): pass

Which is simply syntactic sugar for:

::

    def my_function(): pass
    my_function = decorator(my_function)


Why the _decorator?
===================

.. One question which I previously received is why do we actually need the _decorator?
.. Why can't I just define it like this:

.. Can anyone see what's wrong with this?

.. literalinclude:: code/deco.py
   :pyobject: naive_decorator


::
    
   @naive_decorator
   def my_function(): pass

::
   
   my_function = naive_decorator(my_function)

Here the function get **immediately executed!**, returning None


Simple example
==============

.. literalinclude:: code/deco.py
   :pyobject: verbose


::

    >>> def silly_func():
    >>>     print("Simple function")

    >>> silly_func = verbose(silly_func)

::

    Entering function silly_func
    Simple function
    Exiting function silly_func



Back to memoization
===================

.. XXX: add a big disclaimer saying that 

*memoize* caches the results of generic function calls.

.. literalinclude:: code/deco.py
   :pyobject: memoize


.. explain step by step what happened there

**Completely generic, memoize any recursive function**

See *lru_cache* for a safer implementation:
http://hg.python.org/cpython/file/8e838598eed1/Lib/functools.py

Memoization unfolded
====================

::

    fib(5)
    fib(4) + fib(3)
    (fib(3) + fib(2)) + (fib(2) + fib(1))
    ...

+-------+-----------------------------------+-----------------+
| step# | call                              | cache           |
+-------+-----------------------------------+-----------------+
|     1 | fib(4)                            | {}              |
+-------+-----------------------------------+-----------------+
|     2 | fib(3) + fib(2)                   | {}              |
+-------+-----------------------------------+-----------------+
|     3 | fib(2) + fib(1) + fib(2)          | {}              |
+-------+-----------------------------------+-----------------+
|     4 | fib(1) + fib(0) + fib(1) + fib(2) | {}              |
+-------+-----------------------------------+-----------------+
|     5 | 1 + 1 + fib(1) + fib(2)           | {fib((2, )): 2} |
+-------+-----------------------------------+-----------------+
|     6 | 2 + 1 + 2                         | 5               |
+-------+-----------------------------------+-----------------+


Parametric decorator 1
======================

Here is where things might get hairy, how do I add arguments to a
decorator?

::

    @deco(arg1="value", arg2=100)
    def function..

*Triple* function

.. literalinclude:: code/deco.py
    :pyobject: param_deco    


Parametric decorator 2
======================

Or alternatively overriding the __call__ method.

.. literalinclude:: code/deco.py
    :pyobject: call_decorator


Parametric decorator 3
======================

.. literalinclude:: code/deco.py
    :pyobject: retry_n_times


Class decorator
===============

.. literalinclude:: code/deco.py
    :pyobject: class_decorator


.. code::

    @class_decorator
    class C1:
        pass


Patching classes
================

.. use mock.patch to show how to patch entire classes

.. literalinclude:: code/patch_class.py

Which applies the patch for all the methods found by *inspection*.

Context manager
===============

Introduced in Python 2.5 with the with_statement_.

A context manager is useful whenever you can split the actions in:

- set up
- action
- teardown

::

   try:
       setup_action()
       do_it()
   except Error as e:
       handle_error(e)
   finally:
       teardown()


With statement
==============

The idea is to *not forget cleanup actions*.

::
    
    with open('file.txt') as source:
         text = source.read()
         # a lot
         # more
         # code

Is equivalent to:

::

    source = open('file.txt')
    text = source.read()
    # a lot
    # more
    # code
    source.close()


Implement __enter__ and __exit__
================================

.. pay attention that this function is not thread safe!

.. literalinclude:: code/context.py
    :pyobject: TempFile

Add that there can be an exception handling in the with.

.. try:
.. except:
.. finally:

Handling exceptions
===================

Handle yourself the exception raised!

::

    def __exit__(self, type, value, traceback):




Using contextlib
================

Contextmanager runs the generator until yield, then stops and runs
until the end.

::

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print "<%s>" % name
        yield
        print "</%s>" % name

::
    
     >>> with tag('H1'):
     >>>      print('Title')
    
     '<H1>Title</H1>'


.. TODO: this should be moved at the end of the decorator section maybe


Thanks
======

.. figure:: img/questions.jpg

@andreacrotti
https://github.com/AndreaCrotti/ep2013

.. notslides::

.. _decorator-history: http://wiki.python.org/moin/PythonDecorators
.. _hieroglyph: https://github.com/nyergler/hieroglyph
.. TODO: actually create the repo
.. _github: https://github.com/andreacrotti/pyconuk2012_slides
.. _with_statement: http://www.python.org/dev/peps/pep-0343/
