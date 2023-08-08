#!/python3- code not tested
import random
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis"
}
for i in range(5):
    file = open('quiz%s.txt'%(i+1),'w')
    answer = open('answer%s.txt'%(i+1),'w')
    file.write('Name:\nDate\n')
    file.write('State capital quiz %s'%(i+1))
    states = list(state_capitals.keys())
    random.shuffle(states)
    for j in range(20):
        correct = state_capitals[states[j]]
        wrong = list(state_capitals.values())
        del wrong[wrong.index(correct)]
        wrong_answers = random.sample(wrong,3)
        all_options = [correct] + wrong_answers
        random.shuffle(all_options)
        for k in range(20):
            file.write('%s. What is the capital of %s?\n'%(k+1,state_capitals[k]))
            for z in range(4):
                file.write('  %s. %s\n'%('ABCD'[z]),all_options[z])
            answer.write('%s. %s\n'%(k+1,'ABCD'[all_options.index(correct)]))
    file.close()
    answer.close()
