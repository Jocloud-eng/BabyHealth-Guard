with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderPatientsTable')
print(text[idx+1400:idx+3000])

