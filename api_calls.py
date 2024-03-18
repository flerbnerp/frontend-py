import requests
import os
import subprocess
from urllib.parse import quote
def launch_api():
    project_root = os.path.dirname(os.path.abspath(__file__))  # Get path of frontend-py
    quizzer_dir = os.path.join(project_root, "..", "quizzer")  # Navigate up two directories
    command = f"nohup uvicorn api:app --reload"
    subprocess.Popen(command, shell=True)

def populate_quiz():
    root = "http://127.0.0.1:8000/"
    command_pop_quiz = "populate_quiz"
    data = requests.get(f"{root}{command_pop_quiz}")
    data = data.json()
    question_list = data["question_list"]
    returned_sorted_questions = data["sorted_questions"]
    return question_list, returned_sorted_questions
def extract_question_data(current_question):
    '''
    Takes the current question as an argument
    returns the relevant key:values for that question if they exist
    '''
    file_name = current_question.get("file_name")
    file_path = current_question.get("file_path")
    type = current_question.get("type")
    subject = current_question.get("subject")
    related = current_question.get("related")
    question_text = current_question.get("question_text")
    question_media = current_question.get("question_media")
    answer_media = current_question.get("answer_media")
    answer_text = current_question.get("answer_text")
    next_revision_due = current_question.get("next_revision_due")    
    revision_streak = current_question.get("revision_streak")
    last_revised = current_question.get("last_revised")

def update_score(answer, file_name):
    encoded_file_name = quote(file_name)
    if answer == "correct":
        first_part = "http://127.0.0.1:8000/update_score/{status, file_name}?status=correct&file_name="
        query = first_part + encoded_file_name
        response = requests.get(f"{query}")
    elif answer == "incorrect":
        first_part = "http://127.0.0.1:8000/update_score/{status, file_name}?status=incorrect&file_name="
        query = first_part + encoded_file_name
        response = requests.get(f"{query}")        
    else:
        print("Something went wrong")

def initialize_quizzer():
    root = "http://127.0.0.1:8000/"
    command_initialize_quizzer = "initialize_quizzer"
    requests.get(f"{root}{command_initialize_quizzer}")