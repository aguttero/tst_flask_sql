from flask import Flask, render_template
import requests as rq


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    api_response = rq.get(url=blog_url)
    api_response.raise_for_status()
    all_posts = api_response.json()
    # TST print('all_posts json:\n', all_posts[0]['body'])
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:list_item>')
def get_post(list_item):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    api_response = rq.get(url=blog_url)
    api_response.raise_for_status()
    requested_post = api_response.json()[list_item]
    # TST print('requested_post var:\n', requested_post)
    return render_template("post.html", blog_post=requested_post)




if __name__ == "__main__":
    app.run(debug=True)
