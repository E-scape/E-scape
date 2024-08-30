# 개발환경
ubuntu 24.04

```
sudo apt-get update && sudo apt-get -y upgrade
```

### 종속성 설치
```
sudo add-apt-repository ppa:pipewire-debian/pipewire-upstream

sudo apt install -y python3-venv gpsd gpsd-clients python3-gps portaudio19-dev python3-all-dev git libcairo2-dev libxt-dev libgirepository1.0-dev pipewire libspa-0.2-bluetooth pipewire-audio-client-libraries
```

### pipewire-pulse 설정
```
systemctl --user daemon-reload
systemctl --user --now disable pulseaudio.service pulseaudio.socket
systemctl --user --now enable pipewire pipewire-pulse
systemctl --user mask pulseaudio
systemctl --user --now enable pipewire-media-session.service
pactl info
```

### python venv 설치
```
python -m venv <env_name>
```

### venv 실행 후 pip install
```
source <env_name>/bin/activate
pip install pycairo PyGObject
pip install -r requirements.txt
```

### google cloud cli 설치
```
sudo apt-get install apt-transport-https ca-certificates gnupg curl

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get update && sudo apt-get install google-cloud-cli
```

### gcloud init 하기
```
gcloud init

git config --global user.email "~"
git config --global user.name "~" 
```

## 설정
Escape_code/key.py
Tmap_key, GPT_KEY 입력

Escape_code/config.py
내 파일주소에 맞게 값 변경