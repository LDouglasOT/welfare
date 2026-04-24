
import os
import re

# Files to process
html_files = [
    'index.html', 'about.html', 'causes.html', 'contact.html',
    'donate.html', 'event.html', 'gallery.html', 'blog.html', 'blog-single.html'
]

# Images that exist in both images/ and newimages/
# These should use newimages/ instead
overlapping = {
    'bg_2.jpg', 'bg_3.jpg',
    'cause-1.jpg', 'cause-2.jpg', 'cause-5.jpg',
    'event-1.jpg', 'event-2.jpg', 'event-3.jpeg', 'event-4.jpg', 'event-5.jpg'
}

for fname in html_files:
    if not os.path.exists(fname):
        print(f"Skipping {fname} - not found")
        continue
    
    with open(fname, 'r') as f:
        content = f.read()
    
    original = content
    
    for img in overlapping:
        # Replace url('images/xxx') with url('newimages/xxx')
        pattern1 = r"url\(\s*'images/" + re.escape(img) + r"'\s*\)"
        replacement1 = "url('newimages/" + img + "')"
        content = re.sub(pattern1, replacement1, content)
        
        # Replace url("images/xxx") with url("newimages/xxx")
        pattern2 = r'url\(\s*"images/' + re.escape(img) + r'"\s*\)'
        replacement2 = 'url("newimages/' + img + '")'
        content = re.sub(pattern2, replacement2, content)
        
        # Replace url(images/xxx) with url(newimages/xxx) - no quotes
        pattern3 = r'url\(\s*images/' + re.escape(img) + r'\s*\)'
        replacement3 = 'url(newimages/' + img + ')'
        content = re.sub(pattern3, replacement3, content)
    
    if content != original:
        with open(fname, 'w') as f:
            f.write(content)
        print(f"Updated {fname}")
    else:
        print(f"No changes for {fname}")

print("Done!")
