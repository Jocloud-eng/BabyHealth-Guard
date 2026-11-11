with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect babyData rendering
idx = text.find('function selectBaby')
if idx != -1:
    print("selectBaby function:")
    print(text[idx:idx+1200])

idx2 = text.find('function renderBaby')
if idx2 != -1:
    print("\nrenderBaby function:")
    print(text[idx2:idx2+800])

