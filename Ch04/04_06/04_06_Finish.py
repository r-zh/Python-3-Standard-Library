# Text Wrap Module
import textwrap

websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")
print(textwrap.fill(websiteText))

print("Dedent") # change the line
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print("Fill")
print()
print(textwrap.fill(dedent_text, width=50)) # each line is 50 characters
print(textwrap.fill(dedent_text, width=100))

print("Controlling Indent") # first line space before text, rest line space before text
print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="          "))

print("Shortening Text") # only first 15th char, rest is ...
short = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...")
print(short)