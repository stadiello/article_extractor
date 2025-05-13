# Extractor

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/SCOR-extractor.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SCOR-extractor
    ```
3. Install dependencies using `pyproject.toml`:
    ```bash
    pip install .
    ```

## Usage

Launch the app : 
```bash
streamlit run src/extractor/main.py
```

Connect at the url and follow the instructions.

## Add or modify questions

You just have to add your new question on a new line in the questions.txt in the folder data.

## Minimal config

Modèles d'IA utilisés :
Ollama (dans bot.py) avec le modèle "deepseek-r1:8b"

Selenium pour le web scraping

Configuration minimale recommandée :

CPU :
Intel Core i5/AMD Ryzen 5 (4 cœurs minimum)
2.5 GHz ou plus

RAM :
16 GB minimum recommandé

Stockage :
SSD avec 20 GB d'espace libre (pour les modèles et dépendances)

GPU :
Non obligatoire mais recommandé
Si GPU : NVIDIA avec 4GB VRAM minimum
Sans GPU : le projet fonctionnera mais plus lentement

Note importante :
Le projet peut fonctionner sans GPU car :
Ollama peut s'exécuter sur CPU
Streamlit et Selenium ne nécessitent pas de GPU
Cependant, un GPU améliorerait significativement les performances :

OS supportés :
macOS
Linux
Windows (avec WSL recommandé)

## Contact

For questions or support, please contact the development team at `tadiello.sebastien@gmail.com`.