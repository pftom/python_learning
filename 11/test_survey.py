import unittest

from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """test single answer can be stored safely"""

    def setUp(self):
        """ 
        create a survey object
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chines', 'English', 'Python']
    
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_reponse(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    def test_store_list_response(self):
        responses = ['a', 'b', 'c']
        self.my_survey.store_response(responses)

        for response in responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()