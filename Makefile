requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f extract
	brane remove -f extract
	brane build container.yml
	brane push extract