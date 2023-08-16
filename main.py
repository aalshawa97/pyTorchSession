#Abdullah Mutaz Alshawa
# This is a sample Python script.
import torch
from transformers import pipeline

#Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

#Analyze sentiment of a text
text = input("Could you please write some text for sentiment analysis?")
sentiment = sentiment_analyzer(text)


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_bye(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press ⌘F8 to toggle the breakpoint.
print('Welcome')
#Print sentiment and label
for result in sentiment:
    label = result['label']
    score = result['score']
    print(f"Sentiment: {label}, Score: {score:.4f}")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_bye('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
