from tkinter import *
from textblob import TextBlob

def analyze_review():
    review = review_entry.get("1.0", END).strip()

    if not review:
        emoji_label.config(text="⚠️")
        result_label.config(text="Please enter a review!", fg="black")
        return

    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    result = f"📊 Polarity: {polarity:.2f}\n"
    result += f"🧠 Subjectivity: {subjectivity:.2f}\n"

    if polarity > 0:
        mood = "🟢 Positive Review 😊"
        color = "green"
        emoji = "👍"
    elif polarity < 0:
        mood = "🔴 Negative Review 😠"
        color = "red"
        emoji = "👎"
    else:
        mood = "🟡 Neutral Review 😐"
        color = "orange"
        emoji = "🤔"

    result += "\n" + mood
    emoji_label.config(text=emoji, font=("Arial", 40))
    result_label.config(text=result, fg=color)

# GUI setup
root = Tk()
root.title("🛒 Amazon Review Sentiment Analyzer")
root.geometry("500x450")
root.configure(bg="#fefefe")

title = Label(root, text="Amazon Review Sentiment Analyzer", font=("Helvetica", 16, "bold"), bg="#fefefe")
title.pack(pady=10)

instr = Label(root, text="Paste or write your review below:", font=("Arial", 12), bg="#fefefe")
instr.pack(pady=5)

frame = Frame(root, bg="#333", bd=2)
frame.pack(pady=5)

review_entry = Text(frame, height=6, width=50, font=("Arial", 11), bd=0, wrap=WORD)
review_entry.pack()

analyze_button = Button(root, text="🔍 Analyze Review", command=analyze_review,
                        bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
analyze_button.pack(pady=15)

emoji_label = Label(root, text="", bg="#fefefe")
emoji_label.pack()

result_label = Label(root, text="", font=("Arial", 12), bg="#fefefe", justify=LEFT)
result_label.pack(pady=10)

root.mainloop()

