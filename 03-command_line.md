# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > $<$ The < will take and send the input from the file on the right to the program on the left.    
    $|$ The | takes the output from the command on the left, and "pipes" it to the command on the right.    
    $>>$ The >> takes the output of the command on the left, then appends it to the file on the right.  
    env - sets and displays the current environment variables.  
    pwd	- Indicates the current working directory set by the cd command.  
    path -Indicates search path for commands. It's a colon-separated list of directories in which the shell looks for commands.  
    grep -Used to search text or searches the given file for lines containing a match to the given strings or words.  
    find - Used to find files and directories using a given search criterion.
    DIR - displays files and folders in a directory.
    hostname - the name of the computer.  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls lists the contents of a directory  
    ls -a includes directories whose name begins with a dot  
    ls -l lists is long format  
    ls -lh lists in long format and uses unit suffixes (bytes, kilobytes, megabytes etc)  
    ls -lah lists in long format, uses unit suffixes, and includes directories whose names begin with a dot
    ls -t lists sorted by the time modified    
    ls -Glp lists in long format, writes a slash after each filename if that file is a directory, and enables colorized output
    

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -u	Displays files by the file access time    
    -R  Displays subdirectories as well  
    -r	Displays files in reverse order  
    -d	Displays only directories  
    -m	Displays the names as a comma-separated list  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is used to build and execute command lines from standard input  
e.g. - find /path -type f -print | xargs rm  

 

