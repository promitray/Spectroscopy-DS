import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
import sklearn.linear_model as linear_model

def Gauss(mu, sigma, xrange = np.linspace(100, 200, 1000), intensity = 1):
 return intensity * np.exp(-(0.5 * ((xrange - mu) / sigma) **2))

def normalize(distribution):
  return distribution/np.max(distribution)

def Lorentz(mu, sigma,xrange = np.linspace(100, 200, 1000), intensity=1):
  return intensity * (1 / (1 + ((xrange - mu) / (sigma / 2))**2))

def plot_pure_spectra(components , figure_name = 'pure_spectra.png', x_range =  np.linspace(100, 200, 1000)):
  for i, component in enumerate(components):
   plt.plot (x_range, component, label = 'component ' + str(i + 1))

  plt.title('Known components in our mixture', fontsize = 15)
  plt.xlabel('Wavelength', fontsize = 15)
  plt.ylabel('Normalized intensity', fontsize = 15)
  plt.legend()
  plt.show()

  plt.savefig(figure_name)

def generate_query_spectra(components, concentrations):
  sum = 0
  for i in range(len(components)):
    sum = sum + components[i] * concentrations[i]
  return sum 

def plot_query_spectra(query_spectra, figure_name = 'query_spectra.png', x_range =  np.linspace(100, 200, 1000)):
  plt.plot(x_range, query_spectra, label = 'Mixture spectrum')
  plt.title('Mixture spectrum', fontsize = 15)
  plt.xlabel('Wavelength', fontsize = 15)
  plt.ylabel('Intensity',  fontsize = 15)
  plt.legend()
  plt.show()

  plt.savefig(figure_name)

def return_test_spectrum(components, concentrations, x_range =  np.linspace(100, 200, 1000)):
 
 query_spectra = generate_query_spectra(components, concentrations) + np.random.normal(0, 0.05, len(x_range))

 plot_pure_spectra(components)
 plot_query_spectra(query_spectra)
 return query_spectra








