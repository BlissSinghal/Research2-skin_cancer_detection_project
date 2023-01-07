import _make_components as m_component
import make_component_images as comp_img
import get_fig_1 as fig_one
import make_graphs
import get_ga_results
#import genetic_algorithm as ga
import save_numpy_array as save
dataset_size = 50000
num_components = 8

data = m_component.make_components(data_size= 1, num_components = 25, num_neighbors= 160, preprocessing_method = "ga")
print(data)

#print(m_component.make_components(data_size = 25000, num_components = 500, iteration = 100, preprocessing_method = "ga", population_size = 100))
optimal_pop_size = 29

#print("PCA:" + str(m_component.make_components(preprocessing_method = "genetic algorithm")))
#print("Genetic Algorithm: " + str(m_component.make_components(preprocessing_method="genetic algorithm")))
#x_vals, n_model, lin_model, tree_model = save.get_dataset_array("ga_or_not")


#print(save.get_dataset_array("ga_or_not"))
#make_graphs.make_bar_graph("Using Genetic Algorithm or Not (Dataset Size is 600)", "Genetic Algorithm or Not3", "Accuracy Scores", x_vals, n_model, lin_model, tree_model)

