#derivadas de primeira e segunda ordem
#derivada de u



ux <- D(expression(x^0.6) , "x") 
x=2
ux_2 <- function(){
  y <- 0.6 * 2 ^ -0.4
  return(y)
}

uxx <- D(expression(0.6 * x ^ -0.4), "x")

uxx_2 <- function(){-(0.6 * (2^-(0.4 + 1) * 0.4))}


uy <- D(expression(x^0.3), "x")
#print(uy)

uy_2 <- function() {0.3 * 2^-0.7}
uy_2

uyy <- D(expression(0.3* x ^-0.7), "x")
uyy
