#!/bin/sh

#################################################################
# MODIFY FROM https://gist.github.com/willprice/e07efd73fb7f13f917ea 
#################################################################

setup_git() {
  git config --global user.email $user_email
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout -b gh-pages
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

commit_output_file() {
  git add output/output*.txt
  git commit --message "Travis build  : $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  echo 'Travis push to github'	
  git remote add origin-pages https://${GITHUB_TOKEN}@github.com/yennanliu/web_scraping.git > /dev/null 2>&1
  git push --quiet --set-upstream origin
}

setup_git
commit_output_file
upload_files