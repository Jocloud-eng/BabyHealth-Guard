with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(
    r'src="https://images\.unsplash\.com/photo-1544717305[^"]*"',
    'src="/assets/images/african_lactating_mother.jpg"',
    text
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated lactating mother photo in index.html to /assets/images/african_lactating_mother.jpg!")

