import ollama
import re
from typing import Dict, Optional, List

class OllamaClient:
    def __init__(self, temp=None):
        self.model_name = "deepseek-r1:8b"
        self._ollama_options = temp or {'temperature': 1}
        self.questions = self._load_questions()
    
    def _load_questions(self) -> List[str]:
        questions = []
        with open('data/questions.txt', 'r') as file:
            for line in file:
                questions.append(line.strip())
        return questions

    def summary(self, input_text: str) -> str:
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

    def generation(self, input_text: str) -> Dict[str, str]:
        formatted_questions = "\n".join(f"- {q}" for q in self.questions)
        
        prompt = (
            "You are a bot specialized in legal data extraction.\n\n"
            "If the following text is about lawsuit, process following instruction, otherwise answer 'No Lawsuit'\n"
            "From the following text, extract answers to these questions:\n"
            f"{formatted_questions}\n\n"
            "Format your response exactly like this:\n"
            "When was the claim brought: answer\n"
            "What are the claims: answer\n"
            "Who is the Defendant: answer\n"
            "Who is bringing the proceeding: answer\n"
            "What are the claimed damages: answer\n\n"
            "Be concise and only provide the answers.\n"
            "If the text is not about lawsuit, just answer 'No Lawsuit'.\n"
            "If a question cannot be answered from the text, answer 'No Answer'.\n\n"
            
            f"Text:\n{input_text}\n"
        )

        result = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            stream=False,
            options=self._ollama_options
        )

        return re.sub(r"<think>.*?</think>", "", result['response'], flags=re.DOTALL)

        # response = re.sub(r"<think>.*?</think>", "", result['response'], flags=re.DOTALL)
        
        # if response.strip() == "No Lawsuit":
        #     return {"status": "No Lawsuit"}
            
        # # Convertir la réponse en dictionnaire
        # answers = {}
        # for question in self.questions:
        #     pattern = f"{question}: (.+?)(?=\n|$)"
        #     match = re.search(pattern, response)
        #     answers[question] = match.group(1).strip() if match else "No Answer"
            
        # return answers