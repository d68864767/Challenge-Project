```python
class DesktopAgent:
    def __init__(self):
        self.status = "stopped"

    def start(self):
        """
        Start the Desktop Agent.
        """
        self.status = "running"
        print("Desktop Agent started.")

    def stop(self):
        """
        Stop the Desktop Agent.
        """
        self.status = "stopped"
        print("Desktop Agent stopped.")

    def check_status(self):
        """
        Check the status of the Desktop Agent.
        """
        return self.status

    def handle_task(self, task):
        """
        Handle a task in the Desktop Agent.
        """
        print(f"Handling task: {task}")
        # Add code here to handle the task

    def handle_error(self, error):
        """
        Handle an error in the Desktop Agent.
        """
        print(f"Error: {error}")
        # Add code here to handle the error
```

