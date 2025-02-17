# AI Web Scrapper

A powerful web scraping tool that combines Selenium for data extraction with AI-powered content parsing using Ollama LLM.

## Features

- Web page scraping using Selenium WebDriver
- Content cleaning and preprocessing
- AI-powered content parsing with Ollama LLM
- User-friendly interface built with Streamlit
- Chunk-based processing for handling large content
- Retry mechanism for reliable scraping

## Prerequisites

- Python 3.8+
- Chrome Browser
- Ollama (for AI parsing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anshthakur0999/ai-web-scrapper.git
cd ai-web-scrapper
```

2. Create and activate a virtual environment:
```bash
python -m venv ai
ai\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Install and start Ollama:
- Download from [Ollama's website](https://ollama.ai/download)
- Start the Ollama server:
```bash
ollama serve
```

5. Pull the required language model:
```bash
ollama pull llama3.1
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Enter a website URL in the input field
3. Click "Scrape" to extract the content
4. Enter your parsing requirements in the text area
5. Click "Parse Content" to get AI-processed results

## Project Structure

```
AI-Web-Scrapper/
│
├── main.py           # Main Streamlit application
├── scrape.py        # Web scraping functionality
├── parse.py         # AI parsing implementation
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## Dependencies

- streamlit
- selenium
- beautifulsoup4
- langchain
- langchain-ollama
- httpx

## Configuration

The project uses the following key configurations:

- Chrome WebDriver for web scraping
- Ollama LLM for content parsing
- BeautifulSoup4 for HTML processing
- Streamlit for the user interface

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the awesome web framework
- Ollama for the AI language model
- Selenium for web automation capabilities
