# WebDict

Based on applications from [The Python Mega Course](https://www.udemy.com/course/the-python-mega-course/ "Python Mega Course") on Udemy

A simple command line dictionary program, connecting to a SQL database with a local JSON backup.

## Usage

Upon execution the user will be prompted to enter a word and its definition(s) will be prited to the console. 
Typos and input errors are handled via on screen prompts.

```
PS Dir> python web_dict.py  
Enter a word to get its definition: snake

 - Any reptile of the suborder Serpentes, typically having a scaly cylindrical limbless 
 body, fused eyelids, and a jaw modified for swallowing large prey.

Would you like to define another word? Y/N: Y

Enter a word to get its definition: reptil

That word isn't in this dictionary, did you mean 'reptile' instead? Y/N: Y

 - A class of terrestrial vertebrates, characterized by the lack of hair, feathers, and 
 mammary glands; the skin is covered with scales, they have a three chambered heart and 
 the pleural and peritoneal cavities are continuous.
 - Any cold-blooded vertebrate of the class Reptilia.

Would you like to define another word? Y/N: 3

Sorry I didnt understand that. 

Would you like to define another word? Y/N: Y

Enter a word to get its definition: innn

That word isn't in this dictionary, did you mean 'inn' instead? Y/N: N

innn not found, try another.

Would you like to define another word? Y/N: N

Thank you for using this dictionary.
```
