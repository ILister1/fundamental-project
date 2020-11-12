from application import app

#Declare the conditional under which the app is run

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

