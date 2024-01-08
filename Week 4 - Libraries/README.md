# [Week 4](https://cs50.harvard.edu/python/2022/weeks/4/)

## [Problem Set 4](https://cs50.harvard.edu/python/2022/psets/4/)

### [Emojize](https://cs50.harvard.edu/python/2022/psets/4/emojize/)

Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, `:thumbs_up:`, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, `:thumbsup:`, which will also be automatically converted to 👍.

See [carpedm20.github.io/emoji/all.html?enableList=enable_list_alias](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias) for a list of codes with aliases.

In a file called `emojize.py`, implement a program that prompts the user for a `str` in English and then outputs the “emojized” version of that `str`, converting any codes (or aliases) therein to their corresponding emoji.

----

### [Frank, Ian and Glen’s Letters](https://cs50.harvard.edu/python/2022/psets/4/figlet/)

FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

In a file called `figlet.py`, implement a program that:

- Expects zero or two command-line arguments:
  - Zero if the user would like to output text in a random font.
  - Two if the user would like to output text in a specific font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.
- Prompts the user for a `str` of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.

----

### [Adieu, Adieu](https://cs50.harvard.edu/python/2022/psets/4/adieu/)

n a file called `adieu.py`, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one `and`, three names with two commas and one `and`, and `n` names with `n - 1` commas and one `and`, as in the below:

>Adieu, adieu, to Liesl<br>
>Adieu, adieu, to Liesl and Friedrich<br>
>Adieu, adieu, to Liesl, Friedrich, and Louisa<br>
>Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt<br>
>Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta<br>
>Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta<br>
>Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl<br>

----

### [Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/)

In a file called `game.py`, implement a program that:

- Prompts the user for a level, `n`. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between `1` and `n`, inclusive, using the `random` module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
  - If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
  - If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
  - If the guess is the same as that integer, the program should output `Just right!` and exit.

----

### [Little Professor](https://cs50.harvard.edu/python/2022/psets/4/professor/)

In a file called `professor.py`, implement a program that:

- Prompts the user for a level, `n`. If the user does not input `1`, `2`, or `3`, the program should prompt again.
- Randomly generates ten (10) math problems formatted as `X + Y =`, wherein each of `X` and `Y` is a non-negative integer with `n` digits. No need to support operations other than addition (`+`).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.

----

### [Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/)

In a file called `bitcoin.py`, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, `n`, that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at <https://api.coindesk.com/v1/bpi/currentprice.json>, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any exceptions.
- Outputs the current cost of `n` Bitcoins in USD to four decimal places, using `,` as a thousands separator.

[*Source*](https://cs50.harvard.edu/python/2022/weeks/2/)
