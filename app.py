from flask import render_template,request,Flask

app = Flask(__name__) #
@app.route('/') 

def quiz() : 
    return render_template('Harry_quiz.html')

@app.route('/result', methods=['POST'])

def result():   
    # Get the answers from the form
    answer1 = request.form['q1']
    answer2 = request.form['q2']
    answer3 = request .form['q3']

    houses = {
        'Garudwar' : 0,
        'Nagsakti' : 0,
        'Mehnatkash' : 0 ,
        'Cheelghat' : 0,
    }

    # Calculate the score based on the answers
    if answer1 == "bravery":
        houses["Garudwar"] += 1
    elif answer1 == "Ambitious":
        houses["Nagsakti"] += 1
    elif answer1 == "Intelligence":
        houses["Cheelghat"] += 1
    elif answer1 == "Loyalty":
        houses["Mehnatkash"] += 1

    if answer2 == "Dragon":
        houses["Garudwar"] += 1
    elif answer2 == "Snake":
        houses["Nagsakti"] += 1
    elif answer2 == "Owl":
        houses["Cheelghat"] += 1
    elif answer2 == "Badger":
        houses["Mehnatkash"] += 1

    if answer3 == "Defense":
        houses["Garudwar"] += 1
    elif answer3 == "Potions":
        houses["Nagsakti"] += 1
    elif answer3 == "Charms":
        houses["Cheelghat"] += 1
    elif answer3 == "Herbology":
        houses["Mehnatkash"] += 1

    # Determine the house with the highest score
    selected_house = max(houses, key = houses.get)

    image_filename = selected_house.lower() + ".jpg"  # e.g. garudwar.jpg

    return render_template('result.html', house=selected_house, image=image_filename)