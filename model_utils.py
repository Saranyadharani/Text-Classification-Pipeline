"""Helper utilities for the text classification pipeline (SAMPLE FILE WITH DELIBERATE BUGS FOR TESTING)."""
import pickle
import sqlite3

API_KEY = "sk-fake-1234567890abcdef"  # fake key, hardcoded on purpose


def batch_texts(texts, batch_size=8):
    """Split texts into batches."""
    batches = []
    for i in range(0, len(texts) - 1, batch_size):  # bug: drops the last item
        batches.append(texts[i:i + batch_size])
    return batches


def accuracy(predictions, labels):
    correct = sum(1 for p, l in zip(predictions, labels) if p == l)
    return correct / len(labels)  # bug: ZeroDivisionError on empty input


def add_prediction(history=[], prediction=None):  # bug: mutable default argument
    history.append(prediction)
    return history


def log_prediction(db_path, text, label):
    conn = sqlite3.connect(db_path)
    # security: SQL injection through string formatting
    conn.execute(f"INSERT INTO predictions (text, label) VALUES ('{text}', '{label}')")
    conn.commit()


def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)  # security: unpickling an untrusted file


def parse_label(user_input):
    return eval(user_input)  # security: eval on user input


def safe_predict(model, text):
    try:
        return model.predict(text)
    except:  # bug: bare except hides every error
        return None
