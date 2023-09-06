if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Kichuprozz/Anya-Forger.git /PiroAutoFilterBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PiroAutoFilterBot
fi
cd /PiroAutoFilterBot
pip3 install -U -r requirements.txt
echo "Starting tgmoviespro1bot...."
python3 bot.py
