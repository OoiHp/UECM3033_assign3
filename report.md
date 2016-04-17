UECM3033 Assignment #3 Report
========================================================

- Prepared by: ** OOI HUI PING**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/OoiHp/UECM3033_assign3](https://github.com/OoiHp/UECM3033_assign3)


Explain how you implement your `task1.py` here.

First, to continue with the coding given is to complete the defined function which is called **gausslegendre(f, a, b, n=20)**. The formula: **$x[i]=((a+b)+(b-a)*x[i])/2$** is to extend to a more general interval of [a,b]. Then $f(x)$ is calculated with the new $x_i$. Finally, the function will be returned by $?w_i f(x_i)$, for $i=1,2,...,n-1$ which is also the answer for the integration by using the n-point Gauss-Legendre quadrature method.

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

By using the building function **np.polynomial.legendre.leggauss(n)**.

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

First, a function is defined to solve the differential of  $y_0' = a(y_0 - y_0 y_1 ) $ and $y_1' = b(-y_1 + y_0 y_1)$ with all the information given. **odeint** is used to generate the solution. To pass the parameters b and a to f by using the args argument. 

Put your graphs here and explain.

![Initial condition: $y_0(0) = 0.1$, $y_1(0) = 1.0$;
Graphs of $y_0$ and $y_1$ against $t$](https://github.com/OoiHp/UECM3033_assign3/blob/master/f1a.png)

![Graph of $y_1$ against $y_0$](https://github.com/OoiHp/UECM3033_assign3/blob/master/f1b.png)

![Initial condition: $y_0(0) = 0.11$, $y_1(0) = 1.0$;
Graphs of $y_0$ and $y_1$ against $t$](https://github.com/OoiHp/UECM3033_assign3/blob/master/f2a.png)

![Graph of $y_1$ against $y_0$](https://github.com/OoiHp/UECM3033_assign3/blob/master/f2b.png)


Is the system of ODE sensitive to initial condition? Explain.

No, based on the graph plotted, it does not change much with a little change of initial condition.

-----------------------------------

<sup>last modified: 17/04/2016</sup>