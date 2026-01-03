import xml.etree.ElementTree as ET

def extract(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    data = []
    for med in root.findall('issue'):
        data.append(med.text.strip())
    
    return sorted(set(data))

issues = extract(r"C:\Users\abhis\OneDrive\Documents\GitHub\python-automotive-batch9\Week 3\31 dec\med\medical.xml")
for issue in issues:
    print(issue)