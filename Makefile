slides/%.slides.html: notebooks/%.ipynb
	jupyter nbconvert $^ --to slides --output-dir=slides --reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@3.6.0
