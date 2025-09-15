from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    status = None
    if request.method == "POST":
        try:
            weight = float(request.form.get("weight"))
            height_cm = float(request.form.get("height"))
            height_m = height_cm / 100

            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"
        except:
            bmi = None
            status = "Invalid input"

    return render_template("index.html", bmi=bmi, status=status)

if __name__ == "__main__":
    app.run(debug=True)
