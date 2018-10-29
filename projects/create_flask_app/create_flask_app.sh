# ALL FUNCTION GENERATORS START
gitignore() {
echo "
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
"
}

readme() {
echo "# $1 Flask Application"
}

runsh() {
echo "export FLASK_APP=.
export FLASK_ENV=development

python3 app.py"
}

basic_app() {
echo "from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return \"Hello World\"

if __name__ == '__main__':
    app.run(debug=True)
"
}

full_app() {
echo "from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
"
}

home_html() {
echo "{% extends 'layout.html' %}

{% block title %} Home Page {% endblock %}

{% block body %}

<h1>Home</h1>

{% endblock %}
"
}

layout_html() {
echo "<!DOCTYPE html>
<html>
<head>
    <meta charset=\"utf-8\" />
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <title>{% block title %} {% endblock %} </title>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <link rel=\"stylesheet\" href=\"static/css/style.css\">
</head>
<body>
    {% block body %} {% endblock %}

    <script src=\"static/js/script.js\"></script>
</body>
</html>
"
}

style() {
echo "body {
    background-color: #19B5FE;
}
"
}

script() {
echo "console.log(\"Hello World\")"
}

create_template() {
    mkdir templates
    cd templates
    home_html >> home.html
    layout_html >> layout.html
    cd ..
}

create_static() {
    mkdir static
    cd static

    mkdir css
    cd css
    style >> style.css

    cd ..

    mkdir js
    cd js
    script >> script.js
    cd ../..
}

create_basic() {
    echo -e "\e[92mCreating your app ..."
    gitignore >> .gitignore

    basic_app >> app.py
    readme "Basic" >> README.md

    echo "DONE!"
    echo -e "bash run.sh to run application."
    printf "\n\n"
    echo -e "\e[32mGo to http://localhost:5000/ to view."
    runsh >> run.sh
}

create_full() {
    echo -e "\e[92mCreating your app ..."
    gitignore >> .gitignore
    full_app >> app.py
    readme "Full" >> README.md

    echo -e "\e[92mCreating Templates folder ..."
    create_template

    echo -e "\e[92mCreating Static folder ..."
    create_static

    echo "DONE!"
    echo -e "bash run.sh to run application."
    printf "\n\n"
    echo -e "\e[32mGo to http://localhost:5000/ to view."
    runsh >> run.sh
}
# ALL FUNCTION GENERATORS END

# MAIN LOGIC 

help() {
    printf "\e[96mHelp commands:\n\n"
    echo "create_flask_app dirname : Creates full flask application with the given directory name."
    echo "help  : Lists all the available commands."
    echo "basic : Creates basic flask application."
    echo "full  : Creates full flask application."
}

# CHECKS FOR VALID DIR NAME
valid_dir() {
    if [ ${#1} = 0 ];
    then
        printf "\e[91mError, input valid folder name.\n\n"
        help
        exit 1
    fi
}

case $1 in
"basic")
    valid_dir $2

    mkdir $2
    cd $2
    create_basic
    ;;

"full")
    valid_dir $2

    mkdir $2
    cd $2
    create_full
    ;;

"help")
    help
    ;;
esac