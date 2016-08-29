# Cornell Roster Class Status

This is a simple python project to email the user when a class of their choosing has a spot open. The primary use is during Cornell pre-enroll or add/drop, to learn very quickly when the class you want to get into is open.

To use, run:

```
python emailWhenOpen.py <course number> <email address>
```

For example, `python emailWhenOpen.py 'CS3110' 'john.smith@gmail.com'`, will email john.smith@gmail.com when CS 3110 is open.


*The email functionality requires that your machine has [sendmail](http://www.sendmail.com/sm/open_source/download/ "download sendmail").

