slides/%.html: notebooks/%.ipynb
	jupyter nbconvert $^ --to slides --output-dir=slides
