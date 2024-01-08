# [Week 6](https://cs50.harvard.edu/python/2022/weeks/6/)

## [Problem Set 6](https://cs50.harvard.edu/python/2022/psets/6/)

### [Lines of Code](https://cs50.harvard.edu/python/2022/psets/6/lines/)

in a file called `lines.py`, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.py`, or if the specified file does not exist, the program should instead exit via `sys.exit`.

Assume that any line that starts with `#`, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

----

### [Pizza Py](https://cs50.harvard.edu/python/2022/psets/6/pizza/)

In a file called `pizza.py`, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using `tabulate`, a package on PyPI at [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Format the table using the library’s `grid` format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`.

----

### [Scourgify](https://cs50.harvard.edu/python/2022/psets/6/scourgify/)

In a file called `scourgify.py`, implement a program that:

- Expects the user to provide two command-line arguments:
  - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, `name` and `house`, and
  - the name of a new CSV to write as output, whose columns should be, in order, `first`, `last`, and `house`.
- Converts that input to that output, splitting each `name` into a `first` name and `last` name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via `sys.exit` with an error message.

----

### [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/)

In a file called `shirt.py`, implement a program that expects exactly two command-line arguments:

- in `sys.argv[1]`, the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in `sys.argv[2]`, the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay [shirt.png](https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png) (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with `Image.open`, resize and crop the input with `ImageOps.fit`, using default values for `method`, `bleed`, and `centering`, overlay the shirt with `Image.paste`, and save the result with `Image.save`.

The program should instead exit via `sys.exit`:

- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in `.jpg`, `.jpe`g, or `.png`, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

[*Source*](https://cs50.harvard.edu/python/2022/weeks/2/)
