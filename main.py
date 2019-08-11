from flask import Flask, render_template, request, g, session
from back_end.main import main

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

# app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def input():
#     if request.method == "POST":
#         location1 = request.form['yourlocation']
#         location2 = request.form['nextlocation']
#         select = request.form.get('comp_select').lower()
#
#         return render_template("page.html", l1=location1, l2=location2,
#                                select=select)
#     return render_template("index.html")
#
#
# @app.route('/res')
# def res():
#     lst = main(request.form['l1'], request.form['l2'], request.form['select'])
#     l1 = request.args.get("location1")
#     l2 = request.args.get("location2")
#     message_id = 0
#     if request.method == "POST":
#         if request.form['btn'] == "next":
#             message_id = (int(request.form["message_id"]) + 1) % len(lst)
#     return render_template("page.html", message=lst[message_id],
#                            message_id=message_id, l1=l1, l2=l2)


@app.route('/', methods=["GET", 'POST'])
def input():
    places = []
    if request.method == "POST":
        comm = ""
        first = request.form['yourlocation']
        second = request.form['nextlocation']
        select = request.form['comp_select'].lower()
        lst = main(first, second, select)
        with open("static/cord.txt", 'w') as f1:
            f1.write(first + ' ' + second)
        with open('static/places.txt', "w", encoding="utf-8") as f:
            for place in lst:
                f.write(place.name + "\n")
                f.write(place.location + "\n")
                f.write(str(place.rating) + "\n")
                f.write(str(place.open_now) + "\n")
                f.write(place.number + "\n")
                for comment in place.reviews:
                    comm += comment['text'].replace('\n', '') + "|"

                f.write(comm + "\n")
                comm = ""
                f.write(place.web_page + "\n")
            f.write(" ")
        return redirect(url_for("result"))

    return render_template('index.html')


@app.route("/res", methods=['POST', "GET"])
def result():
    message_id = 0
    lst = []
    ws = []
    with open("static/cord.txt") as f1:
        s = f1.readlines()
        first, second = " ".join(s).split()
    with open("static/places.txt") as f:
        f = f.readlines()
        for i, el in enumerate(f):
            if i % 7 == 0 and i != 0:
                lst.append(ws)
                ws = []
                ws.append(el.strip())
            else:
                ws.append(el.strip())
        print(lst)
    if request.method == "POST":
        message_id = (int(request.form["message_id"]) + 1) % len(lst)
    return render_template("page.html", message=lst[message_id][1],
                           len=len(lst),
                           mes=lst[message_id][0],
                           message_id=message_id, l1=first,
                           l2=second,
                           com=lst[message_id][5].split('|'),
                           num=lst[message_id][4],
                           site=lst[message_id][6],
                           open=lst[message_id][3])


# @app.route("/res", methods=["GET", "POST"])
# def index():
#
#     # lst = [ 'Lviv theatre of opera and ballet', 'Lviv Polytehnik']
#     message_id = 0
#
#


# @app.route("/", methods=["GET", "POST"])
#
# def index():
#     first = "Kozelnytska,2a,Lviv"
#     second = "UCU,Lviv"
#     message_id = 0
#     if request.method == "POST":
#         if request.form['btn'] == "next":
#             message_id = (int(request.form["message_id"]) + 1) % len(request.form['length'])

#     length = len(lst)
#     return render_template("page.html", length=length, message=lst[message_id].location, message_id=message_id, location1=first, l2=second)
# @app.route('/', methods=['GET', 'POST'])
# def my():
#     message_id = 0
#     if request.method == 'POST':

#         if request.form['submit'] == 'Search':

#             lenght = len(lyst)
#             if request.method == 'POST':
#                 if request.form['btn'] == "btn":
#                     message_id = (int(request.form["message_id"]) + 1) % len(
#                         request.form["length"])
#
#             return render_template("page.html", location1=location1,
#                                    l2=location2, tags=select,
#                                    message=lyst[message_id].location,
#                                    lenght=lenght)
#
#         return render_template('index.html')


# @app.route('/result', methods=['POST'])
# def result():
#     location1 = request.form['yourlocation']
#     location2 = request.form['nextlocation']
#     select = request.form.get('comp_select').lower()
#
#     message_id = 0
#

#
#     return render_template("page.html", location1=location1,
#                            l2=location2, tags=select,
#                            message=lyst[message_id].location)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
