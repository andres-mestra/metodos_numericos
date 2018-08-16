#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double f(double x){
    double valor;

    valor = cos(x) - x;
    return valor;
}



int main(void){
    // Vamos a encontrar la raiz de la ecuación 
    //f(x) = cos(x) - x
    //usando el metodo de Newton-Raphson

    double Tol; //Tolerancia
    int Nmax;// Numero maximo de iteraciones
    double p; // p_(n)
    double pn_1;
    double pn_2; // p_(n-1)
    double error;
    int iteration;

    pn_1 = -3.0;
    pn_2 = 5.0;
    error = 1.0;
    Tol = 1.0e-4;
    iteration = 0;
    Nmax = 1000;

    while(error > Tol){
        p = pn_1 - ((pn_1 - pn_2)*f(pn_1)) / (f(pn_1) - f(pn_2));
        error = fabs(p - pn_1);
        printf("pn_2 = %f\t  pn_1 = %f\t  p = %f\t f(p) = %f\t error = %f\n",pn_2 ,pn_1 ,p ,fabs(f(p)),error);
        pn_2 = pn_1;
        pn_1 = p;
        iteration += 1;
        if( iteration > Nmax){
            printf("El metodo no converge  despues de  %d iteraciones \n",Nmax);
            break;
        }

    }


   
    return 0;
}