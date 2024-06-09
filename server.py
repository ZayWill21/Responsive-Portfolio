from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    #Checks if we run the files 


#    <link rel="stylesheet" href="static/style.css">
#    <link rel="stylesheet" href="static/mediaqueries.css">