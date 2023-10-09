from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

DEFAULT_WAIT = 10
EXTENDED_WAIT = 15
NORMAL_WAIT = 5
SHORTER_WAIT = 4
SHORTEST_WAIT = 3
QUICK_WAIT = 2

def sel_text(textArea, timer, text):
    textArea.clear()
    textArea.send_keys(text)
    time.sleep(timer)


def intro(textArea, driver):
    sel_text(textArea, SHORTER_WAIT, "Hello! My name is Daphne, and welcome to my first exploration activity!")
    sel_text(textArea, SHORTER_WAIT, "I am showcasing the Selenium library using Python!")
    sel_text(textArea, SHORTER_WAIT, "Today, we'll be playing a small interactive game")
    sel_text(textArea, NORMAL_WAIT, "Before we play, you will have to click back to your terminal or back to automated Chrome when asked")
    sel_text(textArea, SHORTEST_WAIT, "Alright, shall we get started then?")
    sel_text(textArea, NORMAL_WAIT, "I have a question to ask you, click back to your terminal to answer it")
    fav_animatronic(textArea, driver)

#sel_text(textArea, 3, "")

def expected_title(driver, title):
    try:
        WebDriverWait(driver, DEFAULT_WAIT).until(
            EC.title_is(title)
        )
    except TimeoutException as e:
        print(e)

def click_button(driver, element):
    try:
        button = WebDriverWait(driver, DEFAULT_WAIT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, element))
        )
        button.click()
    except NoSuchElementException as e:
        print(e)

def basic_input():
    fav = input("Your answer: ")
    fav = fav.lower()
    print("Click back to the automated Chrome window")
    return fav

def good_ending(textArea, driver, choice):
    if choice == 1:
        sel_text(textArea, SHORTEST_WAIT, "Let me reward you:")
    driver.get("https://drive.google.com/drive/folders/1ua1tIYD3njUUe9-E5dUVVszFzw5KL_l6?usp=sharing")
    expected_title(driver, driver.title)
    click_button(driver, "[aria-label='RPReplay_Final1696827204.mov Shared Video']")
    expected_title(driver, driver.title)
    time.sleep(EXTENDED_WAIT)

def bad_ending(driver):
    driver.get("https://drive.google.com/drive/folders/1znQuG-00EmQ1mpuEU2npfnzIi8Dy6Tib?usp=sharing")
    expected_title(driver, driver.title)
    click_button(driver, "[aria-label='RPReplay_Final1696827487.mov Shared Video']")
    expected_title(driver, driver.title)
    time.sleep(DEFAULT_WAIT)

def freddy(textArea, driver):
    sel_text(textArea, SHORTER_WAIT, "So Freddy is your favourite, huh?")
    sel_text(textArea, SHORTER_WAIT, "Solid choice. He's my favourite too, so I suppose you have taste.")
    sel_text(textArea, SHORTER_WAIT, "In fact, here's a gift. You got the good ending")
    driver.get("https://drive.google.com/file/d/10tEap_4oLNQOh_8npAsEDGNmAlHImyWS/view?usp=drive_link")
    expected_title(driver, driver.title)
    time.sleep(SHORTER_WAIT)
    good_ending(textArea, driver, 0)

def bonnie(textArea, driver):
    sel_text(textArea, SHORTER_WAIT, "Bonnie is pretty cool. I have another question for you:")
    sel_text(textArea, SHORTER_WAIT, "Do you think he is blue or purple?")
    sel_text(textArea, SHORTER_WAIT, "Click back to your terminal to answer the question")
    print("Is Bonnie blue or purple:")
    print("(b)lue\n(p)urple")
    fav = basic_input()
    time.sleep(NORMAL_WAIT)

    if fav == "b":
        sel_text(textArea, SHORTER_WAIT, "Good choice. You have a good pair of eyeballs")
        good_ending(textArea, driver, 1)
    elif fav == "p":
        sel_text(textArea, QUICK_WAIT, "...")
        sel_text(textArea, SHORTER_WAIT, "Yikes, you may want to check out your eyesight..")
        sel_text(textArea, SHORTER_WAIT, "Actually, let me help you out with that:")
        bad_ending(driver)
    else:
        sel_text(textArea, SHORTER_WAIT, "you think you're a comedian, huh?")
        sel_text(textArea, SHORTER_WAIT, "actually, you know what's funny?")
        bad_ending(driver)

