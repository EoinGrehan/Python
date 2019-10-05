My program allows the user to input their grade percentage for each module along with its credit value. 
To calculate the GPA value, you first take the grade from each module then it must be multiplied by the number of credits 
related to the module. This will return the number of grade points earned. 
Lastly, add up the grade points from all modules and then divide by the total number of credits, this will return the GPA.

The program uses EasyGUI to enhance the program the graphical appearance and to provide a simple interface.

#Client Features

Prompt the user to enter grade for each module
Prompt the user to enter credit value for each module
Send entered values to server
Receive and display overall GPA
Repeat program until user terminates

#Server Features

Receive the inputs from the client (Integers encoded as string)
Completes calculation and returns overall GPA to the client
If the TLS files are missing or corrupt a error message is displayed and the program is terminated





