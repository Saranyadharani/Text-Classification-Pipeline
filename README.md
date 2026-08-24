# Text Classification Pipeline with DistilBERT

## Overview
A complete text classification system that uses **DistilBERT** to classify news articles into **4 categories** with **93.89% accuracy**.

##  Features
- End-to-end pipeline (data → model → predictions)
- AG News dataset: 127,600 labeled articles
- High accuracy: 93.89% on test set
- Fast predictions with confidence scores
- Clean, modular code ready for Colab

##  Dataset
**AG News Categories:**
- World
- Sports
- Business
- Sci/Tech

**Statistics:**
- Total samples: 127,600
- Train: 102,080 (80%)
- Test: 25,520 (20%)
- Balanced classes: 31,900 per category

##  Model Architecture
- **Base Model**: `distilbert-base-uncased`
- **Classifier**: Custom head for 4 classes
- **Tokenizer**: BERT tokenizer (128 max length)
- **Training**: 4 epochs, batch size 8, learning rate 2e-5

## 📈 Results
| Epoch | Train Loss | Val Loss | Accuracy |
|-------|------------|----------|----------|
| 1     | 0.2369     | 0.2018   | 93.89%   |
| 2     | 0.2605     | 0.2222   | 94.67%   |
| 3     | 0.0891     | 0.2434   | 94.79%   |
| 4     | 0.1453     | 0.3016   | 94.74%   |

**Final Test Accuracy: 93.89%**

<img width="1167" height="401" alt="image" src="https://github.com/user-attachments/assets/5a8693e5-bcf1-4752-a170-0992591541be" />
<img width="1232" height="449" alt="image" src="https://github.com/user-attachments/assets/bb388a13-67c4-4b80-aff9-9e72696d319b" />
