def my_function(x):
    return ((3 * x **2) - x)

def return_derivative(x, my_function = my_function, h = 0.0001):
  return  (my_function(x + h) - my_function(x))/h

def gradient_descent(x_start, step_size = 0.15, n_iter = 100, convergence_limit = 0.005):
   
 for i in range(n_iter + 1):
   gradient = return_derivative(x_start)
   new_x = x_start - (gradient * step_size)

   print ((abs(new_x - x_start)), i)

   if (x_start - new_x) >= convergence_limit:
      x_start = new_x
     
   else:
      print ("Alogirthm has converged in " + str(i) + " iterations")
      
      break
   
   if i == n_iter:
      print ("max num of iterations reached without converging - exiting now")

 print ("mimimum is at " + str(new_x) + "and the minimum value of the funtion is " + str(my_function(new_x)))

gradient_descent(x_start = 20)