from generate_spectra import *
import sklearn.linear_model as linear_model
import scipy.optimize as optimization

def solve_normal_equations(mixture_spectra, pure_components):
  # Euclidean norm, minimize it - derive and set resulting expression to zero, solve for c from the normal equations. 
  concentrations = np.dot(inv(np.dot(pure_components, pure_components.T)) , np.dot(pure_components, mixture_spectra))
  return concentrations

def coeff_linear_model(mixture_spectra, pure_components):
 coeffs = linear_model.LinearRegression().fit(pure_components.T, mixture_spectra).coef_
 return coeffs

def func(params, xdata, ydata):
    return (ydata - np.dot(xdata.T, params))**2

def scipy_optimize(mixture_spectra, pure_components):
  x0 = np.ones(len(pure_components))
  return (optimization.leastsq(func, x0, args=(np.array(pure_components), mixture_spectra))[0])


############################### Generate Components ###############################
component_A = normalize(Gauss(mu = 120, sigma = 2) + Gauss(mu = 185, sigma = 2, intensity = 0.3))
component_B = normalize(Lorentz(mu = 150, sigma = 15))
component_C = normalize(Lorentz(mu = 110, sigma = 2, intensity = 0.05) + Gauss(mu = 160, sigma = 10, intensity = 1.0))
## component_d = normalize(Lorentz(mu = 130, sigma = 2, intensity = 0.05) + Gauss(mu = 160, sigma = 10, intensity = 1.0))

### Choose components and concentrations  ####
components = [component_A, component_B, component_C]
concentrations = [0.1, 0.5, 2.1]


################# Generate query spectra, helper functions give pure spectra and mixture spectra #############################

query_spectra = return_test_spectrum(components, concentrations)

print ("Concentrations from normal equations: " + str(solve_normal_equations(query_spectra, np.array(components))))
print ("Concentrations from Linear Regressor: " +  str(coeff_linear_model(query_spectra, np.array(components))))
print ("Concentrations from Scipy Least Suqares: " + str(scipy_optimize(query_spectra, components)))
print ("Finally the real concentrations :) " + str(concentrations)) 
