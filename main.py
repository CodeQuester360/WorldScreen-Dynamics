import datetime
import math
from flask import Flask,render_template,request
from textblob import TextBlob
import pymongo as pm
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/senti")
def sentiment_plot():
    args = request.args
    s_d = args["sd"]
    e_d = args["ed"]
    client = pm.MongoClient("mongodb://localhost:27017/")
    mydb = client["dosth_db"]
    reddit = mydb["Reddit"]
    twitter = mydb["twitter"]
    tw_avg = 0
    data_i = twitter.find({"_id": {"$gte": objectIdWithTimestamp(mydb,s_d,datetime.timedelta(days = 0)),"$lte":objectIdWithTimestamp(mydb,e_d,datetime.timedelta(days = 2))}}).limit(200)
    for val in data_i:
        pol = TextBlob(val["data"]["text"])
        tw_avg += pol.subjectivity
    tw_avg = tw_avg/200
    rd_avg = 0
    for val in reddit.find({"_id": {"$gte": objectIdWithTimestamp(mydb,s_d,datetime.timedelta(days = 0)),"$lte":objectIdWithTimestamp(mydb,e_d,datetime.timedelta(days = 2))}}).limit(200):
        pol = TextBlob(val["title"])
        rd_avg += pol.subjectivity
    rd_avg = rd_avg/200
    polarities = [tw_avg,rd_avg]
    return render_template("scp_plot.html", pol= polarities)

@app.route("/dcp")
def dcp_plot():
    args = request.args
    s_d = args["sd"]
    e_d = args["ed"]
    client = pm.MongoClient("mongodb://localhost:27017/")
    mydb = client["dosth_db"]
    mycol = mydb["IMDB"]
    count = 0
    x_axis = []
    y_axis = []
    startTime = None
    count = 0
    sum = 0
    ids = []
    min  = 10
    max  = 0
    reddit = mydb["Reddit"]
    twitter = mydb["twitter"]


    for item in mycol.find({"_id": {"$gte": objectIdWithTimestamp(mydb,s_d,datetime.timedelta(days = 0)),"$lte":objectIdWithTimestamp(mydb,e_d,datetime.timedelta(days = 2))}}):
        endTime = item["_id"].generation_time
        # if(item["id"] in ids):
        #     continue
        # ids.append(item["id"])
        # x_axis.append(count)
        # y_axis.append(str(item["rating"] if item["rating"] is not None else 0 ))
        if(startTime is None):
            startTime = endTime   
        
        rating = float(item["rating"] if item["rating"] is not None else 0)
        if(rating > 0):
            count +=1
            sum += rating
            if(rating > max):
                max = rating
            if(rating < min):
                min = rating    
        diff = endTime - startTime 

        if(startTime.strftime("%d/") != endTime.strftime("%d/")):
            x_axis.append(startTime.strftime("%m/%d/%Y"))
            y_axis.append(sum/count)
            startTime = None
            count = 0
            sum =0    
            
    return render_template("dcp_plot.html", x=x_axis,y=y_axis)                 
#helper method 
def objectIdWithTimestamp(db, timestamp, delta):
    # /* Convert string date to Date object (otherwise assume timestamp is a date) */
    timestamp = ( datetime.datetime.strptime( timestamp,"%m/%d/%Y" )) + delta

    # /* Convert date object to hex seconds since Unix epoch */
    # hexSeconds = str(math.floor(timestamp/1000))

    # /* Create an ObjectId with that hex timestamp */
    constructedObjectId = ObjectId.from_datetime(timestamp)

    return constructedObjectId

if __name__ == "__main__":
    app.run(port=8006, debug=True, host="0.0.0.0")
