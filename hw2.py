paragraph = """Python is a simple programming language.
This Python course teaches basic Python concepts."""

print("Length:", len(paragraph))
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview:", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("Replace:", paragraph)

paragraph = paragraph.lower()
paragraph = paragraph.strip()

words = paragraph.split()
print("Words:", words)

if "course" in words:
    print("The word course is found.")

print("The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)))