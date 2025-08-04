from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
	return "Hello Algorithm!"
	
	
@app.route("/user")
def user():
	return "Hi from User!"
if __name__=="__main__":
	app.run(host="0.0.0.0",port=6000)
	
