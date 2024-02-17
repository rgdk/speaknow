import requests, json 

######################################################
#
# This is a test script to test the speech model 
# microservice 
#
# It requires that a list of features is posted to it.
#
# The features are all numeric, and need to be in the   
# correct order as shown in the sample call below.
#
# It prints the reponse in json format
#
# author: Daniel Karp
######################################################


# URL of the microservice
url = 'http://localhost:8082/predict'

# Input data
input_data = {"input_data":
		[3,		 ### filler_word_count
		1575,		 ### formants_mean
		1280,		 ### formants_median
		1077,		 ### formants_std
		0,		 ### formants_min
		5767,		 ### formants_max
		-19.98,		 ### mfccs_mean
		31.91,		 ### mfccs_std
		17586446,	 ### mfccs_var
		1930,		 ### spectral_centroid_mean
		1554,		 ### spectral_bandwidth_mean
		1593,		 ### pitch
		0.039929543,	 ### intensity
		0.10577355,	 ### speech_rate
		0.37750025,	 ### intensity_to_speech_rate_ratio
		0.0475,		 ### pauses_duration
		0.386965376,	 ### pauses_frequency
		1.771,		 ### brunets_index
		22.4,		 ### average_sentence_length
		0.6251,		 ### cohesion_score
		7.79,		 ### flesch_kincaid_score
		3.8260,		 ### coleman_liau_index
		12.20836,	 ### automated_readability_index
		2]		 ### repetitions
	}

headers = {'Content-Type': 'application/json'}

data = json.dumps(input_data) 

# Send POST request
response = requests.post(url, data=data, headers=headers)

# Print response
print(response.json())