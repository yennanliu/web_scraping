#!/bin/sh
####################################################################
# MODIFY FROM https://gist.github.com/willprice/e07efd73fb7f13f917ea 
####################################################################

setup_git() {
  git init 
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout -b gh-pages
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

commit_output_file() {
  git status 
  git add output/*
  #git add . 
  git commit --m "Travis build  : $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  echo 'Travis push to github'	
  git push https://yennanliu:${GH_TOKEN}@${GH_REF} HEAD:master --quiet

}

GH_REF=github.com/yennanliu/web_scraping.git
setup_git
commit_output_file
upload_files