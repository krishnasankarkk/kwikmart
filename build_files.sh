echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m manage collectstatic --noinput --clear   
echo "BUILD END"