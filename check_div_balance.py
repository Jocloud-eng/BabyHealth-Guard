with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check view-maternal-care
m_start = text.find('id="view-maternal-care"')
n_start = text.find('id="view-newborn-care"')
a_start = text.find('id="view-appointments"')

m_chunk = text[m_start:n_start]
print(f"view-maternal-care chunk length: {len(m_chunk)}")
print("div count open in maternal:", m_chunk.count('<div'))
print("div count close in maternal:", m_chunk.count('</div'))

n_chunk = text[n_start:a_start]
print(f"\nview-newborn-care chunk length: {len(n_chunk)}")
print("div count open in newborn:", n_chunk.count('<div'))
print("div count close in newborn:", n_chunk.count('</div'))

