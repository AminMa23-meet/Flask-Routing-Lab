from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/product/pc')
def Pc():
    return render_template("product.html",
    product = "Gaming Pc",img = "Pc.jpeg",desc ="Great Pc",price ="1500")
@app.route('/product/chair')
def chair():
    return render_template("product.html",
    product = "Gaming Chair",img = "Chair.jpeg",desc ="comfy gaming chair",price ="160")
    @app.route('/product/mouse')
def mouse():
    return render_template("product.html",
    product = "Gaming Mouse",img = "Mouse.jpeg",desc ="Great Gaming Mouse",price ="70")
    @app.route('/product/keyboard')
def keyboard():
    return render_template("product.html",
    product = "Gaming KeyBoard",img = "KeyBoard.jpeg",desc ="Gaming KeyBoard",price ="60")
@app.route('/cart')
def cart():
    return render_template("cart.html")


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
