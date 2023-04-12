from flask import Flask,request,jsonify
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Tourist place recommender"

@app.route('/predict',methods=['POST'])
def predict():
    Sea_lover = request.form.get('Is that place right for a sea lover?')
    Mountain_lover = request.form.get('Is that place right for a man who loves mountains?')
    History_lover = request.form.get('Is that place right for a history lover?')
    Entertainment_lover = request.form.get('Available Entertainment Facilities')
    Need_hotel = request.form.get('Hotel needed')
    Hotel_type = request.form.get('Hotel type')
    Need_transport = request.form.get('Transport')
    Days = request.form.get('Days')
    Place = request.form.get('Place')
    Budget = request.form.get('Budget')
    Travel_guide = request.form.get('Travel guide')
    Prefer_attractions = request.form.get('Is the place full of natural and man-made attractions?')
    Traveling_partner = request.form.get('Traveling partner')
    Prefer_safety = request.form.get('Is the place safe for a tourist?')
    Foodie = request.form.get('Are there enough food stalls to enjoy various types of foods?')
    Tourist_friendly_place = request.form.get('Are the local people friendly with tourists?')

    Starting_point = request.form.get('Your starting point')


    input_query=np.array([[Sea_lover,Mountain_lover,History_lover,Entertainment_lover,Need_hotel,Hotel_type,Need_transport,Days,Place,Budget,Travel_guide,Prefer_attractions,Traveling_partner,Prefer_safety,Foodie,Tourist_friendly_place,Starting_point]])
    result=model.predict(input_query)[0]

    return jsonify({'Suitable trip':str(result)})



if __name__=='__main__':
    app.run(debug=True)
