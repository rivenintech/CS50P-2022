# [Week 7](https://cs50.harvard.edu/python/2022/weeks/7/)

## [Problem Set 7](https://cs50.harvard.edu/python/2022/psets/7/)

### [NUMB3RS](https://cs50.harvard.edu/python/2022/psets/7/numb3rs/)

In a file called `numb3rs.py`, implement a function called `validate` that expects an IPv4 address as input as a `str` and then returns `True` or `False`, respectively, if that input is a valid IPv4 address or not.

additionally implement, in a file called `test_numb3rs.py`, **two or more functions** that collectively test your implementation of `validate` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```pytest test_numb3rs.py```

----

### [Watch on YouTube](https://cs50.harvard.edu/python/2022/psets/7/watch/)

In a file called `watch.py`, implement a function called `parse` that expects a `str` of HTML as input, extracts any YouTube URL that’s the value of a `src` attribute of an `iframe` element therein, and returns its shorter, shareable `youtu.be` equivalent as a `str`. Expect that any such URL will be in one of the formats below. Assume that the value of `src` will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return `None`.

- `http://youtube.com/embed/xvFZjo5PgG0`
- `https://youtube.com/embed/xvFZjo5PgG0`
- `https://www.youtube.com/embed/xvFZjo5PgG0`

----

### [Working 9 to 5](https://cs50.harvard.edu/python/2022/psets/7/working/)

In a file called `working.py`, implement a function called `convert` that expects a `str` in either of the 12-hour formats below and returns the corresponding `str` in 24-hour format (i.e., `9:00 to 17:00`). Expect that `AM` and `PM` will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`

Raise a `ValueError` instead if the input to `convert` is not in either of those formats or if either time is invalid (e.g., `12:60 AM`, `13:00 PM`, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., `5:00 PM` to `9:00 AM`).

Either before or after you implement `convert` in `working.py`, additionally implement, in a file called `test_working.py`, **three or more** functions that collectively test your implementation of `convert` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```pytest test_working.py```

----

### [Regular, um, Expressions](https://cs50.harvard.edu/python/2022/psets/7/um/)

In a file called `um.py`, implement a function called `count` that expects a line of text as input as a `str` and returns, as an `int`, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like `hello, um, world`, the function should return `1`. Given text like `yummy`, though, the function should return `0`.

Either before or after you implement `count` in `um.py`, additionally implement, in a file called `test_um.py`, **three or more** functions that collectively test your implementation of `count` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```pytest test_um.py```

----

### [Response Validation](https://cs50.harvard.edu/python/2022/psets/7/response/)

In a file called `response.py`, using either [validator-collection](https://pypi.org/project/validator-collection/) or [validators](https://github.com/kvesteri/validators) from PyPI, implement a program that prompts the user for an email address via `input` and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. You may not use `re`. And do not validate whether the email address’s domain name actually exists.

[*Source*](https://cs50.harvard.edu/python/2022/weeks/2/)
