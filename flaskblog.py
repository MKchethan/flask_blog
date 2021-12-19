from flask import Flask, render_template, url_for
app = Flask(__name__)
# setting app as an instance of Flask class
# __name__ is just the name of the module
# Flask(__name__) : instantiated flask application

posts = [
    {
        'author': 'mkc',
        'title': 'Blog post1',
        'content': 'First Post content',
        'date_posted': 'Dec 16, 2021'
    },
    {
        'author': 'mkj',
        'title': 'Blog post2',
        'content': 'Second Post content',
        'date_posted': 'Dec 17, 2021'
    }

]


@app.route('/')    # decorators are just a way to add additional functionality to existing functions
@app.route('/home')
def hello():
    return render_template('home.html', postsh=posts)


@app.route('/about')
def about():
    return render_template("about.html",  title='About')


if __name__ == '__main__':
    app.run(debug=True)

