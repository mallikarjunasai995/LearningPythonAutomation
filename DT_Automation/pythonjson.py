import json 
import requests
import time
import re
# Name/Value pairs: Represents Data, name is followed by ‘:'(colon) and the Name/Value pairs separated by, (comma).
# Curly braces: Holds objects.
# Square brackets: Hold arrays with values separated by, (comma).
import jmespath
print('hi am there')
# json_string = '{"name": "erik", "age": 38, "married": true}'
# result = json.loads(json_string)
# print(type(result))
# print(result)
url = 'http://css-star-dvv-uls-api.wdc.com:8080/Api/Execution/GetExecutionCycleTestCaseDetails'
data = {"ExecutionCycleId":42881,"CurrentStatus":"","TestCaseNm":"","HostName":"","DutSerialNbr":"","ExecutionCycleOperationWorkflowIds":""}
response = requests.post(url,json.dumps(data),headers={"Content-Type":"application/json"})
time.sleep(3)
#print(response.json())
result= response.json()
# finres = jmespath.search('CurrentStatus	:', result)
finres = result[0]
failedinstanceID = []
test_names = []
reg = re.compile('\d{1,}m \d{1,}s')
for i in finres:
    if i['CurrentStatus'] == 'Test Execution - Failed'and reg.search(i['TestExecutionTime']) :
        #i['TestExecutionTime'] == regularexpression
        failedid = i['TestExecutionInstanceId']
        test_name = i['TestNm']
        # print(i['TestExecutionTime'])
        print(i['TestNm'])

        test_names.append(test_name)
        
        failedinstanceID.append(failedid)
        
print(test_names)
# print((failedinstanceID))
# print(test_names)
        
    

# with open('content.json','w') as jsonfile:
#     json.dump(finres, jsonfile)
# for i in result:
#     print(i)
#     break






