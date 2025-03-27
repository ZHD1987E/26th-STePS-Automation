# What is this?

The 25th STePS had this *autoscraper* to automate document generation workflows.

This time round, I decided to extend this to the 26th STePS because there may be even more groups to deal with! In fact, this edition has 69 teams (as of 27 March 2025) compared to 43 teams in the previous iteration.

Since NUS Computing will celebrate some anniversary this time round (and they have hosted the [APAC ICPC](https://apac.icpc.global/) likely for this reason), they might choose to ramp up the number of teams exhibiting with more courses on show. That means a lot of work for staff members! Of course, there was a time that 120+ teams exhibited for this project fair and it required a lot of space to execute.

Therefore, to ease that workflow (especially if 100+ teams were to exhibit at once), I decided to create a central webscraper where people can retrive the needful.

# I thought it was a webscraper? Why did it now use APIs?

Then, someone told me that it's possible to now get the API instead of scraping web data, which means that data syncing can now be done much faster.

From then, it was pretty much a migration over to direct API use, and with the fix to Pytube, it is now possible for me to download videos with a single run of a Python script.

Hopefully, with integration to UVENTS' awards system, it is now possible to fully automate the generation of certificates, thereby reducing the manpower needed.

# How will the data there be used?
There are three output files:
- `26th-steps-data.csv`: This is meant for 'mail merge' operations especially if certificates have to be generated. Otherwise, it is tabular data that can be manipulated for many other reasons.
- `26th-steps-projectnames.md`: This is meant for documents which just need the project names and their associated courses.
- `26th-steps-videolinks.txt`: This is a textfile which `videodownload.py` will use to download the neccessary videos for eventual exhibition.

As always, if you have any more ideas how to automate workflows with this repository, feel free to contact me below.

# Can I use it anywhere else?
If you talk about other UVENTS webpages, this should work well.

However, this repository is specifically geared towards the 26th STePS in the School of Computing, so if you wish to use it anywhere else, you may need to do a bit of modifications.

# Cool, who should I contact?

If you are contacting **regarding the event**, please contact [Anand Bhojan](mailto:bhojan@comp.nus.edu.sg). **DO NOT CONTACT ME.**

If you are contacting **regarding this repository**, please contact me through [Telegram](t.me/zhd1987e), or [email](mailto:zhanghaodong101@outlook.com), or even through [Facebook](https://www.facebook.com/ZhangHaoDongOfficial/).

Of course, you can always find me on GitHub.

©️ ZHD1987E
