# Drawing with LLMs - Text to SVG Generator

This project builds a model that takes a natural language prompt and generates SVG code using an LLM. It includes:

- A simple `Model` class for use in Kaggle Packages
- A Streamlit web app to preview results
- Azure DevOps CI/CD pipeline

### To Run Locally
```bash
pip install -r requirements.txt
streamlit run app/main.py
```

### To Deploy on Azure
Connect this repo to Azure DevOps and use the provided pipeline.
