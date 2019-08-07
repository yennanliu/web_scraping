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
  git commit --m "Travis build  : $TRAVIS_BUILD_NUMBER"
}

commit_new_output_file() {
  d=`date +%Y-%m-%d` && echo $d 
  git status 
  for file in "output"/*
  do 
    if [[ "$file" == *"$d"* ]];then
      echo "no today's new file, nothing to commit"    
    else 
      echo "commit new file..."
      git add output/* 
      git commit --m "Travis build  : $TRAVIS_BUILD_NUMBER"
    fi 
  done
}

upload_files() {
  echo 'Travis push to github'	
  git push https://yennanliu:${GH_TOKEN}@${GH_REF} HEAD:master --quiet

}

GH_REF=github.com/yennanliu/web_scraping.git
setup_git
commit_new_output_file
upload_files