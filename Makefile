all:
	rm -rf out||:
	mkdir out
	python3 test.py
	rm /tmp/*.ttf||:
