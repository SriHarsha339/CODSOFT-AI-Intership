import re

class CollegeChatbot:
    negative_res = ("no", "nope", "nah", "naw", "not interested", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    def __init__(self, college_name, location):
        self.college_name = college_name
        self.location = location
        self.keywords = {
            'greetings': ['hello', 'hi', 'hey', 'howdy'],
            'farewells': ['goodbye', 'bye', 'see you later', 'take care'],
            'admission': ['admission', 'apply', 'enroll', 'application', 'entrance exam', 'eligibility'],
            'courses': ['courses', 'programs', 'degree', 'majors', 'curriculum', 'syllabus'],
            'faculty': ['faculty', 'professors', 'teachers', 'instructors', 'lecturers', 'researchers'],
            'events': ['events', 'activities', 'schedule', 'workshops', 'seminars', 'conferences'],
            'location': [self.location.lower()],
            'college_name': [self.college_name.lower()],
            'about': ['about', 'information', 'details', 'know more'],
            'contact': ['contact', 'reach out', 'get in touch'],
            'farewell_terms': ['thank you', 'thanks', 'appreciate', 'grateful']
        }
        self.responses = {
            'greetings': f"Hello! Welcome to {self.college_name}. How can I assist you today?",
            'farewells': f"Goodbye! Thank you for visiting {self.college_name}. If you have any further questions, feel free to ask!",
            'admission': f"For admission inquiries, please visit our website's admission section. You can also contact our admission office at {self.location}.",
            'courses': f"Chemical Engineering\n Civil Engineering\nComputer Science & Engineering\nComputer Science & Business  Systems(TCS)\nComputer Science & Engineering (DS)\nComputer Science & Engineering (AI & ML)\nComputer Science & Engineering (IoT)\nElectronics and Communication Engineering\nElectrical and Electronics Engineering\nInformation Technology\nMechanical Engineering\nChemistry\nMathematics\nHumanities\nPhysics\nComputer Applications Management Sciences .",
            'faculty': f"Our faculty comprises experienced professionals. Check the faculty section on our website for more details.",
            'events': f"We regularly organize events and activities. Visit our website for the latest updates on events happening at {self.college_name}.",
            'location': f"{self.college_name} is located in {self.location}.",
            'college_name': f"This is {self.college_name}.",
            'about': f"{self.college_name} is committed to providing quality education and fostering a vibrant learning community.",
            'contact': f"You can reach out to us by visiting our website or contacting us directly at {self.location} or Call Us: 91******",
            'farewell_terms': "You're welcome! If you need further assistance, feel free to ask."
            
        }

    def greet(self):
        print(f"Welcome to {self.college_name} chatbot! How can I assist you today?")

    def make_exit(self, reply):
        return any(reply.lower() == command for command in self.exit_commands)

    def chat(self):
        while True:
            reply = input("You: ").lower()
            if self.make_exit(reply):
                print(self.responses['farewells'])
                break
            print(self.generate_response(reply))

    def generate_response(self, query):
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if re.search(r'\b{}\b'.format(keyword), query, re.IGNORECASE):
                    return self.responses[category]
        return "I'm sorry, I couldn't understand your query. Please try again."

# Example usage
college_name = "R.V.R. & J.C.College of Engineering"
location = "Chowdavaram, Guntur, Andhra Pradesh"
chatbot = CollegeChatbot(college_name, location)
chatbot.greet()
chatbot.chat()
