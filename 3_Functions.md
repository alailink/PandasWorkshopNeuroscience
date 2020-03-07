# Functions 

## Motivation

Quite often, there will be an entire folder of data that you would like to synthesize quickly into a manageable dataframe. In our example dataset there are only two, but you can imagine that you have well over 1000 files that you might want to get through before your PhD is over. You can do this by using loops, or even better, using a function. 

## Functions. The pizza analogy with no math.

Let's get back to our pizza example. Suppose you have an oven, and you basically need it to do the same thing every time you operate it. You could call it a process, an algorithm, or a *function*. In python, you might want to make a function if you want to make 1000 pizzas, but you don't want to explicitly give it all the instructions every time. You want to explain to your low-wage worker how to do it, and later just tell them what kind of pizzas they need to make. In python this is what the structure looks like:

```python
def pizza_making_instruction(ingredients, temp, time, slices=10):
  pizza_maker.assemble(ingredients)
  oven.set_temp(temp)
  oven.bake(time)
  pizza_maker.cut(slices)
  return pizza
  
veg_pizza = [pizzadough, sauce, peppers, mushrooms, cheese]
baked_pizza = pizza_making_instruction(veg_pizza, 500, 12)
```
There's a lot going on. The first is **def pizza_making_instruction():**. def signifies a function, and then you name it arbitrarily. Parenthesis and : are not optional.  

Next are what you *pass* into the function. Ingredients, in this example, is actually a list. temp, time, and slices are all integers.  

At the end of the function you *return* whatever you want. In this case we return the pizza. In pandas, we might return a dataframe for every file after we've processed it.

After you have created the function, you can *call* it using what you named it, and passing in the variables. You can either pass them in order, or explicity pass them by using something like **time=12**. There are also defaults that you don't have to pass in, but you can if you want. slices has a default of 10. 

## For Loops
for loops have a weird syntax in python. Here are two examples:
```python
for each_file in list_of_files:
  read(files)
  
for i in range(len(list_of_pizzas)):
  pizza[i].eat()
```
in the first example, the english translation is, "For each file in my list of files, read file 1, then read file 2, ...".  
in the second example, it might read, "for index value in my list of pizzas (and I found the length of the list), eat pizza index 1, then eat pizza index 2, etc...."
