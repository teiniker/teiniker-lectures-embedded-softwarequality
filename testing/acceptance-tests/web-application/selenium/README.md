# Selenium

Selenium is a project for a range of tools and libraries that enable and support the automation of web browsers.

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

* **WebDriver**\
  WebDriver uses **browser automation APIs** provided by browser vendors to **control browser** and run tests.
  This is as if a real user is operating the browser.

* **IDE**\
  IDE (Integrated Development Environment) is the tool you use to develop your Selenium test cases.
  It’s an easy-to-use **Chrome and Firefox extension** and is generally the most efficient way to develop test cases.
  It **records the users’ actions** in the browser for you, using existing Selenium commands, with parameters defined
  by the context of that element.
  This is not only a time-saver but also an **excellent way of learning Selenium** script syntax.

* **Grid**\
  Selenium Grid allows you to **run test cases in different machines** across different platforms.
  The control of triggering the test cases is on the local end, and when the test cases are triggered,
  they are automatically executed by the remote end.
  After the development of the WebDriver tests, you may face the need of running your tests on multiple
  browser and operating system combinations. This is where Grid comes into the picture.


## Selenium IDE
Selenium IDE is an integrated development environment for Selenium tests.
It is implemented as a Firefox extension, and allows you to record, edit, and debug tests.

**Install Selenium IDE addon for Firefox**:
* Using Firefox, vistit the page: https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
* Click the button **[Add to Firefox]**


## Web Driver
WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server,
marks a leap forward in terms of browser automation.

Selenium WebDriver refers to both the language bindings and the implementations of the individual browser
controlling code. This is commonly referred to as just WebDriver.

**Install Web Driver**:
* Download the binary package [geckodriver-v0.36.0-linux64.tar.gz](https://github.com/mozilla/geckodriver/releases)
* Unzip the tar file and store the binary in a local directory:
    ```
    $ cd Downloads
    $ tar xvzf geckodriver-v0.36.0-linux64.tar.gz
    $ mkdir ~/local/webdriver
    $ mv geckodriver ~/local/webdriver/
    ```
* Add the webdriver directory to the PATH environment variable:
    ```
    $ code ~/.bashrc
    [i]
    export WEBDRIVER=/home/student/local/webdriver/
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$COVERAGE/bin:/opt/bin:$WEBDRIVER/:$PATH
    ```

**Install the selenium module for Python**
    ```
    $ pip3 install selenium
    ```

## References
* [https://www.python.org/](https://www.python.org/)

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

* [Selenium Browser Automation Project](https://www.selenium.dev/documentation/en/)

* [Selenium IDE - Getting Started](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started)

* [Selenium with Python](https://selenium-python.readthedocs.io/)

* [YouTube: Python Selenium Tutorial #1 - Web Scraping, Bots & Testing](https://youtu.be/Xjv1sY630Uc)
* [YouTube: Python Selenium Tutorial #2 - Locating Elements From HTML](https://youtu.be/b5jt2bhSeXs)
* [YouTube: Python Selenium Tutorial #3 - Page Navigating and Clicking Elements](https://youtu.be/U6gbGk5WPws)


*Egon Teiniker, 2020-2022, GPL v3.0*
