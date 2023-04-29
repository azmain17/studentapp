from flask import Flask,request,jsonify
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return "Tourist place recommender"

@app.route('/predict',methods=['POST'])
def predict():
    Sea_lover = request.form.get('Sea_lover')
    Mountain_lover = request.form.get('Mountain_lover')
    History_lover = request.form.get('History_lover')
    Entertainment_lover = request.form.get('Entertainment_lover')
    Need_hotel = request.form.get('Need_hotel')
    Hotel_type = request.form.get('Hotel_type')
    Need_transport = request.form.get('Need_transport')
    Days = request.form.get('Days')
    Place = request.form.get('Place')
    Budget = request.form.get('Budget')
    Travel_guide = request.form.get('Travel_guide')
    Prefer_attractions = request.form.get('Prefer_attractions')
    Traveling_partner = request.form.get('Traveling_partner')
    Prefer_safety = request.form.get(' Prefer_safety')
    Foodie = request.form.get('Foodie')
    Tourist_friendly_place = request.form.get('Tourist_friendly_place?')

    Starting_point = request.form.get('Starting_point')


    input_query=np.array([[Sea_lover,Mountain_lover,History_lover,Entertainment_lover,Need_hotel,Hotel_type,Need_transport,Days,Place,Budget,Travel_guide,Prefer_attractions,Traveling_partner,Prefer_safety,Foodie,Tourist_friendly_place,Starting_point]])
    result=model.predict(input_query)[0]

    return jsonify({'Suitable trip':str(result)})



if __name__=='__main__':
    app.run(debug=True)
