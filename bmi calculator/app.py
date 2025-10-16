from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        
        height_m = height / 100
        bmi = weight / (height_m * height_m)
        category = calculate_bmi_category(bmi)
        
        return jsonify({
            "success": True,
            "bmi": round(bmi, 2),
            "category": category
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
