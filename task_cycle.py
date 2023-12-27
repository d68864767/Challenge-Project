```python
from autogpt import AutoGPT
from desktop_agent import DesktopAgent
from browser_manager import BrowserManager
from python_script_experiment import PythonScriptExperiment

class TaskCycle:
    def __init__(self, autogpt: AutoGPT, desktop_agent: DesktopAgent, browser_manager: BrowserManager):
        self.autogpt = autogpt
        self.desktop_agent = desktop_agent
        self.browser_manager = browser_manager
        self.tasks = [PythonScriptExperiment()]
        self.current_task_index = 0

    def get_next_task(self):
        """
        Get the next task in the cycle.
        """
        task = self.tasks[self.current_task_index]
        self.current_task_index = (self.current_task_index + 1) % len(self.tasks)
        return task

    def run_task_in_browser(self, task):
        """
        Run a task in the browser.
        """
        # Generate the task prompt
        prompt = task.get_prompt()

        # Generate the task script using AutoGPT
        script = self.autogpt.generate_text(prompt)

        # Run the script in the browser
        self.browser_manager.run_script_in_current_tab(script)

    def run_next_task(self):
        """
        Run the next task in the cycle.
        """
        task = self.get_next_task()
        self.run_task_in_browser(task)
```
