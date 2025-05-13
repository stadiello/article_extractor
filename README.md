# article_extractor

## Installation

1. Clone the repository:
    ```bash
    https://github.com/stadiello/article_extractor
    ```
2. Navigate to the project directory:
    ```bash
    cd article_extractor
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
## AI Models Used

- **Ollama** (in `bot.py`) with the model `deepseek-r1:8b`
- **Selenium** for web scraping

## Recommended Minimal Configuration

### CPU:
- Intel Core i5/AMD Ryzen 5 (minimum 4 cores)
- 2.5 GHz or higher

### RAM:
- Minimum recommended: 16 GB

### Storage:
- SSD with at least 20 GB of free space (for models and dependencies)

### GPU:
- Not mandatory but recommended
- If using a GPU: NVIDIA with at least 4 GB VRAM
- Without a GPU: The project will work but may run slower

### Important Note:
The project can run without a GPU because:
- Ollama can execute on a CPU
- Streamlit and Selenium do not require a GPU
However, using a GPU will significantly improve performance.

### Supported Operating Systems:
- macOS
- Linux
- Windows (WSL recommended)

## Contact

For questions or support, please contact the development team at `tadiello.sebastien@gmail.com`.
