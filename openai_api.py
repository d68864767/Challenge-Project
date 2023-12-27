```python
import openai

class OpenAI_API:
    def __init__(self, api_key):
        """
        Initialize the OpenAI API with the provided key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def set_api_key(self, api_key):
        """
        Set a new API key for OpenAI.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_api_key(self):
        """
        Get the current API key.
        """
        return self.api_key
```
