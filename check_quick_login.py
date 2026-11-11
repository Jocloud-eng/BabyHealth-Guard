with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function quickLoginWorker')
print(text[idx:idx+1200])

