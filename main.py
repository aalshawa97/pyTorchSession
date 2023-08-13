# This is a sample Python script.
import torch
from transformers import pipeline

#Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

#Analyze sentiment of a text
text = "I love using Hugging Face's Transformers library!"
sentiment = sentiment_analyzer(text)


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
x = torch.empty(1)
print(x)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#Print sentiment and label
for result in sentiment:
    label = result['label']
    score = result['score']
    print(f"Sentiment: {label}, Score: {score:.4f}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
