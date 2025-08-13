# Key Terms Extraction Project

A sophisticated Natural Language Processing (NLP) application that extracts key terms from news articles using advanced text processing techniques and TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.

## 🎯 Overview

This project analyzes news articles stored in XML format and extracts the most relevant key terms from each article. It employs a comprehensive text processing pipeline that includes tokenization, stopword removal, lemmatization, part-of-speech tagging, and TF-IDF scoring to identify and rank the most significant terms in news content.

## 🚀 Features

- **XML News Processing**: Parses structured XML files containing news articles with headlines and body text
- **Advanced Text Preprocessing**: 
  - Tokenization using NLTK's word tokenizer
  - Stopword removal (English language)
  - Punctuation filtering
  - Lemmatization for word normalization
- **Part-of-Speech Filtering**: Extracts only nouns (NN tag) as potential key terms
- **TF-IDF Vectorization**: Uses scikit-learn's TfidfVectorizer to score term importance
- **Intelligent Ranking**: Ranks terms by TF-IDF scores with tie-breaking by alphabetical order
- **Multiple Dataset Support**: Processes multiple XML news files (news.xml, news2.xml, news3.xml)

## 📁 Project Structure

```
Key_Terms_Extraction/
├── Key Terms Extraction/
│   ├── task/
│   │   ├── key_terms.py          # Main extraction script
│   │   ├── news.xml              # Primary news dataset (11 articles)
│   │   ├── news2.xml             # Secondary news dataset (2 articles)
│   │   ├── news3.xml             # Tertiary news dataset (11 articles)
│   │   └── Support_files/        # Additional support and reference files
│   └── [Additional task stages]  # Multi-stage learning modules
└── requirements.txt              # Project dependencies
```

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **lxml**: XML parsing and processing
- **NLTK**: Natural Language Toolkit for text processing
- **scikit-learn**: Machine learning library for TF-IDF vectorization
- **pandas**: Data manipulation and analysis
- **pytest**: Testing framework

## 📋 Prerequisites

- Python 3.6 or higher
- pip package manager

## ⚙️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Key_Terms_Extraction
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (run once)
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('wordnet')
   ```

## 🎯 Usage

### Basic Usage

Navigate to the task directory and run the main script:

```bash
cd "Key Terms Extraction/task"
python key_terms.py
```

### Expected Output

The script processes news articles and outputs headlines followed by their top key terms:

```
Brain Disconnects During Sleep:
sleep consciousness activity brain research

New Portuguese skull may be an early relative of Neandertals:
skull neandertals fossil europe study

Living by the coast could improve mental health:
health mental coast study research
...
```

### XML Data Format

The news XML files follow this structure:

```xml
<?xml version='1.0' encoding='UTF8'?>
<data>
  <corpus>
    <news>
      <value name="head">Article Headline</value>
      <value name="text">Article content text...</value>
    </news>
    <!-- Additional news articles -->
  </corpus>
</data>
```

## 🔧 Technical Details

### Text Processing Pipeline

1. **XML Parsing**: Extracts headlines and article text using lxml
2. **Tokenization**: Splits text into individual words using NLTK
3. **Cleaning**: Removes stopwords, punctuation, and apostrophe-prefixed tokens
4. **Lemmatization**: Reduces words to their base forms
5. **POS Tagging**: Filters for nouns only (NN tag)
6. **TF-IDF Scoring**: Calculates term importance across the corpus
7. **Ranking**: Sorts terms by TF-IDF score (descending) then alphabetically (descending)

### Key Parameters

- **TF-IDF Configuration**:
  - `min_df=0.1`: Terms must appear in at least 10% of documents
  - `max_df=0.6`: Terms appearing in more than 60% of documents are filtered out
  - `ngram_range=(1,1)`: Only single words (unigrams) are considered

## 📊 Dataset Information

### News Articles Coverage
- **news.xml**: 11 diverse news articles covering science, technology, health, and economics
- **news2.xml**: 2 focused articles on archaeology and health research  
- **news3.xml**: 11 articles (duplicate of news.xml content)

### Article Topics
- Neuroscience and sleep research
- Archaeological discoveries
- Health and medical studies
- Technology and AI developments
- Economic analysis
- Entertainment and digital media

## 🧪 Testing

The project includes comprehensive testing infrastructure:

```bash
# Run tests
pytest Key\ Terms\ Extraction/task/tests.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔍 Example Analysis

### Sample Input Article
```
Headline: "Brain Disconnects During Sleep"
Text: "Scientists may have gained an important insight into the age-old mystery of why consciousness fades as we nod off to sleep..."
```

### Processing Steps
1. Tokenization: ["scientists", "may", "have", "gained", ...]
2. Stopword removal: ["scientists", "gained", "important", "insight", ...]  
3. POS filtering: ["scientists", "insight", "mystery", "consciousness", ...]
4. TF-IDF scoring and ranking

### Output
```
Brain Disconnects During Sleep:
sleep consciousness activity brain research
```

## 🚀 Future Enhancements

- Support for additional languages
- Named Entity Recognition (NER) integration
- Sentiment analysis capabilities
- Interactive web interface
- Real-time news feed processing
- Export functionality (JSON, CSV, etc.)

## 📞 Support

For questions, issues, or contributions, please contact the project maintainer or open an issue in the repository.

---

*Built with ❤️ using Python and advanced NLP techniques*