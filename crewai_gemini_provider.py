from crewai.llm import LLM
from google import genai

class GeminiLLM(LLM):
    def __init__(self, model="gemini-2.0-flash", api_key=None):
        super().__init__(model=model, provider="google", api_key=api_key)
        self.client = genai.Client(api_key=api_key)

    def _call(self, prompt, **kwargs):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text
