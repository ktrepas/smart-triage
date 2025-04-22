from flask import Flask, render_template, request

app = Flask(__name__)

def triage_logic(symptoms):
    score = 0
    if "chest_pain" in symptoms:
        score += 2
    if "breathing_difficulty" in symptoms:
        score += 2
    if "bleeding" in symptoms:
        score += 2
    if "unconscious" in symptoms:
        score += 3
    if "fever" in symptoms:
        score += 1
    
    if score >= 5:
        return "🚨 Critical condition. Call emergency services immediately."
    elif score >= 3:
        return "⚠️ Serious symptoms. Seek medical attention soon."
    else:
        return "✅ Symptoms not critical. Monitor at home and rest."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")
        result = triage_logic(symptoms)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)