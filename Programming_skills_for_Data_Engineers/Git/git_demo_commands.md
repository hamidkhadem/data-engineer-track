# Demo
## Git Commands:

Initialize a local git repo:
> git init

List of files (untracked and modified):
> git status

Add a file to index:
> git add "file_name"

Commit files:
> git commit -m "commiting message"

Add all new/ modified files to index:
> git add -A

Commit all new/ modified files:
> git commit -a -m "message"

Log data:
> git log

Create a new branch:
> git branch branch_name

Switch to branch:
> git checkout branch_name

Merging branch to main branch:
> git merge branch_name

Rebasing a brach:
> git rebase main OR branch_name




Connect to remote repo:
> git remote add origin "ssh link"/"link" (most preferably using ssh)

Pull files from remote repo:
> git pull origin main

	if error: fatal: HTTP request failed
	git remote set-url origin "link"

Pushing files: first need to made an SSH key:
-generate SSH key
> ssh-keygen

See the SSH key:
> cat "SSH key path" (near to "saved in")

Authenticating SSH with GitHub:
> ssh -T git@github.com

Push to specific branch:
> git push origin main/ branch_name

