class SalesDevelopmentRepresentativeAgent:
    def __init__(self, name, company="Phone Pe"):
        self.name = name
        self.company = company

    def introduction(self):
        return f"Hello, my name is {self.name} and I am calling from {self.company}. Briefly, the purpose of my call is to engage with you regarding our offerings."

    def language_selection(self, contact_name, preferred_language=None):
        if preferred_language:
            return preferred_language
        if self.is_indian_name(contact_name):
            return "Hindi"
        return "English"

    def is_indian_name(self, name):
        # Simplified check for Indian names
        indian_names = ["Amit", "Priya", "Raj", "Anjali"]  # Example names
        return name.split()[0] in indian_names

    def script_delivery(self, customer_type):
        scripts = {
            "existing": "We appreciate your continued trust in us. I would like to discuss how we can further enhance your experience.",
            "potential": "We have some exciting offerings that could benefit you. May I take a moment to explain?"
        }
        return scripts.get(customer_type, "I would like to share some information with you.")

    def handle_objectives(self, question):
        faq_responses = {
            "company": "We are a leading fintech company providing innovative solutions.",
            "product": "Our products are designed to enhance customer experience and operational efficiency."
        }
        return faq_responses.get(question.lower(), "I can schedule a follow-up meeting for more technical assistance.")

    def qualify_lead(self, questions):
        qualifying_questions = {
            "interest": "How interested are you in our offerings?",
            "needs": "What specific needs do you have that we can address?"
        }
        return {q: qualifying_questions.get(q, "Can you provide more details?") for q in questions}

    def capture_response(self, response):
        # Simulate capturing response
        print(f"Captured response: {response}")

    def next_steps(self, interest_level):
        if interest_level.lower() in ["high", "medium"]:
            return "I will schedule a follow-up meeting with a sales representative."
        return "Thank you for your time. Feel free to reach out if you have any questions."

    def call_summary(self, customer_details, discussion_points, interest_level):
        summary = {
            "customer_details": customer_details,
            "discussion_points": discussion_points,
            "interest_level": interest_level,
            "recommended_next_steps": self.next_steps(interest_level)
        }
        return summary

    def handle_call(self, contact_name, customer_type, questions, responses, interest_level):
        print(self.introduction())
        language = self.language_selection(contact_name)
        print(f"Speaking in {language}")
        print(self.script_delivery(customer_type))
        for question in questions:
            print(self.qualify_lead([question]))
        for response in responses:
            self.capture_response(response)
        print(self.next_steps(interest_level))
        return self.call_summary(contact_name, questions, interest_level)

# Example usage
agent = SalesDevelopmentRepresentativeAgent(name="Rajesh Kumar")
summary = agent.handle_call(
    contact_name="Amit Kumar",
    customer_type="potential",
    questions=["interest", "needs"],
    responses=["Very interested", "Looking for automation solutions"],
    interest_level="high"
)
print(summary)
