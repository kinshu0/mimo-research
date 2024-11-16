import DeepMIMOv3
from data_gen_params import params

# Load the default parameters
# parameters = DeepMIMOv3.default_params()
parameters = params

# Set scenario name
parameters['scenario'] = 'O1_60'

# Set the main folder containing extracted scenarios
parameters['dataset_folder'] = 'dataset/scenarios'

# Generate data
dataset = DeepMIMOv3.generate_data(parameters)