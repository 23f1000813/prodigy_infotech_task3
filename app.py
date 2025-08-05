from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_strength(password):
    length = len(password)
    score = 0
    feedback = []

    if length >= 8:
        score += 1
    else:
        feedback.append("❗ Password should be at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❗ Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❗ Add lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❗ Include numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❗ Use special characters.")

    # Determine strength
    if score == 5:
        strength = "🔒 Very Strong"
    elif score == 4:
        strength = "✅ Strong"
    elif score == 3:
        strength = "🟡 Moderate"
    elif score == 2:
        strength = "⚠ Weak"
    else:
        strength = "❌ Very Weak"

    return strength, feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    feedback = []
    if request.method == 'POST':
        password = request.form['password']
        strength, feedback = check_strength(password)
    return render_template('index.html', strength=strength, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)