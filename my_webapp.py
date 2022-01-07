import pandas as pd
import requests
import pickle
from flask import Flask,render_template,request,jsonify
flask_app=Flask(__name__)

@flask_app.route("/api/<id>")
def api(id):
    data = pd.DataFrame(columns=['contest_id', 'q_rating', 'contest_type', 'question_no', 'accuracy',
                                 'avg_solving_time', 'sub_ratio', 'tried_but_cannot_solved', 'total_participant',
                                 'total_correct_sub_for_each_q', 'total_sub_for_each_q', 'total_time_to_sove_q'])
    standing = requests.get(
        "https://codeforces.com/api/contest.standings?contestId=" + id)
    json_file = standing.json()
    re = json_file['result']['rows']
    contest_name = json_file['result']['contest']['name']
    total_participant = len(re)
    total_correct_sub_for_each_question = {}
    problem_rating = {}
    tried_but_not_solved = {}
    total_time_to_solve_q = {}
    total_sub_for_each_question = {}
    avg_solve_time_for_each_question = {}
    total_no_of_question = 0
    accuracy = {}

    q_list = json_file['result']['problems']
    q_ids = []
    for i in q_list:
        q_ids.append(i['index'])
    for i in q_list:
        if 'rating' in i:
            problem_rating[total_no_of_question + 1] = i['rating']
        else:
            problem_rating[total_no_of_question + 1] = -1
        total_no_of_question += 1
        total_time_to_solve_q[total_no_of_question] = 0
        total_correct_sub_for_each_question[total_no_of_question] = 0
        tried_but_not_solved[total_no_of_question] = 0
        total_sub_for_each_question[total_no_of_question] = 0
        accuracy[total_no_of_question] = 0
    for i in re:
        user_sub_for_each_q = i['problemResults']
        question_id = 1
        temp = []
        for i in user_sub_for_each_q:
            if ('bestSubmissionTimeSeconds' in i):
                temp.append([i['bestSubmissionTimeSeconds'], question_id])
                total_correct_sub_for_each_question[question_id] += 1
            else:
                temp.append([0, question_id])
                if i['rejectedAttemptCount'] > 0:
                    tried_but_not_solved[question_id] += 1
            question_id += 1
        temp.sort()
        prev_time = 0
        for [x, y] in temp:
            total_time_to_solve_q[y] += x - prev_time
            prev_time = x
    for i in range(total_no_of_question):
        total_sub_for_each_question[i +
                                    1] = total_correct_sub_for_each_question[i + 1] + tried_but_not_solved[i + 1]
        if total_sub_for_each_question[i + 1] > 0:
            accuracy[i + 1] = total_correct_sub_for_each_question[i + 1] / \
                              total_sub_for_each_question[i + 1]

    for i in range(total_no_of_question):
        if (total_correct_sub_for_each_question[i + 1] > 0):
            avg_solve_time_for_each_question[i + 1] = total_time_to_solve_q[i + 1] / \
                                                      total_correct_sub_for_each_question[i + 1]
        else:
            avg_solve_time_for_each_question[i + 1] = 0
    contest_type = 4  # for all other contest
    if "Div. 3" in contest_name:
        contest_type = 3
    if "Div. 2" in contest_name:
        contest_type = 2
    if "Div. 1" in contest_name:
        contest_type = 1
    if "Global Round" in contest_name:
        contest_type = 0
    for i in range(total_no_of_question):
        data = data.append(
            {'contest_id': id, 'q_rating': problem_rating[i + 1], 'contest_type': contest_type, 'question_no': i + 1,
             'accuracy': accuracy[i + 1],
             'avg_solving_time': avg_solve_time_for_each_question[i + 1],
             'sub_ratio': total_correct_sub_for_each_question[i + 1] / total_participant,
             'tried_but_cannot_solved': tried_but_not_solved[i + 1], 'total_participant': total_participant,
             'total_correct_sub_for_each_q':
                 total_correct_sub_for_each_question[i + 1], 'total_sub_for_each_q': total_sub_for_each_question[i + 1],
             'total_time_to_sove_q':
                 total_time_to_solve_q[i + 1]}, ignore_index=True)
    data = data.drop(['q_rating'], axis=1)
    rating=[]
    model0 = pickle.load(open('div0_model.sav', 'rb'))
    model1 = pickle.load(open('div1_model.sav', 'rb'))
    model2 = pickle.load(open('div2_model.sav', 'rb'))
    model3 = pickle.load(open('div3_model.sav', 'rb'))
    print(contest_type)
    if contest_type == 0:
        rating = model0.predict(data)
    if contest_type == 1:
        rating = model1.predict(data)
    if contest_type == 2:
        rating = model2.predict(data)
    if contest_type == 3:
        rating = model3.predict(data)
    else:
        rating = model0.predict(data)
    response={
    }
    idx=0
    # print(len(q_ids),len(rating))
    for i in q_ids:
        response[str(i)]=str(rating[idx])
        idx+=1
    # print(response)
    return response

@flask_app.route("/")
def home():
    return render_template('index.html')
