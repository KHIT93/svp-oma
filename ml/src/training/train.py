import pandas
from sklearn import model_selection
from sklearn import tree
import pickle

names = ['rpm', 'temp', 'wind_speed', 'wing_angle', 'brake', 'error_code']
dataset = pandas.read_excel("book1.xlsx", names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,:5]
Y = array[:,5]
validation_size = 0.20
seed = 7
# Split data into training and validation data
train_x, test_x, train_y, test_y = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Create a decisiontree with max depth of 4 to have no overfitting
dtc = tree.DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=4, min_samples_leaf=5)
dtc.fit(train_x, train_y)

# The feature and class names
feature_names = ['rpm', 'temp', 'wind_speed', 'wing_angle', 'brake']
class_names = ['0', '100', '110', '120', '130', '200', '210', '220', '300']

# Generate a dot file with the tree structure
dot_data = tree.export_graphviz(dtc, out_file='C:/tmp/test.dot', feature_names=feature_names, class_names=class_names, filled=True, rounded=True)
# Run dot -Tpng test.dot -o tree.png in C:/tmp to convert the file into an image

# Save model as a pickle
pickle_file = 'dtc_windturbine.pkl'
model_pkl = open(pickle_file, 'wb')
pickle.dumb(dtc, model_pkl)
model_pkl.close()