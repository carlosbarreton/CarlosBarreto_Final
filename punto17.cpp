#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

int main() {

	float x_ini = 0;
	float x_fin = 2;
	float delta_x = 0.01;
	float delta_t = 0.01;
	float t_actual = 0.0;
	float t_fin = 0.5;

	int Nx = (int)(x_fin-x_ini)/0.01;
	float u_n[Nx];
	float u_n_plus_1[Nx];

	ofstream outfile;
	outfile.open("pde.dat");

	// CONDICION INICIAL
	for(int i=0; i < Nx; i++){
		u_n[i] = exp(-0.5*(pow(i*delta_x-1,2))/pow(0.25,2)); 
		outfile << u_n[i] << " ";
	}
	outfile << endl;
/*
	// SOLUCION EC. DIFERENCIAL
	while(t_actual+delta_t < t_fin) {
		outfile << u_n[0] << " ";
		for(int i = 1; i < Nx-1; i++){
			u_n_plus_1[i] = u_n[i] - delta_t/delta_x*u_n[i]*(u_n[i+1]-u_n[i]); 
			outfile << u_n_plus_1[i] << " ";
		}
		outfile << u_n[Nx-1] << " ";
		outfile << endl;
		for(int i = 0; i < Nx; i++){
			u_n[i] = u_n_plus_1[i];
		}
		t_actual += delta_t;
	}

*/
	outfile.close();

	return 0;
}