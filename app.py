from flask import Flask, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return """
        <p>Welcome to the Study-Strategy API.</h1>
        <p>However this is not what you're looking for.</h1>
        <p>Please use the following endpoints to access the ML-Medical API.</p>
        <ul>
            <li>/allocate_hours</li>
            <li>/calculate_ocean_scores</li>
            <li>/suggest_techniques</li>
        </ul>
    """

# Endpoint to allocate study hours based on difficulty
@app.route('/allocate_hours', methods=['POST'])
def allocate_hours():
    try:
        data = request.get_json()
        total_hours = data['total_hours']
        subjects = data['subjects']

        if not isinstance(total_hours, int) or total_hours <= 0 or not subjects:
            return jsonify({'error': 'Invalid input data'}), 400

        total_difficulty = sum([subject['difficulty'] for subject in subjects])

        # Allocate study hours based on difficulty
        for subject in subjects:
            subject['allocated_hours'] = (subject['difficulty'] / total_difficulty) * total_hours

        return jsonify({
            'message': 'Study hours allocated successfully',
            'total_subjects': len(subjects),
            'total_hours': total_hours,
            'subjects': subjects
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to calculate OCEAN personality matrix scores
@app.route('/calculate_ocean_scores', methods=['POST'])
def calculate_ocean_scores():
    try:
        data = request.get_json()
        quiz_responses = data['quiz_responses']

        if not quiz_responses or not all('trait' in response and 'score' in response for response in quiz_responses):
            return jsonify({'error': 'Invalid quiz responses'}), 400

        # Calculate average OCEAN scores
        ocean_scores = {
            'openness': 0,
            'conscientiousness': 0,
            'extraversion': 0,
            'agreeableness': 0,
            'neuroticism': 0
        }

        for response in quiz_responses:
            trait = response['trait']
            score = response['score']
            if trait in ocean_scores:
                ocean_scores[trait] += score

        # Average the scores
        for trait in ocean_scores:
            ocean_scores[trait] /= len(quiz_responses)

        return jsonify({
            'message': 'OCEAN personality scores calculated',
            'ocean_scores': ocean_scores
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to suggest study techniques based on OCEAN scores
@app.route('/suggest_techniques', methods=['POST'])
def suggest_techniques():
    try:
        data = request.get_json()
        ocean_scores = data['ocean_scores']

        if not ocean_scores or not all(trait in ocean_scores for trait in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']):
            return jsonify({'error': 'Invalid OCEAN scores'}), 400

        # Suggest techniques based on OCEAN traits
        techniques = []
        if ocean_scores['openness'] > 70:
            techniques.append('Mind mapping, creative summarization')
        if ocean_scores['conscientiousness'] > 70:
            techniques.append('Pomodoro method, strict scheduling')
        if ocean_scores['extraversion'] < 50:
            techniques.append('Solitary study, self-quizzing')
        if ocean_scores['agreeableness'] > 70:
            techniques.append('Collaborative projects, peer learning')
        if ocean_scores['neuroticism'] > 60:
            techniques.append('Frequent breaks, stress-relief exercises')

        return jsonify({
            'message': 'Study techniques suggested',
            'techniques': techniques
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
