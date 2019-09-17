from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form_post_get():
    name = "formを「post ＆ get」してみました"
    return name

@app.route('/form_post')
def form():
   return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
      result = request.form
      return render_template("confirm.html",result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


