
# コードソース　https://qiita.com/y_a_m_a/items/2fef42212f5ffeb11531


import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        # Use an empty string '' as the default value
        text = f"ここに結果が出力されます{os.environ.get('KEY_VAULT_TEST1', '')}"
        return render_template("page.html", text=text)
    elif request.method == 'POST':
        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
