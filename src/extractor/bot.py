import ollama
import re

questions = []
with open('data/questions.txt', 'r') as file:
    for line in file:
        questions.append("- " + line.strip() + "\n")

class OllamaClient:
    def __init__(self, temp=None):
        self.model_name = "deepseek-r1:8b"
        self._ollama_options = temp or {'temperature': 1}
    
    def summary(self, input_text):
        prompt = (
            "you are a bot specialized in legal texts.\n\n"
            "Summarize the following text in a few lines, and give a list of keywords.\n"
            "For exemple : 'Keywords: word1, word2, word3'\n"
            "Text:\n"
            f"{input_text}\n"
        )
        result = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            stream=False,
            options=self._ollama_options
        )
        return re.sub(r"<think>.*?</think>", "",  result['response'], flags=re.DOTALL)

    def generation(self, input_text):
        
        prompt = (
            "You are a bot specialized in legal data extraction.\n\n"
            "If the following text is about lawsuit, process following instruction, otherwise anwser 'No Lawsuit'\n"
            "From the following text, extract answers to these questions:\n"
            f"{' '.join(questions)}\n"
            "Date,Claims,Defendant,Plaintiff,Damages\n"
            "Be concise and do not add any other information.\n"
            "Just question and answer, no explanation.\n"
            "If the text is not about lawsuit, just answer 'No Lawsuit'.\n\n"
            "If the question is not in the text, just answer 'No Answer'.\n"
            "If the answer is not in the text, just answer 'No Answer'.\n"
            "Text:\n"

            f"Text:\n{input_text}\n"
        )

        result = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            stream=False,
            options=self._ollama_options
        )

        return re.sub(r"<think>.*?</think>", "",  result['response'], flags=re.DOTALL)