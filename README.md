##### This repository is designed to provide the code set relating to the SpeakNow ML Lead Assignment.

As provided, the task was presented as:
Using the provided dataset develop a micro-service that evaluates English proficiency based on short audio clips and written text samples.

The service should assess fluency, grammar, vocabulary, and pronunciation in speech, and grammar, vocabulary, and coherence in writing.

Outline how your model can be scaled for handling large-scale data.

Discuss the model's performance metrics and how you would improve them over time. 

Provide a detailed report explaining your methodology, choice of models, and rationale. Include code comments and a README for setup and execution instructions.

Prepare a short presentation summarizing your approach, challenges faced, and key learnings

**Dataset**:
- https://drive.google.com/drive/folders/1lPofPe-fp0Baa67ttEyRBAOjAHHtCyw9
- SpeakNow_test_data.csv file 


**Expected deliverables**:
- Source Code in Git Repository
- A Report
- A Presentation file such as PPT, PDF or similar (Design not important)


### Source Code ###

The source code includes the jupyter notebooks for generating transcriptions, executing data engineering and generating the models.

### Microservice ###

To run the speech model microservice:
- navigate to the Code directory
- execute the speech_model_service.py python script as:
  python .\speech_model_service.py
- once it is up and running, then open the speech_model_service_test.py script for editing. It is also found in the Code directory
- Alter the feature values relating to the audio file to be assessed (note these need to be extracted separately due to the need to use ChatGPT for the transcription)
- Then save and execute the file from the command line as:
   python .\speech_model_service_test.py

![image](https://github.com/rgdk/speaknow/assets/7219017/59dba98e-bbf1-46b2-a899-158e5cc3021f)

![image](https://github.com/rgdk/speaknow/assets/7219017/1a937abf-6be1-408f-9a04-4b9c111f4368)


  
