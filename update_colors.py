import os

css_path = r"c:\projet antigravity\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace variables from Option 3 to Kerox Official Colors
css = css.replace("--clr-navy: #2D3748;", "--clr-navy: #233C67;")
css = css.replace("--clr-navy-light: var(--clr-navy);", "--clr-navy-light: var(--clr-navy);") # untouched
css = css.replace("--clr-gray-light: #EDF2F7;", "--clr-gray-light: #F8F9FA;")
css = css.replace("--clr-copper: #2B6CB0;", "--clr-copper: #CD9A50;")
css = css.replace("--clr-copper-hover: #2C5282;", "--clr-copper-hover: #B58444;")

# Replace exact RGB values for rgba substitutions if any
css = css.replace("45, 55, 72", "35, 60, 103") # Slate -> Kerox Blue
css = css.replace("43, 108, 176", "205, 154, 80") # Electric Blue -> Kerox Gold

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Colors updated to Kerox Official successfully.")
