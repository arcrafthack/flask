# Packman Game

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Default maps for Packman
maps = [
    [
        "##########",
        "#        #",
        "# ## ## #",
        "#        #",
        "##########"
    ],
    [
        "##########",
        "#  #     #",
        "# ## ## #",
        "#        #",
        "##########"
    ],
    [
        "##########",
        "#        #",
        "# ## ## #",
        "#  #     #",
        "##########"
    ],
    [
        "##########",
        "# ## ## #",
        "#        #",
        "# ## ## #",
        "##########"
    ],
    [
        "##########",
        "#        #",
        "# ## ## #",
        "# ## ## #",
        "##########"
    ]
]

@app.route('/')
def index():
    return render_template('index.html', maps=maps)

@app.route('/maps')
def get_maps():
    return jsonify(maps)

if __name__ == '__main__':
    app.run(debug=True)
