AG News Text Classification with DistilBERT
📌 Overview
A complete text classification pipeline that classifies news articles into 4 categories using DistilBERT. Achieves 93.89% accuracy on the AG News dataset.

🚀 Quick Start
Run the entire code in ONE Google Colab cell (enable GPU):

python
# Copy the complete pipeline code into Colab
# Runtime → Change runtime type → GPU
# Execute the cell
📊 Results
Accuracy: 93.89%

Loss: 0.2018

Model: DistilBERT-base-uncased

Dataset: AG News (127,600 articles)

Categories: World, Sports, Business, Sci/Tech

🎯 Sample Predictions
text
📝 Sample 1: "The government passed a new law..." → World (80.61%)
📝 Sample 2: "The basketball team won..." → Sports (98.60%)
📝 Sample 3: "New AI technology breakthrough..." → Sci/Tech (96.52%)
📝 Sample 4: "Federal Reserve raises interest rates..." → Business (97.94%)
📈 Training Performance
Epoch	Train Loss	Val Accuracy
1	0.2369	93.89%
2	0.2605	94.67%
3	0.0891	94.79%
4	0.1453	94.74%
🔧 Features
✅ Automatic Dataset Download - AG News from GitHub
✅ Complete Pipeline - Data to predictions in one cell
✅ High Accuracy - 93.89% on test set
✅ Confidence Scores - Top-3 predictions with percentages
✅ Easy Customization - Modify for your own dataset

📁 Dataset
Source: AG News public dataset

Size: 127,600 samples

Split: 80% train (102,080), 20% test (25,520)

Classes: Balanced - 31,900 samples each category

🛠️ Technical Details
python
# Key Parameters
model_name = "distilbert-base-uncased"
learning_rate = 2e-5
batch_size = 8
epochs = 4
max_length = 128
📦 Output Files
text
results/     # Model checkpoints
logs/        # Training logs
Console output with all metrics
💡 How to Use Your Own Data
Modify label_names with your categories

Replace dataset loading with your texts/labels

Adjust num_labels in model initialization

Run the pipeline

⚠️ Requirements
bash
pip install torch transformers datasets scikit-learn pandas numpy
