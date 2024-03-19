import os
import requests
import time
from urllib.parse import quote

import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from api_calls import launch_api, populate_quiz, update_score,initialize_quizzer


class QuestionInterface(Widget):
    #############################
    # Variable Defines
    # ham_menu = ObjectProperty(None)
    # ####################################
    # question_data = ObjectProperty(None)
    # stats_feed = ObjectProperty(None)
    # question_text = ObjectProperty(None)
    # question_media = ObjectProperty(None)
    # answer_text = ObjectProperty(None)
    # answer_media = ObjectProperty(None)
    # user_input = ObjectProperty(None)
    #################################### 
       
            
    def __init__(self, **kwargs):
        super(QuestionInterface, self).__init__(**kwargs)
        # Main Script
        # Populate a quiz upon launch
        self.question_list, self.returned_sorted_questions = populate_quiz()
        # Display the first question
        self.display_question()
        self.has_seen_answer = False
        # Startup complete
        
    def make_quiz_if_empty(self):
        if len(self.question_list) <= 0:
            self.question_list, self.returned_sorted_questions = populate_quiz() 
        
    def display_question(self):
        '''
        Displays a question and returns data about that question
        First Phase of the Loop
        '''
        self.has_seen_answer = False
        self.make_quiz_if_empty()
        self.current_question = self.question_list[0]
        if self.current_question.get("file_name") != None:
            self.file_name = self.current_question.get("file_name")
            
        if self.current_question.get("file_path") != None:
            self.file_path = self.current_question.get("file_path")
            
        if self.current_question.get("type") != None:
            self.type = self.current_question.get("type")
            
        if self.current_question.get("subject") != None:
            self.subject = self.current_question.get("subject")
            data_label_string = f"{'Subject(s)':<23}:{' & '.join(self.subject)}\n"
            
            
        if self.current_question.get("related") != None:
            self.related = self.current_question.get("related")
        
        
        if self.current_question.get("question_text") != None:
            self.question_text = self.current_question.get("question_text")
            self.ids.question_text.text = self.question_text
            
        if self.current_question.get("question_media") != None:
            self.question_media = self.current_question.get("question_media")
            # Load media
        else:
            self.ids.question_media.text = ""
            
        if self.current_question.get("answer_media") != None:
            self.answer_media = self.current_question.get("answer_media")
            
        if self.current_question.get("answer_text") != None:
            self.answer_text = self.current_question.get("answer_text")
        else:
            self.answer_text = ""
            
        if self.current_question.get("next_revision_due") != None:
            self.next_revision_due = self.current_question.get("next_revision_due")
            
        if self.current_question.get("revision_streak") != None:    
            self.revision_streak = self.current_question.get("revision_streak")
            data_label_string += f"{'Streak':<25}:{str(self.revision_streak)}\n"
        if self.current_question.get("last_revised") != None:
            self.last_revised = self.current_question.get("last_revised")
            data_label_string += f"{'Last Reviewed':<18}:{str(self.last_revised)}\n"
        
        # Fill in stats_feed section
        label_string = f"{'Questions for Review':<25}: {str(len(self.returned_sorted_questions)-(25-len(self.question_list)))}"
        self.ids.stats_feed.text = label_string
        self.ids.question_data.text = data_label_string
        return None
    
    def show_answer(self):
        '''
        When button pressed, function shows the answer and enables the use of the scoring buttons
        Second Phase of the Loop
        '''
        self.has_seen_answer = True
        self.ids.answer_text.text = self.answer_text
        if self.answer_media != None:
            pass # Need to look up image display to get this portion to work #FIXME
    def question_correct(self):
        if self.has_seen_answer == True:
            # Update Score, then display the next question
            answer = "correct"
            file_name = self.file_name
            update_score(answer, file_name)
            self.question_list.pop(0)
            self.clear_fields()
            self.display_question()

            
        else:
            print("Button Disabled")
        
    def question_incorrect(self):
        if self.has_seen_answer == True:
            answer = "incorrect"
            file_name = self.file_name
            update_score(answer, file_name)
            self.question_list.pop(0)
            self.clear_fields()
            self.display_question()

        else:
            print("Button Disabled")
    def question_skip(self):
        '''Skips the question, removing it from the list with no score update'''
        self.question_list.pop(0)
        self.clear_fields()
        self.display_question()
        
    def clear_fields(self):
        self.ids.answer_text.text = ""
        self.ids.answer_media.text = "" #FIXME
        self.ids.question_text.text = ""
        self.ids.question_media.text = "" #FIXME
        self.ids.question_data.text = ""
        self.ids.stats_feed.text = ""
        self.ids.user_input.text = ""
    
    
    
class Quizzer(App):
    def build(self):
        return QuestionInterface()

if __name__ == '__main__':
    # launch_api()
    initialize_quizzer()
    Quizzer().run()    


