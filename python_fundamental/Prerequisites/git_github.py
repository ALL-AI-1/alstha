#git init
#git status
#git add . /git add <filename>
#git commit -m "<message>"

#git config --global user.name "<Your Name>"
#git config --global user.email "<your-email@example.com>"

#git remote add origin <your-repo-url>
#git push -u origin main 
#(-u for the first time it remember the branch in future no need to use -u only write git push or pull)

#git pull origin main
#git clone <your-repo-url>
#git log --oneline
#git log --graph --oneline --all --decorate
#git branch

#git revert <commit_id>
#git checkout <commit_id>
#git reset --hard <commit_id>   # resets to a specific commit and discards changes
#git reset --soft <commit_id>   # resets to a specific commit but keeps changes staged
#git reset --mixed <commit_id>  # resets to a specific commit and keeps changes unstaged
#git restore <filename>         # restores a file to the last committed state
#git checkout <branch_name>     # switch to another branch

#other useful commands

#git fetch                # fetches changes from remote but doesn't merge
#git stash                # temporarily saves changes not yet committed
#git stash pop            # restores stashed changes
#git diff                 # shows changes between commits, branches, or working directory
#git rm <filename>          # removes a file from the working directory and staging area
#git mv <old> <new>           # renames or moves a file
#git tag                  # lists tags (versions) in the repo
#git tag -a <v1.0> -m "<msg>" # creates an annotated tag
#git cherry-pick <commit_id> # applies changes from a specific commit
