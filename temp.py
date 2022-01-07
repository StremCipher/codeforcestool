import requests
import json
# response=requests.get("https://flaskapitesting.herokuapp.com/api1/")
# print(response.status_code)
# print(response.json())
# response_json=response.json()
import pandas as pd

def api(id):
    data = pd.DataFrame(columns=['contest_id', 'q_rating', 'contest_type', 'question_no', 'accuracy',
                                 'avg_solving_time', 'sub_ratio', 'tried_but_cannot_solved', 'total_participant',
                                 'total_correct_sub_for_each_q', 'total_sub_for_each_q', 'total_time_to_sove_q'])
    standing = requests.get(
        "https://codeforces.com/api/contest.standings?contestId=" + id)
    json_file = standing.json()
    re = json_file['result']['rows']
    # contest_name = json_file['result']['contest']['name']
    # total_participant = len(re)
    # total_correct_sub_for_each_question = {}
    # problem_rating = {}
    # tried_but_not_solved = {}
    # total_time_to_solve_q = {}
    # total_sub_for_each_question = {}
    # avg_solve_time_for_each_question = {}
    # total_no_of_question = 0
    # accuracy = {}

    q_list = json_file['result']['problems']
    print("q_list",q_list)
    # for i in q_list:
    #     q_list.append(i['index'])
    #     print(i['index'])
# api("1620")


# arr={
#     "a":123,
#     "b1":122,
#     "b2":1234
# }
# ls=list(arr)
# print(ls)
# for q in ls:
#     print(q,arr[str(q)])
# contests = requests.get(
#         "https://codeforces.com/api/contest.list")
# json_file_1 = contests.json()
# print(json_file_1)
# contests=json_file_1['result']
# print(contests)
rating=requests.get("https://flaskapitesting.herokuapp.com/api/1617")
print(rating.json())
print(rating.json())
ls=(rating.json())
# print(ls)
arr=[]
for attribute, value in ls.items():
    print(attribute,value)
    arr.append([attribute,value])
print(arr)
# json1_data = json.loads(rating.json())[0]
# print(json1_data)
# response=requests.get("https://flaskapitesting.herokuapp.com/api/1616")
# print(response.status_code)
# print(response.json())
# # try:
#     print("ERROR1")
#     ls = list(response.json())
#     print(ls)
# except:
#     print("ERROR")