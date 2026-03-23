import re
import codecs

css_path = r"c:\projet antigravity\styles.css"
with codecs.open(css_path, "r", "utf-8") as f:
    css = f.read()

# Make body white
css = re.sub(r'body\s*{[^}]+background-color:\s*var\(--clr-gray-light\);', lambda m: m.group(0).replace('var(--clr-gray-light)', 'var(--clr-white)'), css)

# Make nav white glass
css = css.replace('background: rgba(45, 55, 72, 0.85); /* Navy transparent */', 'background: rgba(255, 255, 255, 0.95); /* White transparent */')
css = css.replace('background: rgba(45, 55, 72, 0.95);', 'background: rgba(255, 255, 255, 0.98);')
css = css.replace('.logo {\n    font-family: var(--font-heading);\n    font-size: 1.8rem;\n    font-weight: 700;\n    color: var(--clr-white);\n}', 
                  '.logo {\n    font-family: var(--font-heading);\n    font-size: 1.8rem;\n    font-weight: 700;\n    color: var(--clr-navy);\n}')
css = css.replace('.nav-links a:hover, .nav-links a.active {\n    color: var(--clr-white);\n}', 
                  '.nav-links a:hover, .nav-links a.active {\n    color: var(--clr-copper);\n}')

# Make Hero White
css = css.replace('.hero-section {\n    position: relative;\n    min-height: 100vh;\n    background-color: var(--clr-navy);\n',
                  '.hero-section {\n    position: relative;\n    min-height: 100vh;\n    background-color: var(--clr-white);\n')
css = css.replace('.hero-content h1 {\n    font-size: clamp(3rem, 5vw, 4.5rem);\n    color: var(--clr-white);\n',
                  '.hero-content h1 {\n    font-size: clamp(3rem, 5vw, 4.5rem);\n    color: var(--clr-navy);\n')

# Replace subtitle with slogan box
old_sub = """.subtitle {
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--clr-copper);
    display: block;
    margin-bottom: 1rem;
}"""
new_slogan = """.subtitle-slogan {
    display: inline-block;
    background-color: var(--clr-navy);
    color: var(--clr-white);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 10px rgba(35, 60, 103, 0.2);
}"""
css = css.replace(old_sub, new_slogan)

# About section white/light
css = css.replace('.about-section {\n    background-color: var(--clr-navy-light);\n    color: var(--clr-white);\n',
                  '.about-section {\n    background-color: var(--clr-gray-light);\n    color: var(--clr-navy);\n')
css = css.replace('.about-text h2 {\n    color: var(--clr-white);\n',
                  '.about-text h2 {\n    color: var(--clr-navy);\n')

# Footer white/light
css = css.replace('.footer {\n    background-color: var(--clr-navy);\n    padding: 4rem 2rem 2rem;\n    color: var(--clr-gray);\n}',
                  '.footer {\n    background-color: var(--clr-gray-light);\n    border-top: 1px solid var(--clr-gray-light);\n    padding: 4rem 2rem 2rem;\n    color: var(--clr-navy);\n}')
css = css.replace('.footer-brand h2 {\n    color: var(--clr-white);\n',
                  '.footer-brand h2 {\n    color: var(--clr-navy);\n')
css = css.replace('.footer-links h3 {\n    color: var(--clr-white);\n',
                  '.footer-links h3 {\n    color: var(--clr-navy);\n')

# Premium Card
old_premium = """.zirc-card-premium {
    background-color: var(--clr-navy-light);
    border-color: var(--clr-copper);
    color: var(--clr-white);
}"""
new_premium = """.zirc-card-premium {
    background-color: var(--clr-white);
    border: 2px solid var(--clr-copper);
    color: var(--clr-navy);
}"""
css = css.replace(old_premium, new_premium)
css = css.replace('.zirc-card-premium h3 {\n    color: var(--clr-white);\n',
                  '.zirc-card-premium h3 {\n    color: var(--clr-navy);\n')
css = css.replace('.zirc-card-premium .tag {\n    background-color: rgba(255, 255, 255, 0.1);\n    color: var(--clr-white);\n}',
                  '.zirc-card-premium .tag {\n    background-color: rgba(205, 154, 80, 0.1);\n    color: var(--clr-copper);\n}')
css = css.replace('.zirc-card-premium p {\n    color: var(--clr-gray-light);\n}',
                  '.zirc-card-premium p {\n    color: var(--clr-navy);\n    opacity: 0.8;\n}')

with codecs.open(css_path, "w", "utf-8") as f:
    f.write(css)
