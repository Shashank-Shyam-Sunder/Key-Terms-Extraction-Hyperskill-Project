from lxml import etree
from nltk.tokenize import word_tokenize
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Uncomment these lines if you need to download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

stop_words = stopwords.words('english')
punctuations = string.punctuation

# Parse XML
file_path = "news.xml"
tree = etree.parse(file_path)
root = tree.getroot()

headlines_list = []
news_list = []

# Extract headlines and text from XML
for news in root[0]:  # <corpus> contains multiple <news> items
    head_text = ""
    body_text = ""
    for value in news:
        if value.get("name") == "head":
            head_text = value.text
        elif value.get("name") == "text":
            body_text = value.text
    headlines_list.append(head_text)
    news_list.append(body_text)

# Tokenize text
tokens_list = [word_tokenize(news.lower()) for news in news_list]

# Clean tokens: remove stopwords, punctuation, and tokens starting with apostrophes
tokens_list_clean = []
for tokens in tokens_list:
    cleaned_tokens = [t for t in tokens if t not in stop_words and t not in punctuations]
    cleaned_tokens = [t for t in cleaned_tokens if not t.startswith("'")]
    tokens_list_clean.append(cleaned_tokens)

# Lemmatize tokens and filter by length
lemmatizer = WordNetLemmatizer()
tokens_lemmas_list = []
for tokens in tokens_list_clean:
    lemmas_list = [lemmatizer.lemmatize(word) for word in tokens]
    lemmas_list = [word for word in lemmas_list if len(word) > 1]
    tokens_lemmas_list.append(lemmas_list)

# Filter for nouns only (NN tag)
tokens_list_noun = []
for tokens in tokens_lemmas_list:
    post_tags = nltk.pos_tag(tokens)
    # nouns_list = [word for word, tag in post_tags if tag.startswith('NN')]
    nouns_list = [word for word, tag in post_tags if tag == 'NN']
    tokens_list_noun.append(nouns_list)

### Step 6.1 Converting tokens_list_nouns into sentences for further processing by TfidfVectorizer from sklearn.feature_extraction.text
news_sentences = [" ".join(tokens) for tokens in tokens_list_noun]
# print(news_sentences)
### Step 6.3: Computing tf-idf scores of each word in all the documents
vectorizer = TfidfVectorizer(input='content', lowercase=True, ngram_range=(1, 1), min_df=0.1, max_df=0.6)
X = vectorizer.fit_transform(news_sentences)
features_name = vectorizer.get_feature_names_out()
# print(features_name)
X_array = X.toarray()
# print(X_array)

# creating tfidf dict for each news item
tfidf_dict_list = []
for i in range(len(X_array)):
    tfidf_dict = {}
    X_array_row = X_array[i]
    tfidf_dict = {word: float(score) for word, score in zip(features_name, X_array_row) if score > 0.0}
    # tfidf_dict = {word: float(score) for word, score in zip(features_name, X_array_row)}
    tfidf_dict_list.append(tfidf_dict)

# %%
# Step 7: Count tokens
# tokens_count_list = [Counter(sorted(tokens,reverse=True)) for tokens in tokens_list]
# tokens_count_list = [Counter(tokens) for tokens in tokens_list_noun]
# %%
# Step 7: Print headlines and top 5 tokens with tie-breaking by token name descending
for i in range(len(headlines_list)):
    headline = headlines_list[i]
    token_count = tfidf_dict_list[i]

    # Sort: first by frequency (descending), then by token (descending)
    top_5 = sorted(token_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # print(top_5)
    # top_5 = sorted(top_5, key=lambda x: (-x[1], x[0]), reverse=False)
    key_words = [key for key, _ in top_5]
    # key_words = [key for key, value in token_count.most_common(5)]

    print(f"{headline}:")
    print(" ".join(key_words))
    print()
# %%
