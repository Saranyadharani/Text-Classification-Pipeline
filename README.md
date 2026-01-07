Text Classification Pipeline (DistilBERT + AG News)

A complete, end-to-end text classification pipeline built with Hugging Face Transformers, PyTorch, and scikit-learn, designed to run in one Google Colab cell.

🚀 Features

Uses AG News dataset (World, Sports, Business, Sci/Tech)

Fine-tunes DistilBERT

Automatic train/test split

Training, evaluation, and prediction included

Fallback to synthetic data if download fails

Achieves ~94% accuracy

📊 Dataset

AG News (127,600 samples)

4 balanced classes:

World

Sports

Business

Sci/Tech

🧠 Model

distilbert-base-uncased

Hugging Face Trainer API

Cross-entropy loss with accuracy metric

▶️ How to Run

Open Google Colab

Paste the full script into one cell

Run the cell — everything is handled automatically

🧪 Output

Training & validation metrics per epoch

Final test accuracy and loss

Predictions with confidence scores

Top-k class probabilities for sample inputs

📦 Requirements

Python 3.8+

transformers

datasets

torch

scikit-learn

pandas

numpy

(Automatically available in Google Colab)

✅ Example Results

Test Accuracy: ~93–95%

Fast training with GPU support

📌 Use Cases

News classification

NLP fine-tuning demos

Text classification projects

Learning Hugging Face Trainer workflow
