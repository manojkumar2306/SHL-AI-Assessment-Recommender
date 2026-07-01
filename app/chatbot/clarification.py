QUESTIONS = {
    "role": "What role are you hiring for?",
    "skills": "What are the key skills you want to assess?"
}


def clarification_question(missing):

    if len(missing) == 0:
        return None

    return QUESTIONS[missing[0]]