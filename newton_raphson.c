#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double f(double x){
    double valor;

    valor = cos(x) - x;
    return valor;
}

double  dfdx(double x){
    double value;
    value = -sin(x) - 1.0;
    return value;
}


int main(void){
    // Vamos a encontrar la raiz de la ecuación 
    //f(x) = cos(x) - x
    //usando el metodo de Newton-Raphson

    double Tol; //Tolerancia
    int Nmax;// Numero maximo de iteraciones
    double p; // p_(n)
    double p_prev; // p_(n-1)
    double error;
    int iteration;

    p_prev = 3.0;
    error = 1.0;
    Tol = 1.0e-3;
    iteration = 0;
    Nmax = 1000;

    while(error > Tol){
        p = p_prev - f(p_prev)/dfdx(p_prev);
        error = fabs(p - p_prev);
        printf("p_previo = %f\t  p = %f\t error = %f\t f(p) = %f\n",p_prev ,p,error,fabs(f(p)));
        p_prev = p;
        iteration += 1;
        if( iteration > Nmax){
            printf("El metodo no converge  despues de  %d iteraciones \n",Nmax);
            break;
        }

    }


   
    return 0;
}


