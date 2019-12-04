all: sigma.png solar.png

sigma.png:	punto15.py valores.txt
	python punto15.py

solar.png: punto16.py monthrg.dat
	python punto16.py

clean:
	rm sigma.png solar.png