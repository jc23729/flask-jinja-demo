from flask import Flask, request, render_template
from random import choice, sample

from flask_debugtoolbar import DebugToolbarExtension


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
#to install dowload it through PIP, IMPORT IT ON TOP(from flask_debugtoolbar import DebugToolbarExtension), and intitialize it by passing in our flask app(ebug = DebugToolbarExtension(app))
debug = DebugToolbarExtension(app)

#so it looks like you would create the html in templates folder first then make the route after
"""
Dynamic Templates
Jinja will replace things like {{ msg }} with value of msg passed when rendering:

templates/lucky.html
<h1>Hi!</h1>

<p>Lucky number: {{ lucky_num }}</p>
 
app.py
@app.route("/lucky")
def show_lucky_num():
    "Example of simple dynamic template"

    num = randint(1, 100)

    return render_template("lucky.html",
                          lucky_num=num)
"""
@app.route('/')
def index():
    """Return homepage."""

    return render_template("hello.html")


# SIMPLE VERSION OF FORM/GREET

@app.route('/form')
def show_form():
    """Show greeting form."""

    return render_template("form.html")


@app.route('/greet')
def offer_greeting():
    """Give player compliment."""

    player = request.args["person"]
    nice_thing = choice(COMPLIMENTS)

    return render_template("compliment.html", 
                           name=player, 
                           compliment=nice_thing)


# BETTER VERSION OF FORM/GREET    

@app.route('/form-2')
def show_better_form():
    """Show better greeting form."""

    return render_template("form-2.html")


@app.route('/greet-2')
def offer_better_greeting():
    """Give player optional compliments."""

    player = request.args["person"]

    # if they didn't tick box, `wants_compliments` won't be
    # in query args -- so let's use safe `.get()` method of
    # dict-like things
    wants = request.args.get("wants_compliments")

    nice_things = sample(COMPLIMENTS, 3) if wants else []

    return render_template("compliments.html",
                           compliments=nice_things, 
                           name=player)


@app.route("/mypage")
def my_page():
    """Show mypage, an example of template inheritance"""

    return render_template("mypage.html")