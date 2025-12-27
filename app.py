#!/usr/bin/env pyton3

# Terzo Technical Flask Front End
# (c) 2025-2025 Shannon Douglas Ware

from flask import Flask

app = Flask(__name__)

page = """
<html><head><title>Terzo Technical</title></head>
<body><h1>Terzo Technical for DopamineMenu.Net</h1><p>Welcome to a Terzo Technical Proof of Concept. Actions recorded: <span id="actions">0</span></p>
<ol><li>Labour is infinite, capital is finite</li><li>Go into production</li><li>This work will lead to that work</li></ol>
</html>
"""

@app.route("/")
def hello_world():
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
