# [Week 0](https://cs50.harvard.edu/python/2022/weeks/0/)

## [Problem Set 0](https://cs50.harvard.edu/python/2022/psets/0/)

### [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/)

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.

----

### [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/)

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

----

### [Making Faces](https://cs50.harvard.edu/python/2022/psets/0/faces/)

In a file called `faces.py`, implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a slightly smiling face) and any `:(` converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`. Be sure to call `main` at the bottom of your file.

----

### [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/)

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

----

### [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/)

In a file called `tip.py`, implement two functions:

- `dollars_to_float`, which should accept a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), remove the leading `$`, and return the amount as a `float`. For instance, given `$50.00` as input, it should return `50.0`.
- `percent_to_float`, which should accept a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. For instance, given `15%` as input, it should return `0.15`.

Assume that the user will input values in the expected formats.

[*Source*](https://cs50.harvard.edu/python/2022/weeks/1/)
