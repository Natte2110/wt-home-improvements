from flask import render_template, request, redirect, flash, url_for, jsonify
from wt_home import app

@app.route("/")
def home():
    """Provides routing for the website's home page

    Returns:
        The index.html page with the title of "Home"
    """
    # return render_template("index.html", title="Home")
    return "<h1>Test</h1>"


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def internal_server_error(error):
#     return render_template('500.html'), 500