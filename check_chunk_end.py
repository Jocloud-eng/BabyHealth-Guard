with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m_start = text.find('id="view-maternal-care"')
n_start = text.find('id="view-newborn-care"')

print("=== END OF MATERNAL CHUNK (last 600 chars) ===")
print(text[n_start-600:n_start+200])

