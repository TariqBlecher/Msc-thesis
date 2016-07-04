#!make

git_all: 
	git add -A :/ 
	git commit -m 'automated commit'
	git push origin master 

git_commit: 
	git add -A :/ 
	git commit -m 'automated commit'
