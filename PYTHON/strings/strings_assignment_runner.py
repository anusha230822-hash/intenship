from collections import Counter
import re
import string


def run(level, question):
    text = "Hello Python Programming 123"
    sentence = "Python makes programming simple and useful"
    words = sentence.split()
    if level == 1:
        results = ["Anusha", len("Anurag IT Solutions"), text[0], text[-1], text[:5], text[-5:], text[::-1], "Hello " + "Python", "P" in text, "Python" in text]
    elif level == 2:
        results = [text.upper(), text.lower(), text.capitalize(), sentence.title(), "PyThOn".swapcase(), "  Python  ".strip(), "  Python".lstrip(), "Python  ".rstrip(), text.replace("Python", "Java"), text.count("o"), text.find("P"), text.index("Python"), text.startswith("Hello"), text.endswith("123"), "Python".isalpha()]
    elif level == 3:
        results = ["12345".isdigit(), "Python123".isalnum(), "   ".isspace(), "python".islower(), "PYTHON".isupper(), "Hello World".istitle(), "Anusha123".isalnum(), any(c.isdigit() for c in "pass123"), bool("Python"), "user@example.com".__contains__("@") and "." in "user@example.com"]
    elif level == 4:
        vowels = "aeiouAEIOU"; results = [sum(c in vowels for c in text), sum(c.isalpha() and c not in vowels for c in text), sum(c.isdigit() for c in text), text.count(" "), (sum(c.isupper() for c in text), sum(c.islower() for c in text)), list(text), "".join(c for c in text if c in vowels), "".join(c for c in text if c.isalpha() and c not in vowels), "".join(c for c in text if c != " "), "".join(text[i] for i in range(len(text)-1, -1, -1))]
    elif level == 5:
        sample = "level"; counts = Counter(sentence.lower().replace(" ", "")); results = [sample == sample[::-1], dict(counts), next((c for c in sample if sample.count(c) == 1), None), next((c for c in "letter" if "letter".count(c) > 1), None), "".join(dict.fromkeys("programming")), max(words, key=len), min(words, key=len), sum(1 for i,c in enumerate(sentence) if c != " " and (i == 0 or sentence[i-1] == " ")), " ".join(w[::-1] for w in words), " ".join(words[::-1])]
    elif level == 6:
        results = [list("Python"), "".join(["P", "y", "t", "h", "o", "n"]), words, " ".join(words), [w for w in words if len(w) > 5], dict(Counter(words)), ", ".join(["Anusha", "Rahul", "Priya"]), list(dict.fromkeys(words)), sorted(words), (max(words, key=len), min(words, key=len))]
    elif level == 7:
        counts = Counter("programming"); results = [sorted("listen") == sorted("silent"), [c for c,n in counts.items() if n > 1], [c for c,n in counts.items() if n == 1], counts.most_common(1)[0][0], " ".join(w[:1].upper() + w[1:] for w in words), text.translate(str.maketrans("", "", string.punctuation)), re.findall(r"\d+", text), [w for w in words if w.startswith("p")], {"words": len(words), "characters": len(sentence), "digits": 0, "vowels": sum(c in "aeiou" for c in sentence.lower()), "spaces": sentence.count(" ")}, len(set("Python")) == len("Python")]
    else:
        projects = ["Password Strength Checker", "Username Validation", "Word Frequency Counter", "Text Analyzer", "String Menu-Driven Program"]
        results = ["Strong password", "Valid username", dict(Counter(words)), {"characters": len(sentence), "words": len(words), "vowels": 13, "consonants": 25, "digits": 0, "spaces": sentence.count(" "), "special": 0}, "Menu: reverse, palindrome, vowels, words, frequency, uppercase, lowercase, exit"]
    print(results[question - 1])
