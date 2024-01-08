# [Week 8](https://cs50.harvard.edu/python/2022/weeks/8/)

## [Problem Set 8](https://cs50.harvard.edu/python/2022/psets/8/)

### [Seasons of Love](https://cs50.harvard.edu/python/2022/psets/8/seasons/)

In a file called `seasons.py`, implement a program that prompts the user for their date of birth in `YYYY-MM-DD` format and then prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from *Rent*, without any `and` between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.

Either before or after you implement `seasons.py`, additionally implement, in a file called `test_seasons.py`, **one or more** functions that test your implementation of any functions besides `main` in `seasons.py` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```pytest test_seasons.py```

----

### [Cookie Jar](https://cs50.harvard.edu/python/2022/psets/8/jar/)

In a file called `jar.py`, implement a `class` called `Jar` with these methods:

- `__init__` should initialize a cookie jar with the given `capacity`, which represents the maximum number of cookies that can fit in the cookie jar. If `capacity` is not a non-negative `int`, though, `__init__` should instead raise a `ValueError`.
- `**str**` should return a `str` with `n 🍪`, where `n` is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then `str` should return `"🍪🍪🍪"`
- `deposit` should add `n` cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, `deposit` should instead raise a `ValueError`.
- `withdraw` should remove `n` cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, `withdraw` should instead raise a `ValueError`.
- `capacity` should return the cookie jar’s capacity.
- `size` should return the number of cookies actually in the cookie jar, initially `0`.

Either before or after you implement `jar.py`, additionally implement, in a file called `test_jar.py`, **four or more** functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```pytest test_jar.py```

----

### [CS50 Shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/)

In a file called `shirtificate.py`, implement a program that prompts the user for their name and outputs, using [fpdf2](https://pypi.org/project/fpdf2/), a CS50 shirtificate in a file called `shirtificate.pdf` similar to [this one for John Harvard](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf), with these specifications:

- The [orientation](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be Portrait.
- The [format](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as [text](https://py-pdf.github.io/fpdf2/Text.html), centered horizontally.
- The shirt’s [image](https://py-pdf.github.io/fpdf2/Images.html) should be centered horizontally.
- The user’s name should be on top of the shirt, in white [text](https://py-pdf.github.io/fpdf2/TextStyling.html).

[*Source*](https://cs50.harvard.edu/python/2022/weeks/2/)
