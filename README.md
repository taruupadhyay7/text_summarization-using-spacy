# 📝 Text Summarizer App

A powerful AI-powered text summarization application built with Streamlit that supports both extractive and abstractive summarization methods. Quickly summarize articles, emails, or PDF documents instantly.

## ✨ Features

- **Dual Summarization Methods**
  - **Extractive**: Extracts key sentences from the original text using spaCy NLP
  - **Abstractive**: Generates new, concise summaries using Facebook's BART AI model

- **Multiple Input Options**
  - Paste text directly into the application
  - Upload and process PDF files

- **Intelligent Analysis**
  - Automatic keyword extraction from documents
  - Word frequency analysis
  - Reduction statistics (original vs. summary word count)

- **User-Friendly Interface**
  - Clean, step-by-step interface
  - Customizable summary length for extractive method
  - Real-time processing with status indicators
  - Detailed statistics display

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or download this repository:
```bash
cd text_summarization
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download spaCy language model (required for extractive summarization):
```bash
python -m spacy download en_core_web_sm
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📦 Project Structure

```
text_summarization/
├── app.py              # Main Streamlit application
├── abstractive.py      # Abstractive summarization using BART model
├── extractive.py       # Extractive summarization using spaCy
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## 📚 How It Works

### Extractive Summarization
- Analyzes word frequencies and removes stopwords
- Scores sentences based on word frequency
- Selects the top N sentences in their original order
- Fast and interpretable (uses actual text from source)

### Abstractive Summarization
- Uses Facebook's BART (Bidirectional and Auto-Regressive Transformers) model
- Generates completely new sentences that capture the meaning
- More concise but requires more computational power
- First run may take 1-2 minutes to load the AI model

## 🔧 Configuration

### Extractive Method
- Adjust the number of sentences in the summary using the slider (1-10 sentences)

### Abstractive Method
- Maximum input: 900 words (automatically truncated if longer)
- Summary length: 40-150 tokens (automatically optimized)

## 📋 Requirements

Key dependencies:
- **streamlit**: Web application framework
- **pdfplumber**: PDF text extraction
- **transformers**: BART model for abstractive summarization
- **spacy**: NLP library for extractive summarization
- **accelerate**: Performance optimization for transformers

See `requirements.txt` for the complete list.

## 💡 Usage Tips

1. **For Quick Summaries**: Use Extractive method - it's faster and works great for most documents
2. **For Refined Summaries**: Use Abstractive method - generates more polished, AI-generated summaries
3. **For PDFs**: The app automatically extracts text from all pages
4. **Text Length**: Works best with texts longer than 30 words
5. **Keywords**: Top 5 keywords are automatically extracted for all summaries

## ⚙️ Technical Details

- **spaCy Model**: `en_core_web_sm` for English NLP processing
- **BART Model**: `facebook/bart-large-cnn` fine-tuned on CNN news articles
- **Framework**: Streamlit for rapid web development
- **Processing**: Cached model loading for optimal performance

## 📝 Example Use Cases

- Summarize long articles for quick reading
- Generate executive summaries from emails
- Extract key points from research papers
- Condense meeting notes
- Summarize news articles

## 🐛 Troubleshooting

**Issue**: Model takes a long time to load on first run
- **Solution**: This is normal - the BART model (~1.5GB) is downloaded on first use. Subsequent runs will be faster due to caching.

**Issue**: "Could not extract text from this PDF"
- **Solution**: Ensure the PDF contains extractable text (not scanned images). Try a different PDF file.

**Issue**: Text too short error
- **Solution**: Provide at least 30 words for reliable summarization.

## 📄 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Support

For issues or questions, please check the troubleshooting section or create an issue in the project repository.

---

**Enjoy faster reading with AI-powered text summarization! 🚀**
