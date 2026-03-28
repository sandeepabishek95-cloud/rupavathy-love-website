from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index_20260328.html')

# Memories Page
@app.route('/memories')
def memories():
    return render_template('memories_20260328.html')

# Quiz Page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = [
        {"q": "Where did we first meet?", "a": "park"},
        {"q": "Your favorite color?", "a": "red"},
        {"q": "Favorite vacation spot?", "a": "beach"},
        {"q": "First movie we watched together?", "a": "inception"},
        {"q": "Your favorite dessert?", "a": "chocolate"}
    ]
    
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            ans = request.form.get(f'q{i}')
            if ans and ans.lower() == q["a"].lower():
                score += 1
        if score == len(questions):
            return redirect(url_for('reward'))
        else:
            return render_template('quiz_20260328.html', questions=questions, score=score)
    return render_template('quiz_20260328.html', questions=questions, score=None)

# Reward Page
@app.route('/reward')
def reward():
    return render_template('reward_20260328.html')

if __name__ == "__main__":
    app.run(debug=True)
