class AnonymousSurvey():
    """collect anonymous survey response"""

    def __init__(self, question):
        """save a question, ready for save answer"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """show survey question"""
        print(self.question)
    
    def store_response(self, new_response):
        """save single / list survey response"""
        if isinstance(new_response, list):
            for response in new_response:
                self.responses.append(response)
        else:
            self.responses.append(new_response)
    
    def show_results(self):
        """show all the collected response"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)



