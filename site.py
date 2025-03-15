from flask import Flask, render_template
import os

p_list = [("Віктор","Київ"),
          ("Вололимир","Київ"),
          ("Юлія","Одеса"),
          ("Микола","Луцьк"),
          ("Іван","Київ"),
          ("Петро","Рівне")]


def index():
    return render_template("index.html", p_list=p_list, city="Київ")


folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)
app.add_url_rule("/", "index", index)


if __name__ == "__main__":
    app.run()
