from flask import Flask, render_template, request, redirect, url_for
import random as rd
import datetime as dt
import requests as rq

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    random_number = rd.randint(0,9)
    current_year = dt.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year )

@app.route('/guess/<uri_name>')
def greet(uri_name):
    parameters = {
        'name': uri_name.title(),
    }
    #api_response = rq.get(url="https://api.genderize.io", params=parameters)
    api_response = rq.get(url=f"https://api.genderize.io?name={uri_name}")
    api_response.raise_for_status()
    print(api_response)
    print("api_json:\n", api_response.json())
    api_response_gender = api_response.json()['gender'] 
    return render_template('greet.html', name=api_response.json()['name'].title(), gender=api_response_gender)

@app.route('/blog/<num>')
def get_post(num):
    print("num:", num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    api_response = rq.get(url=blog_url)
    api_response.raise_for_status()
    all_posts = api_response.json()
    return render_template('blog.html', posts=all_posts)


@app.route("/add")
def add():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

