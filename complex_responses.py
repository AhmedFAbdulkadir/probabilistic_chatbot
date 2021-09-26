import random

R_REVISION = "Research revision techniques, and use the calendar to organise and measure daily progress! Here's some material to start you off: https://www.bbc.co.uk/news/health-22565912"
R_SCHEDULE = "You can find your timetable here: https://canvas.bham.ac.uk/courses/47172/pages/timetables"
R_CALENDAR = "Your calendar can be accessed via: https://canvas.bham.ac.uk/calendar"
R_AI = "The AI module can be accessed via: https://canvas.bham.ac.uk/courses/46066/modules"
R_DEADLINE = "Your upcoming deadlines can be located on your personalised calendar: https://canvas.bham.ac.uk/calendar"
R_COMPUTER_SYSTEMS = "Computer Systems module lectures can be accessed via: https://canvas.bham.ac.uk/courses/46238/modules"
R_DATA_STRUCTURES = "Data Structures module lectures can be accessed via: https://canvas.bham.ac.uk/courses/46241/modules"
R_FULL_STACK = "Full Stack lecture notes can be accessed here: https://canvas.bham.ac.uk/courses/46056/modules"
R_PROJECT = "The research project module can be accessed here: https://canvas.bham.ac.uk/courses/46340"
R_WELFARE = "If appropriate, please feel free to contact welfare via: https://canvas.bham.ac.uk/courses/47814"
R_DIRECTIONS = "You should find your queries answered here: https://canvas.bham.ac.uk/courses/47172"
R_STRESS = "It's important you have a healthy control on stress levels. Please consult your wellbeing officers via email: cswelfare@contacts.bham.ac.uk."
R_LIBRARY = "For any remote access support or further information about library service, use this link: https://canvas.bham.ac.uk/courses/43955"


def unknown():
    response = ["Could you re-word that please? ",
                "...",
                "What does that mean?"][
        random.randrange(3)]
    return response
