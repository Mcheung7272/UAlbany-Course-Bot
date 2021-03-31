# UAlbany-Course-Bot
This bot helps students at UA look up courses in real time instead of navigating through multiple webpages. Students can look up almost all courses offered at UA. 

## !look
This command takes in specific Course prefix and number and will return real time information about it in regards to dates and free seats.
```
!look <Course Subject> <Course Number> #returns Class Number, Course Info, Meeting Info, Seats Available as of lookup and Comments.
```
![example output](https://github.com/Mcheung7272/UAlbany-Course-Bot/blob/master/exampleoutputCourse.png?raw=true "Example Output")

## !subjects
Outputs all subjects my database has courses of stored inside as well as the prefix associated for easier look up.

![example output](https://github.com/Mcheung7272/UAlbany-Course-Bot/blob/master/subjectsShow.png "Example Output")

## !whatis
Very similar to !look, thats in Course Prefix and Number. Big difference is, !look is limited to current semester and has to be in real time for accurate amount of free seats. This command has almost no lookup time and offers information about ALL courses.
```
!whatis <Course Prefix> <Course Number>
```
![example output](https://github.com/Mcheung7272/UAlbany-Course-Bot/blob/master/whatIsShow.png "Example Output")

## !courses for
This command takes in a subject prefix and outputs ALL courses offered for that subject. For example, if you do the command for CS, all CS courses offered at UA will be displayed.
```
!coursesfor <Course Prefix>
```
![example output](https://github.com/Mcheung7272/UAlbany-Course-Bot/blob/master/coursesForShow.png "Example Output")

## Contributing
This is made specfically for students at SUNY Albany but pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
