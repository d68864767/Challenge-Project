```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BrowserManager:
    def __init__(self):
        self.driver = webdriver.Firefox()  # Use Firefox as the browser
        self.current_tab = 0

    def open_new_tab(self, url="about:blank"):
        """
        Open a new tab in the browser.
        """
        self.driver.execute_script(f"window.open('{url}');")
        self.current_tab += 1
        self.driver.switch_to.window(self.driver.window_handles[self.current_tab])

    def close_current_tab(self):
        """
        Close the current tab in the browser.
        """
        self.driver.close()
        self.current_tab -= 1
        self.driver.switch_to.window(self.driver.window_handles[self.current_tab])

    def run_script_in_current_tab(self, script):
        """
        Run a script in the current tab of the browser.
        """
        self.driver.execute_script(script)

    def get_page_source(self):
        """
        Get the source code of the current page in the browser.
        """
        return self.driver.page_source

    def navigate_to_url(self, url):
        """
        Navigate to a specific URL in the current tab of the browser.
        """
        self.driver.get(url)
```
