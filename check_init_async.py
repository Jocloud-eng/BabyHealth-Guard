with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('initDashboard')
while idx != -1:
    print(text[idx-30:idx+60].replace('\n', ' '))
    idx = text.find('initDashboard', idx+1)

