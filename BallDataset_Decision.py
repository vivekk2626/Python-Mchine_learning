from sklearn import tree;
import pandas as pd;



def Decision(weight,surface):

	print("\nLoad Data :");
	data=pd.read_csv("MarvellousInfosystems_PlayPredictor.csv");
	
	BallsFeatures=[[35,1],[47,1],[90,1],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]	,[35,1],[95,0]]

	target=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

	print("\nClassifier :")	
	clf=tree.DecisionTreeClassifier();

	print("\nModel {} Train :".format(clf))
	clf=clf.fit(BallsFeatures,target);

	print("\nModel Test :")
	result=clf.predict([[weight,surface]]);

	if(result==1):
		print('\nYour Object Looks Like a Tennis Ball :');

	elif result==2:
		print('\nYour Object Looks Like a Cricket Ball :');		
			


def main():

	weight=input("Enter the Weight :");

	surface=input("Enter the Surface :");


	if surface.lower()=='rough':
		surface=0;

	elif weight.lower()=='smooth':
		surface=1;


	Decision(weight,surface);


if __name__ == '__main__':
	main()