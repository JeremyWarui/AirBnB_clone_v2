# 0x04. AirBnB clone - Web framework

> Project focusing on learning web framework for serving our files

## TASKS

**0. Hello Flask!**

`0-hello_route.py` - script that starts a Flask web application. Routes: /hbnb: display “HBNB”

**1. HBNB**

`1-hbnb_route.py` - Routes: /: display “Hello HBNB!”, /hbnb: display “HBNB”

**2. C is fun!**

`2-c_route.py` - Routes:

- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ” followed by the value of the text variable (replace underscore \_ symbols with a space )

**3. Python is cool!**

`3-python_route.py` - script that starts a Flask web application

Routes:

- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
  - The default value of text is “is cool”

**4. Is it a number?**

`4-number_route.py` - script that starts a Flask web application

Routes:

- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
  - The default value of text is “is cool”
- /number/<n>: display “n is a number” only if n is an integer

**5. Number template**

`5-number_template.py, templates/5-number.html` - script that starts a Flask web application

Routes:

- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
  - The default value of text is “is cool”
- /number/<n>: display “n is a number” only if n is an integer
- /number_template/<n>: display a HTML page only if n is an integer:
  - H1 tag: “Number: n” inside the tag BODY

**6. Odd or even?**

`6-number_odd_or_even.py, templates/6-number_odd_or_even.html` - script that starts a Flask web application

Routes:

- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore \_ symbols with a space )
  - The default value of text is “is cool”
- /number/<n>: display “n is a number” only if n is an integer
- /number_template/<n>: display a HTML page only if n is an integer:
  - H1 tag: “Number: n” inside the tag BODY
- /number_odd_or_even/<n>: display a HTML page only if n is an integer:
  - H1 tag: “Number: n is even|odd” inside the tag BODY
