from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import requests

def lookup(subject, number):
    response = requests.head('https://www.albany.edu/registrar/schedule-of-classes-spring.php').status_code
    if(response != 200):
        return "down"
    opts = Options()
    opts.headless = True
    assert opts.headless

    browser = Chrome(options=opts)

    browser.get('https://www.albany.edu/registrar/schedule-of-classes-spring.php')
    search_form = browser.find_element_by_id('Course_Subject')
    search_form.send_keys(subject)
    search_form = browser.find_element_by_id('Course_Number')
    search_form.send_keys(number)
    search_form.submit()
    results = browser.find_elements_by_tag_name('body')
    list1 = []
    body = ""
    for i in results:
        body += i.text

    newbody = body[21:]
    list1 = newbody.split("\n")
    
    browser.close()
    return list(list1)

def allInfo(group):
    classNum = []
    courseInfo = []
    meetingInfo = []
    seats = []
    comments = []

    for i in group:
        if("Class Number:" in i):
            sliced = i[14:]
            classNum.append(sliced)
        elif("Course Info:" in i):
            sliced = i[13:]
            courseInfo.append(sliced)
        elif("Meeting Info:" in i):
            sliced = i[14:]
            meetingInfo.append(sliced)
        elif("Seats" in i):
            seats.append(i)
        elif("Comments:" in i):
            sliced = i[10:]
            comments.append(sliced)
    
    return list(classNum), list(courseInfo), list(meetingInfo), list(seats), list(comments)


# print(classNum)
# print(courseInfo)
# print(meetingInfo)
# print(seats)
# print(comments)

# for i in range(len(classNum)):
#     print(classNum[i])
#     print(courseInfo[i])
#     print(meetingInfo[i])
#     print(seats[i])
#     print("---------------------------------------------------------------")
