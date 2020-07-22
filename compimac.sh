git checkout master
git pull
rm -rf build/
rm -rf dist/

pyinstaller --name luncher --icon luncher.png --windowed --noconsole --clean --noconfirm main.py

cp -R public dist/luncher/public
cp -R locale dist/luncher/locale
mv dist/luncher/public/settings/luncher.cfg.dist dist/luncher/public/settings/luncher.cfg
rm -rf build
find . -type d -name "__pycache__" -exec rm -Rf {} \;
find . -type d -name "*.pyc" -exec rm -Rf {} \;
