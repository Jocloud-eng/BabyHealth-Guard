with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function initDashboard')
print(text[idx:idx+1500])

