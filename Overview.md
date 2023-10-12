# Overview
The library I chose for my first exploration activity was Selenium. I showcased some of the uses for the library using Python.

## About Selenium
Selenium is a testing tool used for automated web application testing [[ref]](https://www.headspin.io/blog/selenium-testing-a-complete-guide#:~:text=Selenium%20is%20a%20popular%20open,different%20browsers%20and%20operating%20systems.). It allows programmers to test the functionality of websites on various browsers (Chrome, Firefox, Microsoft Edge, etc) and operating systems. Programmers can write automated tests in multiple programming languages such as Python, Java, JavaScript, C#, and more [[ref]](https://www.browserstack.com/selenium#:~:text=Selenium%20allows%20developers%20and%20testers,%2C%20and%20C%23%2C%20among%20others.).

### How is it used?
Below is some of the more common concepts in Selenium testing:
**Locating Web Elements** [[ref]](https://selenium-python.readthedocs.io/locating-elements.html)
By using the example page source below, commons ways to find a web element will be explained:
```html
<html>
 <body>
  <form id="loginForm">
   <p class="info">Login Info</p>
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
</html>
```
- By **ID**: `loginForm = driver.find_element(By.ID, 'loginForm')` variable _loginForm_ points to the entire login form by specifying its ID
- By **NAME**: `username = driver.find_element(By.NAME, 'username')` variable _username_ points to the username input box by specifying its NAME
- By **CLASS**: `info = driver.find_element(By.CLASS_NAME, 'info')` variable _info_ points to the Login Info paragraph by specifying its CLASS
- By **XPATH**: `loginForm = driver.find_element(By.XPATH, "//form[2]")` variable _loginForm_ points to the entire login form by specifying its XPATH (`//form[2]` points to the username input box since its the second element in the **form** tag)
- By **CSS SELECTOR Part 1**: `info = driver.find_element(By.CSS_SELECTOR, 'p.info')` variable _info_ points to the Login Info paragraph by specifying its CLASS (**.** represents the ID attribute)
- By **CSS SELECTOR Part 2**: `loginForm = driver.find_element(By.CSS_SELECTOR, 'form#loginForm')` variable _loginForm_ points to the entire login form by specifying its CSS SELECTOR (**#** represents the ID attribute)

**Actions** [[ref]](https://selenium-python.readthedocs.io/navigating.html)
Most common actions:
- `element.send_keys("some text")` sends the words "some text" into the input box the varible `element` is assigned to
- `element.send_keys(Keys.RETURN)` functions as hitting the _RETURN_ button on the keyboard
- `element.clear()` clears all the text in the `elem` web element
- `driver.find_element(By.ID, "submit").click()` finds the web element with the ID _submit_ and clicks it
- `driver.get("http://www.example.com")` changes the tab to the _http://www.example.com_ website

**Waits** [[ref]](https://selenium-python.readthedocs.io/waits.html)
There are two types of waits in Selenium:
1. Explicit Waits
2. Implicit Waits

_Explicit Waits_: An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code [[ref]](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html).
Some common examples include:
- `element_to_be_clickable` Waits for the element to be visible and clickable
- `visibility_of_element_located` Waits for the element to be present on the DOM of the page and visible to the user
- `text_to_be_present_in_element` Checks if the given text is in the specified element

_Implicit Waits_: WebDriver waits a given amount of time to search for an element to appear in the DOM. If the element does not appear within the specified time, a _NoSuchElementExcepction_ will be thrown.

### Functionalities (From my Program)
- `driver = webdriver.Chrome()` Lets the program know that the testing will be happening on the Chrome web browser
- `driver.get("https://blankslate.io")` The web browser (Chrome in this case) switches to the provided link
- `textArea = driver.find_element(By.CSS_SELECTOR, "textarea.note-area")` Assigns the provided CSS selector to the variable _textArea_. You can read about how to get and specify CSS selectors [here](https://www.swtestacademy.com/css-selenium/)
- `textArea.send_keys(text)` Enters the provided text into an input element
- `textArea.clear()` Clears the content in an input element
- `button.click()` Clicks the button. `button` is a variable in this piece of code. A way to assign `button` a web element is by using a CSS selector stated in point 3.
- `driver.close()` Closes the web browser
```Python
def click_button(driver, element):
    try:
        button = WebDriverWait(driver, DEFAULT_WAIT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, element))
        )
        button.click()
    except NoSuchElementException as e:
        print("NoSuchElementException: " + e)
```
This function is called whenever a button is needed to be clicked. First, it waits until the element is clickable and then clicks it. If the element is not clickable during after the specified time (in seconds), then an _NoSuchElementException_ will be caught. I made sure to catch the exception so that the program will not crash [[ref]](https://coderslegacy.com/python/selenium-tutorial-element_to_be_clickable-function/).
```Python
def expected_title(driver, title):
    try:
        WebDriverWait(driver, DEFAULT_WAIT).until(
            EC.title_is(title)
        )
    except TimeoutException as e:
        print("TimeoutException: " + e)
```
This function is called whenever the program switches to a new window. It makes sure that the title of the window matches the given title within a given amount of seconds. The variable `title` is always given the value `driver.title` which returns the title of the current window. If the title does not match the given title, then a TimeoutException will be caught [[ref]](https://www.geeksforgeeks.org/exceptions-selenium-python/).

You can read about Selenium exception handling [here](https://www.geeksforgeeks.org/exceptions-selenium-python/).

Selenium was created in 2004 by Jason Huggins, an engineer working in ThoughtWorks. It was originally named JavaScriptTestRunner but then renamed it as it eventually became an open source tool to be usable with multiple programming langueages [[ref]](https://www.webomates.com/blog/software-testing/selenium-testing/#:~:text=Selenium%20was%20initially%20developed%20by,the%20need%20to%20curb%20monotony.).

## Personal Overview
I selected Selenium because it was my favourite aspect from my previous co-op. I had fixed automation test cases to ensure the correct web elements were being selected. Since I had a lot of fun with the project, I wanted to study the library again but use it with a different language. Previously, I used Selenium with Java, but the only difference is the syntax. Locating web elements functions in the exact same way.

Learning Selenium helped me understand Python’s syntax more. With test automation, there are many ways for something to go wrong as in an element not being found in time, so I was introduced to how exception handling worked in Python to catch the _Timeout_ and _NoSuchElement_ exceptions. Additionally, having testing websites through automation usually doesn’t involve user input. However, since I wanted to create a mini interactive game, I was able to find a way to implement user input in a simple way with a library that is strictly used for testing web features without any interaction from the user. It was satisfying to be able to mix in some of Python’s basic functions with Selenium’s functions and get the desired result.

As someone who is interested in working in the field of Quality Assurance, I had an overall great and fun time working with the library. Its documentation was very clear, and it was also extremely helpful that I could always find extra resources for any confusions I had while developing the project. However, I did struggle with finding a way to end the program as soon as the videos stopped playing as to just forcing the program to wait a certain of seconds (by using `time.sleep()`) and hope the video would have fully played out. Forcing the program to wait causes an issue because not all networks have the same speed. I noticed that the videos would play quite quickly at home, but it would take longer to load on campus. I would definitely recommend this library to anyone who is interested in learning about QA, specifically about test automation. Just learning the basics as in clicking an element gives one enough knowledge on how it functions. I will continue to use this library as I wish to soon make a website for a personal project. I will use Selenium to help test its features to ensure everything is working as it should and to also delve into its more complex concepts.

### Extra References
**Pictures**
- [Freddy](https://www.google.com/url?sa=i&url=https%3A%2F%2Ffivenightsatfreddys.fandom.com%2Fwiki%2FFreddy_Fazbear&psig=AOvVaw0stF1BEjLQEatVhRXeAZm3&ust=1697158872112000&source=images&cd=vfe&opi=89978449&ved=0CBMQjhxqFwoTCMDOt9Cn74EDFQAAAAAdAAAAABAE)
- ["Handsome" Freddy](https://www.reddit.com/r/fivenightsatfreddys/comments/zk7py0/my_name_is_freddy_fazbear_yo/)
- [Bonnie](https://www.google.com/url?sa=i&url=https%3A%2F%2Ffivenightsatfreddys.fandom.com%2Fwiki%2FBonnie&psig=AOvVaw0KGtxA-seqKumI1PW1aMKx&ust=1697158829666000&source=images&cd=vfe&ved=0CBIQjhxqFwoTCPDT77un74EDFQAAAAAdAAAAABAE)
- [Chica](https://www.google.com/url?sa=i&url=https%3A%2F%2Ffivenightsatfreddys.fandom.com%2Fwiki%2FChica&psig=AOvVaw16XDxlsmEeFBJay0y2aslF&ust=1697158845914000&source=images&cd=vfe&ved=0CBIQjhxqFwoTCICE4sOn74EDFQAAAAAdAAAAABAE)
- [Foxy](https://www.google.com/url?sa=i&url=https%3A%2F%2Ffivenightsatfreddys.fandom.com%2Fwiki%2FFoxy&psig=AOvVaw1QjuJPP1r7ZALAoB-qeWnj&ust=1697158846504000&source=images&cd=vfe&ved=0CBIQjhxqFwoTCNDPzsOn74EDFQAAAAAdAAAAABAE)