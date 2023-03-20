from flask import Flask
from flask import request
from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    a =8+3
    return "this is my function to run app {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return "this is data value input by you in the url {}".format(data)


# Calculation on the html page 
@app.route('/home',methods = ['GET','POST'])
def home_page():
    return render_template("index.html")

# GET means send through the url , and POST means sent through the body / form


# Data pass through the form ..
@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(ops=='add'):
            sum = num1+num2
            result = "the sum of "+str(num1)+"  and  "+str(num2)+ " is "+str(sum)
            return render_template("results.html",result = result)

        if(ops=='subtract'):
            sub = num1-num2
            result = "the substraction  of "+str(num1)+"  and  "+str(num2)+ " is "+str(sub)
            return render_template("results.html",result = result)

        if(ops=='multiply'):
            mul = num1*num2
            result = "the Multiplaction of "+str(num1)+"  and  "+str(num2)+ " is "+str(mul)
            return render_template("results.html",result = result)

        if(ops=='divide'):
            div = num1/num2
            result = "the Division of "+str(num1)+"  and  "+str(num2)+ " is "+str(div)
            return render_template("results.html",result = result)


# Data pass using some other methods  --->> using postman

# Postman is a tool which is use to test all the api

@app.route('/postman_data',methods=['POST'])
def postman():
    if(request.method=='POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(ops=='add'):
            sum = num1+num2
            result = "the sum of "+str(num1)+"  and  "+str(num2)+ " is "+str(sum)
            return jsonify(result)

        if(ops=='subtract'):
            sub = num1-num2
            result = "the substraction  of "+str(num1)+"  and  "+str(num2)+ " is "+str(sub)
            return jsonify(result)
        if(ops=='multiply'):
            mul = num1*num2
            result = "the Multiplaction of "+str(num1)+"  and  "+str(num2)+ " is "+str(mul)
            return jsonify(result)

        if(ops=='divide'):
            div = num1/num2
            result = "the Division of "+str(num1)+"  and  "+str(num2)+ " is "+str(div)
            return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=9000)
