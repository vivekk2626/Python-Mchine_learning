from sklearn.datasets import load_iris;
import numpy as np;
from sklearn import tree;


def main():

	dataset=load_iris();

	print("\nDatasets Features :")
	print(dataset.feature_names);	

	print("\nDatasets Target :")
	print(dataset.target_names);

	print("\nTest Indexes :")
	test_index=[1,51,101]
	print(test_index);

	print("\nSplitting Train Data And Test Data :")
	train_data=np.delete(dataset.data,test_index,axis=0);
	train_target=np.delete(dataset.target,test_index)

	test_data=dataset.data[test_index];
	test_target=dataset.target[test_index];

	classifier=tree.DecisionTreeClassifier();

	print("\nClassifier {} is Loaded Successfully \n".format(classifier))


	classifier=classifier.fit(train_data,train_target);

	print(test_target);

	print("\nResult Of Prediction :\n");
	print(classifier.predict(test_data));


if __name__ == '__main__':
	main()