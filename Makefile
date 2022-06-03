requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f extract 1.0.0
	brane remove -f extract
	brane build container.yml
	brane push extract
