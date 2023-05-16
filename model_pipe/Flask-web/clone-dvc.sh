rmdir -R data
echo "Delete data"
USER="h4438"
EMAIL="www.hao2912@gmail.com"
TOKEN="7d5a95fcb968cb2697edf3cc170dcc576e29a6d2"
REPO_NAME="Stock-Indicator-News"
REPO="https://"$USER":"$TOKEN"@dagshub.com/h4438/"$REPO_NAME".git"
DVC_REPO="https://dagshub.com/"$USER"/"$REPO_NAME".dvc"
mkdir data
cd data
pwd
git clone $REPO
cd $REPO_NAME
git pull origin master
echo "Git cloned"
pwd
git config --global user.email $EMAIL
git config --global user.name $USER
dvc remote default origin --local
dvc remote modify origin --local auth basic
dvc remote modify origin --local user $USER
dvc remote modify origin --local password $TOKEN
dvc pull -r origin
echo "DVC pulled"
echo "Press any key to exit"
read