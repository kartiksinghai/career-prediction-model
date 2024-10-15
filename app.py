from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from recommendation_model import find_top_professions

app = Flask(__name__)

# Serve the chatbot HTML page
@app.route('/')
def home():
    return render_template('app.html')

# Define the route that will handle profession requests
@app.route('/get_professions', methods=['POST'])
def get_professions():
    data = request.json  # Get JSON data from the request

    # Extract the list of interests from the request
    interests = data.get('interests', [])
    
    if not interests:
        return jsonify({'error': 'Please provide a list of interests.'}), 400

    # Define the path to your dataset
    dataset_path = '/Users/kartiksinghai/Desktop/coding/vscode/python.py/sihdata1.csv'  # Make sure this path is correct

    try:
        # Call the model function to get top professions
        top_professions = find_top_professions(dataset_path, interests)

        # Return the top professions as a JSON response
        return jsonify({'top_professions': top_professions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for serving favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
