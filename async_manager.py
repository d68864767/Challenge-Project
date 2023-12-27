```python
import asyncio

class AsyncManager:
    def __init__(self):
        self.tasks = []

    async def run_task(self, task):
        """
        Run a task asynchronously.
        """
        task_future = asyncio.ensure_future(task.run())
        self.tasks.append(task_future)

        # Wait for all tasks to complete
        await asyncio.gather(*self.tasks)

        # Clear the tasks list
        self.tasks.clear()

    async def run_tasks(self, tasks):
        """
        Run a list of tasks asynchronously.
        """
        for task in tasks:
            await self.run_task(task)
```
