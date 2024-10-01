from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')


@app.route("/response")
def render_response():
    response = request.args["place"]
    name1 = request.args["user"]
    response2 = request.args["week"]
    response3 = request.args["person"]
    
    if response == 'South America':
        reply1 = "Hi " + name1 + ", I suggest you go to Brazil"
    
    elif response == 'North America': 
        reply1 = "Hi " + name1 + ", I suggest you take a trip to the USA"
    
    elif response == 'Europe':   
        reply1 = "Hi " + name1 + ", I suggest you visit France"
    
    elif response == 'Africa':   
        reply1 = "Hi " + name1 + ", I suggest you take a trip to South Africa"
    
    elif response == 'Asia':   
        reply1 = "Hi " + name1 + ", I suggest you go to Japan"
    
    else:
        reply1 = "Hi " + name1 + ", I suggest you take a trip to New Zealand"



    if response2 == 'Less than a week':
        reply2 = reply1 + " for four days!"
    
    elif response2 == '1-2 weeks': 
        reply2 = reply1 + " for ten days!"
    
    elif response2 == '2-4 weeks':   
        reply2 = reply1 + " for three weeks!"
    
    else:
        reply2 = reply1 + " for 3 months!"
        
        
        
    if response3 == '1 person':
        reply3 = reply2 + " It is an excellent destination to explore solo."
    
    elif response3 == '2 people': 
        reply3 = reply2 + " It is an excellent destination for a couple of people."
    
    elif response3 == '3-4 people':   
        reply3 = reply2 + " It is an excellent destination for a small group to visit."
    
    else:
        reply3 = reply2 + " It is an excellent destination for a large group to experience"

    return render_template('response.html', response3 = reply3,)
    
    
    

    
if __name__=="__main__":
    app.run(debug=False)