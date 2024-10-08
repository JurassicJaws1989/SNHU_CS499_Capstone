# SNHU CS-499 Capstone
***SNHU - BS Computer Science Capstone ePortfolio for Justin Smith***

![Justin Smith with Catfish in 2019 - Lake Champlain, VT](./Pictures/catfish.jpg)

This site was built using [GitHub Pages](https://pages.github.com/).

# Self Introduction
My name is Justin Smith, and I have been in the Computer Science program at Southern New Hampshire University since 2019. During this time, I have gained both experience and incredible confidence professionally. The following portfolio aims to showcase some of this, in which it will detail enhancements in the following categories, software design and engineering, data structures and algorithms, and databases. 
With my program coming to a close, I have enjoyed looking back at my work as a whole. It really puts into perspective the growth I have seen in this time period. From simple “Hello World” examples to get acclimated to various programming languages, to creating a fully interactive 3D representation of an Airbus A320 in C++. It is amazing to see what one can accomplish in a short period of time with both personal willpower, and the right resources. 
Throughout the course of my educational journey, I have seen success translate into my professional career as well. I have already begun using these skills in a professional setting, in which I collaborate with a small engineering team to create programs that offer solutions to currently faced problems. Educationally, collaboration with peers was a major point in which I draw certain successes. While this program was entirely online, I was still able to work with my peers to help troubleshoot problems and bounce ideas around between each other. 
Aside from the benefits of communication and collaboration, I now confidently have the skills to really be an impactful member of my team. I currently work in a data focused environment. The skills I now have allow me to work with and analyze these data in much improved methods. I have created utilities that interact with large datasets and allow users to acquire, output, and analyze results quickly. I have also found a love for creating an optimized user experience. Due to this, I enjoy putting the extra effort into making functionality easily accessible to the end user. 
The following artifacts will provide some evidence into what my capabilities are, along with showcasing the possibilities when a goal is followed through. These artifacts will detail my focus on creating and adaptive user experience while maintaining the base functionality of a program. It will show my ability to adapt, as shown by porting a BST from C++ to Python. They will also detail my ability to interact with large datasets with the end user in mind. 



# Code Review
[![Watch the video](https://img.youtube.com/vi/5JeJtqMttag/0.jpg)](https://www.youtube.com/watch?v=5JeJtqMttag)

# Enhancement One: Software Design/Engineering
[Click Here For Source Code](https://github.com/JurassicJaws1989/SNHU_CS499_Capstone/tree/main/Software_Engineering_and_Design)

For the software design and engineering element, I decided to choose a calculator application I wrote in Python back in 2020. This was the first real application I created, and one of my earliest creations in Python. The calculator provides process improvements in a laboratory environment and hosts relatively simply functionality in an easy to use interface. 
My reasoning for choosing this element comes from the fact that I did not have the knowledge set I have now when I initially created this application. It was in desperate need of both a functionality overhaul, along with massive improvements in terms of how the code itself was written. One of the biggest elements that I changed within this application that show off my current skillset is the complete rewriting of the application’s code. During the enhancement, I was able to do the following,
*	Adjust variable/function names to adhere to a standard practice
*	Add in commenting and documentation
*	Reduce/eliminate redundant code blocks with better use of function calls

By doing this, the code is much more clean and readable, and more effective in the process. 
Another aspect that I enhanced shows off my ability to adhere to best practices in UI/UX principles by greatly improving the user interface of this application. I was able to consolidate the entire application within a single window, cleaning up the interface significantly. I also performed a complete overhaul of the “theme” selection within the utility, making it not only more user friendly when choosing the customizable layout, but much easier to add in new themes on a programming end. 
By performing this enhancement, I was able to meet the objectives I had previously planned. These surrounded demonstrating the execution of properly written code that is readable, maintainable, and functional, along with fully displaying my knowledge on creating a fully functional user interface that adheres to best practices. I was able to demonstrate that I am meeting the following course outcomes,

* Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices
* Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals
  
While working through the enhancement process, I was met with challenges throughout the process (as to be expected with any project). The first real challenge was dealing with the original code. As I mentioned, this was written exclusively by myself quite a few years ago. This was before I had any real experience in programming. Due to this, I found it difficult to recall what exactly was going on within this code, especially given the lack of commenting and poor readability within the code. I had to instead use the original application’s functionality as a basis/starting point, and re-write the code entirely from the ground up. This added time, but made the enhancement much easier in the end. 
I also ran into some minor trouble with the execution of the theme selection within the utility. In the previous code, I was calling multiple configuration function calls throughout when users would select a new color scheme via a button press. This was messy, both in the interface, and in the code. I wanted instead to feature a theme dropdown on the main menu, and store specific widget colors as variables. At first, I found difficulty in passing these color variables throughout all of the various screens. I was able to overcome this by declaring them globally within the theme function definition. Although I found this a bit more challenging than simply calling colors via button clicks, it was more rewarding when it became functional. It also looks significantly better within the application. 
Attached, you will find some screenshots that detail the enhanced utility in operation. 

![Calculator Demo Screens](./Pictures/Calc_Demo.JPG)

# Enhancement Two: Algorithms and Data Structure
[Click Here For Source Code](https://github.com/JurassicJaws1989/SNHU_CS499_Capstone/tree/main/Algorithms_and_Data_Structures)

The artifact I chose for the Algorithms and Data Structure element is from a project that we worked on during CS-260 (Data Structures and Algorithms). Specifically, from module six, where we were tasked with creating a binary search tree function in C++ that interacts with a large data structure of electronic bids. The emphasis of the assignment was to understand how a binary tree search works, and to showcase its improvement in terms of speed when searching large data structures. We were also tasked with creating a test interface within the terminal to interact with the functionality. The functionality we were tasked on adding was,
*	Load Bids – read in data from .csv file and appropriately add it to a binary tree
*	Display Bids – display all bids in record
*	Find Bid – perform the search within the binary search tree by entering a bid ID
*	Display Time – record and display the elapsed time of the search

One of the major reasons I chose this artifact was the fact that I did not completely recall how this search function worked. I wanted to use this exercise as a means to familiarize myself with this particular algorithm, along with challenge myself with attempting to port this functionality to an entirely different language, Python. Furthermore, since this original artifact only had a test interface within the terminal, I wanted to further showcase my skills in creating a user focused utility to house this functionality. I was glad that I made this choice, as I now feel very comfortable with the understanding of how this search algorithm works, and why it is able to drastically improve search times. Although challenging at first, I am also quite impressed with my ability to recreate this functionality in Python.
After creating the binary search tree class, I was also able to wrap everything up within a fairly standard, yet functional user interface. The following screenshots provide this in more detail,

# LOAD BIDS:
![EBID](./Pictures/Load_Bids.png)

# DISPLAY BIDS:
![EBID](./Pictures/Display_Bids.png)

# SEARCH BIDS:
![EBID](./Pictures/Search_Bids.png)

I was able to meet the objectives I laid out for myself for this enhancement, and found it to be extremely rewarding albeit a bit challenging at times. Some of the challenges I faced initially surrounded my initial unfamiliarity with how the class was defined and how the algorithm operates. My initial comments within the original C++ element did not provide me with enough detail to hit the ground running. With a little research back into the resources for CS-260, I was able to better understand this. I also ran into an issue with the way my BST was being created. I was inserting bids (keys) into the tree depending on the size of the overall tuple. This ended up making it impossible to correctly traverse the tree when searching for ID numbers specifically. I ended up having to get creative within the search to correctly traverse, yet still identify specific bid ID numbers (and still maintain high speed). This ended up being useful as I progress to the third enhancement element, where I will further improve the ability to both search and interact with this relatively large data structure. 

# Enhancement Three: Database
[Click Here For Source Code](https://github.com/JurassicJaws1989/SNHU_CS499_Capstone/tree/main/Database)

The element for my third and final enhancement, the database element, was a follow up on my previously enhanced element, the electronic bid search function. It originated as a simple terminal based binary search tree function in C++. In the last milestone, I ported this functionality over to Python and created an interface to interact with the ID search.
What I wanted to do with this further enhancement, was to completely overhaul the search and display functionality for this large dataset, and make it more user interactive within the utility. I ended up making use of a Pandas data frame to interact with this data set, and made it more visible within the utility in a nice tabular view. Furthermore, I added the functionality to sort the dataset by numerous fields via a radio button click. Now, as for the search functionality, one thing I wanted to enhance within this utility was to allow for the user to search for more than just the ID. So, I added the ability to search by numerous fields via a drop down, in which the program will display all of the bids that match the specified criteria. 
I also wanted to add some level of protection to this utility by making it password protected. So, the user must enter a password before being allowed access to the utility’s functionality. So, let’s take a look at the end result,
# Password Functionality
The user enters the correct password before access is granted.
![EBID](./Pictures/PW.png)

# Bids loaded and displayed automatically
![EBID](./Pictures/LOAD.png)

# Sort and Display
![EBID](./Pictures/SORT.png)

# Search by Specific Variable
![EBID](./Pictures/SEARCH.png)
![EBID](./Pictures/SEARCH2.png)

By implementing these changes to this utility, I have shown my ability to work with large datasets and create the appropriate functionality to allow a user to interact with them as well. I have also shown my continued ability to keep the user in mind when designing applications that are both functional, and easy to operate. I have also shown adherence to security protocols by locking functionality behind some level of user protection and control measures. 
Previously, I did not have a wealth of experience with using the Pandas module in Python. While much of the functionality is possible that exists in other database specific languages like SQL, I found the specific syntax to perform the queries to be difficult at first. Furthermore, wrapping this all into the utility while passing all of the needed variables around successfully was challenging. Throughout all of these enhancements, I feel that I have learned so much more about these fundamentals and it has all happened in a pretty short amount of time. I am astonished at the work I was able to complete and the fact that I was able to meet the goals that I had set out to meet in the beginning of this course. 
With this said, I have shown through these enhancements that I meet the following course outcomes,

*	Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science
*	Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts
*	Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices (data structures and algorithms)
*	Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals (software engineering/design/database)
*	Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources


