import re
import complex_responses as complex


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-:]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def check_all_messages(message):
    highest_prob_list = {}

    def response(bothoven_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bothoven_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello, welcome!', ['hello', 'hi', 'hey'], single_response=True)
    response('If I don\'t see ya: good morning, good evening and good night!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], single_response = True)
    response('Using a mix of cramming and distributive practice is best.', ['how', 'revise', 'way', 'best', 'revision'], single_response = True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    # Complex responses stored in separate file
    response(complex.R_REVISION, ['give', 'revision', 'advice', 'revise', 'struggling'], single_response=True)
    response(complex.R_SCHEDULE, ['timetable', 'time', 'table'], single_response=True)
    response(complex.R_CALENDAR, ['calendar', 'month'], single_response =True)
    response(complex.R_AI, ['module', 'lectures', 'ai'], required_words = ['ai'])
    response(complex.R_COMPUTER_SYSTEMS, ['module', 'lectures', 'computer', 'systems'], required_words = ['computer', 'systems'])
    response(complex.R_DATA_STRUCTURES, ['module', 'lectures', 'data', 'structures'], required_words = ['data', 'structures'])
    response(complex.R_PROJECT, ['module', 'lectures', 'project', 'research'], required_words = ['project'])
    response(complex.R_FULL_STACK, ['module', 'lectures', 'full', 'stack'], required_words = ['full', 'stack'])
    response(complex.R_DIRECTIONS, ['way','travel', 'campus', 'directions'], single_response = True)
    response(complex.R_WELFARE, ['stress', 'help', 'welfare'], single_response = True)
    response(complex.R_STRESS, ['stress', 'depress', 'depression'], single_response = True)
    response(complex.R_DEADLINE, ['deadlines', 'deadline', 'exams', 'tests', 'exam', 'test'], single_response =True)
    response(complex.R_LIBRARY, ['library', 'support', 'it'], required_words = ['library'])
    
    


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return complex.unknown() if highest_prob_list[best_match] < 5 else best_match


# Start of the chatbot
while True:
    print('Bothoven: ' + get_response(input('You: ')))