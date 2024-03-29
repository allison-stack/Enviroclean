## INSTALLATION INSTRUCTIONS:
1. Download the latest version of Python at: https://www.python.org/downloads/
2. Download PyCharm (the software that will be running the program) at: https://www.jetbrains.com/pycharm/download/#section=windows
3. Download all files in the EnvrioClean Github repository
4. Open up main.py and main.kv files with PyCharm
5. Install libraries: by typing: 'pip install kivy' , 'pip install kivymd' , 'pip install pyzbar' , 'pip install Pillow' , 'pip install opencv-python' , 'pip install beautifulsoup4', 'pip install keras' , 'pip install tensorflow' into the PyCharm terminal separately
6. Now you can run the program on PyCharm (using the green play button near the top right corner of the screen)!

## HOW FILES WERE SHARED BETWEEN GROUP MEMBERS: 

Files were posted on this collaborative repository, then converted into a shared google drive including classified model (the machine learning model used to classify scanned barcodes, main.py and images (used as icons)

## USER INSTRUCTIONS

After running main.py, user will be directed to page below:
![image](https://user-images.githubusercontent.com/100422268/172062849-a1f939a6-1290-4c1a-8a04-137cc52346c9.png)

If you have an item to scan, click the top option: I want to scan something, to open the camera. Then place your item's barcode close to the camera. Ensure your local environment has good lighting. 
If you do not have an item to scan, click no barcode. Then, a menu of different types of recyclable items will pop up, choose according to product at hand.
![image](https://user-images.githubusercontent.com/75755575/172087855-a8eccfe0-009e-4ee3-96d6-28bb7df36a9f.png)

## NOTES 

Scanning speed is dependent on your network connection.
In very rare cases, an incorrrect barcode match is made because the database referenced, Barcode Spider, contains errors within the database itself, though it will scan correctly. 

ex. code 068274000218 
On Barcode Spider, it returns:
![image](https://user-images.githubusercontent.com/100422268/172064322-d26371e6-0f29-4522-8c6e-72e48ac6c363.png)

However the actual product is a Nestle water bottle: 
![image](https://user-images.githubusercontent.com/100422268/172064266-4dd5aaa0-e81d-49dd-af43-24917a18b4de.png)

When scanned, one would obtain the classification of the serum bottle. 



## TOOLS 

Barcode Scanner: if you have an item with a barcode to scan, you can obtain the classification of where to dispose the item- the compost, garbage or recycling bin. 





