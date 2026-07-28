library(Deriv)
#u <- expression(x^0.6 * y^0.3)
u <- expression(log(7*x+2*y))
u_x <- Deriv(u, "x")
u_y <- Deriv(u, "y")
u_xx <- Deriv(u_x, "x")
u_yy <- Deriv(u_y, "y")
u_xy <- Deriv(u_x, "y")
u_yx <- Deriv(u_y, "x")

x <- 2; y <- 1
cat(round(eval(u_x), 3), round(eval(u_y), 3), round(eval(u_xx), 3),
    round(eval(u_yy), 3), round(eval(u_xy), 3), round(eval(u_yx), 3))
