from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = input("Enter URL of the first assignment: \n")
last_assignment = input("Enter the chapter and assignment number of the last assignment (ex: 4.12):\n")

browser = webdriver.Chrome('C:/Users/veyro/OneDrive/Desktop/chromedriver_win32/chromedriver.exe')
browser.get(url)

input("Okay to Proceed?")

last_loop = False

while (True):

    text_areas = browser.find_elements_by_class_name('zb-text-area')
    show_answer_buttons = browser.find_elements_by_class_name('show-answer-button')

    for show_answer_button in show_answer_buttons:
        show_answer_button.click()
        show_answer_button.click()

    answers = browser.find_elements_by_class_name('forfeit-answer')

    while(len(text_areas) > len(answers)):
        text_areas.pop(0)

    for i in range(len(text_areas)):
        text_areas[i].send_keys(answers[i].text)
        text_areas[i].send_keys(Keys.ENTER)

    labels = browser.find_elements_by_css_selector('div.zb-radio-button label[aria-hidden="true"]')
    browser.execute_script('arguments[0].scrollIntoView();', browser.find_element_by_class_name('activity-title-bar'))
    for label in labels:
        label.click()

    if last_loop == True:
        break;

    next_button = browser.find_element_by_class_name('next-section-link')
    next_button.click()

    time.sleep(4)

    current_assignment_label = browser.find_element_by_class_name('zybook-section-title')
    current_assignment = current_assignment_label.text.split(' ')[0]

    if current_assignment == last_assignment:
        last_loop = True




#TODO
# start_button = browser.find_element_by_class_name('start-button')
# start_button.click()
# two_times_speed_button = browser.find_element_by_class_name('2b-checkbox')
# two_times_speed_button.click()
# steps = browser.find_elements_by_class_name('step')
# for i in range (len(steps) - 1):
#     try:
#         play_button = browser.find_element_by_class_name('play-button')
#     except:
#         time.sleep(5.5)
#     play_button.click()

