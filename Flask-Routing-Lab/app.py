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
@app.route('/product/HeadSet')
def headset():
    return render_template("product.html",
    product = "HeadSet",img = "HeadSet.jpeg",desc ="comy high quality headset",price ="180")
@app.route('/product/poster1')
def poster1():
    return render_template("product.html",
    product = "One Piece Poster",img = "OnePIece.jpeg",desc ="High quality poster",price ="30")
@app.route('/product/zoro')
def zoro():
    return render_template("product.html",
    product = "One Piece Poster",img = "zoro.jpeg",desc ="high quality poster",price ="40")
@app.route('/product/luffy')    
def luffy():
    return render_template("product.html",
    product = "One Piece Poster",img = "luffy.jpeg",desc ="high quality poster",price ="40")    
@app.route('/product/figure1')    
def figure1():
    return render_template("product.html",
    product = "One Piece figure",img = "figure1.jpeg",desc ="high quality figure",price ="60")
@app.route('/product/figure2')    
def figure2():
    return render_template("product.html",
    product = "One Piece figure",img = "figure2.jpeg",desc ="high quality figure",price ="60")
@app.route('/product/kidney')    
def kidney():
    return render_template("product.html",
    product = "Kidney",img = "kidney.jpeg",desc ="high quality kidney",price ="1000")     

@app.route('/cart')
def cart():
    return render_template("cart.html")


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
