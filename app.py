from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        draft_round = int(request.form.get("draft_round"))
        age = int(request.form.get("age"))
        college_yards = int(request.form.get("college_yards"))
        position = request.form.get("position").lower()
        years_played = int(request.form.get("years_played"))
        early_declare = request.form.get("early_declare").lower()
        college = request.form.get("college").strip()
        dash_time = float(request.form.get("dash_time"))
        opportunity = request.form.get("opportunity").lower()

        score = 0

        # Scoring system (same as your notebook logic)
        if draft_round == 1:
            score += 10
        elif draft_round == 2:
            score += 8
        elif draft_round == 3:
            score += 6
        elif draft_round == 4:
            score += 4
        elif draft_round == 5:
            score += 2
        elif draft_round == 6:
            score += 1
        elif draft_round == 7:
            score += 0
        else:
            score -= 2

        if college_yards > 4500:
            score += 4
        elif college_yards > 3000:
            score += 3
        elif college_yards > 2000:
            score += 2
        elif college_yards > 1000:
            score += 1

        if age <= 21:
            score += 2
        elif age == 22:
            score += 1

        if years_played <= 3:
            score += 1

        if early_declare == "yes":
            score += 1

        if dash_time <= 4.45:
            score += 1
        elif dash_time <= 4.6:
            score += 0.5

        if opportunity == "good opportunity":
            score += 2
        elif opportunity == "okay opportunity":
            score += 1

        # Simple projection logic
        if score >= 20:
            proj = [950, 1100, 1200]
        elif score >= 16:
            proj = [800, 1000, 1100]
        elif score >= 12:
            proj = [650, 850, 950]
        else:
            proj = [400, 600, 750]

        return f"""
        <h2>📊 Player Score: {score}/25</h2>
        <h3>🔮 Projection Based on Score:</h3>
        <ul>
          <li>Year 1: {proj[0]} yards</li>
          <li>Year 2: {proj[1]} yards</li>
          <li>Year 3: {proj[2]} yards</li>
        </ul>
        <br><a href="/">Try Another Player</a>
        """

    return '''
        <h2>Enter Prospect Info</h2>
        <form method="post">
            Draft Round: <input name="draft_round" /><br>
            Age: <input name="age" /><br>
            College Yards: <input name="college_yards" /><br>
            Position (RB, WR, TE, QB): <input name="position" /><br>
            Years in College: <input name="years_played" /><br>
            Early Declare? (yes/no): <input name="early_declare" /><br>
            College Name: <input name="college" /><br>
            40-Yard Dash Time: <input name="dash_time" /><br>
            Depth Chart Opportunity (good opportunity / okay opportunity / bad opportunity): <input name="opportunity" /><br>
            <input type="submit" />
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
