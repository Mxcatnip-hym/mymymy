token = ‘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’

t = Github(token)
user = t.get_user()

followers = user.get_following()

for follower in followers:
    repos = follower.get_repos()
    for repo in repos:
        with open('repos.txt', 'a') as file:
            file.write(f"{follower.login} : {repo.name}\n")
            
