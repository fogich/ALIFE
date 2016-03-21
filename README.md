# ALIFE


# Group Assignment Content
### 1. Introduction and problem statement
What problem are you trying to solve? Why is this important?

The aim of the project is to provide proof of concept of a more user friendly experience for open-ended evolution systems like PicBreedr.org. In our opinion these systems have a powerful creative potential locked inside a cumbersome interface which seems closer to developers and academic environment rather than the average user. In this way we are attempting to show the beautiful possibilities of these concepts to a larger main-steam audience.

### 2. Background
Has this been done before? How? If not, what's the closest related research? (Both using similar approaches and other algorithms.) What's novel with your research?

Websites like PicBreeder.org and EndlessForms.com has been around for a while. A better ways of interaction with similar technologies, at least to our knowledge, hasn't.

### 3. Methods
How does your algorithm/idea work? Describe in as much detail as you can fit into the report.

Our approach is to map the genotype to the 2D space of a mouse touchpad (eventually creating more pseudo-dimensions in order to accomodate all evolved features). Every change of the mouse position initiates the creation of the next generation of individuals and according to the new mouse position the feature(s) mapped in this direction/dimension have much higher chance of mutation rather than the rest. It is assumed that a mouse touchpad or a touch screen is used and that each interaction starts with a finger positioned at the center of the touchpad/screen field. Other input devices/ways of interaction will work, but they won't lend themselves as good to the point we are trying to demonstrate. After each change of the mouse position the new phenotype is displayed on the screen. In practice all this is happening in real time, creating the illusion of morphing different features of the same individual. Therefore the user is left with a feeling of better control and understanding of the whole process.

### 4. Results
Did it work? How well? Provide some figures, and a table or two. Reread some of the papers from class and compare how they report their results.

### 5. Discussion
What are the strengths and shortcomings of your method? Why did you choose method X instead of Y? How would you develop it further, if you had time?
Plus:
 - Real-time morphing/evolution
 - More natural for of user input: mouse movement in 2D space VS. clicking buttons
 - intuitive relationship between a movement and a feature
Minus:
 - dependent on input device/method
 - mutation only, no cross-over
 - relatively limited evolution: predetermined base object VS the power of CPPN



### 6. References
You need to include at least 10 references, of which at least 5 should be academic papers. The formatting of the references should follow any of the standard academic reference formats.