def chica(textArea, driver):
    sel_text(textArea, SHORTER_WAIT, "Chica is kinda like me ngl. Pizza is mad delicious")
    sel_text(textArea, SHORTER_WAIT, "Do you think her cupcake is cute?")
    sel_text(textArea, SHORTER_WAIT, "Let me refresh your mind on how it looks:")
    nav_to_cupcake(driver)
    textArea = driver.find_element(By.CSS_SELECTOR, "textarea.note-area")
    sel_text(textArea, SHORTER_WAIT, "Now that you've gotten a good look at it,")
    sel_text(textArea, SHORTER_WAIT, "Click back to your terminal to answer the question")
    fav = cupcake_question(1)
    time.sleep(NORMAL_WAIT)

    if fav == "n":
        sel_text(textArea, QUICK_WAIT, "Great answer!")
        good_ending(textArea, driver, 1)
    elif fav == "y":
        sel_text(textArea, QUICK_WAIT, "...")
        sel_text(textArea, SHORTEST_WAIT, "Take a look at it again man..")
        nav_to_cupcake(driver)
        textArea = driver.find_element(By.CSS_SELECTOR, "textarea.note-area")
        sel_text(textArea, SHORTER_WAIT, "Click back to your terminal to answer the question...")
        fav = cupcake_question(2)
        time.sleep(NORMAL_WAIT)

        if fav == "n":
            sel_text(textArea, SHORTEST_WAIT, "Yeah I thought so...")
            good_ending(textArea, driver, 1)
        else:
            sel_text(textArea, QUICK_WAIT, "...")
            sel_text(textArea, QUICK_WAIT, "no")
            bad_ending(driver)
    else:
        sel_text(textArea, SHORTER_WAIT, "that wasn't even one of the answers bro..")
        sel_text(textArea, SHORTEST_WAIT, "jumpscare incoming in 3 seconds:")
        bad_ending(driver)

def cupcake_question(choice):
    if choice == 1:
        print("Do you think the cupcake is adorable?")
    else:
        print("Do you think the cupcake is adorable...?")

    print("(y)es\n(n)o")
    fav = input("Your answer: ")
    fav = fav.lower()
    print("Click back to the automated Chrome window")
    return fav

def nav_to_cupcake(driver):
    driver.get("https://drive.google.com/drive/folders/1VocJye7S1GrQnnM49CzSHB9PI9UvRpJn?usp=sharing")
    expected_title(driver, driver.title)
    click_button(driver, "[aria-label='chica cupcake.jpeg Shared Image']")
    time.sleep(DEFAULT_WAIT)
    expected_title(driver, driver.title)
    driver.get("https://blankslate.io")
    expected_title(driver, driver.title)

def foxy(textArea, driver):
    sel_text(textArea, SHORTEST_WAIT, "Pirates are cool")
    sel_text(textArea, QUICK_WAIT, "uh..")
    sel_text(textArea, SHORTER_WAIT, "I don't have anything else to say, so..")
    good_ending(textArea, driver, 1)


def fav_animatronic(textArea, driver):
    print("Who is your favourite FNAF 1 animatronic? Select one of the 4 options below:")
    print("(f)reddy\n(b)onnie\n(c)hica\n(fo)xy")
    fav = basic_input()
    time.sleep(NORMAL_WAIT)

    if fav == "f":
        freddy(textArea, driver)
    elif fav == "b":
        bonnie(textArea, driver)
    elif fav == "c":
        chica(textArea, driver)
    elif fav == "fo":
        foxy(textArea, driver)
    else:
        sel_text(textArea, SHORTEST_WAIT, "hey man, not cool...")
        sel_text(textArea, SHORTEST_WAIT, "that wasn't one of the answers...")
        sel_text(textArea, SHORTEST_WAIT, "you're gonna regret that")
        bad_ending(driver) 