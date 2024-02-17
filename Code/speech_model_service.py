from flask import Flask, request, jsonify
import pickle
import pandas as pd

######################################################
#
# This script is the microservice that runs the speech 
# model given a list of features posted to it.
#
# Ideally we would have posted an mp3 file instead and 
# then processed it, but since the model relies on the 
# ChatGPT transcription service, this costs money and 
# requires an OpenAI Key, so will not be posted on the 
# Github repository
#
# It returns the predicted CEFR in json format to the 
# calling service
#
# author: Daniel Karp
######################################################

# Load the pickled model
try:
    with open('../Models/generated/gradient_boost_regressor_speech_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: Model file not found.")
    exit(1)
except Exception as e:
    print("Error loading model:", e)
    exit(1)

# Initialize Flask application
app = Flask(__name__)

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from request
        data = request.json
        
        # Check if 'input_data' exists in the request JSON
        if 'input_data' not in data:
            return jsonify({'error': 'Input data not provided.'}), 400

        data = data.get('input_data')

        # Validate input_data
        if not isinstance(data, list) or len(data) != 24:
            return jsonify({'error': 'Invalid input data format.'}), 400

        # Convert list to DataFrame
        data_df = pd.DataFrame({
            "filler_word_count": data[0],
            "formants_mean": data[1],
            "formants_median": data[2],
            "formants_std": data[3],
            "formants_min": data[4],
            "formants_max": data[5],
            "mfccs_mean": data[6],
            "mfccs_std": data[7],
            "mfccs_var": data[8],
            "spectral_centroid_mean": data[9],
            "spectral_bandwidth_mean": data[10],
            "pitch": data[11],
            "intensity": data[12],
            "speech_rate": data[13],
            "intensity_to_speech_rate_ratio": data[14],
            "pauses_duration": data[15],
            "pauses_frequency": data[16],
            "brunets_index": data[17],
            "average_sentence_length": data[18],
            "cohesion_score": data[19],
            "flesch_kincaid_score": data[20],
            "coleman_liau_index": data[21],
            "automated_readability_index": data[22],
            "repetitions": data[23]
        }, index=[0])
        
        # Make prediction using the loaded model
        prediction = model.predict(data_df)
        
        # Return prediction as JSON response
        return jsonify({'Predicted CEFR': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': 'An error occurred during prediction.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on port 8082
    app.run(debug=True, port=8082)
