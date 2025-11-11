# Github-Tracker
This program displays the recent activity of a github account.  
This idea was taken from suggested projects by roadmap.sh.  
Source: https://roadmap.sh/projects/github-user-activity

**Usage**: python3 gitsee.py username123 -t  

**Note**:  
When data is listed it is done by newest at the start to oldest at the end.  
Using any option that is not **-t** or **--total** lists up to the last 30 events that have occured.

**Options**: -t, -p, -pl, -s, -cr, -co, and -f  
**-t** or **Total**: Displays a total count of all recent events  
**-p** or **Push**: Displays all recent account push events  
**-pl** or **Pull**: Displays all recent account pull events  
**-s** or **Star**: Displays all recent account star events  
**-cr** or **Create**: Displays all recent account create events  
**-co** or **Comment**: Displays all recent account comment events  
**-f** or **Fork**: Displays all recent account fork events
