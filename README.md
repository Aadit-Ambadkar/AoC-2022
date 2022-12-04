# AoC-2022
I'm not golfing this years AoC that was day one only it's too hard and I'm too lazy

I'm in PST so we start at 21:00 military time, so that's what is used in `scrape.py`. Change that to 00:00 or whatever else works for you.

First find your session by navigating to Day 1's input, inspecting the network flow, refreshing the page, taking a look at the request, and scrolling to the cookies section.
In a .env file add your session. Please note that the session listed is my actual session. If I find people misuising it, I will clear cookies and refresh the session token. Act in Good Faith.

Near the start of the day, run `init.py` to spawn up the python file for the day.
Then run `scrape.py`. That automatically pings the server once it hits midnight, and loads up your input in the day's input file.
You can safely leave the terminal open and read the problem statement without having to copy the input.

To edit the program, simply edit `solve1` for part 1 and `solve2` for part 2.
To run the program, run `python day#.py` to run part 1, and `python day#.py -2` to run part 2. # is the day.

this should speed up my code time. i hope.
