all: sigma.png solar.png resultado.png 

sigma.png:	punto15.py valores.txt
	python punto15.py

solar.png: punto16.py monthrg.dat
	python punto16.py

resultado.png: pde.dat punto17.cpp punto17.py
	python punto17.py

pde.dat: punto17.x
	./punto17.x > pde.dat

punto17.x: punto17.cpp
	c++ punto17.cpp -o punto17.x

clean:
	rm sigma.png solar.png resultado.png pde.dat punto17.x