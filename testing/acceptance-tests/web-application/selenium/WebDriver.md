# Selenium WebDriver Programming 

Everything Selenium does is send the browser commands to do something or 
send requests for information. Most of what we will do with Selenium is 
a combination of these basic commands.

## Basic Components 

* **Start the session**:

    ```Python
    driver = webdriver.Firefox()
    ```

* **Take action on browser**:

    ```Python
    driver.get("http://localhost:8080")
    ```

* **Request browser information**:

    ```Python
    title = driver.title
    ```

* **Establish Waiting Strategy**:

    Synchronizing the code with the current state of the browser is one of 
    the biggest challenges with Selenium, and doing it well is an advanced 
    topic.

    Essentially we want to make sure that the element is on the page before 
    we attempt to locate it and the element is in an interactable state 
    before we attempt to interact with it.

    An **implicit wait** is rarely the best solution, but it’s the easiest 
    to demonstrate here.

    ```Python
    driver.implicitly_wait(0.5)
    ```

* **Find an element**:

    The majority of commands in most Selenium sessions are element related, 
    and we can’t interact with one without first finding an element.

    ```Python
    driver.find_element(By.NAME, "amplitude")`
    ```

* **Take action on element**:

    There are only a handful of actions to take on an element, but we
     will use them frequently.

    ```Python
    driver.find_element(By.NAME, "waveform").click()
    ```

* **Request element information**:

    Elements store a lot of information that can be requested.

    ```Python
    driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text
    ```

* **End the session**:

    This ends the driver process, which by default closes the 
    browser as well. No more commands can be sent to this 
    driver instance. 

    ```Python
    driver.quit()
    ```


## Find Elements 

The `find_element()` method is our primary tool for interacting with a webpage. 
It acts like a digital "pointer," searching the DOM (Document Object Model) to 
locate a specific element so you can perform actions like clicking, typing, or 
reading text.

* **By.ID**: The ID is the gold standard of locators. It is designed to be 
    unique within a single HTML page, making it the fastest and most reliable 
    way to find an element.

    _Example:_ 
    ```Python
    HTML:   <input type="text" id="user_email_address" placeholder="Enter Email">
    Python: driver.find_element(By.ID, "user_email_address")
    ```

* **By.NAME**: This searches for elements based on the name attribute within 
    the HTML tag. It is common in forms and is usually more stable than an 
    auto-generated ID.

    _Example:_ 
    ```Python
    HTML:   <input name="amplitude" type="text">
    Python: driver.find_element(By.NAME, "amplitude")`
    ```

* **By.CSS_SELECTOR**: This is one of the most powerful and flexible locators. 
    It uses the same syntax that developers use to style elements. It allows 
    us to navigate complex parent-child relationships.   

    _Example:_ 
    ```Python
    HTML:   It looks for the 4th child within a list of options (likely a dropdown menu).
    Python: driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)")
    ```

* **By.LINK_TEXT**: This is specific to anchor tags `<a>`. It looks for the 
    exact visible text displayed on the screen for a hyperlink. 

    _Example:_ 
    ```Python
    HTML:   <a href="/home">back</a>
    Python: driver.find_element(By.LINK_TEXT, "back")
    ```

* **By.XPATH** (XML Path Language): Allows us to navigate through the entire HTML 
    structure of a page, moving up, down, or even searching for elements based on 
    the text they contain.



## References

* [Selenium Documentation: Write your first Selenium script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)
* [Selenium Documentation: Locator strategies](https://www.selenium.dev/documentation/webdriver/elements/locators/)


*Egon Teiniker, 2020-2026, GPL v3.0*