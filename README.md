# google-dork
This will grab a random dork and then save the output to a text file

This is what i use for finding all my XSS's.

Only note is the proxy is there as i use it with burp and then via tor browser socks.

You can remove this but remember google will give you the lovely capture!

I've made this using python 3 but it should work in python2.



Requirements
----

```
pip install -r requirements.txt
```

Note
------

I have not used inurl:"DORK" inurl:"&" as you end up getting results once and then you have to change the proxy each time.

It uses my XSS dork server https://xsses.rocks/dork/ - everytime i find a reflective parameter it's logged and put in to the list.


Please send a PR request if you can remove any results with ASCII and also urldecode the results.




To do
------
Remove youtube links
Remove VK links
Urldecode links
Remove ASCII links
